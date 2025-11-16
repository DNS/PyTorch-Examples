import torch
from torch import nn

import torch.nn.functional as F

import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import torchmetrics


t = torch.tensor([1,2,3])
t.dtype
t.shape
t.device

torch.tensor([1,2,3])
torch.zeros(2,3)
torch.randn(3, 10)


# Dense layer / fully-connected layer
#linear = nn.Linear(in_features=10, out_features=5)
linear = nn.Linear(10, 5)
x = torch.randn(3, 10)   # shape: (batch, in_features)
y = linear(x)            # shape: (3, 5)
print(y)

linear.weight
linear.bias

nn.Sigmoid()
nn.Softmax(dim=-1)
nn.ReLU()
nn.LeakyReLU(negative_slope=0.05)
nn.Dropout(p=0.5)

model = nn.Sequential(
	nn.Linear(n_features, i),
	nn.Linear(i, j),
	nn.Linear(j, n_classes),
	nn.Softmax(dim=-1)
)



