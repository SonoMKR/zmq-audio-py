# Send Audio through Zeromq

This project demonstrates how to send audio on the network via [ZeroMQ](https://zeromq.org)
This exemple uses the `arecord` and `aplay` available on most Linux distributions.

## Install

`pip install pyzmq`

## Using

on one terminal use :

`arecord -D plughw:0,0 -r 8000 -f FLOAT_LE | ./zmq-audio-record.py`

on the other use :

`./zmq-audio-play.py | aplay -D plughw:0,0 -r 8000 -f FLOAT_LE`
