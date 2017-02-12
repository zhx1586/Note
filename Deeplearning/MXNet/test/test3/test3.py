#!/usr/bin/python
# -*- coding:utf-8 -*-

import mxnet as mx
import logging as log
import mnist
import net

# Set Log
log.getLogger().setLevel(log.DEBUG)

# Init Net
# MLP       [128, 64, 10]  0.9676
#            [50, 24, 10]  0.9655
#            [48, 24, 10]  0.9604
#            [60,  5, 10]  0.9586
#            [48,  4, 10]  0.9554
#           [200, 50, 10]  0.9707
#          [500, 120, 10]  0.9743
#         [1500, 120, 10]  0.9741
mlp = net.multi_perceptron([1500, 120, 10])

model = mx.model.FeedForward(
    ctx=mx.gpu(),
    symbol=mlp,
    num_epoch=10,
    learning_rate=0.1
)

# Init Dataset
mnist = mnist.MNIST()
batch_size = 100

model.fit(
    X=mnist.get(batch_size),
    eval_data=mnist.get(batch_size, isTrain=False),
    batch_end_callback=mx.callback.Speedometer(batch_size, 200)
)
