# Part I  Linear Regression

## 0 Basic conceptions 
    
The $j$-th feature of the $i$-th sample : $ x_j^{(i)} $ 

Parameter : $ \theta = [\theta_0, \cdots ,\theta_n]^T $

Hypotheses (corresponding to sample):     

\begin{equation\*}
   h_\theta(x^{(i)}) = \sum_{j=0}^n \theta_j x_j^{(i)} = \theta^T x^{(i)}
\end{equation\*}

Cost function (corresponding to feature):

\begin{equation\*}
    J(\theta) = \frac{1}{2} \sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2
\end{equation\*}

## 1 LMS algorithm (Least Mean Square algorithm)

Gradient descent algorithm

\begin{equation\*}
    \theta_j := \theta_j - \alpha \frac {\partial} {\partial \theta_j} J(\theta)
\end{equation\*}

where 

\begin{equation\*}
    \frac {\partial} {\partial \theta_j} J(\theta) = (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}
\end{equation\*}

and $\alpha$ is called learning rate.

Therefore, the rule for only one training sample is:

\begin{equation\*}
    \theta_j := \theta_j	+ \alpha (y^{(i)} - h_\theta(x^{(i)})) x_j^{(i)}
\end{equation\*}

For more than one example, we can use 

####1.1 Batch Gradient Descent

In every training step, update every $\theta_j$ with $\vec{x} = [x^{(1)}, \cdots, x^{(m)}]^T$. 

####1.2 Stochstic Gradient Descent

In every training step, update every $\theta_j$ with only one $x^{(i)}$.

## 2 Normal equation

With the help of matrix derivations, we get that

\begin{aligned}
	\nabla_\theta J(\theta)  &=  \nabla_\theta \frac {1} {2} (X\theta - \vec{y})^T(X\theta - \vec{y})  \\\
	&= X^TX\theta - X^T\vec{y}  \\\
	&= 0 
\end{aligned}

Then we get the normal equation

\begin{equation\*}
	X^TX\theta = X^T\vec{y}
\end{equation\*}

Therefore we can get $\vec{y}$ directly

\begin{equation\*}
	\theta = (X^TX)^{-1}X^T\vec{y}
\end{equation\*}

## 3 Local weighted linear regression

LWR algorithm, assuming there is sufficient training data, can make the choice of features less critical.

To use this algrithm, we need to change the definition of the cost function.

\begin{equation\*}
	J(\theta) = \sum_{i=0}^m \omega^{(i)}(y^{(i)} - h_\theta(x^{(i)}))
\end{equation\*} 

where 

\begin{equation\*}
	\omega^{(i)} = e^{-\frac {(x^{(i)}-x)^2}{2\tau^2}}
\end{equation\*}

# Part II Classification and Logistic Regression

## 1 Logistic Regression

Hypotheses : 

  $$ h_\theta (x) = g(\theta^T x) = \frac {1} {1 + e^{-\theta^T x } } $$

where 

  $$ g(z) = \frac {1} {1 + e^{-z}} $$

is called logisitic function or sigmoid function.

The deriviation of $g(z)$ has a useful property, which is 

  $$ g'(z) = g(z)(1 - g(z)) $$

With the help of the property, we can get the update rule of $\theta$ for this algorithm

  $$ \theta_j := \theta_j + \alpha (y^{(i)} - h_\theta (x^{(i)})) x_j^{(i)} $$

## 2 Perceptron Learing Algorithm

Hypotheses :
	
  $$ h_\theta (x) = g(\theta^T x) $$

where 

\begin{equation\*}
    g(z) = 
    \begin{cases}
    1 & \quad x\ge0 \\\
    0 & \quad x < 0
    \end{cases}
\end{equation\*}

Update rule:

  $$ \theta_j := \theta_j + \alpha (y^{(i)} - h_\theta (x^{(i)})) x_j^{(i)} $$





    

