#! /usr/bin/python2
# -*- coding:utf-8 -*-

import numpy as np
import scipy.io as spio


def getData():
    # Load IMAGES.mat File
    rawData = spio.loadmat('IMAGES.mat')
    rawImage = rawData['IMAGES']
    # Sample Data
    patchSize = 8
    patchNum = 10000
    patches = np.zeros([patchSize * patchSize, patchNum])
    for i in range(patchNum):
        dim1 = np.random.randint(0, 64, dtype=np.int)
        dim2 = np.random.randint(0, 64, dtype=np.int)
        dim3 = np.random.randint(0, 10, dtype=np.int)
        for m in range(patchSize):
            for n in range(patchSize):
                patches[m * patchSize + n, i] = rawImage[dim1 * patchSize + m, dim2 * patchSize + n, dim3]
    # Normalize Data
    patches = patches - np.mean(patches)
    pstd = 3 * np.std(patches)
    patches = np.maximum(np.minimum(patches, pstd), -pstd) / pstd
    patches = (patches + 1) * 0.4 + 0.1
    return patches
