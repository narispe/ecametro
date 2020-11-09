#  [sets]:
#    0 = <mensaje de bienvenida>
#    1 = <mensaje al estudiar>
#    2 = <mensaje de despedida>
#    3 = <decimales>

# # [cursos]:
#     X = [ramo_X]:
#     .            0 = <nombre ramo_X>
#     .            1 = [actividades ramo_X]:
#     .                                     Y = [actividad_Y de ramo_X]:
#     .                                     .                           0 = <nombre actividad_Y de ramo_X>
#     .                                     .                           1 = <tiempo actividad_Y de ramo_X>


import func_eca as func
archivo = "data//informacion.txt"
margenes = ""
mg = margenes

sets, cursos = func.leer_info(archivo, mg)
print(f"{sets[0].center(60)}\n")
menu = func.verify(f"{mg}1->Cronometrar   2->Mostrar   3->Exit   4->Reset   0->Configurar\n{mg}: ", f"{mg}Debes seleccionar una de las opciones: ", 0, 4)
while menu != 3:

    if menu == 1:
        if len(cursos) > 0:
            func.estudiar(cursos, sets[1], mg)
        else:
            print(f"{mg}No tienes ramos configurados")

    elif menu == 2:
        if len(cursos) > 0:
            op = func.verify(f"{mg}1->Actividades de un ramo   2->Todos los ramos\n{mg}: ", f"{mg}Debes seleccionar una de las opciones: ", 0, 2)
            if op == 1:
                id_ramo = func.elegir(cursos, mg)
                if id_ramo > -1:
                    ramo = cursos[id_ramo]
                    print(f"\n{mg}{ramo[0]}")
                    print(func.show_time(sets[3], ramo[1], mg))
            elif op == 2:
                total = []
                for ramo in cursos:
                    tiempo_ramo = 0
                    for actividad in ramo[1]:
                        tiempo_ramo += actividad[1]
                    total.append([ramo[0], tiempo_ramo])
                print(f"\n{func.show_time(sets[3], total, mg)}")
        else:
            print(f"{mg}No tienes ramos para mostrar")

    elif menu == 4:
        confirm_reset = func.verify(f"{mg}1->Confirmar  0->Cancelar\n{mg}: ", f"{mg}Selecciona una de las opciones", 0, 1)
        if confirm_reset == 1:
            for ramo in cursos:
                for actividad in ramo[1]:
                    actividad[1] = 0
            print(f"{mg}Se han reseteado todos los tiempos")

    elif menu == 0:
        mg = mg + "\t|  " 
        config = func.verify(f"\n{mg}0->Return\n{mg}1->Añadir tiempo\n{mg}2->Mensajes\n{mg}3->Decimales\n{mg}4->Ramos\n{mg}: ", f"{mg}Debes seleccionar una de las opciones: ", 0, 4)
        while config != 0:

            if config == 1:
                if len(cursos) > 0:
                    func.tiempo_manual(cursos, mg)
                else:
                    print(f"{mg}No tienes ramos configurados")

            elif config == 2:
                config_mess = func.verify(f"{mg}\n{mg}1->Saludo de inicio\n{mg}2->Mensaje al estudiar\n{mg}3->Mensaje al finalizar\n{mg}: ", f"{mg}Selecciona una de las  opciones: ", 0, maxim=3)
                if config_mess > 0:
                    sets[config_mess-1] = input(f"{mg}Ingresa el nuevo mensaje: ").upper()
                    print(f"{mg}Nuevo mensaje guardado exitosamente")

            elif config == 3:
                decim = input(f"{mg}Ingresa la cantidad de decimales para las horas: ")
                while not decim.isdigit() or int(decim)%1!=0 or int(decim)< 0:
                    decim = input(f"{mg}Debes ingresar un número entero mayor o igual a 0: ")
                sets[3] = int(decim)
                print(f"{mg}Configuracion guardada")

            elif config == 4:
                confirmacion = func.verify(f"{mg}1->Confirmar  0->Cancelar\n{mg}: ", f"{mg}Selecciona una de las opciones: ", 0, 1)
                if confirmacion == 1:
                    cursos = func.config_ramos(mg)
                    print(f"{mg}Ramos ingresados correctamente")

            func.save(archivo, sets, cursos)
            config = func.verify(f"{mg}\n{mg}0->Return\n{mg}1->Añadir tiempo\n{mg}2->Mensajes\n{mg}3->Decimales\n{mg}4->Ramos\n{mg}: ", f"{mg}Debes seleccionar una de las opciones: ", 0, 4)

        mg = margenes

    func.save(archivo, sets, cursos)
    menu = func.verify(f"\n{mg}1->Cronometrar   2->Mostrar   3->Exit   4->Reset   0->Configurar\n{mg}: ", f"{mg}Debes seleccionar una de las opciones: ", 0, 4)

input(f"{sets[2].center(60)}\n")