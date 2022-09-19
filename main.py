# TRIVIA DEL MUNDIAL 2022 - CURSO ABC- PYTHON - MTPE
#Importar librerías
import random, time    # Importamos la librería random y time

#Lo primero es mostrar en la pantalla texto de bienvenida para quien juege la tivia

#Declaración de Constantes
C_AZUL = '\033[34m'
C_ROJO = '\033[31m'
C_VERDE = '\033[32m'
C_AMARILLO = '\033[33m'
C_LILA = '\033[35m'
C_CELESTE = '\033[36m'
RESET = '\033[39m'
T_ESPERA = time.sleep(3)

#Declaración de variables
line = C_ROJO+'\n------------------------------------------------------------------------------------'+RESET
nom = ""
iniciar_trivia = True
puntaje = random.randint(0, 100)
#repetir_trivia = True
#Contadores
intentos = 0

print(line, C_AMARILLO+"\n\t\t BIENVENIDOS A MI TRIVIA")
print("\t¿Cuánto sabes del mundial CATAR 2022?", line)
print(C_AMARILLO+"\tPonemos a prueba nuestros conocimientos"+RESET)

#Es importante las instrucciones sobre el cómo jugar al juego
print("El juego consta de preguntas con respuestas múltiples, si respondes bien sumaras puntos\nsi respondes mal restaran puntos al aza y 3 segundo para responder también al iniciar \nel juego se te asignara al azar el puntaje inicial, tendrás 3 intentos. \n"+C_VERDE+"\t\t\t\tDIVIÉRTETE AL MÁXIMO \t"+ RESET, line)

#Conoceremos a nuestro jugador
while not nom:
  try:
    nom = str(input("Nombre del jugador:\t"+C_AZUL))
  except:
    nom = ""
  print("Debe ingresar su nombre para continuar\t"+C_ROJO,RESET)

print("-> ",nom,RESET +"Puedes acumular puntajes por cada repuesta correcta, empiezas con "+C_LILA, puntaje, RESET +" puntos\n")
#Para dar con la respuesta correcta, se tendra un solo intento
#Iniciar trivia



