import speech_recognition as sr
from nltk.tokenize import word_tokenize

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

        # Tokenização do texto para análise de comandos
        tokens = word_tokenize(texto.lower())  # Convertendo para minúsculas para padronização
        
        # Verificar se algum comando reconhecido está presente no texto
        for comando, funcao in comandos.items():
            comando_tokens = word_tokenize(comando.lower())
            if all(token in tokens for token in comando_tokens):
                funcao()
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
    temperatura = 40  # Valor de temperatura simulado
    print("A temperatura do computador é", temperatura, "graus Celsius.")

def porcentagem_processamento():
    # Implemente a lógica para obter a porcentagem de processamento do computador
    print("Porcentagem de processamento: 50%")  # Simulação

def tempo_uso_software():
    # Implemente a lógica para obter o tempo de uso de um determinado software
    software = "ExemploSoftware"  # Software de exemplo
    tempo_uso = "2 horas"  # Tempo de uso simulado
    print("Tempo de uso do software", software + ":", tempo_uso)

def dispositivos_entrada_conectados():
    # Implemente a lógica para listar os dispositivos de entrada conectados à máquina
    dispositivos = ["Mouse", "Teclado", "Webcam"]  # Dispositivos de exemplo
    print("Dispositivos de entrada conectados:", dispositivos)

# Mapeamento de comandos de voz para funções
comandos = {
    "Qual é o seu nome": nome_assistente,
    "Temperatura do computador": obter_temperatura_computador,
    "Porcentagem de processamento": porcentagem_processamento,
    "Tempo de uso de determinado software": tempo_uso_software,
    "Dispositivos de entrada conectados": dispositivos_entrada_conectados
}

if __name__ == "__main__":
    ouvir_microfone()
