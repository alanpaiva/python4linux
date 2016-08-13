#!/usr/bin/python

from Modules.SSHOps import SSHOps

class DockerOps(SSHOps):
    def create_container(self,id,image):
                                    # 1_website
                                    # 52_backup
        cmd = "docker run -tdi --name %s %s /bin/bash"%("%s_%s"%(image,id),"ubuntu")
        #nome do produto + id + imagem(ubuntu)
        result = self.run_command(cmd) #gera comando de install
        if result.get("status") ==1:
            print result["message"]
