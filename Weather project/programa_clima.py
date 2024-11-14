from datetime import datetime,timedelta

import json

"""
FUNCIONES PARA ABRIR Y GUARDAR ARCHIVOS JSON Y CSV
"""
corte="⫘⫘⫘⫘⫘⫘☀"*10
def abrirJSON (rutaArchivo):
    contenido=open(rutaArchivo,"r")
    archivo=json.load(contenido)
    contenido.close()
    return archivo

def guardarJSON (rutaArchivo, archivo):
    texto="{"
    ind="    "
    ultima_fecha=""
    ultima_variable=""
    ultimo_codigo=''
    i=0
    e=0
    q=0
    for sapo in archivo:
        ultimo_codigo+=sapo+","
    ultimo_codigo=ultimo_codigo.strip(",")
    ultimo_codigo=split(ultimo_codigo,",")
    uc=ultimo_codigo[-1]

    for line1 in archivo:
        texto+="\n"+ind+f"\"{line1}\""+":"+" "+"{"
        
        
        for line2 in archivo[line1]:
            texto+="\n"+ind*2+f"\"{line2}\""+":"+" "+"{"
            
            for sapo1 in archivo[line1]:
                ultima_variable+=sapo1+","
            ultima_variable=ultima_variable.strip(",")
            ultima_variable=split(ultima_variable,",")
            uv=ultima_variable[-1]
            
            for fecha in archivo[line1][line2]:
                ultima_fecha+=fecha+','
            ultima_fecha=ultima_fecha.strip(",")
            ultima_fecha=ultima_fecha.split(",")
            
            for line3 in archivo[line1][line2]:  
                if i==0:
                    try:
                        e=0
                        for dato in archivo[line1][line2][line3]:
                            e+=1
                        texto+="\n"+ind*3+f"\"{line3}\""+":"+" "+"["
                        
                        q=0
                        for dato in archivo[line1][line2][line3]:
                            q+=1
                            if q==e:
                                if dato == archivo[line1][line2][line3][-1]:
                                    texto+="\n"+ind*4+f"{dato}"
                            
                            else:
                                texto+="\n"+ind*4+f"{dato}"+","
                            
                            if dato == archivo[line1][line2][line3][-1]:
                                if line3 == ultima_fecha[-1]:
                                    if line3 == ultima_fecha[-1] and line2 == uv:   
                                        if line3==ultima_fecha[-1] and line2 == uv and line1 != uc: 
                                            texto+="\n"+ind*3+"]"+"\n"+ind*2+"}"+"\n"+ind+"},"
                                        else:
                                            if q==e:
                                                texto+="\n"+ind*3+"]"+"\n"+ind*2+"}"+"\n"+ind+"}"
                                    else:
                                        if q==e:
                                            texto+="\n"+ind*3+"]"+"\n"+ind*2+"},"
                                else:
                                    if q==e:
                                        texto+="\n"+ind*3+"],"
                            
                            
                            if line3 == ultima_fecha[-1]:
                                if dato == archivo[line1][line2][line3][-1] and line1 == uc and line2 == uv and q==e:
                                    texto+="\n"+"}"
                        
                                        
                    except:
                       
                        i=1
                        texto+="\n"+ind*3+f"\"{line3}\""+":"+" "+str(archivo[line1][line2][line3])+","
                        
                else:
                    if type(archivo[line1][line2][line3])==str:
                        texto+="\n"+ind*3+f"\"{line3}\""+":"+" "+"\""+str(archivo[line1][line2][line3])+"\""
                    else:
                        texto+="\n"+ind*3+f"\"{line3}\""+":"+" "+str(archivo[line1][line2][line3])
                    
                    if line3 != ultima_fecha[-1]:
                        texto+=","
                    if line3 == ultima_fecha[-1] and line2 == uv:
                        texto+="\n"+ind*2+"}"+"\n"+ind*1+"}"+"\n"+"}"
                    elif line3== ultima_fecha[-1]:
                        texto+="\n"+ind*2+"}"+','
                     
            
            
            
            ultima_fecha=""
            ultima_variable=""
            ultimo_codigo=""

    cance=open(rutaArchivo,"w")
    cance.write(texto)
    cance.close()



    
