# Pytorch 教程笔记

## 1 Tensors （张量）运算

- 创建一个 Tensor

  ```python
  import torch
  
  x = torch.empty(5, 3) # 创建一个 5*3 大小的未初始化矩阵
  x = torch.rand(5, 3) # 创建一个 5*3 大小的随机初始化的矩阵
  x = torch.zeros(5, 3, dtype=torch.long) # 创建一个 5*3 大小、数据类型为 long 、初始化为 0 的矩阵
  
  x = torch.tensor([5.5 3]) # 直接使用数据创建 Tensor
  
  x = x.new_ones(5, 3, dtype=torch.double) # 使用已有的 Tensor 创建 Tennsor，重用未显式指明的属性
  x = torch.randn_like(x, dtype=torch.float) # 使用已有的 Tensor 创建 Tennsor，重用未显式指明的属性
  ```

-  Tensor 相关操作

  ```python
  x = torch.rand(5, 3)
  y = torch.rand(5, 3)
  
  z = x + y # 加法运算，形式1
  z = torch.add(x, y) # 加法运算，形式2
  torch.add(x, y, out=z) # 加法运算，形式3
  y.add_(x) # 加法运算，形式4
  
  z = x[:, 1] # 与 NumPy 类似的索引操作
  
  x = torch.rand(4, 4) 
  y = x.view(16) # 使用 view方法 改变 Tensor 的大小
  z = x.view(-1, 8) # view方法 中的 -1 表示该维度的大小由其它维度计算得到
  
  x = torch.rand(1) 
  y = x.item() # 使用 item方法 将只含有一个元素的 Tensor 转化为 Python 内置类型的数值
  ```

- Tensor 与 NumPy 的转换

  ```python
  a = torch.ones(5)
  b = a.numpy() # 将 Tensor 转换为 NumPy Array
  
  a = np.ones(5)
  b = torch.form_numpy(a) # 将 NumPy Array 转换为 Tensor
  ```

  - 注意：`Tensor` 和 `NumPy Array` 在转换前后使用相同的内存空间

- Tensor 与 CUDA Tensor 的转换

  ```python
  a = torch.ones(2, 3) # 创建一个 TensorT
  b = a.to("cuda") # 使用 to方法 将 Tensor 转换为 Cuda Tensor
  
  a = torch.ones(2, 3, device="cuda") # 创建一个 Cuda Tensor
  b = a.to("cpu") #  使用 to方法 将 Cuda Tensor 转换为 Tensor
  ```

## 2 AutoGrad：自动求导

- Tensor 中与 AutoGrad 相关的属性

  - `Tensor.requires_grad` ：
    - 置为`True` 时，torch 会记录所有与之相关的操作，并在 `backward()` 调用时为其自动计算梯度。
    - 使用`with torch.no_grad():` 的代码块中 Tensor 的该属性为 `False` 。
  - `Tensor.grad` ：
    - 存放自动计算得到的梯度的值。

  - `Tensor.grad_fn` ：
    - 当 Tensor 是由其它 Tensor 计算得到（而不是直接创建）时，存放生成该 Tensor 使用的操作。
  - `Tensor.retain_grad()`：
    - 为非叶节点的 Tensor 保存梯度信息。
  - `Tensor.backward(gradient=None)`：
    - 计算当前 Tensor 相对于计算图中叶节点的梯度。
    - 当前 Tensor 含有多个元素时需要显式地指定 `gradient`参数。
    - 计算前应注意清空原有的梯度信息。

- `autograd` 如何记录操作历史

  - `autograd` 是反向自动求导系统。从概念上来讲，`autograd` 记录一张图，记录执行操作时所有创建数据的操作，最终得到一张有向无环图，图中的叶节点对应输入张量，图中的根节点对应输出张量。通过从根节点到叶节点回溯这张图，你可以使用微积分中的链式法则自动地计算梯度。
  - 在内部，`autograd` 将此图表示为 `Function` 对象的图（真实实现），可以使用 `apply()` 来计算图的输出结果。在进行前向传播计算时，`autograd`在执行请求的计算的同时构建一张图来表示用于计算梯度的函数（Tensor 的 `grad_fn` 属性正是这张图的一个入口点）。前向传播完成后，我们在反向传播过程中使用这张图来计算梯度。
  - 值得重视的一点是，在每次迭代中计算图都会被从头构建，这也正是任意的 Python 控制语句都能够使用的原因，在每次迭代过程中都可以改变整张图的形状和大小。在开始训练之前不必将所有可能的路径编码，求导在运行时执行（what you run is what you differentiate）。

- 注意：在使用 `autogard` 时应当尽量避免使用就地操作（in-place operations）。

## 3 构建 NN（神经网络）

- 使用 `torch.nn` 来构建神经网络。`nn` 依靠 `autograd` 来定义模型和对模型求导。

- 基本流程：

  - 定义包含一系列可学习的参数（权重）的网络；
  - 在数据集上迭代获得输入；
  - 完成输入的前向传播；
  - 计算损失函数；
  - 完成误差的反向传播；
  - 更新网络中的可学习参数（权重）。

