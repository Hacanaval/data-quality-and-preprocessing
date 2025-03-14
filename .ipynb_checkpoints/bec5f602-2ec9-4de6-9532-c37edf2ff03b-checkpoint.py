#!/usr/bin/env python
# coding: utf-8

# Los servicios en línea de la Administración empezaron a analizar el comportamiento y a tomar decisiones basadas en datos para mejorar la experiencia en línea.
# 
# Tu primera tarea consiste en evaluar la calidad de una muestra de datos recogidos y prepararla para futuros análisis.
# 

# # Paso 1
# 
# Vamos a evaluar la calidad de los datos recogidos sobre los ciudadanos. Te han pedido que revises los datos recopilados y propongas cambios. A continuación, verás datos sobre un usuario o una usuaria en particular; los revisaremos e identificaremos cualquier posible problema.
# 

# In[ ]:


id_card_no = 3428563
name_surname = 'Joseph_Kobe_Steeler '
age = '74'
subscriptions = ['TAXES', 'social security']


# Examina las opciones que aparecen a continuación y selecciona las que reflejen los problemas que has detectado en los datos recogidos sobre el ciudadano anterior.
# 
# **Opciones:**
# 
# 1. El tipo de datos de `id_card_no` no debe cambiarse de entero a cadena.
#     
# 2. La variable `name_surname` contiene cadenas con espacios innecesarios y guiones bajos entre las partes del nombre.
#     
# 3. El tipo de datos de `age` es incorrecto.
#     
# 4. La lista `subscriptions` contiene cadenas en mayúsculas y minúsculas para las distintas entradas. No hay ningún problema en que las listas sean así.
# 

# Escribe en la siguiente celda Markdown los números de las opciones que has identificado como problemas. Si has encontrado varios problemas, sepáralos con comas.

# "**Escribe aquí tu respuesta y explica tus argumentos:**

# # Paso 2
# 
# Empecemos a hacer cambios para los problemas que hemos identificado. Primero, necesitamos corregir los problemas de la variable `user_name` Tenemos que eliminar los espacios y sustituir los guiones bajos por espacios.
# 

# In[ ]:


name_surname = 'Joseph_Kobe_Steeler '
name_surname = # escribe tu código aquí
name_surname = # escribe tu código aquí

print(name_surname)


# # Paso 3
# 
# Vamos a dividir el nombre completo almacenado en la variable `name_surname` en subcadenas. Necesitamos obtener una lista que contenga los nombres por separado.
# 

# In[ ]:


name_surname = 'Joseph Kobe Steeler'
name_split = # escribe tu código aquí

print(name_split)


# # Paso 4
# 
# Arreglemos la variable `age`, ya que tiene un tipo de datos incorrecto.
# 

# In[ ]:


age = '74'

print(type(age))
age = # escribe tu código aquí

print(age)
print(type(age))


# # Paso 5
# 
# ¿Y qué pasaría si en lugar de la edad tuviéramos otra cosa que no fuera exactamente un número? No podríamos convertirlo a `int`. Si lo intentáramos, nuestro sistema se bloquearía.
# 
# Vamos a escribir un fragmento de código para evitar que el sistema se bloquee, en su lugar mostrará un mensaje de error amigable.
# 

# In[ ]:


age = 'seventy four'

try:
    age = # escribe tu código aquí
except:
    print('La edad debe ser un valor numérico.')


# # Paso 6
# 
# Supongamos ahora que la Administración lanza una cuenta corriente (CA, del inglés "current account") en línea para los ciudadanos, en la que estos pueden consultar las devoluciones de impuestos y otras subvenciones como números enteros positivos, y los impuestos adeudados y las cotizaciones a la Seguridad Social como números negativos. Nos gustaría saber cuánto tiene que recibir o pagar cada ciudadano, así como el mayor valor que el ciudadano recibirá Y pagará. Para eso tenemos lo siguiente:
# 
# - El importe total sería la suma de todos los importes. Si es negativo, el ciudadano tendrá que pagar impuestos, y si es positivo, recibirá dinero.
# - El importe mínimo será el mayor impuesto/contribución que tenga que pagar el ciudadano, ya que aparecen como números negativos.
# - El importe máximo será la mayor bonificación/subvención fiscal que pueda recibir el ciudadano.
# 
# Vamos a calcular estos valores y mostrarlos en la pantalla:
# 

