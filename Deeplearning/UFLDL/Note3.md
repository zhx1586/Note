# 卷积神经网络

## 概述

卷积神经网络（CNN）包括一个或多个（往往带有子采样步骤的）卷积层，之后是一个或多个标准多层神经网络中的全连接层。
CNN的架构被设计为便于利用输入图像的二维结构的形式。这种架构通过局部连接和绑定参数来实现，之后是几种形式的池化层，这些池化层会产生移不变特性。
CNN的另一个优势在于，它们更加便于训练，并且与含有同样数目隐藏单元的全连接网络相比，所包含的参数数目更少。
在这篇文章中，我们会讨论CNN的架构和根据模型中的参数计算梯度的反向传播算法，以便对模型进行基于梯度的优化。

## 架构

CNN 由大量的卷积层和子采样层组成，之后是可选的全连接层。
卷积层的输入是 $m\times m\times r$ 的图片，其中 $m$ 表示图像的高度和宽度，$r$ 表示图像的通道数。
卷积层含有 $k$ 个大小为 $n \times n \times q$ 的滤波器（卷积核）。
滤波器的大小会导致局部连接的结构，与图像卷积后产生 $k$ 个大小为 $m-n+1$ 的特征映射。
接下来每个映射在 $p\times p$大小的连续区域上通过最大值池化或均值池化来进行子采样，其中 $p$ 范围通常为为 $2～5$（与图像尺寸有关，随图像尺寸增大而增大）。
在子采样层的之前或者之后，一个额外的偏置和sigmoid非线性特性会被应用到每一个特征映射。
之后会有一层或者多层与标准多层神经网络中相同的全连接层。

## 反向传播

令 $\delta^{(l+1)}$ 为网络中第 $l+1$ 层对于损失函数 $J(W,b;x,y)$ 的误差项。
如果第 $l$ 层与第 $l+1$ 层是全连接的，那么 $\delta^{(l)}$ 可由下式计算得到
$$ \delta^{(l)} = \bigg(\big(W^{(l)}\big)^T \delta^{(l+1)}\bigg) \cdot f'\big(z^{(l)}\big)$$
并且梯度为
$$ \nabla_{W^{(l)}} J(W,b;x,y) = \delta^{(l+1)}\big(a^{(l)}\big)^T $$
$$ \nabla_{b^{(l)}} J(W,b;x,y) = \delta^{(l+1)} $$
如果第 $l$ 层是卷积和子采样层，那么误差反向传播的公式为：
$$ \delta_k^{(l)}  = upsample\bigg(\big(W_k^{(l)}\big)^T \delta_k^{(l+1)}\bigg) \cdot f'(z_k^{(l)})$$
其中 $k$ 指示着滤波器的序号，$f'(z_k^{(l)})$ 是激活函数的导数。
$upsample$ 操作用于传递误差通过池化层，通过计算相对每个池化层输入单元的误差 $w.r.t$。





