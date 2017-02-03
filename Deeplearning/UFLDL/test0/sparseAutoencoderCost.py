#! /usr/bin/python2
# -*- coding:utf-8 -*-

import numpy as np


def calcCost(theta, visiableSize, hiddenSize, lambd, sp, beta, data):
    # Get parameters from theta
    '''
    W1 = np.reshape(theta[0:visiableSize * hiddenSize], (hiddenSize, visiableSize))
    W2 = np.reshape(theta[visiableSize * hiddenSize: 2 * visiableSize * hiddenSize], (visiableSize, hiddenSize))
    b1 = np.reshape(theta[2 * visiableSize * hiddenSize: 2 * visiableSize * hiddenSize + hiddenSize], (hiddenSize, 1))
    b2 = np.reshape(theta[2 * visiableSize * hiddenSize + hiddenSize: 2 * visiableSize * hiddenSize + hiddenSize + visiableSize], (visiableSize, 1))
    '''
    W1 = theta[0]
    W2 = theta[1]
    b1 = theta[2]
    b2 = theta[3]
    # Define cost and grad
    cost = 0
    W1grad = np.zeros(W1.shape)
    W2grad = np.zeros(W2.shape)
    b1grad = np.zeros(b1.shape)
    b2grad = np.zeros(b2.shape)
    p = np.zeros(b1.shape)
    m = data.shape[1]
    for i in range(1):
        a1 = np.reshape(data[:, i], (visiableSize, 1))  # (visiableSize,1)
        a2 = sigmoid(np.dot(W1, a1) + b1)  # (hiddenSize,1)
        a3 = sigmoid(np.dot(W2, a2) + b2)  # (visiableSize,1)
        j3 = - (a1 - a3) * a3 * (1 - a3)  # (visiableSize,1)
        j2 = np.dot(W2.T, j3) * a2 * (1 - a2)  # (hiddenSize,1)
        cost += np.linalg.norm(j3)
        W1grad += np.dot(j2, a1.T)
        W2grad += np.dot(j3, a2.T)
        b1grad += j2
        b2grad += j3
        p += a2
    kl = sp * np.log(sp / p) + (1 - sp) * np.log((1 - sp) / (1 - p))
    cost = cost + 0.5 * lambd * (np.sum(W1 * W1) + np.sum(W2 * W2)) + beta * np.sum(kl)
    W1grad = W1grad / m + lambd * np.sum(W1)
    W2grad = W2grad / m + lambd * np.sum(W2)
    b1grad = b1grad / m
    b2grad = b2grad / m
    grad = [W1grad, W2grad, b1grad, b2grad]
    return (cost, grad)


def sigmoid(x):
    return 1. / (1. + np.exp(- x))
