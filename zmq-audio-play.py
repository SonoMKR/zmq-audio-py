#!/usr/bin/env python3

import sys
import zmq
import array

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:1234")
socket.subscribe('')

out_buffer = sys.stdout.buffer

while True:
    audio_data_bytes = socket.recv()

    audio_data =  array.array('f', audio_data_bytes)
    # audio_data contains a list of floats representing audio values

    out_buffer.write(audio_data_bytes)