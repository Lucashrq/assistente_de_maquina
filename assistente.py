import nltk
import speech_recognition as sr

def escutar_comando():
    reconhecer = sr.Recognizer()

    with sr.Microphone() as source:
        reconhecer.pause_threshold = 1
        reconhecer.adjust_for_ambient_noise(source)

        print("Me faça um pedido!")
        audio = reconhecer.listen(source)

    try:
        comando = reconhecer.recognize_google(audio, language="pt-BR")
        print("Comando reconhecido", comando)
        executar_comando(comando)
    except sr.UnknownValueError:
        print("Comando não reconhecido")
    except sr.RequestError:
        print("Não foi possível acessar o serviço de reconhecimento de voz.")

def executar_comando(comando):
    ...

def main():
    while True:
        escutar_comando()

#método principal
if __name__ == "__main__":
    ...