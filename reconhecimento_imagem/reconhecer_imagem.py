# reconhecimento_imagem/reconhecimento_objetos.py (Versão PyTorch)
import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import transforms
import os
from PIL import Image

# --- É ESSENCIAL QUE A ESTRUTURA DA CLASSE SEJA IDÊNTICA À DO TREINAMENTO ---
class Net(nn.Module):
    def __init__(self, num_classes=2): # O número de classes precisa ser o mesmo do treino
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
        x = x.view(-1, 64 * 8 * 8)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def iniciar_reconhecimento_objetos():
    try:
        # --- Configurações ---
        MODEL_NAME = "reconhecedor_objetos_pytorch.pth"
        # IMPORTANTE: A ordem das classes deve ser a mesma que o script de treino mostrou!
        class_names = ['garrafas', 'gatos'] # Ajuste se a ordem for ['gatos', 'garrafas']

        caminho_script = os.path.dirname(os.path.abspath(__file__))
        caminho_raiz = os.path.dirname(caminho_script)
        caminho_modelo = os.path.join(caminho_raiz, MODEL_NAME)

        if not os.path.exists(caminho_modelo):
            print(f"ERRO: Arquivo do modelo '{MODEL_NAME}' não encontrado.")
            return

        # Carregar o modelo
        model = Net(num_classes=len(class_names))
        model.load_state_dict(torch.load(caminho_modelo))
        model.eval() # Coloca o modelo em modo de avaliação

        # Transformações para a imagem da webcam
        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        camera = cv2.VideoCapture(0)
        
        while True:
            status, frame = camera.read()
            if not status: break

            # Pré-processamento do frame
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            input_tensor = transform(frame_rgb)
            input_batch = input_tensor.unsqueeze(0) # Cria um "lote" com uma única imagem

            # Predição
            with torch.no_grad():
                output = model(input_batch)
                _, pred_index = torch.max(output, 1)
                predicted_class = class_names[pred_index.item()]
            
            texto = f"{predicted_class}"
            cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow("Reconhecimento de Imagem", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'camera' in locals() and camera.isOpened():
            camera.release()
        cv2.destroyAllWindows()

        # --- Bloco de Teste ---
# Este código só será executado quando você rodar este arquivo diretamente
if __name__ == '__main__':
    print("Executando o módulo de reconhecimento de imagem em modo de teste...")
    iniciar_reconhecimento_objetos()