def abrirCSV(rutaArchivo):
    archivo=open(rutaArchivo, 'r')
        
      
        
    encabezados=archivo.readline()
    encabezados=encabezados.strip()
    encabezados=split(encabezados,",")
    datos={}
      
    for linea in archivo:
          linea=linea.strip()
          colum=[]
          espac=""
          for caracter in linea:
              if caracter==',':
                  colum.append(espac)  
                  espac=""  
              else:
                  espac+=caracter 
          colum.append(espac)  
          
          
          fila ={}
          for i in range(len(encabezados)):
              fila[encabezados[i]] = colum[i]
          codigo = fila["codigo"]
          datos[codigo] = fila

    return datos


def guardarCSV(rutaArchivo,datos):
    encabezado=""
    encabezadodef=""
    linea=""
    texto=""
    nombre=""
    i=0
    a=0
    cantidad=0
    for codigo in datos:
        cantidad=0
        for code in datos[codigo]:
            cantidad+=1
            
    for codigo in datos:
        
        for code in datos[codigo]:
            
            encabezado+=code+","
            if i<cantidad:
                encabezadodef=encabezado
                encabezadodef=encabezadodef.strip(",")
                i+=1
            if a<cantidad:
                linea+=datos[codigo][code]+","
                a+=1
                if a==cantidad:
                    nombre=linea.strip(",")
                    texto+=nombre+"\n"
                    linea=""
                    a=0
    texto=encabezadodef+"\n"+texto

    archivo=open(rutaArchivo,"w")
    archivo.write(texto)
    archivo.close()

"""
OPCIONES VARIAS
"""
def opcionMenu():
    

    opcionn=True
    while opcionn:
        opcion=input("Digite el numero de la opcion que requiere.\n1. Usuario Registrado\n2. Usuario Visitante\n3. Salir\n")
        if opcion == "1":
            opcionn=False
        elif opcion == "2":
            opcionn=False
        elif opcion == "3":
            opcionn=False
    return opcion

def validarUser(users):
    opcion="1"
    if opcion == "1":
        documento=False
        contrasenaa=False
        while documento != True and contrasenaa != True:
            validaciones=False
            while validaciones!=True:
                validacion_lon=False
                while validacion_lon!=True:
                    doc=input("Ingrese su documento\n")
                    if validar_documento(doc) == False:
                        print("Longitud o caracteres prohibidos en su documento, intente nuevamente")
                    else:
                        validacion_lon=True
                validacion_doc=False 
                if doc not in users:
                    print("Documento equivocado, intente nuevamente")
                else:
                    validacion_doc=True
                if validacion_lon==True and validacion_doc==True:
                    validaciones=True
            documento=True
            passw=False
            while passw!=True:
                validacion_lon=False
                while validacion_lon !=True:
                    password=input("Ingrese su contrasena porfavor\n")
                    if validar_passw(password)==False:
                        print("Tamano de la contrasena incorrecto")
                    else:
                        validacion_lon=True
                    validacion_doc=False
                    if password != users[doc]["clave"]:
                            print('Contrasena incorrecta, intente nuevamente')
                    else:
                        validacion_doc=True
                if validacion_lon==True and validacion_doc==True:
                    passw=True
                    div="-"*81
                    print(f'Documento y contrasena correctas\n{div}\nBienvenido {users[doc]["nombre"]}')
            contrasenaa=True
    if users.get(doc):
        rol=users[doc]["rol"]
    return rol,doc

