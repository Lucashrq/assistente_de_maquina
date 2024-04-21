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

        # Leitura dos comandos a partir do arquivo JSON
        with open('comandos.json') as json_file:
            comandos = json.load(json_file)['comandos']
        
        # Tokenização do texto para análise de comandos
        tokens = word_tokenize(texto.lower())  # Convertendo para minúsculas para padronização
        
        # Verificar se algum comando reconhecido está presente no texto
        for comando, funcao in comandos.items():
            comando_tokens = word_tokenize(comando.lower())
            if all(token in tokens for token in comando_tokens):
                # Chamar a função correspondente ao comando
                globals()[funcao]()  # Chama a função pelo nome
                break
        else:
            print("Comando não reconhecido.")

    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala; {0}".format(e))

def nome_assistente():
    print("Olá, me chamo Jarvis.")

def obter_temperatura_computador():
    # Simulação da obtenção da temperatura do computador
    temperatura = random.randint(20, 100)  # Valor de temperatura simulado
    print("A temperatura do computador é", temperatura, "graus Celsius.")

def porcentagem_processamento():
    # Gerar uma porcentagem aleatória entre 0 e 100
    porcentagem = random.randint(0, 100)
    print("Porcentagem de processamento:", porcentagem, "%")


def tempo_uso_software():
    # Implemente a lógica para obter o tempo de uso de um determinado software
    software = "Instagram"  # Software de exemplo
    tempo_uso = random.randint(0,24)  # Tempo de uso simulado
    print("Tempo de uso do software", software + ":", tempo_uso, "horas")

def dispositivos_entrada_conectados():
    # Implemente a lógica para listar os dispositivos de entrada conectados à máquina
    dispositivos = ["Mouse", "Teclado", "Webcam"]  # Dispositivos de exemplo
    print("Dispositivos de entrada conectados:", dispositivos)

if __name__ == "__main__":
    ouvir_microfone()