# In[ ]:


citizen_CA = [-465, 156, -567, -6051, 8607]

total_amount = # escribe tu código aquí
max_tax_due = # escribe tu código aquí
max_rebate = # escribe tu código aquí

print(total_amount)
print(max_tax_due)
print(max_rebate)


# # Ejercicio 7
# 
# La Administración quiere enviar un correo electrónico con el siguiente texto al ciudadano, notificando el inicio de la devolución de impuestos: `Estimado Citizen_name, ha gastado más de 10,000 en el mes month_nº. Su devolución de impuestos se inicia el mes que viene, el month_nº+1.`
# 

# In[ ]:


name_surname = 'Joseph Kobe Steeler'
months = 5

message = # escribe tu código aquí
print(message)


# Presentaremos un caso cotidiano real. El banco ABC ha lanzado recientemente su servicio de banca privilegiada para clientes de alto poder adquisitivo.
# 
# Nuestro objetivo principal es organizar el almacenamiento de información para los nuevos clientes. A continuación, investigaremos sobre los primeros clientes para comprender mejor quiénes son.

# ### Ejercicio 1
# 
# La información sobre cada nuevo cliente deberá facilitarse en el siguiente orden: documento de identidad, nombre, edad, ingresos netos anuales y ocupación. Esta es la lista que contiene los datos de Jack: `32456`, `'Jack Wilson'`, `32`, `150000`, `'Healthcare'`. Crea la variable `client_info` con la información sobre Jack e imprímela.

# In[ ]:


client_info = # escribe tu código aquí
print(client_info)


# ### Ejercicio 2
# 
# Para organizar el almacenamiento de la información de varios clientes, hemos creado la variable `clients` y le hemos asignamos una lista vacía.
# 
# La información sobre Jack se almacena en la variable `client_info`. El objetivo es añadir esta información a la lista existente `clients` como una lista anidada. Hazlo. Cuando acabes, no te olvides de imprimir la lista `clients`.

# In[ ]:


clients = []
client_info = [32456, 'Jack Wilson', 32, 150000, 'Healthcare']

# escribe tu código aquí

print(clients)


# ### Ejercicio 3
# 
# Se ha añadido información sobre una nueva clienta, Nina Brown, a la lista de `clients`. El banco está interesado en su ingreso neto anual, que se sitúa en la 4ª posición de la lista. Nuestro objetivo es extraer esta información, asignarla a la variable `client_income` e imprimirla.

# In[ ]:


clients = [
    [32456, 'Jack Wilson', 32, 150000, 'Healthcare'],
    [34591, 'Nina Brown', 45, 250000, 'Telecom']
]

client_income = # escribe tu código aquí
print(client_income)


# ### Ejercicio 4
# 
# El número de clientes crece rápidamente. Dos clientes más se han unido recientemente al servicio y ya figuran en la lista de `clients`. Sin embargo, un empleado del banco ha cometido un error tipográfico al añadir la información del cliente, concretamente en el campo de ocupación de Brian Pérez (`'Transportatiion'`). Dado que esta entrada no es válida, debe eliminarse de la lista de `clients`. Tu objetivo es eliminar toda la sublista errónea de la lista `clients` e imprimir esta última.

# In[ ]:


clients = [
    [32456, 'Jack Wilson', 32, 150000, 'Healthcare'],
    [34591, 'Nina Brown', 45, 250000, 'Telecom'],
    [37512, 'Alex Smith', 39, 210000, 'IT'],
    [39591, 'Brian Perez', 29, 340000, 'Transportatiion']
]

