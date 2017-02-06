#!/usr/bin/python
# -*- coding:utf-8 -*-

from sklearn.datasets import fetch_mldata
import numpy as np
import mxnet as mx
import matplotlib.pyplot as plt


class MNIST():
    def __init__(self):
        mnist = fetch_mldata('MNIST original', data_home='~/Datasets/')
        self.num_train = 60000
        self.num_test = 10000
        p_train = np.random.permutation(self.num_train)
        p_test = self.num_train + np.random.permutation(self.num_test)
        self.X_train = mnist.data[p_train].reshape(self.num_train, 1, 28, 28).astype(np.float32) / 255
        self.Y_train = mnist.target[p_train]
        self.X_test = mnist.data[p_test].reshape(self.num_test, 1, 28, 28).astype(np.float32) / 255
        self.Y_test = mnist.target[p_test]
        self.pos = 0

    def get(self, batch_size, isTrain=True):
        if isTrain:
            data_iter = mx.io.NDArrayIter(self.X_train, self.Y_train, batch_size, shuffle=True)
        else:
            data_iter = mx.io.NDArrayIter(self.X_test, self.Y_test, batch_size)
        return data_iter

    def plot(self):
        for i in range(10):
            plt.subplot(1, 10, i + 1)
            plt.imshow(self.X_train[i].reshape(28, 28), cmap='Greys_r')
            plt.axis('off')
        print('label: %s' % (self.Y_train[0:10]))
        plt.show()
