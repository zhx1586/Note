# Back-propagation Algortithm

## 1 Neural Network model

$n_l$: the number of layers in the network

$L_l$: the $l$-th layer in the network, therefore $L_1$ is the input layer and $L_{n_l}$ is the output layer 

$(W,b)$: the parameters

$$(W,b)=(W^{(1)},b^{(1)},\cdots,W^{(n_l-1)},b^{(n_l-1)})$$

$W_{ij}^{(l)}$: the weight associated with the connection between the $j$-th unit in the layer $L_l$ and the $i$-th unit in the layer $L_{l+1}$

$b_i^{(l)}$: the bias associated with the $i$-th unit in the layer $L_{l+1}$

$z_i^{(l)}$: the inner product of the input to the $i$-th unit in layer $L_l$

$a_i^{(l)}$: the activation of the $i$-th unit in the layer $L_l$

$$z^{(l+1)} = W^{(l)}a^{(l)}+b^{(l)}$$

\begin{equation\*}
a^{(l+1)} = 
            \begin{cases}
            f(z^{(l+1)}) \quad &l \ge 1\\\
            x  &l=0
            \end{cases} 
\end{equation\*}

$$h_{W,b}(x) = a^{(n_l)}$$

## 2 Back-propagation Algorithm

Given a training set $\{(x^{(1)},y^{(1)}),\cdots,(x^{(m)},y^{(m)})\}$ of $m$ training examples

Define the cost function with respect to one example to be:

$$J(W,b;x,y) = \frac{1}{2}\|h_{W,b}(x)-y\|^2$$

Define the overall cost function of m examples to be:

\begin{aligned}
J(W,b)&=\bigg[\frac{1}{m} \sum_{i=1}^m J(W,b;x^{(i)},y^{(i)})\bigg]+\frac{\lambda}{2} \sum(W_{ij}^{(l)})^2 \\\
      &=\bigg[\frac{1}{m} \sum_{i=1}^m\bigg(\frac{1}{2}\|h_{W,b}(x)-y\|^2\bigg)\bigg]+\frac{\lambda}{2} \sum(W_{ij}^{(l)})^2 
\end{aligned}

The term $\frac{\lambda}{2} \sum(W_{ij}^{(l)})^2$ is a regularization term (also called a weight decay term) that tends to decrease the magnitude of the weights and helps prevent overfitting

Our goal is to minimize $J(W,b)$ as a function of $W$ and $b$.

Update rules for $W$ and $b$ :

$$ W_{ij}^{(l)} = W_{ij}^{(l)} - \alpha \frac {\partial}{\partial W_{ij}^{(l)}} J(W,b)$$

$$ b_i^{(l)} = b_i^{(l)} - \alpha \frac {\partial}{\partial  b_i^{(l)}} J(W,b)$$

where $\alpha$ is the learning rate.

Define error term of the unit in the output layer to be:

\begin{aligned}
\delta_i^{(n_l)} &= \frac {\partial}{\partial z_i^{(n_l)}} \frac{1}{2} \|y-h_{W,b}(x)\|^2 \\\
&= -(y_i-a_i^{(n_l)}) f'(z_i^{(n_l)})
\end{aligned}

Define error term of the unit in the hidden layer to be:

$$\delta_i^{(l)}=\bigg(\sum_{j=1}^{s_l+1}W_{ij}^{(l)}\delta_j^{(l+1)}\bigg)f'(z_i^{(l)})$$

Therefore we can get the desired partial derivatives:

$$\frac {\partial}{\partial W_{ij}^{(l)}} J(W,b;x,y) = a_j^{(l)}\delta_i^{(l+1)}$$

$$\frac {\partial}{\partial b_i^{(l)}}J(W,b;x,y) = \delta_i^{(l+1)}$$

In matrix-vectorial notation:

- Backward Propagation: 

$$ f'(z_i^{(l)}) = a_i^{(l)}\big(1-a_i^{(l)}\big)$$

$$\vec\delta^{(n_l)} = -(\vec y - \vec a^{(n_l)})*f'(z^{(n_l)}) $$

$$\vec \delta^{(l)} = \big((\vec W^{(l)})^T\vec\delta^{(l+1)})\big)*f'(z^{(l)})$$

- The desired partial derivatives:

$$\nabla_{W^{(l)}} J(W,b;x,y) = \delta^{(l+1)}\big(a^{(l)}\big)^T$$

$$\nabla_{b^{(l)}} J(W,b;x,y) = \delta^{(l+1)}$$

## 3 Summery: A iteration of batch gradient descent

- 1 Set $\Delta W^{(l)} = \vec 0$,$\Delta b^{(l)} = \vec 0$ for all $l$

- 2 For i = 1 to m,
    
    - a Use back-propagation to compute $\nabla_{W^{(l)}} J(W,b;x,y)$ and $\nabla_{b^{(l)}} J(W,b;x,y)$
    - b Set $\Delta W^{(l)} = \Delta W^{(l)} + \nabla_{W^{(l)}} J(W,b;x,y)$
    - c Set $\Delta b^{(l)} = \Delta b^{(l)} + \nabla_{b^{(l)}} J(W,b;x,y)$

- 3 Update the parameters:
$$ W^{(l)} = W^{(l)} - \alpha \bigg[\bigg(\frac{1}{m} \Delta W^{(l)}\bigg)+\lambda W^{(l)}\bigg]$$

$$ b^{(l)} = b^{(l)} - \alpha\bigg[\frac{1}{m}\Delta b^{(l)}\bigg] $$

## 4 Gradient Checking

Back-propagation is difficult to debug and therefore we need another method to make sure we have the right implementation of it.

## 5 Advanced Optimization

L-BFGS Algorithm 

Conjugate Gradient Algorithm











