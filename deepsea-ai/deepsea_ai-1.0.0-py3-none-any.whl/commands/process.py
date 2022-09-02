# !/usr/bin/env python
__author__ = "Danelle Cline, Duane Edgington"
__copyright__ = "Copyright 2022, MBARI"
__credits__ = ["MBARI"]
__license__ = "GPL"
__maintainer__ = "Duane Edgington"
__email__ = "duane at mbari.org"
__doc__ = '''

Process a collection of videos; assumes videos have previously been uploaded with the upload command

@author: __author__
@status: __status__
@license: __license__
'''

import os
import inspect
import boto3
import sys
import json
from datetime import datetime
from pathlib import Path
from . import config

from sagemaker.processing import ScriptProcessor, ProcessingInput, ProcessingOutput

code_path = Path(os.path.abspath(inspect.getfile(inspect.currentframe())))

# A known pretrained model
default_model_s3 = 's3://902005-public/models/yolov5x_mbay_benthic_model.tar.gz'

# benthic tracking config
default_track_config_s3 = {'deepsort':  "s3://902005-public/models/deep_sort_benthic.yaml",
              'strongsort':"s3://902005-public/models/strong_sort_benthic.yaml" }

def script_processor_run(input_s3: tuple, output_s3: tuple, model_s3: tuple, model_size: int,
                        volume_size_gb:int, instance_type:str, config_s3: str, save_vid: bool,
                         conf_thresh: float, tracker:str):
    """
    Process a collection of videos with the ScriptProcessor
    """
    user_name = config.get_username()

    if tracker not in ['deepsort', 'strongsort']:
        raise Exception(f'{tracker} not currently supported')

    ## TODO: check of config_s3 is a valid s3 bucket with a valid object
    arguments = ['dettrack',
                 f'--conf-thres={conf_thresh}',
                 f'--model-size={model_size}',
                 f'--model-s3=s3://{model_s3.netloc}{model_s3.path}',
                 ]
    if config_s3:
        arguments.append(f'--config-s3={config_s3}')
    else:
        arguments.append(f'--config-s3={default_track_config_s3[tracker]}')
    if save_vid:
        arguments.append('--save-vid')
    print(arguments)

    print(os.listdir(os.getcwd()))
    print(os.getcwd())
    account = config.get_account()
    image_uri = {'deepsort':  f"{account}.dkr.ecr.us-west-2.amazonaws.com/deepsort-yolov5:1.3.2",
                  'strongsort': f"{account}.dkr.ecr.us-west-2.amazonaws.com/strongsort-yolov5:1.0.1"}
    script_processor = ScriptProcessor(command=['python3'],
                                       image_uri=image_uri[tracker],
                                       role=config.get_role(),
                                       instance_count=1,
                                       base_job_name=f'{tracker}-yolov5-{user_name}',
                                       instance_type=instance_type,
                                       volume_size_in_gb=volume_size_gb,
                                       max_runtime_in_seconds=172800,
                                       tags=config.get_tags())
    script_processor.run(code=f'{code_path.parent.parent.parent}/deepsea_ai/pipeline/run_{tracker}.py',
                         arguments=arguments,
                         inputs=[ProcessingInput(
                             source=f's3://{input_s3.netloc}{input_s3.path}',
                             destination='/opt/ml/processing/input')],
                         outputs=[ProcessingOutput(source='/opt/ml/processing/output',
                                                   destination=f's3://{output_s3.netloc}{output_s3.path}')]
                         )


def batch_run(resources: dict, video_path: Path, job_name: str, user_name: str, clean: bool):
    """
    Process a collection of videos in with a cluster in the Elastic Container Service [ECS]
    """
    # the queue to submit the processing message to
    queue_name = resources['VIDEO_QUEUE']

    # Get the service resource
    sqs = boto3.resource('sqs')

    prefix_path = video_path.parent.as_posix().split("Volumes/")[1]

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    message_dict = {"video": f"{prefix_path}/{video_path.name}",
                    "clean": "True" if clean else "False",
                    "user_name": user_name,
                    "job_name": job_name}
    json_object = json.dumps(message_dict, indent=4)

    now = datetime.utcnow()

    # create a message group based on the time; somewhat arbitrary; maybe refine to the hour to avoid collisions
    # from multiple users submitting the same kind of job
    group_id = now.strftime("%Y%m%dT%H%M%SZ")

    # create a new message
    response = queue.send_message(MessageBody=json_object, MessageGroupId=resources['CLUSTER'] + f"{group_id}")
    print(f"Message queued to {queue_name}. MessageId: {response.get('MessageId')}")
