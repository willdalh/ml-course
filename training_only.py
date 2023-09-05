import torch
import torch.nn as nn
import torchvision.transforms as transforms

from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from tqdm import tqdm # Progress bar

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(in_features=28*28, out_features=200)
        self.layer2 = nn.Linear(in_features=200, out_features=42)
        self.layer3 = nn.Linear(in_features=42, out_features=10) # 10 digits to differentiate between

        self.sigmoid = nn.Sigmoid()
        self.softmax = nn.Softmax(dim=1) # Softmax will be computed for each batch element separately 

    def logits(self, data):
        flattened_data = torch.flatten(data, start_dim=1, end_dim=-1) # Flatten the tensor from shape (batch_size, 1, 28, 28) to shape (batch_size, 1 * 28 * 28)

        out = self.layer1(flattened_data)
        out = self.sigmoid(out)

        out = self.layer2(out)
        out = self.sigmoid(out)

        out = self.layer3(out)
        return out
    
    def forward(self, data):
        logits = self.logits(data)
        return self.softmax(logits)

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Pipeline of processing operations
    image_processing = transforms.Compose([
        transforms.ToTensor(), # Cast into tensor
        transforms.Normalize((0.5,), (0.5,)) # Pixel-values will range in [-1, 1]
        ])

    train_dataset = MNIST(root='./data', train=True, transform=image_processing, download=True)
    test_dataset = MNIST(root='./data', train=False, transform=image_processing, download=True) # Test data for later

    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=32)

    model = Model() # Initialize model
    model.to(device)

    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    
    num_epochs = 3

    for epoch in range(num_epochs):
        with tqdm(train_loader, unit="batch") as pbar:
            pbar.set_description(f"Epoch {epoch}")
            for i, (data, labels) in enumerate(pbar):
                data = data.to(device)
                labels = labels.to(device)
                pred = model.logits(data) # Query model for predictions
                loss = loss_fn(pred, labels)
                
                loss.backward() # Propagate the computational graph and calculate gradients
                optimizer.step() # Uses the calculated gradients on the registered parameters to perform an update
                optimizer.zero_grad() # Remove the gradients
    print("Finished training.\nNow testing the model.")
    test_loader = DataLoader(test_dataset, shuffle=True, batch_size=32)
    
    correct = 0
    for data, labels in test_loader:
        data = data.to(device)
        labels = labels.to(device)

        pred = model.forward(data)
        correct += torch.sum(pred.argmax(dim=1) == labels)
    accuracy = correct/len(test_dataset)

    print(f"The accuracy of the model on the test set is {accuracy}")
    print(f"Saving the model...")
    torch.save(model.state_dict(), "saved_models/model.pt")


if __name__ == "__main__":
    main()