def menuRol(rol,estaciones,registros,variables,docuser,usuarios):
    rol=rol.lower()
    if rol == "operador":
        print("Este son las opciones como Operador")
        opcion=input("1. Seleccionar estacion.\n2. Salir\n")
        print(corte,"\n\n")
        if opcion =="1":
            i=0
            for fila in estaciones:
                i+=1
                print (fila,f" {estaciones[fila]['nombre']}")
        
            Verdadero=True
            while Verdadero:
                numeroest=input("\nDigite el numero de codigo de la estacion\n")
                
                for car in numeroest:
                    num="0123456789"
                    if car not in num:
                        print("Contiene caracteres no validos")
                    else:
                        try:
                            car=int(car)
                            if car > i or car<= 0:
                                print("Contiene estacion invalida, intente nuevamente")
                            else:
                                Verdadero=False
                                    
                        except ValueError:
                            print("Caracter invalido, vuelve a intentarlo")
        
            print(corte,"\n\n")
            print (f"Entrando a datos de - {estaciones[numeroest]['nombre']} -")
            
            eleccion=input("1. Mostrar medidas\n2. Ingresar medidas\n")
            
            print(corte,"\n\n")
            if eleccion=="1":
                datos=""
                lista=[]
                try:
                    for linea in registros[numeroest]:
                        encabezado=split(linea)
                        for fecha in registros[numeroest][linea]:
                            datos+=fecha+","
                            i=0
                            for dato in registros[numeroest][linea][fecha]:
                                i+=1
                                dato=str(dato)
                                if i < len(registros[numeroest][linea][fecha]):
                                    datos+=dato+","
                                else:
                                    datos+=dato
                            
                            minilista=split(datos,",")
                            lista.append(minilista)
                            datos=""
                            
                        imprimir_tabla(lista, 12, encabezado)
                        lista=[]
                    
                except:
                    print("No hay datos registrados para esa estacion")
                return "tabla"  
            else:
                print(f"Fecha y hora de la sesion:{datetime.now()}")
                print("Estas son las medidas a ingresar")
                datos=""
                lista=[]
                for linea in variables:
                    
                    for var in variables[linea]:
                       
                        encabezado=var.split()
                        for dato in variables[linea][var]:
                            
                            datos+=dato+","+str(variables[linea][var][dato])
                            
                            datos=datos.strip(",")
                            minilista=split(datos,",")
                            lista.append(minilista)
                            datos=""
                            
                        imprimir_tabla(lista, 12, encabezado)
                        print("\n")
                        lista=[]
                ingresarDatosJSON(registros,numeroest,variables)
        else:
            return False
     
    if rol =="administrador":
         i=0   
         print("Este son las opciones como Administrador")
         opcion=input("1. Volver al menu inicial.\n2. Gestionar estaciones\n3. Gestionar usuario\n4. Depuracion de registros\n")
         if opcion=="2":
             estaciones1=input("1. Crear estacion\n2. Editar estacion\n3. Eliminar estacion\n")
             if estaciones1=="1":
                 nombreest=input("Ingrese el nombre de la estacion\n")
                 for estacion in estaciones:
                     i+=1
                 estaciones[f"{i+1}"]={"codigo":f"{i+1}","nombre":nombreest}
             elif estaciones1=="2":
                 limpiar_pantalla()
                 for fila in estaciones:
                     print (fila,f" {estaciones[fila]['nombre']}")
                 estacionsele=input("Selecciona una de las estaciones existentes\n")
                 print(f"Estacion a editar: {estaciones[estacionsele]['nombre']}")
                 newna=input("Ingresa el nuevo nombre para la estacion\n")
                 estaciones[estacionsele]={"codigo":estaciones[estacionsele]["codigo"],"nombre":newna}
                 print("Nombre cambiado con exito")  
             
             else:
                 for fila in estaciones:
                     print (fila,f" {estaciones[fila]['nombre']}")
                 estacionsele=input("Selecciona una de las estaciones existentes\n")
                 if registros.get(estacionsele):
                     print("Esta estacion tiene datos almacenados y no puede ser eliminada")
                 else:
                     del estaciones[estacionsele]
         elif opcion=="3":
             user1=input("1. Crear usuario\n2. Editar usuario\n3. Eliminar usuario\n")
             if user1=="1":
                 samedoc=True
                 nocarneed=True
                 while samedoc == True and nocarneed==True:
                     a=0
                     validacionsame=True
                     idd=input("Ingresa documento para el nuevo usuario\n")
                     while validacionsame:
                         while a==0:
                             if idd in usuarios:
                                 print("Documento repetido, intente nuevamente")
                                 
                             else:
                                 validacionsame=False
                             a=1
                         if validar_documento(idd)==False:
                             print("Caracter o longitud invalida, intenta nuevamente")
                         else:
                             nocarneed=False
                 nombrever=False
                 while nombrever==False:
                     nombre=input("Ingrese nombre completo\n")
                     nombrever=validar_nombre(nombre)
                     if nombrever==False:
                         print("Caracteres invalidos, intente nuevamente")
                 passw=False
                 while passw == False:
                     paass=input("Ingresa una contrasena porfavor\n")
                     passw=validar_passw(paass)
                     if passw==True:
                         confirm=input("Confirme contrasena porfavor\n")
                         if paass != confirm:
                             passw=False
                 rol=input("Selecciona rol.\n1. Operador\n2. Administrador\n")
                 if rol == "1":
                     rolfinal="Operador"
                     
                 else:
                     rolfinal="Administrador"
                 usuarios[idd]={"codigo":idd,"nombre":nombre,"clave":paass,"rol":rolfinal}
             elif user1=="2":
                 print("Digita el codigo del usuario a editar")
                 for user in usuarios:
                     print (user,f" {usuarios[user]['nombre']}")
                 useer=input()
                 
                 if usuarios.get(useer):
                     print("Nombre: ",usuarios[useer]["nombre"],"\nClave: ",usuarios[useer]["clave"],"\nRol: ",usuarios[useer]["rol"])
                     nombrever=False
                     while nombrever==False:
                         nombre=input("Ingrese nombre completo\n")
                         nombrever=validar_nombre(nombre)
                         if nombrever==False:
                             print("Caracteres invalidos, intente nuevamente")
                     passw=False
                     while passw == False:
                         paass=input("Ingresa una contrasena porfavor\n")
                         passw=validar_passw(paass)
                         if passw==True:
                             confirm=input("Confirme contrasena porfavor\n")
                             if paass != confirm:
                                 passw=False
                     rol=input("Selecciona rol.\n1. Operador\n2. Administrador\n")
                     if rol == "1":
                         rolfinal="Operador"
                     else:
                         rolfinal="Administrador"
                     usuarios[useer]={"codigo":useer,"nombre":nombre,"clave":paass,"rol":rolfinal}
                         
                 else:
                     print("Usuario no encontrado")
             else:
                 print("Digita el codigo del usuario a editar")
                 for user in usuarios:
                     print (user,f" {usuarios[user]['nombre']}")
                 delus=input()
                 if usuarios.get(delus):
                     if docuser==delus:
                         print("Usuario actual, no es posible eliminar")
                     else:
                         del usuarios[delus]
         elif opcion=="4":
             
             depurarArch(registros, "./plantillas/archivos/registros_v2.json", estaciones)
         else:
             return "1"
            
        
