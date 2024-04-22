import speech_recognition as sr
from nltk.tokenize import word_tokenize
import json
import random

def ouvir_microfone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconhecendo...")
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse:", texto)

        with open('comandos.json') as json_file:
            comandos = json.load(json_file)['comandos']
        
        tokens = word_tokenize(texto.lower())  
        
        for comando, funcao in comandos.items():
            comando_tokens = word_tokenize(comando.lower())
            if all(token in tokens for token in comando_tokens):
               
                globals()[funcao]()  
                break
        else:
            print("Comando não reconhecido.")

    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala; {0}".format(e))

def obter_temperatura_computador():
    temperatura = random.randint(20, 100)  
    print("A temperatura do computador é", temperatura, "graus Celsius.")

def porcentagem_processamento():
    porcentagem = random.randint(0, 100)
    print("Porcentagem de processamento:", porcentagem, "%")


def tempo_uso_software():
    software = "Instagram" 
    tempo_uso = random.randint(0,24)  
    print("Tempo de uso do software", software + ":", tempo_uso, "horas")

def dispositivos_entrada_conectados():
    dispositivos = ["Mouse", "Teclado", "Webcam"]  
    print("Dispositivos de entrada conectados:", dispositivos)

if __name__ == "__main__":
    ouvir_microfone()
