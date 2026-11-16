# perguntas_respostas/respostas_generativas.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- CONFIGURAÇÃO DA API (feita uma vez quando o módulo é importado) ---
try:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("A variável GOOGLE_API_KEY não foi encontrada no arquivo .env")
    genai.configure(api_key=api_key)
    
    # Inicializa o modelo aqui para ser reutilizado em todas as chamadas
    modelo_generativo = genai.GenerativeModel('gemini-2.0-flash')
    print("[LOG] Módulo de respostas generativas carregado e configurado.")

except Exception as e:
    print(f"ERRO CRÍTICO ao configurar a API do Gemini no módulo: {e}")
    modelo_generativo = None

# --- FUNÇÃO PRINCIPAL DO MÓDULO ---
def obter_resposta_gemini(pergunta: str) -> str:
    """
    Recebe uma pergunta do usuário, envia para a API do Gemini e retorna a resposta.
    
    Args:
        pergunta: A string contendo a pergunta do usuário.
        
    Returns:
        A string com a resposta da IA ou uma mensagem de erro.
    """
    if not modelo_generativo:
        return "Desculpe, a inteligência generativa não está disponível no momento devido a um erro de configuração."

    try:
        print("[DEBUG] Enviando a pergunta para a API do Gemini. Aguardando...")
        
        # Gera o conteúdo com base na pergunta recebida
        response = modelo_generativo.generate_content(pergunta)
        
        print("[DEBUG] Resposta recebida da API!") # Se essa linha não aparecer, ele travou aqui.
        return response.text
    except Exception as e:

        print(f"Erro na API Gemini ao gerar resposta: {e}")
        return "Desculpe, ocorreu um erro ao tentar gerar a sua resposta."
    
    # --- BLOCO DE TESTE INDEPENDENTE ---
# Este código só será executado quando você rodar este arquivo diretamente
if __name__ == '__main__':
    print("--- Realizando teste de API independente ---")
    # Vamos usar uma pergunta simples para o teste
    pergunta_teste = "Qual a capital do Brasil? Me responda em português."
    print(f"Enviando pergunta: '{pergunta_teste}'")
    
    # Chama a função principal do próprio módulo
    resposta = obter_resposta_gemini(pergunta_teste)
    
    print("\n--- Resposta da API ---")
    print(resposta)
    print("----------------------")