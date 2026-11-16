import cv2
import os # Importa a biblioteca 'os' para lidar com caminhos de arquivos

# A lógica principal agora está dentro de uma função
def iniciar_reconhecimento_facial():
    print("Iniciando reconhecimento facial... Pressione 'q' na janela para voltar ao menu.")
    
    try:
                           # --- Manipulação de Caminhos ---
        # Pega o caminho do diretório do script atual (.../reconhecimento_facial)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Sobe um nível para chegar na pasta raiz do projeto (a pasta 'alexa')
        project_root = os.path.dirname(script_dir)
        
        # Monta o caminho completo para o classificador que está na pasta raiz
        classificador_path = os.path.join(project_root, 'classificadorLBPH.yml')

        detectorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        reconhecedor = cv2.face.LBPHFaceRecognizer_create()
        
        # Verifica se o arquivo .yml existe antes de tentar ler
        if not os.path.exists(classificador_path):
            print(f"Erro: Arquivo classificador não encontrado em: {classificador_path}")
            print("Certifique-se de ter executado o treinamento.py primeiro.")
            return # Sai da função se o arquivo não existir

        reconhecedor.read(classificador_path)
        
        largura, altura = 220, 220
        font = cv2.FONT_HERSHEY_SIMPLEX
        camera = cv2.VideoCapture(0)

        while True:
            status, imagem = camera.read()
            if not status: break
            
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100, 100))

            for (x, y, l, a) in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y+a, x:x+l], (altura, largura))
                cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 255), 2)
                
                nome_id, confianca = reconhecedor.predict(imagemFace)
                
                nome = "Desconhecido"
                if confianca < 75:
                    if nome_id == 1: nome = 'Karine'
                    elif nome_id == 2: nome = 'Gabriel'
                    elif nome_id == 3: nome = 'Yuji'
                else:
                    nome = 'desconhecido'

                cv2.putText(imagem, nome, (x, y + (a+30)), font, 1.2, (0, 0, 255))

            cv2.imshow("Reconhecimento Facial", imagem)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Ocorreu um erro no reconhecimento facial: {e}")
    finally:
        if 'camera' in locals() and camera.isOpened():
            camera.release()
        cv2.destroyAllWindows()

# Este bloco permite que o script ainda seja executado de forma independente
if __name__ == '__main__':
    iniciar_reconhecimento_facial()