import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 
# print (type(hora)) 
if int(hora) >= 19:
	print ("Es hora de irse a casa") 
else:
    print ("Aun no es tiempo para ir a casa, son las ", hora," horas", minutos,"minutos") 