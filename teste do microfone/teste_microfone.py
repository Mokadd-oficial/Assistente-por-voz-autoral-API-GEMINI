# teste_microfone.py
import speech_recognition as sr

# Inicializa o reconhecedor
r = sr.Recognizer()

# Usa o microfone como fonte de áudio
with sr.Microphone() as source:
    print("Ajustando para o ruído do ambiente... Por favor, fique em silêncio por 2 segundos.")
    # Ajuste automático de sensibilidade com base no ruído
    r.adjust_for_ambient_noise(source, duration=2)
    print("Pronto! Fale alguma coisa agora.")
    
    try:
        # Tenta ouvir o que você diz
        audio = r.listen(source, timeout=5)
        
        print("Ok, processando o que você disse...")
        
        # Tenta reconhecer a fala usando a API do Google
        texto = r.recognize_google(audio, language='pt-BR')
        print(f"Eu acho que você disse: '{texto}'")

    except sr.WaitTimeoutError:
        print("ERRO: O tempo acabou e eu não ouvi nada. O microfone está captando áudio?")
    except sr.UnknownValueError:
        print("ERRO: Não consegui entender o que você disse. Pode haver muito ruído ou a fala não foi clara.")
    except sr.RequestError as e:
        print(f"ERRO: Não foi possível conectar ao serviço do Google; {e}")