# escribe tu código aquí

print(clients)


# ### Ejercicio 5
# 
# La información sobre Brian Pérez ha sido actualizada. Además, otros dos clientes se han unido recientemente al servicio. Ahora el banco quiere analizar a los clientes para determinar la distribución de edades de mayor a menor.
# 
# En el precódigo, encontrarás la variable `ages` que contiene las edades de todos los clientes actuales. Nuestro objetivo es ordenar esta lista en orden descendente e imprimirla. Para ordenar, utiliza el método `sort()`.

# In[ ]:


ages = [32, 45, 39, 29, 25, 32]

# escribe tu código aquí

print(ages)


# ### Ejercicio 6
# 
# El departamento de seguridad del banco nos pidió una lista con los nombres de nuestros primeros clientes. Actualmente, esta información está disponible como una cadena en la que todos los nombres están separados por comas y que se almacena como la variable `names`.
# 
# Para ayudar, vamos a convertir la cadena en una lista llamada `names_split`, donde cada elemento representa el nombre de un cliente. No olvides mostrar la lista resultante.

# In[ ]:


names = 'Jack Wilson,Nina Brown,Alex Smith,Brian Perez,David Martinez,John Kim'

names_split = # escribe tu código aquí

print(names_split)


# Los servicios en línea de la Administración empezaron a analizar el comportamiento y a tomar decisiones basadas en datos para mejorar la experiencia en línea.
# 
# Tu primera tarea consiste en evaluar la calidad de una muestra de datos recogidos y prepararla para futuros análisis.
# 

# # Paso 1
# 
# Vamos a evaluar la calidad de los datos recogidos sobre los ciudadanos. Te han pedido que revises los datos recopilados y propongas cambios. A continuación, verás datos sobre un usuario o una usuaria en particular; los revisaremos e identificaremos cualquier posible problema.
# 

# In[ ]:


id_card_no = 3428563
name_surname = 'Joseph_Kobe_Steeler '
age = '74'
subscriptions = ['TAXES', 'social security']


# Examina las opciones que aparecen a continuación y selecciona las que reflejen los problemas que has detectado en los datos recogidos sobre el ciudadano anterior.
# 
# **Opciones:**
# 
# 1. El tipo de datos de `id_card_no` no debe cambiarse de entero a cadena.
#     
# 2. La variable `name_surname` contiene cadenas con espacios innecesarios y guiones bajos entre las partes del nombre.
#     
# 3. El tipo de datos de `age` es incorrecto.
#     
# 4. La lista `subscriptions` contiene cadenas en mayúsculas y minúsculas para las distintas entradas. No hay ningún problema en que las listas sean así.
# 

# Escribe en la siguiente celda Markdown los números de las opciones que has identificado como problemas. Si has encontrado varios problemas, sepáralos con comas.

# **Escribe aquí tu respuesta y explica tus argumentos:**
# 
# Veamos la primera opción. Un tarjeta de identificación suele ser un número, y ahora mismo es un entero, pero podría ser necesario escribir letras también; y las identificaciones son secuencias a las que no se aplican operaciones aritméticas, por lo que deberíamos guardarlas como cadenas. Esta opción no es correcta y no la vamos a anotar.
# 
# Para la segunda opción, la variable name_surname realmente contiene cadenas con espacios y guiones bajos y esto es algo que tenemos que arreglar, ya que un nombre de persona normalmente no tiene guiones bajos ni tampoco espacios. Anotamos esta opción como una de las respuestas.
# 
# La tercera opción indica que el tipo de edad es incorrecto tal y como es ahora mismo, una cadena. No debemos indicar las edades como cadena, ya que las utilizamos para hacer cálculos y la edad siempre es un número. Así que anotamos esta opción como una de las respuestas.
# 
# En la cuarta opción se afirma que tenemos una lista con cadenas en mayúsculas y minúsculas, lo cual es cierto. Pero también se dice que no hay ningún problema en que las listas se almacenen así y esto no es cierto, ya que añade dificultad a la hora de seguir analizando los datos, por ejemplo, para encontrar duplicados. Deberíamos cambiar estos elementos para utilizar solo mayúsculas o minúsculas, y la mejor práctica es que todo se escriba en minúsculas. Por lo tanto, tenemos que cambiarlo. Anotamos esta opción como una de las respuestas.
# 
# Por eso, el estudiante debe escribir aquí la respuesta:
# 
# 2, 3, 4.
# 
# Para el nº 2: Explicación de por qué debe corregirse
# 
# Para el nº 3: Explicación de por qué debe corregirse
# 
# Para el nº 4: Explicación de por qué debe corregirse
# 

