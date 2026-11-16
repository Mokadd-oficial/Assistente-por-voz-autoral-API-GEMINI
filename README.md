# 🎙️ Assistente Virtual Inteligente (Estilo Alexa + Gemini API)

Um assistente virtual de voz desenvolvido em Python, potencializado pela inteligência artificial do **Google Gemini** e integrado com recursos de **Visão Computacional** (OpenCV e PyTorch) e **Automação de Sistema Operacional**. 

Capaz de responder a qualquer pergunta de forma natural, abrir aplicativos locais (Calculadora, Youtube), reconhecer rostos (basta treinar previamente com rosto desejado de reconhecimento), identificar objetos/animais em tempo real (base de dados publica do Kaggle de garrafas e gatos) e gerenciar compromissos em uma agenda.txt local.

---

## ✨ Funcionalidades Principais

* 🧠 **IA Conversacional (Gemini API):** Responde a perguntas gerais, tira dúvidas e mantém diálogos utilizando o modelo de linguagem do Google.
* 💻 **Controle do Sistema & Web:** Executa comandos locais por voz, como abrir a Calculadora, iniciar o YouTube no navegador, entre outras habilidades extras.
* 👤 **Reconhecimento Facial:** Identificação biométrica facial utilizando algoritmos clássicos do OpenCV (`Eigenfaces` e `LBPH`).
* 🐾 **Reconhecimento de Objetos e Animais:** Detecção e classificação em tempo real utilizando redes neurais com **PyTorch**.
* 📝 **OCR (Reconhecimento de Texto):** Leitura e extração de texto a partir de imagens.
* 📅 **Agenda Inteligente:** Anota, consulta e gerencia eventos e lembretes diretamente no arquivo local `agenda.txt`.

---

## 📂 Estrutura do Projeto

A organização dos diretórios e arquivos do projeto segue a estrutura abaixo:

```text
├── agenda_sistema/                  # Módulos de gerenciamento de eventos
├── fotos/                           # Base de imagens para treinamento/testes
├── habilidades_extras/              # Scripts de automação (Calculadora, YouTube, etc.)
├── identificador_imagem/            # Processamento auxiliar de imagens
├── opencv/                          # Configurações e recursos do OpenCV
├── perguntas_respostas/             # Lógica de interação e integração com Gemini
├── reconhecimento_facial/           # Scripts de captura e reconhecimento de rostos
├── reconhecimento_imagem/           # Scripts de classificação visual
├── reconhecimento_texto/            # Módulos de OCR
├── teste do microfone/              # Utilitários para calibração e teste de áudio
├── .env                             # Variáveis de ambiente (Chave da API)
├── agenda.txt                       # Banco de dados em texto dos eventos agendados
├── assistente_voz.py                # Arquivo principal (Ponto de entrada do assistente)
├── classificadoreigen.yml           # Modelo treinado (Eigenfaces)
├── classificadorLBPH.yml            # Modelo treinado (LBPH)
├── reconhecedor_objetos_pytorch.pth # Pesos do modelo PyTorch para objetos/animais
└── requirements.txt                 # Dependências do projeto
🚀 Pré-requisitos e Instalação
Clone o repositório:

Bash
git clone https://github.com/Mokadd-oficial/Assistente-por-voz-autoral-API-GEMINI
cd seu-repositorio
Crie e ative um ambiente virtual (Recomendado):

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash
pip install -r requirements.txt
🔑 Configuração da API (.env)
Para que o assistente se conecte à inteligência do Gemini, é obrigatório configurar a sua chave de API antes de rodar o código.

Obtenha sua chave gratuita no Google AI Studio.

Na raiz do projeto, crie (ou edite) o arquivo chamado .env.

Adicione a sua chave no seguinte formato (ajuste o nome da variável caso no seu código esteja diferente, como GOOGLE_API_KEY):

Snippet de código
GEMINI_API_KEY="sua_chave_api_aqui"
⚠️ Aviso de Segurança: Nunca envie o seu arquivo .env para o GitHub! Certifique-se de adicionar .env dentro de um arquivo .gitignore para evitar que outras pessoas usem a sua cota da API.

▶️ Como Executar
Com o ambiente virtual ativado, a chave da API configurada e o microfone conectado, inicie o assistente executando o script principal:

Bash
python assistente_voz.py
(Opcional) Caso tenha problemas na captação de áudio, utilize os scripts da pasta teste do microfone/ para verificar o índice do seu dispositivo de entrada.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Inteligência Artificial / LLM: Google Gemini API

Visão Computacional & Deep Learning: OpenCV, PyTorch

Reconhecimento e Síntese de Voz: SpeechRecognition, pyttsx3 / gTTS (ajuste conforme seu requirements.txt)

Gerenciamento de Ambiente: python-dotenv
