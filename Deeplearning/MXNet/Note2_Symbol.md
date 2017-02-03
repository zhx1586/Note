# Symbol

## Symbol Composition

#### Basic Opearators

Create the placeholder

    a = mx.sym.Variable('a')

Most NDArray operators can be applied to Symbol

    a = mx.sym.Variable('a')
    b = mx.sym.Variable('b')
    c = a + b
    d = a * b
    e = mx.sym.dot(a, b)
    f = mx.sym.Reshape(d + e, shape = (1, 4))
    g = mx.sym.broadcast_to(f, shape = (2, 4))
    mx.viz.plot_network(symbol = g)

#### Basic Neural Networks

    net = mx.sym.Variable('data')
    net = mx.sym.FullyConnected(data=net, name='fc1', num_hidden=128)
    net = mx.sym.Activation(data=net, name='relu1', act_type="relu")
    net = mx.sym.FullyConnected(data=net, name='fc2', num_hidden=10)
    net = mx.sym.SoftmaxOutput(data=net, name='out')
    mx.viz.plot_network(net, shape={'data':(100,200)})

#### Modulelized Construction for Deep Networks

    def ConvFactory(data, num_filter, kernel, stride=(1,1), pad=(0, 0), name=None, suffix=''):
        conv = mx.symbol.Convolution(data=data, num_filter=num_filter, kernel=kernel, stride=stride, pad=pad, name='conv_%s%s' %(name, suffix))
        bn = mx.symbol.BatchNorm(data=conv, name='bn_%s%s' %(name, suffix))
        act = mx.symbol.Activation(data=bn, act_type='relu', name='relu_%s%s' %(name, suffix))
        return act
    prev = mx.symbol.Variable(name="Previos Output")
    conv_comp = ConvFactory(data=prev, num_filter=64, kernel=(7,7), stride=(2, 2))
    shape = {"Previos Output" : (128, 3, 28, 28)}
    mx.viz.plot_network(symbol=conv_comp, shape=shape)

## Symbol Manipulation

#### Shape Interface

For each symbol, we can query its inputs (or arguments) and outputs. 

    arg_name = c.list_arguments()  # get the names of the inputs
    out_name = c.list_outputs()    # get the names of the outputs
    arg_shape, out_shape, _ = c.infer_shape(a=(2,3), b=(2,3))  

#### Band with Data and Evaluate

    # Define the symbols
    a = mx.sym.Variable('a')
    b = mx.sym.Variable('b')
    c = a + b
    # Bind symbol with NDArray
    ex = c.band(ctx =   mx.gpu(),args={'a':mx.nd.ones((2,3),mx.gpu()),'b':mx.nd.ones((2,3),mx.gpu())})
    # Excute
    ex.forward()
    # Get the output
    ex.outputs[0].asnumpy()

#### Load and Save

    c.save('symbol-c.json')
    c2 = mx.symbol.load('symbol-c.json')

#### Customized Symbol

## Advanced Usage

#### Type Cast

    a = mx.sym.Variable('data')
    b = mx.sym.Cast(data = a, dtype = 'float16')

#### Variable Sharing

    a = mx.sym.Variable('a')
    b = mx.sym.Variable('b')
    c = mx.sym.Variable('c')
    d = a + b * c
    # 
    data = mx.nd.ones((2,3))*2
    ex = d.bind(ctx=mx.cpu(), args={'a':data, 'b':data, 'c':data})
    ex.forward()
    ex.outputs[0].asnumpy()
