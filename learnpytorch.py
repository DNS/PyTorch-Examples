import torch
from torch import nn

import torch.nn.functional as F

import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import torchmetrics



# Create a linear layer with 10 in features and out features
linear_layer = nn.Linear(in_features=10, out_features=10)

# Create an Identity layer
identity_layer = nn.Identity()
# Create a Conv1d layer (often used for text with a singular dimension)
conv1d = nn.Conv1d(in_channels=1, out_channels=10, kernel_size=3)


# Create a Conv2d layer (often used for images with Height x Width dimensions)
conv2d = nn.Conv2d(in_channels=3, # 3 channels for color images (red, green, blue)
                   out_channels=10,
                   kernel_size=3)                   

# Create a Conv3d layer (often used for video with Height x Width x Time dimensions)
conv3d = nn.Conv3d(in_channels=3, out_channels=10, kernel_size=3)


# Create a Transformer model (model based on the paper "Attention Is All You Need" - https://arxiv.org/abs/1706.03762)
transformer_model = nn.Transformer()
# Create a single Transformer encoder cell
transformer_encoder = nn.TransformerEncoderLayer(d_model=768, # embedding dimension
                                                 nhead=12) # number of attention heads
# Stack together Transformer encoder cells
transformer_encoder_stack = nn.TransformerEncoder(encoder_layer=transformer_encoder, # from above
                                                  num_layers=6) # 6 Transformer encoders stacked on top of each other

# Create a single Transformer decoder cell
transformer_decoder = nn.TransformerDecoderLayer(d_model=768,
                                                 nhead=12)

# Stack together Transformer decoder cells
transformer_decoder_stack = nn.TransformerDecoder(decoder_layer=transformer_decoder, # from above
                                                  num_layers=6) # 6 Transformer decoders stacked on top of each other