# # Paso 2
# 
# Empecemos a hacer cambios para los problemas que hemos identificado. Primero, necesitamos corregir los problemas de la variable `user_name` Tenemos que eliminar los espacios y sustituir los guiones bajos por espacios.
# 

# In[ ]:


name_surname = 'Joseph_Kobe_Steeler '
name_surname = name_surname.strip()
name_surname = name_surname.replace('_', ' ')

print(name_surname)


# # Paso 3
# 
# Vamos a dividir el nombre completo almacenado en la variable `name_surname` en subcadenas. Necesitamos obtener una lista que contenga los nombres por separado.
# 

# In[ ]:


name_surname = 'Joseph Kobe Steeler'
name_split = name_surname.split()

print(name_split)


# # Paso 4
# 
# Arreglemos la variable `age`, ya que tiene un tipo de datos incorrecto.
# 

# In[ ]:


age = '74'

print(type(age))
age = int(age)

print(age)
print(type(age))


# # Paso 5
# 
# ¿Y qué pasaría si en lugar de la edad tuviéramos otra cosa que no fuera exactamente un número? No podríamos convertirlo a `int`. Si lo intentáramos, nuestro sistema se bloquearía.
# 
# Vamos a escribir un fragmento de código para evitar que el sistema se bloquee, en su lugar mostrará un mensaje de error amigable.
# 

# In[ ]:


age = 'seventy four'

try:
    age = int(age)
except:
    print('La edad debe ser un valor numérico.')


# # Paso 6
# 
# Supongamos ahora que la Administración lanza una cuenta corriente (CA, del inglés "current account") en línea para los ciudadanos, en la que estos pueden consultar las devoluciones de impuestos y otras subvenciones como números enteros positivos, y los impuestos adeudados y las cotizaciones a la Seguridad Social como números negativos. Nos gustaría saber cuánto tiene que recibir o pagar cada ciudadano, así como el mayor valor que el ciudadano recibirá Y pagará. Para eso tenemos lo siguiente:
# 
# - El importe total sería la suma de todos los importes. Si es negativo, el ciudadano tendrá que pagar impuestos, y si es positivo, recibirá dinero.
# - El importe mínimo será el mayor impuesto/contribución que tenga que pagar el ciudadano, ya que aparecen como números negativos.
# - El importe máximo será la mayor bonificación/subvención fiscal que pueda recibir el ciudadano.
# 
# Vamos a calcular estos valores y mostrarlos en la pantalla:
# 

# In[ ]:


citizen_CA = [-465, 156, -567, -6051, 8607]

total_amount = sum(citizen_CA)
max_tax_due = min(citizen_CA)
max_rebate = max(citizen_CA)

print(total_amount)
print(max_tax_due)
print(max_rebate)


# # Ejercicio 7
# 
# La Administración quiere enviar un correo electrónico con el siguiente texto al ciudadano, notificando el inicio de la devolución de impuestos: `Estimado Citizen_name, ha gastado más de 10,000 en el mes month_nº. Su devolución de impuestos se inicia el mes que viene, el month_nº+1.`
# 

# In[ ]:


name_surname = 'Joseph Kobe Steeler'
months = 5

