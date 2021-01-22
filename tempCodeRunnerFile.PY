sacar=lista_respaldo[aleatorio_lista]
                                        filtro=(sacar in lista_formateada)
                                                
                                        if filtro == False:
                                                control= 0
                                                while control == 0:
                                                        aleatorio_lista=random.randint(0,num_aleatorio)
                                                        sacar = lista_respaldo[aleatorio_lista]
                                                        filtro = (sacar in lista_formateada)
                                                        if filtro == False:
                                                                control += 1

                                        else:
                                                f_num=int(aleatorio_lista)
                                                contador.delete(0,END)
                                                contador.insert(0,f_num)
                                                #print(aleatorio_lista)
                                                #print(lista_respaldo)