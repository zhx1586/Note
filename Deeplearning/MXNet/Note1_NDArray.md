# NDArray

## The Basic

Important attributs: 
    
    nd.shape 
    nd.dtype
    nd.size
    nd.context

#### Array creation

Create from a regular Python list or tuple.

    a = mx.nd.array([[1, 2, 3]])

Create from an Numpy.ndarray. In default, dtype is `np.float32`

    c = np.arange(15).reshape(3, 5)
    a = mx.nd.array(c)

Create from functions.

    c = mx.nd.zeros((2, 3))
    c = mx.nd.ones((2, 3))
    c = mx.nd.full((2, 3), 7)
    c = mx.nd.empty((2, 3))

#### Printing Arrays

    b = mx.nd.ones((2, 3))
    b.asnumpy()

#### Basic operations

Arithmetic operators on arrays apply elementwise.

The matrix-matrix multiplication is `mx.nd.dot()`

#### Indexing and Slicing 

The slice operator `[]` applies on axis 0. 
We can also slice a particular axis with the method `mx.nd.slice_axis()`

    a = mx.nd.ones((2,3))
    d = mx.nd.slice_axis(a, axis = 1, begin = 1, end = 2)

#### Shape Manipulation

    a = mx.nd.array(np.arange(24))
    b = a.reshape((2, 3, 4))

Method `mx.nd.concatenate` stacks multiple arrays along the first dimension. (Their shapes must be the same).

    a = mx.nd.ones((2, 3))
    b = mx.nd.ones((2, 3)) * 2
    c = mx.nd.concatenate([a, b])

#### Reduce

Reduce an array to a scalar,

    a = mx.nd.ones((2, 3))
    b = mx.nd.sum(a)

or along a particular axis.

    c = mx.nd.sum_axis(a, axis = 1)

#### Broadcast

    a = mx.nd.array(np.arange(6).reshape((6,1))
    b = a.broadcast_to(6, 2)

Broadcast can be applied to operations such as * and +.

    a = mx.nd.ones((1, 2))
    b = mx.nd.ones((3, 2))
    c = a + b

#### Copies

Pass by reference (assign, slice, return by a function)

    a = mx.nd.ones((2, 3))
    b = a
    b is a

    True

    a = mx.nd.ones((2, 3))
    b = a[:]
    b is a

    True

    def f(x):
        return x
    a is f(a)

    True

Pass by value (`a.copy()`)

    a = mx.nd.ones((2, 3))
    b = a.copy()
    b is a

    False

## The Advanced

#### GPU Support

Manage the data between CPU and GPU.

    a = mx.nd.ones((2, 3), mx.gpu())

    with mx.Context(mx.gpu()):
        f()

    a = mx.nd.ones((2, 3))
    b = a.as_in_context(mx.gpu())

#### Serialize from/to (Distributed) Filesystems

Save data to disk or load data from disk: 

    a = mx.nd.ones((2, 3))
    b = mx.nd.ones((2, 3))
    mx.nd.save("temp1.ndarray",[a, b])
    c = mx.nd.load("temp1.ndarray")

or

    a = mx.nd.ones((2, 3))
    b = mx.nd.ones((2, 3))
    d = {'a': a, 'b': b}
    mx.nd.save("temp2.ndarray",d) 
    c = mx.nd.load("temp2.ndarray")





