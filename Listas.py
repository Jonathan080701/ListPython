"""

"""



#Cadena larga generada por un generador de Lorem ipsum.
cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi dapibus risus non pulvinar viverra. Vestibulum congue eros leo, sed euismod quam bibendum et. Cras vitae nibh eget nulla fringilla tempor. Nulla orci odio, venenatis eget lorem nec, accumsan rhoncus massa. Cras lacinia, purus a pulvinar semper, augue nisi ultricies metus, eu convallis ex felis ut diam. In libero libero, bibendum sit amet nisl id, blandit laoreet orci. Aenean sed dictum tortor. Fusce eget consequat lacus, quis convallis lectus. Sed mollis semper metus. Donec vulputate vulputate turpis, non scelerisque eros facilisis imperdiet. Aliquam euismod ex diam, nec vestibulum arcu condimentum id. Suspendisse congue, magna quis fermentum cursus, risus diam congue sapien, nec convallis felis turpis et ligula. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In hac habitasse platea dictumst. Maecenas dolor nibh, consequat et vehicula eget, rhoncus at orci. Mauris id ex pretium, ornare tortor sed, finibus dui.

Morbi et ipsum nisi. Ut venenatis ipsum sed nisl laoreet interdum. Morbi tristique justo a leo volutpat, sed pulvinar odio semper. Sed rutrum libero sed sapien rhoncus, vel pretium justo varius. Donec neque magna, ultrices imperdiet eros at, vulputate malesuada diam. Suspendisse ex libero, ultrices ac sollicitudin id, tincidunt ac felis. Duis vel augue et urna ultrices pulvinar.

Sed quam justo, maximus et ligula vitae, pulvinar feugiat erat. Aenean rutrum mattis lacus ut imperdiet. Fusce malesuada mattis nunc, et ullamcorper diam ornare ac. Etiam finibus eros non sapien maximus pulvinar. Pellentesque consequat ex nec ligula pharetra, eget placerat arcu tincidunt. Nam pharetra iaculis massa, ac cursus leo commodo in. Nunc tempus lorem nec dolor dapibus, at dictum arcu gravida. Donec sed sagittis ex. Ut interdum pretium dolor, condimentum dignissim risus condimentum non. Nulla facilisi. Vestibulum vestibulum leo ut turpis volutpat, ac viverra lectus cursus. Suspendisse potenti. Phasellus non elit vitae turpis fringilla eleifend eu eget mi. Maecenas varius ligula magna, sed pretium ligula ornare ut.

Fusce vitae nunc ante. Vestibulum auctor, erat et pretium ornare, sem nibh placerat mauris, at dictum lectus felis id leo. Nulla lacinia dui massa, sed tempor neque lobortis rhoncus. Proin bibendum, magna id pellentesque luctus, purus massa molestie turpis, et sodales odio eros ac odio. Vestibulum eu augue in libero consectetur imperdiet. Sed fringilla consequat posuere. Ut in quam lobortis, consectetur mi id, fringilla velit. Donec placerat, sem a lobortis rutrum, dui augue eleifend augue, in pharetra nisl sapien eget lorem. Curabitur sit amet felis vitae metus pulvinar viverra. Praesent elementum turpis magna, nec imperdiet mauris efficitur sed. Praesent in odio et lectus mattis blandit. Proin vel bibendum mi.

Nullam lorem augue, molestie a bibendum nec, semper sed tellus. Quisque dignissim, libero ac suscipit facilisis, magna quam finibus justo, eu auctor lorem tellus sit amet sapien. Donec quis laoreet orci. Curabitur neque turpis, molestie in ex vitae, elementum cursus augue. In blandit augue nec est ultrices, nec mollis diam semper. Vivamus tristique euismod ultrices. Maecenas dapibus ligula nunc, id tristique elit semper eu. Nulla facilisi. Donec eu lorem quam. Integer a ultrices enim, quis euismod neque. Donec interdum, odio in bibendum eleifend, nulla felis tempor quam, nec ornare eros neque sed velit. Maecenas eu varius sem. Maecenas congue et orci id lobortis. Proin id pharetra velit. Pellentesque cursus tempor ligula in malesuada. Cras luctus id urna non viverra.
"""
letras= ['abcdefghijklmnñopqrstuvwxyz']
caracteres = ['a', 'b', 'c', 'd', 'e', ' ', ',', '.']
estadisticas = ['Total de caracteres: ', 'Total de letras: ', 'Total de vocales a: ', 'Total de letras e: ', 'Total de letras i: ', 'Total de letras o: ', 'Total de letras u: ', 'Total de espacios: ', 'Total de comas: ', 'Total de puntos']
estadisticas = [0,0,0,0,0,0,0,0,0,0]

"""
1. Crear lista cadenaLarga
2. crear lista caracteres
3. crear lista de estadisticas
4. crear lista totales
5. Recorrer cadena larga
6. Ir acumulando los valores de totales según caracteres
7. Imprimir totales tomando los valores de las listas "estadisticas y totales"
"""

#Podemos imprimir cadenas largas
print(cadenaLarga)


# Dividimos las cadenas, de tal forma que se hace una lista de parrafos. Esto se realiza con la función .split()
parrafos = cadenaLarga.strip().split('\n\n')


# Creamos las variablespara almacenar las cantidades que le corresponde a cada variable
total_caracteres = 0 #caracteres =`['a', 'e','i', 'o','u', ' ', ',' ]` 
total_letras = 0 #(incluyendo vocales)
total_vocales = 0 #('aeiou')
total_a = 0 #('a')
total_e = 0 #('e')
total_i = 0 #('i')
total_o = 0 #('o')
total_u = 0 #('u')
total_f = 0 #('f')
total_espacios = 0 #(' ')
total_comas = 0 #(',')
total_palabras = 0 #(parrafo.split()) 


# Recorremos cada parrafo de la lista
for parrafo in parrafos:
    # Calcular estadísticas para el párrafo actual
    total_caracteres += len(parrafo) #Leemos cada parrafo de la lista y se almacenan los caracteres
    total_letras += sum(c.isalpha() for c in parrafo)  #Para la suma de cada letra utilizamos un metodo y dentro una iteración con la cual podemos detectar por cada caracter si es una letra.
    total_vocales += sum(c.lower() in 'aeiou' for c in parrafo)# Con el metodo  este metodo podemos detectar que la vocales seaqn minusculas, muy similar a la anterior iteración.
    #Contamos el número de ocurrencias para cada vocal.
    total_a += parrafo.lower().count('a')
    total_e += parrafo.lower().count('e')
    total_i += parrafo.lower().count('i')
    total_o += parrafo.lower().count('o')
    total_u += parrafo.lower().count('u')
    total_f += parrafo.lower().count('f')
    total_espacios += parrafo.count(' ')
    total_comas += parrafo.count(',')
    total_palabras += len(parrafo.split())
#Se realiza cada vuelta, hasta calcular cada uno de las variables.


# Imprimimos el resultado de cada variable.
print("Total de caracteres:", total_caracteres)
print("Total de letras (incluyendo vocales):", total_letras)
print("Total de vocales:", total_vocales)
print("Total de vocales a:", total_a)
print("Total de vocales e:", total_e)
print("Total de vocales i:", total_i)
print("Total de vocales o:", total_o)
print("Total de vocales u:", total_u)
print("Total de vocales f:", total_f)
print("Total de espacios:", total_espacios)
print("Total de comas:", total_comas)
print("Total de palabras:", total_palabras)