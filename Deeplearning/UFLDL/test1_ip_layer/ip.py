#!/usr/bin/python2
# -*- coding:utf-8 -*-

import numpy as np


class LOSS:
    def forward(self, y, t):
        self.loss_y = y - t
        self.loss = np.sum(self.loss_y * self.loss_y) / self.loss_y.shape[1] / 2
        return self.loss

    def backward(self):
        return self.loss_y


class IP:
    def __init__(self, input_size, output_size, learning_rate):
        self._input_size = input_size
        self._output_size = output_size
        self.w = np.random.randn(self._output_size, self._input_size)  # (output_size, input_size)
        self.b = np.zeros((self._output_size, 1))  # (output_size, 1)

    def _sigmoid(self, x):
        return 1. / (1. + np.exp(- x))

    def forward(self, data):
        self.top_val = np.dot(self.W, data) + self.b  # (output_size, N)
        self.botto_val = data  # (input_size, N)
        return self.top_val

    def backward(self, loss):
        loss_z = loss * self.top_val * (1 - self.top_val)  # (output_size, N)
        grad_w = np.dot(loss_z, self.botto_val.T)  # (output_size, input_size)
        grad_b = np.dot(loss_z, np.ones((loss_z.shape[1], 1)) / loss_z.shape[1])  # (output_size, 1)
        self.w -= self.learning_rate * grad_w
        self.b -= self.learning_rate * grad_b
        loss_x = np.dot(self.w.T, loss_z)  # (input_size, N)
        return loss_x
