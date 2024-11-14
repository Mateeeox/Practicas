"""
Programa para organismo del clima

Informatica I
Mateo Madrid
Cristian
"""

import programa_clima


registros=programa_clima.abrirJSON("./plantillas/archivos/registros.json")
usuarios=programa_clima.abrirCSV("./plantillas/archivos/usuarios.csv")
estaciones=programa_clima.abrirCSV("./plantillas/archivos/estaciones.csv")
variables=programa_clima.abrirJSON("./plantillas/archivos/variables.json")

trabajando=True
while trabajando:
    programa_clima.printIntro("./try/logo.txt")
    corte="⫘⫘⫘⫘⫘⫘☀"*10
    print (corte)
    print("\n--- Bienveido a Rainbow, servicio climatologico de Antioquia")
    opcionmenu=programa_clima.opcionMenu()
    print(corte)
    if opcionmenu=="1":
        rol,doc=programa_clima.validarUser(usuarios)
        trabajando=programa_clima.menuRol(rol, estaciones, registros, variables, doc, usuarios)
        if trabajando == "tabla":
            analizando=True
            while analizando:
                a=input("Ingrese 1 cuando quiera dejar de ver\n")
                if a == "1":
                    analizando=False
        trabajando=True
    elif opcionmenu=="2":
        fechai,fechaf=programa_clima.menuVisitante()
        estacion=programa_clima.elegirEstacion(estaciones)
        datoss=programa_clima.elegirVariables(variables, registros)
        fechasvalidas=programa_clima.conseguirRegistros(estacion, datoss, registros, fechai, fechaf)
        estadisticas=programa_clima.estadisticasRegistros(datoss, estacion, registros, fechasvalidas, estaciones)    
        programa_clima.maneraDatos(estadisticas)
        analizando=True
        while analizando:
            a=input("Ingrese 1 cuando quiera dejar de ver\n")
            if a == "1":
                analizando=False
    else:
        programa_clima.printIntro("./try/outro.txt")
        trabajando=False
    
programa_clima.guardarJSON("./plantillas/archivos/registros.json", registros)
programa_clima.guardarJSON("./plantillas/archivos/variables.json", variables)
programa_clima.guardarCSV("./plantillas/archivos/usuarios.csv",usuarios)
programa_clima.guardarCSV("./plantillas/archivos/estaciones.csv",estaciones)
            