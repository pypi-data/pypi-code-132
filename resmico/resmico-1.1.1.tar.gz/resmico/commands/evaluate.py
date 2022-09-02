from __future__ import print_function
from pkg_resources import resource_filename
import os
import argparse
import logging

from resmico import evaluate
from resmico.commands import arguments


# functions
def get_desc():
    desc = 'Evaluate model'
    return desc


def parse_args(test_args=None, subparsers=None):
    desc = get_desc()
    epi = """DESCRIPTION:
    Evaluate trained resmico model or the one generated by `resmico train`.

    Contig features used for evaluation must have been generated with resmico-sm.
    """
    if subparsers:
        parser = subparsers.add_parser('evaluate', description=desc, epilog=epi,
                                       formatter_class=argparse.RawTextHelpFormatter)
    else:
        parser = argparse.ArgumentParser(description=desc, epilog=epi,
                                         formatter_class=argparse.RawTextHelpFormatter)

    # default trained model
    pkg_model = resource_filename('resmico', 'model/resmico.h5')
    parser_g1 = parser.add_argument_group('Evaluation-specific arguments')
    parser_g1.add_argument('--model', default=pkg_model, type=str,
                        help='Location of the saved deep learning model (default: %(default)s)')
    parser_g1.add_argument('--batch-size', default=100, type=int,
                        help='Batch size (default: %(default)s)')
    parser_g1.add_argument('--embeddings', action='store_true', default=False,
                        help='Produce embeddings for an intermidiate layer (default: %(default)s)')
    parser_g1.add_argument('--emb-ind', default=0, type=int,
                        help='Layer index to produce embedding (default: %(default)s)')
    parser_g1.add_argument('--verify-insert-size', action='store_true', default=False,
                        help='Check if the insert size distribution is similar to the n9k-train dataset (default: %(default)s)')
    arguments.add_common_args(parser)

    # running test args
    if test_args:
        args = parser.parse_args(test_args)
        return args

    return parser


def main(args=None):
    if args is None:
        args = parse_args()

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging._nameToLevel[args.log_level.upper()])

    print()
    print(args)
    print()
    evaluate.main(args)


if __name__ == '__main__':
    pass
