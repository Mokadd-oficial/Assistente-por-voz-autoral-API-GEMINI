# treinar_objetos.py (Versão PyTorch)
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader
import os

# --- Configurações ---
DATA_DIR = 'identificador_imagem'
MODEL_FILENAME = "reconhecedor_objetos_pytorch.pth"
IMG_SIZE = 32
BATCH_SIZE = 16
EPOCHS = 20 # PyTorch pode precisar de um pouco mais de épocas

# 1. Transformações nas imagens: redimensionar, converter para tensor e normalizar
data_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# 2. Carregar o dataset a partir das pastas
print("Carregando imagens do diretório...")
full_dataset = datasets.ImageFolder(DATA_DIR, data_transforms)
class_names = full_dataset.classes
num_classes = len(class_names)
print("Classes encontradas:", class_names)

# Dividir em treino e validação
train_size = int(0.8 * len(full_dataset))
val_size = len(full_dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(full_dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# 3. Definir o modelo CNN (usando uma Classe, como pedido no bônus)
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(-1, 64 * 8 * 8) # Flatten
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = Net()

# 4. Definir a função de perda e o otimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 5. Treinar o modelo
print("\nIniciando treinamento...")
for epoch in range(EPOCHS):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
    
    epoch_loss = running_loss / len(train_loader.dataset)
    print(f"Época {epoch+1}/{EPOCHS} - Perda (Loss): {epoch_loss:.4f}")

# 6. Salvar o modelo treinado
torch.save(model.state_dict(), MODEL_FILENAME)
print(f"\nTreinamento concluído! Modelo salvo como '{MODEL_FILENAME}'")