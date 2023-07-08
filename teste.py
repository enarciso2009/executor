
caminho = '/home/everton/PycharmProjects/executor/'
arquivo = open('config.txt')
arq = arquivo.readline()
start = arq[6]
print(start)
st = start
if st == '1':
    print('sistema entrou no if do start')

print('sistema esta na ultima linha')