def ingresarDatosJSON(registros,estacion,arch):
    print('Recuerda ingresar todos los datos necesarios')
    i=0
    fecha= datetime.now()
    dia=fecha.day
    mes=fecha.month
    ano=fecha.year
    fecha=f"{ano}-{mes:02d}-{dia:02d}"
    datos=""
    dato=""
    variaa=""
    for linea in arch:
        
        for var in arch[linea] :
            variaa+=var.lower()+","
    variaa=variaa.strip(",")
    variaa=split(variaa,",")
                

    ingresando=True
    while ingresando:
        while dato not in variaa:
            dato=input ("Ingrese el nombre del dato a ingresar\n")
            dato=dato.lower()
            
            
            if dato not in variaa:
                print("Nombre de dato invalido, ingrese uno existente")
        if dato == "pm10" or dato== "pm25":
            dato=dato.upper()
        else:
            letra=dato[0].upper()
            dato=letra+dato[1:]
        while i!=5:
            a=input(f"Ingresa la medida para el dato {dato}\n")
            
            if a.upper() =="ND":
                datos+=str(-999)+","
                i+=1
            else: 
                try:
                    a=float(a)
                    minimo=arch["variables"][dato]["minimo"]
                    maximo=arch["variables"][dato]["maximo"]
                    if a >=minimo and a<=maximo:
                        i+=1
                        datos+=str(a)+","
                    else:
                        print("Dato invalido, intente nuevamente")
                except ValueError:
                    print("Dato ingresado invalido, su valor sera ND")
                    datos+=str(-999)+","
                    i+=1
                
        
        datos=datos.strip(",")
        lista=split(datos,",")
        if registros.get(estacion):
            if estacion not in registros:
                registros[estacion] = {}

    
            if dato not in registros[estacion]:
                registros[estacion][dato] = {}

            if fecha not in registros[estacion][dato]:
                registros[estacion][dato][fecha] = []
                registros[estacion][dato][fecha]=(lista)
            else:
                registros[estacion][dato][fecha]=(lista)
                
        else:
            if estacion not in registros:
                registros[estacion] = {}

    
            if dato not in registros[estacion]:
                registros[estacion][dato] = {}

            if fecha not in registros[estacion][dato]:
                registros[estacion][dato][fecha] = []
            
            registros[estacion]={dato:{str(fecha):(lista)}}
        
                
            
            

        res=input("Si no quiere ingresar mas datos, ingrese 1\nDe lo contrario, ingrese cualquier otro caracter\n")
        dato="0"
        datos=""
        i=0
        if res=="1":
            print("Guardado exitosamente")
            return registros
    
    
