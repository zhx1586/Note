# Softmax Regression

Softmax Regression allows us to handle $y^{(i)} \in \{1,\cdots,K\}$ where $K$ is the number of classes.

## Hypothesis

Our hypothesis $h_\theta(x)$ takes the form

\begin{equation\*}
h_\theta(x) = 
\begin{bmatrix}
P(y=1|x;\theta)  \\\
P(y=2|x;\theta)  \\\
\vdots \\\
P(y=K|x;\theta)
\end{bmatrix}
= \frac{1}{\sum_{j=1}^K e^{\theta^{(j)T} x}}
\begin{bmatrix}
e^{\theta^{(1)T} x}  \\\
e^{\theta^{(2)T} x}  \\\
\vdots  \\\
e^{\theta^{(K)T} x}  
\end{bmatrix}
\end{equation\*}

where $\theta^{(1)}, \theta^{(2)}, \cdots, \theta^{(K)} \in R^n$ are the parameters of our model and the term $\sum_{j=1}^K e^{\theta^{(j)T} x}$ is used to normalize the distribution.

For convenience, we write an $n\times K$ matrix $\theta$ to denote all the parameters in the model.

$$ \theta = [\theta^{(1)}, \theta^{(2)}, \cdots, \theta^{(K)}] $$

## Cost Function

The cost function of Softmax Regression is :

\begin{equation\*}
J(\theta) = - \sum_{i=1}^m \sum_{k=1}^K 1\\{y^{(i)}=k\\} \log \frac{e^{\theta^{(k)T}x}} {\sum_{j=1}^K e^{\theta^{(j)T}x}}
\end{equation\*}

And the gradient is :

\begin{equation\*}
\nabla_{\theta^{(k)}} J(\theta) = -\sum_{i=1}^m x^{(i)}\bigg(1\big\\{y^{(i)}=k\big\\} - P\big(y^{(i)}=k|x^{(i)};\theta\big)\bigg)
\end{equation\*}
