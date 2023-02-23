#!/usr/bin/env python3

import sys
import zmq
import array

BLOCK_SIZE = 1024

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:1234")

input_buffer = sys.stdin.buffer

while True:
    audio_data_bytes =  input_buffer.read(BLOCK_SIZE)

    audio_data = array.array('f', audio_data_bytes)
    # audio_data contains a list of BLOCK_SIZE // 4 floats representing audio values

    socket.send(audio_data_bytes)