
'''
import datetime
import time

import banco as bco
import os
import teste
# comparar a data atual com a data que foi gravada no banco de dados

servico = bco.select_servico()
print(servico)
n=1

horarios_inicio = bco.select_horainicio()

for i in horarios_inicio:
    hor1 = (i[0])
    hor2 = (i[1])
    hor3 = (i[2])
    hor4 = (i[3])
    hor5 = (i[4])
    hor6 = (i[5])
    hor7 = (i[6])
    hor8 = (i[7])
    hor9 = (i[8])
    hor10 = (i[9])
    hor11 = (i[10])
    hor12 = (i[11])

horarios_termino = bco.select_horatermino()

for i in horarios_termino:
    hor13 = (i[0])
    hor14 = (i[1])
    hor15 = (i[2])
    hor16 = (i[3])
    hor17 = (i[4])
    hor18 = (i[5])
    hor19 = (i[6])
    hor20 = (i[7])
    hor21 = (i[8])
    hor22 = (i[9])
    hor23 = (i[10])
    hor24 = (i[11])

while n == 1:
    print("entrou no while")
    hora = datetime.datetime.now()
    print(hora)
    agora = hora.strftime("%H:%M")
    print(agora)
    print(f'dentro do while',hor13)

    if agora == hor1:
        print(f'agora é:' + hor1 +'vai rodar o start do serviço')
        os.system(f'netstart {servico}')
    if agora == hor2:
        print(f'agora é:' + hor2 + 'vai rodar o start do serviço')
    if agora == hor3:
        print(f'agora é:' + hor3 + 'vai rodar o start do serviço')
    if agora == hor4:
        print(f'agora é:' + hor4 +'vai rodar o start do serviço')
    if agora == hor5:
        print(f'agora é:' + hor5 + 'vai rodar o start do serviço')
    if agora == hor6:
        print(f'agora é:' + hor6 + 'vai rodar o start do serviço')
    if agora == hor7:
        print(f'agora é:' + hor7 +'vai rodar o start do serviço')
    if agora == hor8:
        print(f'agora é:' + hor8 + 'vai rodar o start do serviço')
    if agora == hor9:
        print(f'agora é:' + hor9 + 'vai rodar o start do serviço')
    if agora == hor10:
        print(f'agora é:' + hor10 +'vai rodar o start do serviço')
    if agora == hor11:
        print(f'agora é:' + hor11 + 'vai rodar o start do serviço')
    if agora == hor12:
        print(f'agora é:' + hor12 + 'vai rodar o start do serviço')
    if agora == hor13:
        print(f'agora é:' + hor13 + 'vai rodar o stop do serviço')

    if agora == hor14:
        print(f'agora é:' + hor14 + 'vai rodar o stop do serviço')
    if agora == hor15:
        print(f'agora é:' + hor15 + 'vai rodar o stop do serviço')
    if agora == hor16:
        print(f'agora é:' + hor16 + 'vai rodar o stop do serviço')
    if agora == hor17:
        print(f'agora é:' + hor17 + 'vai rodar o stop do serviço')
    if agora == hor18:
        print(f'agora é:' + hor18 + 'vai rodar o stop do serviço')
    if agora == hor19:
        print(f'agora é:' + hor19 + 'vai rodar o stop do serviço')
    if agora == hor20:
        print(f'agora é:' + hor20 + 'vai rodar o stop do serviço')
    if agora == hor21:
        print(f'agora é:' + hor21 + 'vai rodar o stop do serviço')
    if agora == hor22:
        print(f'agora é:' + hor22 + 'vai rodar o stop do serviço')
    if agora == hor23:
        print(f'agora é:' + hor23 + 'vai rodar o stop do serviço')
    if agora == hor24:
        print(f'agora é:' + hor24 + 'vai rodar o stop do serviço')
    time.sleep(55)
    if teste.alguma == 1:
        n = 0

'''