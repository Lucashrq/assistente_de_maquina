import nltk
import speech_recognition as sr

def ouvir_microfone():
    # Crie um objeto reconhecedor
    recognizer = sr.Recognizer()

    # Use o microfone como fonte de entrada de áudio
    with sr.Microphone() as source:
        print("Por favor, fale algo...")
        # Ajuste automaticamente o nível de ruído para o ambiente
        recognizer.adjust_for_ambient_noise(source)
        # Ouça o áudio do microfone
        audio = recognizer.listen(source)

    try:
        print("Reconhecendo...")
        # Use o Google Speech Recognition para converter o áudio em texto
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse:", texto)

        if "Qual é o seu nome" in texto:
            print("Olá, me chamo Jarvis")
        
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala; {0}".format(e))

if __name__ == "__main__":
    ouvir_microfone()