def menuVisitante ():
    valido=True
    validacion=True
    while valido:
        rang=input("1. 7 dias\n2. 30 dias\n3. Ingresar fechas manualmente\n\n")
        hoy = datetime.now()
        if rang == "1":
            fechaf = hoy
            fechai = hoy - timedelta(days=7)
            valido=False
            dia=hoy.day
            mes=hoy.month
            ano=hoy.year
            fechaf=f"{ano}-{mes:02d}-{dia:02d}"
            dia=fechai.day
            mes=fechai.month
            ano=fechai.year
            fechai=f"{ano}-{mes:02d}-{dia:02d}"
            print(corte)
            print(f"\n\nFechas seleccionadas:\nInicio:{fechai}\nFin:{fechaf}\n\n")
        elif rang == "2":
            fechaf= hoy
            fechai = hoy - timedelta(days=30)
            valido=False
            dia=hoy.day
            mes=hoy.month
            ano=hoy.year
            fechaf=f"{ano}-{mes:02d}-{dia:02d}"
            dia=fechai.day
            mes=fechai.month
            ano=fechai.year
            fechai=f"{ano}-{mes:02d}-{dia:02d}"
            print(corte)
            print(f"\n\nFechas seleccionadas:\nInicio:{fechai}\nFin:{fechaf}\n\n")
        else:
            while validacion:
                fechais = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                fechafs = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    
                fechai = validar_fecha(fechais)
                fechaf = validar_fecha(fechafs)
    
                if fechai and fechaf:
                    fechai=datetime.strptime(fechais, "%Y-%m-%d")
                    fechaf=datetime.strptime(fechafs, "%Y-%m-%d")
                    if fechai <= fechaf:
                        valido=False
                        validacion=False
                        print(corte)
                        print(f"\n\nFechas seleccionadas:\nInicio:{fechais}\nFin:{fechafs}\n\n")
                        fechai=fechais
                        fechaf=fechafs
                    else:
                        print("La fecha de inicio debe ser anterior a la fecha de fin")
                else:
                    print("Fecha inválida. Asegúrese de que la fecha esté en formato YYYY-MM-DD.")
    return fechai,fechaf
        
