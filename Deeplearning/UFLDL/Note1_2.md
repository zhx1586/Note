# Sparse Autoencoder

## 1 Autoencoder

An autoencoder nerual network is an unsupervised learning alogrithm that applies backpropagation, setting the target values to be equal to the inputs, which tries to learn a function $h_{W,b}(x) = x$.

## 2 Sparsity

By placing constraints on the network, such as by limiting the number of the hidden units, we can discover insteresting structure about the data because the network is forced to learn a compressed representation.

## 3 Implementation

We would like to constrain the neurons to be inactive most of the time. 

Let $a_j^{(2)}(x)$ denote the activation of the hidden unit $j$ when the network is given a specific input $x$.

Further, let 

$$\hat\rho_j = \frac{1}{m}\sum_{i=1}^m\bigg[a_j^{(2)}(x^{(i)})\bigg]$$

be the average activation of hidden unit $j$ (averaged over the training set).



