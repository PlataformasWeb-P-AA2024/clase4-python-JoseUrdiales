archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()
lineas = [l.split("|") for l in lineas]

for i, x in enumerate(lineas[1:]): 
    #el lineas[1:] es para que omita la primera linea del csv que son los encabezados, 
    #así solo salen 25362 archivos en vez de 25363
    
    cadena = """<b>Torneo:</b> %s <br> <b>Ganador:</b> %s""" % (x[0], x[9])
    print(cadena)
    archivo_generado = open("data/ganador_%d_%s.html" % (i + 1, x[9]), "w")
    archivo_generado.writelines("%s\n" % cadena)
    archivo_generado.close()
    
print(len(lineas)) #para saber cuantas líneas existen en el csv