import time


def leer_info(archivo, margen):
    import os
    import errno
    try:
        os.mkdir("data")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    with open(archivo, "a") as doc:
        pass
    
    with open(archivo, "r", encoding="UTF-8") as doc:
        info = doc.readlines()
    cursos = []
    if len(info) > 1:
        sets = info[0].strip().split(";")
        sets[3] = int(sets[3])

        for linea in info[1:]:
            ramo = linea.strip().split(":")
            act = ramo[1].split(";")
            for a in range(len(act)):
                act[a] = act[a].split(",")
                act[a][1] = int(act[a][1])
            cursos.append([ramo[0], act])

    else:

        print(f"\tBIENVENIDO A ECAMETRO\n{margen}Comienza ingresando tus ramos y sus actividades")
        sets, cursos = ["BIENVENIDO", " ", "FIN", 1], config_ramos(margen)
        save(archivo, sets, cursos)
        print(f"{margen} Ahora ya puedes empezar a usar ecametro\n")
    return sets, cursos


def save(archivo, sets, cursos):
    with open(archivo, "w", encoding="UTF-8") as doc:
        info = ";".join(sets[:3]) + ";" + str(sets[3]) + "\n"
        for ramo in cursos:
            ramo_info = []
            for act in ramo[1]:
                ramo_info.append(act[0] + "," + str(act[1]))
            ramo_info = (ramo[0] + ":" + ";".join(ramo_info) + "\n")
            info += ramo_info
        doc.write(info)


def show_time(d, cursos, margen, indent=False):
    show = []
    len_name, hrs_total, mins_total = [], 0, 0
    for ramo in cursos:
        len_name.append(len(ramo[0]))
        hrs_total += round(ramo[1]/60, d)
        mins_total += ramo[1]

    hrs_total, mins_total = str(round(hrs_total, d)), str(mins_total)
    hrs_total += "0" * (d+2 - len(hrs_total))
    fill_hrs, fill_mins = len(hrs_total), len(mins_total)
    fill_name = max(len_name)
    if indent:
        margen += "\t"

    for ramo in cursos:
        name = ramo[0]
        mins = str(ramo[1])
        hrs = str(round(int(mins)/60, d))
        hrs += "0" * (d+2 - len(hrs))
        show.append(margen + name.rjust(fill_name) + ":\t" + hrs.rjust(fill_hrs) +
                    " horas  ||  " + mins.rjust(fill_mins) + " minutos")
    show.append(margen + "TOTAL".rjust(fill_name) + ":\t" + hrs_total.rjust(fill_hrs) +
                " horas  ||  " + mins_total.rjust(fill_mins) + " minutos")

    return ("\n".join(show))


def verify(mensaje_input, mensaje_error, minim, maxim=10):
    valor = input(mensaje_input)
    while not valor.isdigit() or int(valor)<minim or int(valor)>maxim:
        valor = input(mensaje_error)
    valor = int(valor)
    return valor


def eleccion(lista, margen):
    i = 0
    for linea in lista:
        print(f"{margen}{i+1}->{linea[0]}")
        i += 1
    posicion = verify(f"{margen}: ", f"{margen}Ingresa una de las opciones: ", 0, maxim=len(lista)) - 1
    return posicion


def config_ramos(margen):
    cursos = []
    cant_ramos = verify(f"\n{margen}Ingresa la cantidad de ramos: ",f"{margen}Debes ingresar un valor válido: ", 1)
    for R in range(cant_ramos):
        ramo = []
        name_ramo = input(f"{margen}  Nombre ramo {R+1}: ")
        ramo.append(name_ramo)
        actividades = []
        cant_act = verify(f"{margen}  Ingresa la cantidad de actividades de este ramo: ", f"{margen}  Debes ingresar un valor válido: ", 1)
        for A in range(cant_act):
            name_actividad = input(f"{margen}    Nombre actividad {A+1}: ")
            actividades.append([name_actividad, 0])
        ramo.append(actividades)
        cursos.append(ramo)
    return cursos


def estudiar(cursos, mensaje, margen):
    print(f"{margen}¿Cuál ramo vas a estudiar?")
    id_ramo = eleccion(cursos,margen)
    if id_ramo > 0:
        ramo = cursos[id_ramo]
        print(f"{margen}¿Qué actividad vas a realizar?")
        id_actividad = eleccion(ramo[1],margen)
        if id_actividad > -1:
            actividad = ramo[1][id_actividad]
            t_inicio = time.time()
            input(f"\n{margen}Estudiando {actividad[0]} de {ramo[0]}...\n{margen}{mensaje}\n{margen}Presiona ENTER cuando termines\t")
            t_final = time.time()
            actividad[1] += round((t_final-t_inicio)/60)