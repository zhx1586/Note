# 02_GBDT

## 1 引言

- 全称为 Gradient Boosting Decision Tree，是一种常用的 Ensemble Learning 算法。
- 包含两个概念
  - GB（Gradient Boosting）：模型融合方法。
  - DT（Decision Tree）：弱分类器。

## 2 Boosting 算法

- 核心思想：给定仅比随机预测略好的弱学习算法，将其提升为强学习算法。

### 2.1 AdaBoost

- 概述：AdaBoost （Adaptive Boosting）针对的是两分类问题。

- 算法：

    ![](http://ww1.sinaimg.cn/large/005Npy0Fly1fuywwtg9soj30k00dbjss.jpg)

- 理解：
  - **算法本质：**迭代更新样本分布，然后对新的分布下的样本学习一个弱分类器，以及对应的权重。
  - **样本分布的更新规则：**减小之前弱分类器分类效果较好的数据的概率，增大之前弱分类器分类效果较差的数据的概率。
  - **最终的分类器：** 多个弱分类器的线性组合。

### 2.3 Gradient Boosting

- 概述：GB 每一次建立模型是在之前建立模型的损失函数的梯度下降方向。

- 算法：

  ![](http://ww1.sinaimg.cn/large/005Npy0Fly1fuyxh8fupxj30d4062aac.jpg)

- 