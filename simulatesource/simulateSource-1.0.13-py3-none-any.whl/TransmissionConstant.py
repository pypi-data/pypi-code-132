﻿#*
# * Created by cai on 2020/8/6.
# 
class TransmissionConstant(object):

    #响应轨迹发送
    RESPBOND_TRACK_SEND = 0x01
    #cmd
    START_SIMULATE = 0x01
    STOP_SIMULATE = 0x02
    SET_OUTPUT_SIGNAL_GAIN = 0x10
    SET_SIMULATE_SCENE_TIME = 0x11
    ENABLE_STATIC_SCENE = 0x12
    ENABLE_LOCAL_EPH_DATA = 0x13
    SET_SIMULATESOURCE_DISPLAY_SPEED = 0x14
    SET_RF_TEST_STATE = 0X15
    QUERY_DEVICE_STATE = 0x20
    RESPONSE_DEVICE_TRACE_REQUEST_FRAME = 0x30
    #
    # RETRANSMIT_LAST_EPHTRAN_EXPERT_INDEX = 0x40
    # RETRANSMIT_LAST_TRACETRAN_EXPERT_INDEX = 0x41

    RESET_EPHTRAN_INDEX = 0x40
    RESET_TRACETRAN_INDEX = 0x41

    ENABLE_STATIC = 0x01
