#!/usr/bin/python

import paramiko

class SSHOps:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname="192.168.0.2")
        

    def run_command(self,cmd):
        stdin,stdout,stderr = self.client.exec_command(cmd)#roda cmd no docker
        if stderr.channel.recv_exit_status() !=0:
            return {"status":1,"message":stderr.read()} # se estiver com erro
        else:
            return {"status":0,"message":stdout.read()} # sucesso
