import torch
import torch.nn as nn
import torch.optim as optim

# Step 1: Generate Random Data
torch.manual_seed(42)  # For reproducibility

# Random training data (inputs and labels)
X_train = torch.rand(100, 2)  # 100 samples, 2 features each
y_train = torch.sum(X_train, dim=1, keepdim=True)  # Output is the sum of the inputs

# Random testing data
X_test = torch.rand(20, 2)
y_test = torch.sum(X_test, dim=1, keepdim=True)

# Step 2: Define the Neural Network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.layer1 = nn.Linear(2, 4)  # Input layer (2 nodes) -> Hidden layer (4 nodes)
        self.layer2 = nn.Linear(4, 1)  # Hidden layer -> Output layer (1 node)
    
    def forward(self, x):
        x = torch.relu(self.layer1(x))  # Apply ReLU activation on hidden layer
        x = self.layer2(x)  # Linear transformation to output
        return x

# Initialize the model, loss function, and optimizer
model = SimpleNN()
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent

# Step 3: Train the Model
num_epochs = 500
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()  # Clear the gradients
    predictions = model(X_train)  # Forward pass
    loss = criterion(predictions, y_train)  # Compute the loss
    loss.backward()  # Backpropagation
    optimizer.step()  # Update the weights
    
    # Print loss for every 50 epochs
    if (epoch + 1) % 50 == 0:
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# Step 4: Test the Model
model.eval()
with torch.no_grad():
    predictions = model(X_test)
    test_loss = criterion(predictions, y_test)
    print(f"\nTest Loss: {test_loss.item():.4f}")

# Visualize Results (optional)
print("\nSample Test Predictions:")
for i in range(5):  # Show 5 predictions
    print(f"Input: {X_test[i]}, Predicted: {predictions[i].item():.4f}, Actual: {y_test[i].item():.4f}")
