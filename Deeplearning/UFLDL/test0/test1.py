#! /usr/bin/python2
# -*- coding:utf-8 -*-

import sampleImages as sample
import initializeParameters as initPara
import sparseAutoencoderCost as spcost

data = sample.getData()
theta = initPara.initPara(64, 25)

aa = spcost.calcCost(theta, 64, 25, 0.0001, 0.01, 3, data)
print(aa)
