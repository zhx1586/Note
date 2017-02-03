#! /usr/bin/python2
# -*- coding:utf-8 -*-

import numpy as np


def initPara(visiableSize, hiddenSize):
    r = np.sqrt(6) / np.sqrt(visiableSize + hiddenSize + 1)
    W1 = np.random.rand(hiddenSize, visiableSize) * 2 * r - r
    W2 = np.random.rand(visiableSize, hiddenSize) * 2 * r - r
    b1 = np.zeros((hiddenSize, 1))
    b2 = np.zeros((visiableSize, 1))
    return [W1, W2, b1, b2]