message = f'Estimado {name_surname}, ha gastado más de 10,000 en el mes de {months}. Su devolución de impuestos comienza en el mes siguiente, {months+1}.'
print(message)


# Presentaremos un caso cotidiano real. El banco ABC ha lanzado recientemente su servicio de banca privilegiada para clientes de alto poder adquisitivo.
# 
# Nuestro objetivo principal es organizar el almacenamiento de información para los nuevos clientes. A continuación, investigaremos sobre los primeros clientes para comprender mejor quiénes son.

# ### Ejercicio 1
# 
# La información sobre cada nuevo cliente deberá facilitarse en el siguiente orden: documento de identidad, nombre, edad, ingresos netos anuales y ocupación. Esta es la lista que contiene los datos de Jack: `32456`, `'Jack Wilson'`, `32`, `150000`, `'Healthcare'`. Crea la variable `client_info` con la información sobre Jack e imprímela.

# In[ ]:


lient_info = [32456, 'Jack Wilson', 32, 150000, 'Healthcare']
print(client_info)


# ### Ejercicio 2
# 
# Para organizar el almacenamiento de la información de varios clientes, hemos creado la variable `clients` y le hemos asignamos una lista vacía.
# 
# La información sobre Jack se almacena en la variable `client_info`. El objetivo es añadir esta información a la lista existente `clients` como una lista anidada. Hazlo. Cuando acabes, no te olvides de imprimir la lista `clients`.

# In[ ]:


clients = []
client_info = [32456, 'Jack Wilson', 32, 150000, 'Healthcare']

clients.append(client_info)

print(clients)


# ### Ejercicio 3
# 
# Se ha añadido información sobre una nueva clienta, Nina Brown, a la lista de `clients`. El banco está interesado en su ingreso neto anual, que se sitúa en la 4ª posición de la lista. Nuestro objetivo es extraer esta información, asignarla a la variable `client_income` e imprimirla.

# In[ ]:


clients = [
    [32456, 'Jack Wilson', 32, 150000, 'Healthcare'],
    [34591, 'Nina Brown', 45, 250000, 'Telecom']
]

client_income = clients[1][3]
print(client_income)


# ### Ejercicio 4
# 
# El número de clientes crece rápidamente. Dos clientes más se han unido recientemente al servicio y ya figuran en la lista de `clients`. Sin embargo, un empleado del banco ha cometido un error tipográfico al añadir la información del cliente, concretamente en el campo de ocupación de Brian Pérez (`'Transportatiion'`). Dado que esta entrada no es válida, debe eliminarse de la lista de `clients`. Tu objetivo es eliminar toda la sublista errónea de la lista `clients` e imprimir esta última.

# In[ ]:


clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportatiion"],
]

clients.pop(3)

print(clients)


# ### Ejercicio 5
# 
# La información sobre Brian Pérez ha sido actualizada. Además, otros dos clientes se han unido recientemente al servicio. Ahora el banco quiere analizar a los clientes para determinar la distribución de edades de mayor a menor.
# 
# En el precódigo, encontrarás la variable `ages` que contiene las edades de todos los clientes actuales. Nuestro objetivo es ordenar esta lista en orden descendente e imprimirla. Para ordenar, utiliza el método `sort()`.

# In[ ]:


ages = [32, 45, 39, 29, 25, 32]

ages.sort(reverse=True)
print(ages)


# ### Ejercicio 6
# 
# El departamento de seguridad del banco nos pidió una lista con los nombres de nuestros primeros clientes. Actualmente, esta información está disponible como una cadena en la que todos los nombres están separados por comas y que se almacena como la variable `names`.
# 
# Para ayudar, vamos a convertir la cadena en una lista llamada `names_split`, donde cada elemento representa el nombre de un cliente. No olvides mostrar la lista resultante.

# In[ ]:


names = 'Jack Wilson,Nina Brown,Alex Smith,Brian Perez,David Martinez,John Kim'

names_split = names.split(',')

print(names_split)

