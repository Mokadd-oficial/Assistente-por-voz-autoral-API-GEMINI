# -*- coding: utf-8 -*-

# --- BIBLIOTECAS PADRÃO ---
import speech_recognition as sr
import pyttsx3
import datetime

# --- IMPORTAÇÃO DOS SEUS CÓDIGOS MODULARES ---
from reconhecimento_facial.reconhecimento import iniciar_reconhecimento_facial
from reconhecimento_texto.reconhecimento_texto import iniciar_reconhecimento_texto
from perguntas_respostas.respostas_generativas import obter_resposta_gemini
from habilidades_extras.habilidades import contar_piada, abrir_sites_e_programas, calcular
# --- NOVAS IMPORTAÇÕES ---
from agenda_sistema.agenda import Agenda
from reconhecimento_imagem.reconhecer_imagem import iniciar_reconhecimento_objetos


# --- CONFIGURAÇÕES E INICIALIZAÇÕES ---

# Palavra de ativação
NOME_ASSISTENTE = "assistente"

# --- NOVA INSTÂNCIA DA CLASSE AGENDA (CUMPRINDO REQUISITO OOP) ---
minha_agenda = Agenda()

# Inicializa o reconhecedor de voz
reconhecedor = sr.Recognizer()

# Inicializa o sintetizador de voz (TTS)
sintetizador = pyttsx3.init()
sintetizador.setProperty('rate', 180)
sintetizador.setProperty('volume', 1.0)


# --- FUNÇÕES AUXILIARES E DE AÇÃO ---

def falar(texto):
    """Função central para a assistente falar."""
    if texto:
        print(f"Assistente: {texto}")
        sintetizador.say(texto)
        sintetizador.runAndWait()

def escutar_comando():
    """Escuta o microfone e retorna o texto reconhecido."""
    try:
        with sr.Microphone() as mic:
            reconhecedor.adjust_for_ambient_noise(mic, duration=1)
            print("Aguardando comando...")
            audio = reconhecedor.listen(mic, timeout=5, phrase_time_limit=20)
            print("Reconhecendo...")
            texto_comando = reconhecedor.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto_comando}")
            return texto_comando.lower()
    except sr.WaitTimeoutError:
        print("Tempo de escuta esgotado.")
        return None
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado na escuta: {e}")
        return None

def informar_data_hora():
    """Informa a data e a hora atuais."""
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("Hoje é %d de %B de %Y")
    hora_formatada = agora.strftime("e agora são %H horas e %M minutos")
    falar(f"{data_formatada}, {hora_formatada}.")

# --- NOVA FUNÇÃO PARA CONVERSA DA AGENDA ---
def gerenciar_novo_evento():
    """Orquestra a conversa de múltiplos passos para cadastrar um novo evento."""
    falar("Qual o dia do evento?")
    dia = escutar_comando()
    if not dia:
        falar("Não entendi o dia. Operação cancelada.")
        return

    falar("Que horas?")
    horas = escutar_comando()
    if not horas:
        falar("Não entendi a hora. Operação cancelada.")
        return
        
    falar("Qual a duração?")
    duracao = escutar_comando()
    if not duracao:
        falar("Não entendi a duração. Operação cancelada.")
        return

    falar("Por último, qual o nome do evento?")
    nome = escutar_comando()
    if not nome:
        falar("Não entendi o nome. Operação cancelada.")
        return
        
    evento_completo = f"Evento: {nome}, no dia {dia} às {horas}, com duração de {duracao}."
    confirmacao = minha_agenda.adicionar_evento(evento_completo)
    falar(confirmacao)


# --- LOOP PRINCIPAL DO ASSISTENTE ---
if __name__ == "__main__":
    falar("Assistente virtual iniciado. Diga 'assistente' para me ativar.")

    while True:
        print(f"\nOuvindo para a palavra de ativação '{NOME_ASSISTENTE}'...")
        comando_inicial = escutar_comando()

        if comando_inicial and NOME_ASSISTENTE in comando_inicial:
            falar("Sim? Estou ouvindo o seu comando.")
            comando_final = escutar_comando()

            if not comando_final:
                falar("Não ouvi seu comando. Por favor, tente novamente.")
                continue

            # --- INTERPRETAÇÃO E EXECUÇÃO DOS COMANDOS (VERSÃO FINAL) ---
            if "reconhecimento facial" in comando_final:
                falar("Ok, iniciando o reconhecimento facial.")
                iniciar_reconhecimento_facial()
                falar("Módulo de reconhecimento facial finalizado.")
            
            elif "reconhecer imagem" in comando_final or "reconhecer objeto" in comando_final:
                falar("Ok, iniciando o reconhecimento de objetos.")
                iniciar_reconhecimento_objetos()
                falar("Módulo de reconhecimento de objetos finalizado.")

            elif "texto" in comando_final and ("reconhecer" in comando_final or "ler" in comando_final or "reconheça" in comando_final):
                falar("Certo, iniciando o reconhecimento de texto pela câmera.")
                iniciar_reconhecimento_texto()
                falar("Módulo de reconhecimento de texto finalizado.")

            elif "que dia é hoje" in comando_final or "qual a data" in comando_final or "que horas são" in comando_final:
                informar_data_hora()

            elif "marcar evento" in comando_final or "cadastrar evento" in comando_final:
                gerenciar_novo_evento()

            elif "ler agenda" in comando_final:
                resposta_agenda = minha_agenda.ler_eventos()
                falar(resposta_agenda)

            elif "limpar agenda" in comando_final:
                resposta_agenda = minha_agenda.limpar_agenda()
                falar(resposta_agenda)
            
            elif "abrir" in comando_final:
                abrir_sites_e_programas(comando_final, falar)

            elif "piada" in comando_final:
                contar_piada(falar)

            elif "quanto é" in comando_final or "calcule" in comando_final:
                calcular(comando_final, falar)
            
            elif "encerrar" in comando_final or "desligar" in comando_final:
                falar("Encerrando. Até a próxima!")
                break
                
            else:
                resposta_da_ia = obter_resposta_gemini(comando_final)
                falar(resposta_da_ia)