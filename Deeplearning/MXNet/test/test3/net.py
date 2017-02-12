#!/usr/bin/python
# -*- coding:utf-8 -*-

import mxnet as mx


def multi_perceptron(num_hidden):
    data = mx.sym.Variable('data')
    data = mx.sym.Flatten(data=data)
    fc1 = mx.sym.FullyConnected(data=data, name='fc1', num_hidden=num_hidden[0])
    act1 = mx.sym.Activation(data=fc1, name='relu1', act_type='relu')
    fc2 = mx.sym.FullyConnected(data=act1, name='fc2', num_hidden=num_hidden[1])
    act2 = mx.sym.Activation(data=fc2, name='relu2', act_type='relu')
    fc3 = mx.sym.FullyConnected(data=act2, name='fc3', num_hidden=num_hidden[2])
    mlp = mx.sym.SoftmaxOutput(data=fc3, name='softmax')
    return mlp
