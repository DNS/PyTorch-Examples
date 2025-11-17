import torch

# Example tensors
A = torch.tensor([[1., 2., 3.],
                  [4., 5., 6.]])          # shape (2, 3)

B = torch.tensor([[7., 8.],
                  [9., 10.],
                  [11., 12.]])          # shape (3, 2)

# Standard matrix multiplication
C = torch.matmul(A, B)   # or A @ B
print(C)


