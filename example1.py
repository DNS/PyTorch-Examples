import torch
import torch.nn as nn
import torch.optim as optim

# 1️⃣ Define a simple linear model: y = wx + b
class LinearModel(nn.Module):
	def __init__(self):
		super().__init__()
		self.linear = nn.Linear(in_features=1, out_features=1)  # 1‑D input → 1‑D output

	def forward(self, x):
		return self.linear(x)

model = LinearModel()

# 2️⃣ Create some synthetic data (y = 2x + 1 + noise)
torch.manual_seed(0)
x_train = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # shape (100, 1)
y_train = 2 * x_train + 1 + 0.2 * torch.randn(x_train.size())

# 3️⃣ Choose a loss function and optimizer
criterion = nn.MSELoss()                # mean‑squared error
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 4️⃣ Training loop
epochs = 200
for epoch in range(epochs):
	model.train()

	# Forward pass
	predictions = model(x_train)
	loss = criterion(predictions, y_train)

	# Backward pass & update
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()

	if (epoch + 1) % 40 == 0:
		print(f'Epoch {epoch+1:3d} | Loss: {loss.item():.4f}')

# 5️⃣ Test the trained model
model.eval()
with torch.no_grad():
	test_x = torch.tensor([[0.5]])
	test_y = model(test_x)
	print(f'\nInput 0.5 → Predicted output {test_y.item():.3f}')