def elegirEstacion (estaciones):
    i=0
    print(corte)
    for fila in estaciones:
        i+=1
        print ("\n",fila,f" {estaciones[fila]['nombre']}")
    Verdadero=True
    while Verdadero:
        estacion=input("\nIngresa el codigo de las estaciones separados por una \",\"\n\n")
        estacion=estacion.strip(",")
        estacion=split(estacion,",")
        for car in estacion:
            num="0123456789"
            if car not in num:
                print("Contiene caracteres no validos")
            else:
                try:
                    car=int(car)
                    if car > i or car<= 0:
                        print("Contiene estacion invalida, intente nuevamente")
                            
                except ValueError:
                    print("Caracter invalido, vuelve a intentarlo")
        print(corte)
        print("\n\nEstaciones seleccionadas:")
        try:
            for codigo in estacion:
                print (codigo,f" {estaciones[codigo]['nombre']}")
                Verdadero=False
        except KeyError:
            print("Codigo de estacion invalido, intenta nuevamente")
            Verdadero=True
    return estacion

def elegirVariables(variables,registros):
    print("\n\n")
    datos=""
    lista=[]
    i=0
    print(corte,"\n\n\n")
    for linea in variables:
        
        for var in variables[linea]:
            i+=1
            datos+=var+","
        datos=datos.strip(",")
        minilista=split(datos,",")
        lista.append(minilista)
        datos=""
                
        imprimir_tabla(lista, 14)
        lista=[]
    
    variaaa=[]
    variables=minilista
    ingresando=True
    while ingresando:
        datoss=input ("\nIngrese el nombre de los datos a evaluar separados por \",\"\n")
        datoss=datoss.lower()
        datoss=datoss.strip(",")
        datoss=split(datoss,",")
        for dato in datoss:
            if dato == "pm10" or dato== "pm25":
                dato=dato.upper()
            else:
                letra=dato[0].upper()
                dato=letra+dato[1:]
                
            
            if dato not in variables:
                print("Nombre de dato invalido, ingrese uno existente")
            else:
                ingresando=False
                variaaa.append(dato)
                
    return variaaa

def conseguirRegistros(estacionesss,variables,registros,fechai,fechaf):
    fechais=datetime.strptime(fechai, "%Y-%m-%d")
    fechafs=datetime.strptime(fechaf, "%Y-%m-%d") 
    fechasvalidas = {estacion: {variable: [] for variable in variables} for estacion in estacionesss}
    
    for estac in estacionesss:    
        for dato in variables:
            lista=[]
            try:
                for fecha in registros[estac][dato]:
                
                    fecha=datetime.strptime(fecha,"%Y-%m-%d")
                    if fecha>=fechais and fecha<=fechafs:
                        b=0
                        esta=True
                        while esta:
                            if variables[b]==dato:
                                dia=fecha.day
                                mes=fecha.month
                                ano=fecha.year
                                fecha=f"{ano}-{mes:02d}-{dia:02d}"
                                lista.append(fecha)
                                esta=False
                            else:
                                b+=1
                        esta=True
            except:
                print("Una de las estaciones no tiene datos")
                    
            fechasvalidas[estac][dato]=lista
    return fechasvalidas
def estadisticasRegistros(variables,estacionesss,registros,fechasvalidas,estaciones):
    estadisticas = {estacion: {variable: {"Maximo":"","Minimo":"","Promedio":""} for variable in variables} for estacion in estacionesss}
    for estacion in registros:
        if estacion in fechasvalidas:               
            for dato in registros[estacion]:
                a=0
                b=0
                if dato in fechasvalidas[estacion]:
                    for fechass in registros[estacion][dato]:
                        if fechass in fechasvalidas[estacion][dato]:
                            max1=0
                            valores=registros[estacion][dato][fechass]
                            valorinicial=valores[0]
                            for valor in valores:#max
                                if valor > valorinicial:
                                    valorinicial=valor
                            max1=valorinicial
                            if a==0:
                                max2=valorinicial
                                maxx=valorinicial
                                a=1
                            else:
                                if max1>max2:
                                    maxx=max1
                                else:
                                    maxx=max2
                            estadisticas[estacion][dato]["Maximo"]=str(maxx)+","+fechass+","+estaciones[estacion]["nombre"]
                            
                        if fechass in fechasvalidas[estacion][dato]:
                            
                            valores=registros[estacion][dato][fechass]
                            valorinicial=valores[0]
                            for valor in valores:#min
                                if valor < valorinicial:
                                    valorinicial=valor
                            min1=valorinicial
                            if b==0:
                                min2=valorinicial
                                minn=valorinicial
                                b=1
                            else:
                                if min1>min2:
                                    minn=min1
                                else:
                                    minn=min2
                            estadisticas[estacion][dato]["Minimo"]=str(minn)+","+fechass+","+estaciones[estacion]["nombre"]
                        if fechass in fechasvalidas[estacion][dato]:
                            
                            valores=registros[estacion][dato][fechass]
                            sumaval=0
                            i=0
                            for valor in valores:#prom
                                sumaval+=valor
                                i+=1
                            promedio=sumaval/i
                            estadisticas[estacion][dato]["Promedio"]=str(promedio)+","+fechass+","+estaciones[estacion]["nombre"]
    return estadisticas
