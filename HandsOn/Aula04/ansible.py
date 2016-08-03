#!/usr/bin/python
#arquivo ansible.py eh para automatizar tarefas

import paramiko #tem a confirmacao parecido com ssh!
from datetime import datetime

client = paramiko.SSHClient() #le o arquivo known_hosts
client.load_system_host_keys() #aceita fingerprint automaticamente 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#para new servers

#conecta na maquina:
client.connect(hostname="127.0.0.1",username="root",password="4linux")
#executa o comando:
log = datetime.now()
stdin,stdout,stderr = client.exec_command("pwd")
# exibe valores:
'''print stderr.read(),stdout.read()
print "Certo: ",stdout.read()
print "Falhou: ",stdout.read()'''

if stderr.channel.recv_exit_status() !=0: #se o erro for diferente de 0..
    print stderr.read()
else:
    print stdout.read()
    print "Executado as: ",log
