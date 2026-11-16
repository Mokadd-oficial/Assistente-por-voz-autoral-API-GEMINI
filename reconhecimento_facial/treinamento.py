import cv2
import os
import numpy as np

lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagemPeloNome():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    print("Lendo imagens para treinamento...")
    faces = []
    ids = []

    for caminhoImagem in caminhos:
        imagemFace = cv2.imread(caminhoImagem, 0)
        
        # --- LINHA CORRIGIDA ---
        # Extrai o nome e já converte para minúsculas para evitar erros
        nome = os.path.split(caminhoImagem)[-1].split('_')[0].lower()
        
        # Agora a comparação funcionará mesmo que o nome no arquivo seja "Karine" ou "KARINE"
        if nome == 'karine':
            ids.append(1)
        elif nome == 'gabriel':
            ids.append(2)
        elif nome == 'yuji':
            ids.append(3)
        elif nome == 'bruno':
            ids.append(4)
        
        faces.append(imagemFace)
    
    return np.array(ids), faces

ids, faces = getImagemPeloNome()

if len(faces) == 0:
    print("Nenhuma imagem encontrada na pasta 'fotos'.")
elif len(ids) != len(faces):
     print(f"Erro: Inconsistência de dados. Foram encontradas {len(faces)} faces mas apenas {len(ids)} IDs correspondentes.")
     print("Verifique se todos os nomes de arquivo na pasta 'fotos' estão no bloco if/elif do treinamento.")
else:
    print(f"\nIniciando treinamento com {len(faces)} imagens e {len(ids)} IDs...")
    lbph.train(faces, ids)
    print("Treinamento concluído.")
    lbph.write('classificadorLBPH.yml') 
    print("Arquivo 'classificadorLBPH.yml' salvo com sucesso!")