def maneraDatos(estadisticas):  
    gratifi=True
    while gratifi:
        eleccionelegida=input("Ingresa de que manera deseas ver los datos\n1. Texto en pantalla\n2. Archivo \n")
        if eleccionelegida=="1":
            datos=""
            
            for linea in estadisticas:   
                
                for var in estadisticas[linea]:
                    encabezado=[f"Variable:{var}","Valor","Fecha","Estacion"]
                    lista=[]
                    
                    for dato in estadisticas[linea][var]:
                        if estadisticas[linea][var][dato] == "":
                            datos+="-999," * 4
                        else:
                            datos+=dato+","+str(estadisticas[linea][var][dato])
                        
                        datos=datos.strip(",")
                        minilista=split(datos,",")
                        lista.append(minilista)
                        datos=""
                        
                    imprimir_tabla(lista, 20, encabezado)
                    lista=[]
            
            print("Interprete \"-999\" que en esa fecha no habia datos")
            gratifi=False
        elif eleccionelegida=="2":
            texto=""
            gratifi=False
            for linea in estadisticas:
                for var in estadisticas[linea]:
                    
                    texto+=f"\n{var}\n--------- Variable ---- Valor -------- Fecha ---------------- Estacion -----------------\n\n\n\n"
                    for dato in estadisticas[linea][var]:
                        if estadisticas[linea][var][dato]=="":
                            texto+="----------------999"*4+"\n"
                        else:
                            quitarcosos=split(dato+","+str(estadisticas[linea][var][dato]),",")
                            for kkk in quitarcosos:
                                if kkk=="Promedio":
                                    texto+="        "+kkk
                                else:
                                    texto+="          "+kkk
                            texto+="\n"
            hoy=datetime.now()
            dia=hoy.day
            mes=hoy.month
            ano=hoy.year
            fechaf=f"{ano}-{mes:02d}-{dia:02d}"
            contenido=open(f"Estadisticas-{fechaf}.txt","w")
            contenido.write(texto)
            contenido.close()
            


