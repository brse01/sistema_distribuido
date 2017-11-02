# -*- coding: utf-8 -*-

import socket
import sys
import netifaces as ni
import datetime
from random import randint
import string
import random
import time

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_ip_from_interface(interface):
    ni.ifaddresses(interface)
    return ni.ifaddresses(interface)[2][0]['addr']

date_time = datetime.datetime.now()
hostname = sys.argv[1]
host_ip = get_ip_from_interface('%s-eth0' % hostname)


def log(text):
    filename = open('log/[%s] [%s].txt' % (hostname, host_ip), 'a')
    save_string = '[%s] %s\n' % (date_time, text)
    print(save_string)
    filename.write(save_string)
    filename.close()

ip_parts = host_ip.split('.')
rand_int = int(sys.argv[2]) +1


buffer_size = 1024
server_port = 10000

# CAPITURA O VALOR QUE É PASSADO COMO PARAMETRO 
horario = sys.argv[3]
listSokect = []
listClient = []
pergunta = 'Qual seu horario?'
listData = []
listDiferenca = []
listResposas = []

try:	
	for k in range(2,rand_int):
		listSokect.append(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
		client  = '%s.%s.%s.%s' % (ip_parts[0], ip_parts[1], ip_parts[2], k)    		
		log("Conectando a %s" % (client))
		listClient.append(client)
		
	
	
	aux = 0
	for k in range(2,rand_int):		
		listSokect[aux].connect((listClient[aux],server_port))
		print("Perguntando o horario aos clientes")
		log("Perguntando a hora do %s" % listClient[aux])
		listSokect[aux].sendall("Qual o seu horario?@1")
		aux+=1	
		
	aux = 0	
	for k in range(2,rand_int):
		listData.append(listSokect[aux].recv(buffer_size))
		aux+=1

	soma = 0
	soma += int(horario) 
	aux =0
	for k in range(len(listData)):
		soma += int(listData[aux])
		aux+=1

	media = soma / rand_int
	horario = media
	aux =0
	for k in range(2,rand_int):
		listDiferenca.append(media - int(listData[aux]))
		aux+=1

	aux = 0
	for k in range(2,rand_int):
		log('Mensagem "%s" recebida de "%s"' % (listData[aux], listClient[aux]))
		aux +=1

	aux = 0
	for k in range(2,rand_int):
		log("Conectando a %s" % (listClient[aux]))
		aux +=1


	aux = 0
	for k in range(2,rand_int):
		log('Diferença para o cliente "%s" é "%s"' % (str(listClient[aux]),listDiferenca[aux]))
		resposta = str(listDiferenca[aux]) +'@2'
		listSokect[aux].sendall(resposta)
		aux+=1

	print 'horario final do servidor depois do processo %d' % horario

	aux = 0
	for k in range(2,rand_int):
		listSokect[aux].close()


finally:
	pass
