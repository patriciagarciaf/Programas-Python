import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    recognizer = sr.Recognizer()

    # configurar el micrófono
    with sr.Microphone() as origen:

        # tiempo de espera
        recognizer.pause_threshold = 0.8

        # informar que comenzó la grabación
        print('Ya puedes hablar')

        # guardar lo que escuche como audio
        audio = recognizer.listen(origen)

        try:
            # buscar en google lo escuchado
            pedido = recognizer.recognize_google(audio, language='es-ES')

            # prueba de que pudo escuchar
            print(f'Dijiste: {pedido}')

            # devolver pedido
            return pedido

        # error: no comprende el audio
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print('ups, no hay servicio')

            # devolver error
            return 'Sigo esperando'

        # error: no pudo resolver el pedido
        except sr.RequestError:

            # prueba de que no resolvió el pedido
            print('ups, no lo entendí')

            # devolver error
            return 'Sigo esperando'

        # error inesperado
        except:

            # prueba de que no comprendió el audio
            print('ups, algo salió mal')

            # devolver error
            return 'Sigo esperando'


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # decir el mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar del día de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()

    # crear una variable para el dia de semana
    dia_semana = dia.weekday()

    # diccionario con nombres de dias
    dias_semana = {0: 'Lunes',
                   1: 'Martes',
                   2: 'Miércoles',
                   3: 'Jueves',
                   4: 'Viernes',
                   5: 'Sábado',
                   6: 'Domingo'}

    # diccionario con nombres de meses
    meses = {1: 'Enero',
             2: 'Febrero',
             3: 'Marzo',
             4: 'Abril',
             5: 'Mayo',
             6: 'Junio',
             7: 'Julio',
             8: 'Agosto',
             9: 'Septiembre',
             10: 'Octubre',
             11: 'Noviembre',
             12: 'Diciembre'}

    # asistente que diga dia semana
    hablar(f'Hoy es {dias_semana[dia_semana]}, {dia.day} de {meses[dia.month]} de {dia.year}')


# informar de la hora
def pedir_hora():
    # crear variable con datos de la hora
    hora = datetime.datetime.now()

    # decir la hora
    hablar(f'Son las {hora.hour} y {hora.minute}')


# saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 14:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    # decir el saludo
    hablar(f'{momento}, soy tu asistente virtual. Dime en qué te puedo ayudar')


# centro de pedidos
def pedir_cosas():
    # activar saludo inicial
    saludo_inicial()

    # variable de fin
    comenzar = True
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abre youtube' in pedido:
            hablar('Estoy abriendo YouTube')
            webbrowser.open('www.youtube.com')
            continue
        elif 'abre el navegador' in pedido:
            hablar('Estoy abriendo el navegador')
            webbrowser.open('www.google.es')
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscándolo en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(resultado)
            continue
        elif 'busca en google' in pedido:
            hablar('Buscándolo en google')
            pedido = pedido.replace('busca en wikipedia', '')
            pywhatkit.search(pedido)
            continue
        elif 'reproduce' in pedido:
            hablar('Lo reproduzco')
            pedido = pedido.replace('reproduce', '')
            pywhatkit.playonyt(pedido)
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'Apple': 'APPL',
                       'apple': 'APPL',
                       'Amazon': 'AMZN',
                       'amazon': 'AMZN',
                       'google': 'GOOGL',
                       'Google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón, pero no la he encontrado')
        elif 'adiós' in pedido:
            hablar('Chao pescao')
            break


pedir_cosas()