- 定义网络（继承 `nn.Module`）

  ```python
  import torch
  import torch.nn as nn
  import torcn.nn.functional as F
  
  class Net(nn.Module):
      
      def __init__(self):
          super(Net, self).__init__()
          self.conv1 = nn.Conv2d(1, 6, 5)
          self.conv2 = nn.Conv2d(6, 16, 5)
          self.fc1 = nn.Linear(16*5*5, 120)
          self.fc2 = nn.Linear(120, 84)
          self.fc3 = nn.Linear(84, 10)
          
      def forward(self, x):
          x = F.max_pool2d(F.relu(self.conv1(x)), 2)
          x = F.max_pool2d(F.relu(self.conv2(x)), 2)
          x = x.view(-1, self.num_flat_features(x))
          x = F.relu(self.fc1(x))
          x = F.relu(self.fc2(x))
          x = self.fc3(x)
          return x
      
      def num_flat_features(self, x):
          size = x.size()[1:]
          num_features = 1
          for s in size:
              num_features *= s
          return num_features
  
      
  net = Net()
  
  ```

- 前向传播

  ```python
  output = net(input)
  ```

- 计算损失函数

  ```python
  criterion = nn.MSELoss()
  loss = criterion(output, target)
  ```

- 反向传播

  ```python
  net.zero_grad()
  loss.backward()
  ```

- 更新参数（权重）

  ```python
  import torch.optim as optim
  
  optimizer = optim.SGD(net.parameters(), lr=0.01)
  
  optimizer.step()
  ```

## 4 自定义数据集类

- `torch.utils.data.Dataset` 是一个用于表示数据集的抽象类。自定义数据集类应当继承自 `Dataset`类并重写下面的两个方法：

  - `__len__` ：返回数据集的大小；
  - `__getitem__` ：提供下标索引操作支持。

  ```python
  import os
  import torch
  import pandas as pd
  from skimage import io, transform
  from torch.utils.data import Dataset, DataLoader
  
  class FaceLandmarksDataset(Dataset):
      
      def __init__(self, csv_file, root_dir, transform=None):
          self.landmarks_frame = pd.read_csv(csv_file)
          self.root_dir = root_dir
          self.transform = transform
      
      def __len__(self):
          return len(self.landmarks_frame)
      
      def __getitem(self, idx):
          img_name = os.path.join(self.root_dir, self.landmarks_frame.iloc[idx, 0])
          image = io.imread(img_name)
          landmarks = self.landmarks_frame.iloc[idx, 1:].as_matrix()
          landmarks = landmarks.astype('float').reshape(-1, 2)
          sample = {'image': image, 'landmarks': landmarks}
         	if self.transform:
              sample = self.transform(sample)
          return sample
      
  ```

- 自定义变换 `transforms`

  - 将其实现为可调用类，而不是简单的函数，从而不必在每次调用时都传入变换相关的参数。

  - 自定义变换继承自 `object` 类，需要实现其 `__call__` 方法，必要时也需要实现其 `__init__` 方法。

  - 调用效果

    ```python
    tsfm = Transform(params)
    transformed_sample = tsfm(sample)
    ```

  - 自定义变换的实例 `Rescale` ：

    ```python
    class Rescale(object):
        s
        def __init__(self, output_size):
            assert isinstance(output_size, (int, tuple))
            self.output_size = output_size
        
    	def __call__(self, sample):
            image, landmarks = sample['image'], sample['landmarks']
            h, w = image.shape[:2]
            if isinstance(self.output_size, int):
                if h > w:
                    new_h, new_w = self.output_size * h / w, self.output_size
                else:
                    new_h, new_w = self.output_size, self.output_size * w / h
            else:
                new_h, new_w = self.output_size
            new_h, new_w = int(new_h), int(new_w)
            img = transform.resize(image, (new_h, new_w))
            # h and w are swapped for landmarks because for images,
            # x and y axes are axis 1 and 0 respectively
            landmarks = landmarks * [new_w / w, new_h / h]
            return {'image': img, 'landmarks': landmarks}
    ```

  - 自定义变换实例 `ToTensor`：

    ```python
    class ToTensor(object):
        def __call__(self, sample):
    		image, landmarks = sample['image'], sample['landmarks']
            # swap color axis because
            # numpy image: H x W x C
            # torch image: C X H X W
            image = image.transpose((2, 0, 1))
            return {'image': torch.from_numpy(image), 'landmarks': torch.from_numpy(landmarks)}
    ```

- `torch.utils.data.Dataloader` 是一个可以分批、打乱、并行加载数据的迭代器。

  ```python
  transformed_dataset = FaceLandmarksDataset(csv_file='faces/face_landmarks.csv',
                                             root_dir='faces/',
                                             transform=transforms.Compose([
                                                 Rescale(256),
                                                 RandomCrop(224),
                                                 ToTensor()
                                             ]))
  dataloader = DataLoader(transformed_dataset, batch_size=4, shuffle=True, num_workers=4)
  
  for i_batch, sample_batched in enumerate(dataloader):
      show_landmarks_batch(sample_batched)
  ```