while iniciar_trivia == True:
  if intentos < 3:
    intentos += 1
    #puntaje = random.randint(0, 100)
    print( "\n\t Intento Número: "+ C_ROJO, intentos)
    print(RESET +"Su puntaje inicial es: " + C_LILA, puntaje)
    input(RESET+"Presione Enter para continuar <>")
    print(line)
    
      #Pregunta 01
    print(C_AZUL +'1) ¿Qué selección no se clasificó al Mundial de Qatar 2022?\n')
    print(C_CELESTE +'\ta)Brasil', '\n\tb)Alemania', '\n\tc)Francia', '\n\td)Colombia')
    print("Tienes 3s antes de contestar la pregunta")
    T_ESPERA
    for i in range(5, -1, -1):
      time.sleep(1.2)
      if i == 0:
        respuesta01 = input(RESET+ "\nEscriba su respuesta: \t"+ C_AZUL)            
          #str(input('Escriba la letra correspondiante:\
        while respuesta01 not in ('a', 'b', 'c', 'd'):
          respuesta01 = input(C_VERDE+"Debes responder con a, b, c, d :" +C_AZUL)
          
          # Verificamos
        if (respuesta01 == 'd'):
          puntaje += random.randint(0, 50)
          print(RESET+"\nRespuesta correcta!!!"+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)
        else:
          puntaje -= random.randint(0, 20)  
          print(C_ROJO + "\nRespuesta incorrecta!!!"+C_AZUL, nom, RESET +", Colombia no clasifico a Catar 2022, su puntaje: "+C_LILA, puntaje, line)
        
      #Par dar con la respuesta se debe captar los datos de respuesta seleccionada
    
        
      #Pregunta 02
    print(C_AZUL +"\n¿Cuándo empieza el Mundial Qatar 2022?")
    print(C_CELESTE+"\ta)15 de Junio", "\n\tb)01 de Agosto", "\n\tc)20 de Noviembre", "\n\td)20 Diciembre")
    print("Tienes 3s antes de contestar la pregunta")
    T_ESPERA
    for i in range(5, -1, -1):
      time.sleep(1.2)
      if i == 0:
        respuesta02 = input(RESET+ "\nEscriba su respuesta: \t"+ C_AZUL)
        while respuesta02 not in ('a', 'b', 'c', 'd'):
          respuesta02 = input(C_VERDE+"Debes responder con a, b, c, d :"+C_AZUL)
          
        if (respuesta02 == 'c'):
          puntaje += random.randint(0, 50)
          print(RESET+"\nRespuesta correcta!!!"+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)
        else:
          puntaje -= random.randint(0, 20)
          print(C_ROJO+"\nRespuesta incorrecta"+C_AZUL, nom, RESET +", El mundial esmpesara el 20 de Nobiembre, su puntaje: "+C_LILA, puntaje, line)
          
      #Pregunta 03
    print(C_AZUL +"\n¿Cuál es el estadio de inaguración del Mundial Qatar 2022?")
    print(C_CELESTE+"\ta)Estadio Al Bayt", "\n\tb)Estadio Al Janoub","\n\tc)Estadio Al Thumama", "\n\td)Estadio Ras Abau Abaud")
    T_ESPERA
    for i in range(5, -1, -1):
      time.sleep(1.2)
      if i == 0:
        respuesta03 = input(RESET+ "\nEscriba su respuesta: \t"+ C_AZUL)
        while respuesta03 not in ('a', 'b', 'c', 'd'):
          respuesta03 = input(C_VERDE+"Debes responder con a, b, c, d :"+C_AZUL)
          
        if (respuesta03 == 'a'):
          puntaje += random.randint(0, 50)
          print(RESET+"\nRespuesta correcta!!!"+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)
        else:
          puntaje -= random.randint(0, 20)
          print(C_ROJO+"\nRespuesta incorrecta!!!"+C_AZUL, nom, RESET +", Estadio Al Bayt, su puntaje: "+C_LILA, puntaje, line)
      
      #Pregunta 04
    print(C_ROJO+"PREGUNTA COMBO"+RESET)
    print(C_AZUL +"\n¿Cúal es el nombre del balón oficial del Mundial Catar 2022 ?")
    print(C_CELESTE+"\ta)Al Ala", "\n\tb)Al Rihla", "\n\tc)Rihla Al", "\n\td)Brazuca")
    respuesta04 = str(input('Esgoce la repuesta: \t'))
    while respuesta04 not in ('a', 'b', 'c', 'd'):
      respuesta04 = input('Debes responder con a, b, c, d :')
      
    if (respuesta04 == 'a'):
      puntaje = puntaje - 5
      print('\nRespuesta incorrecta!!!'+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)
    if (respuesta04 == 'c'):
      puntaje = puntaje / 2
      print('\nRespuesta totalmente incorrecta!!!'+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)  
    if (respuesta04 == 'd'):
      puntaje = puntaje + 5
      print('\nRespuesta incorrecta!!!'+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)
    else:
      puntaje = puntaje * 2
      print('\nRespuesta correcta!!!'+C_AZUL, nom, RESET+"su puntaje es:"+C_LILA, puntaje, line)
      
    print("\nExelente, "+C_AZUL, nom,RESET +"has obtenido un puntaje TOTAL de "+C_LILA, puntaje)  
    if puntaje > 0:
      if puntaje >100:
        print(C_VERDE+"\tSuperaste el Juego")
      if puntaje <100:
        print(C_AMARILLO+"\tCompletaste el Juego")
    else:
        print(C_ROJO+"\tNo superaste el Juego")
      
    print(C_VERDE+"\n¿Deseas intentar jugar la trivia nuevamente?"+RESET)
    repetir_trivia = str(input("Escriba"+C_ROJO+" 'si'"+RESET+" para jugar un nuevo intento, o cualquier tecla para finalizar: "+C_AZUL).lower())
    puntaje = random.randint(0, 100)
    print(line)
    
    if repetir_trivia != "si":
      print(C_AZUL+"\n Espero te hayas divertido vuelve pronto!")
      iniciar_trivia = False 
  else :
    print(C_LILA+"Superaste el numero de intetos")
    iniciar_trivia = False

print(line)