def depurarArch(registros1, rutaArchivo2, estaciones):
    registros2=abrirJSON(rutaArchivo2)
    comunes = {}
    for estacion in registros1:
        if estacion in registros2:
            comunes[estacion] = {}
            for variable in registros1[estacion]:
                if variable in registros2[estacion]:
                    comunes[estacion][variable] = {}
                    for fecha in registros1[estacion][variable]:
                        if fecha in registros2[estacion][variable]:
                            datos1 = registros1[estacion][variable][fecha]
                            datos2 = registros2[estacion][variable][fecha]
                            if datos1 == datos2:
                                comunes[estacion][variable][fecha] = datos1
    unicos = {}
    for estacion in registros1:
        if estacion not in unicos:
            unicos[estacion] = {}
        for variable in registros1[estacion]:
            if variable not in unicos[estacion]:
                unicos[estacion][variable] = {}
            for fecha in registros1[estacion][variable]:
                if estacion not in registros2 or variable not in registros2[estacion] or fecha not in registros2[estacion][variable]:
                    unicos[estacion][variable][fecha] = registros1[estacion][variable][fecha]
                elif registros1[estacion][variable][fecha] != registros2[estacion][variable][fecha]:
                    unicos[estacion][variable][fecha] = {
                        'archivo1': registros1[estacion][variable][fecha],
                        'archivo2': registros2[estacion][variable][fecha]
                    }
    for estacion in registros2:
        if estacion not in unicos:
            unicos[estacion] = {}
        for variable in registros2[estacion]:
            if variable not in unicos[estacion]:
                unicos[estacion][variable] = {}
            for fecha in registros2[estacion][variable]:
                if estacion not in registros1 or variable not in registros1[estacion] or fecha not in registros1[estacion][variable]:
                    unicos[estacion][variable][fecha] = registros2[estacion][variable][fecha] 
    print("Registros comunes:")
    for estacion in comunes:
        print(f"\n\nEstación: {estacion} -- {estaciones[estacion]['nombre']}\n\n")
        for variable in comunes[estacion]:
            print(f"Variable: {variable}")
            for fecha in comunes[estacion][variable]:
                print(f"-- Fecha: {fecha} == {comunes[estacion][variable][fecha]}")
    print("\nRegistros únicos o diferentes en cualquiera de los dos archivos:")
    for estacion in unicos:
        print(f"\n\nEstación: {estacion} -- {estaciones[estacion]['nombre']}\n\n")
        for variable in unicos[estacion]:
            print(f"Variable: {variable}")
            for fecha in unicos[estacion][variable]:
                datos = unicos[estacion][variable][fecha]
                try:
                    print(f"-- Fecha: {fecha}")
                    print(f" Archivo 1: {datos['archivo1']}")
                    print(f" Archivo 2: {datos['archivo2']}")
                except:
                    print(f"-- Fecha: {fecha}, Datos: {datos}")















            
def limpiar_pantalla():
    '''
    Imprime varias líneas en blanco, para dar la ilusión 
    de limpiar la pantalla
    '''
    print('\n'*20)
            

            
def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
        fila: Lista con los textos de las celdas de la fila
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)








def validar_nombre(nombre):
    
    '''
    Valida nombre válido (solo letras y espacios)
    Argumentos:
        nombre: String a validar
    return -> Boolean (True or False) si es valido o no
    '''
    alp = "abcdefghijklmnopqrstuvwxyz"
    alp_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    space=" "
    verd = False
    nombre = ""
    
    for char in nombre:
        
        if char in alp or char in alp_upper or char in space:
            verd=True
            
        else:
            
            return False
    return True

def validar_documento(documento):
    
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    
    Argumentos:
        documento: string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    num = "0123456789"
    ver = False
    
    if len(documento)!=10:
        ver = False

        return ver
        
    else: 
        for c in documento:
            
            if c in num:
                ver = True
                
            else:
                ver = False
                
                return ver
                
        return ver
    
def validar_fecha(fecha):
    '''
    Valida que un string corresponda a una fecha válida (con formato yyyy-mm-dd).
    
    Argumentos:
        fecha -> string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError: #Si el bloque try tira error, except se ejecuta
        return False
    return True

def validar_passw (contrasena):
    if len(contrasena)<4:
        return False
    else:
        return True

def split(text: str, sep = ' ') -> list:
    '''
    Parametros
    ----------
    text : str
        Texto a combertir en lista.
    sep : str, optional
        Indicador para separar el texto. El valor por defecto es ' '.

    Returns
    -------
    list
        Lista con el texto separado según el separador.
    
    Ejemplo
    -------
    
    >>> split('cama, casa, cosa, comida, candado', ', ')
    ['cama', 'casa', 'cosa', 'comida', 'candado']

    '''   
    
    L = []
    i = 0
    j = len(sep)
    aux = ''
    while j < len(text) + len(sep):
        if sep == text[i:j]:
            L += [aux]
            aux = ''
            i += len(sep) - 1
            j += len(sep) - 1
        else:
            aux += text[i]
        j = j + 1
        i = i + 1
    return L + [aux]





def printIntro(fileName):


    welcome=open(fileName,)
    print(welcome.read())
    welcome.close()



