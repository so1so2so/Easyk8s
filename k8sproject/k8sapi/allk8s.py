#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
from kubernetes import client, config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file=os.path.join(os.path.join(BASE_DIR,'keys'),'config')
print(config_file)
class My_k8s_api():
    def __init__(self,k8s_obj,*args,**kwargs):
        self._k8s_obj=k8s_obj
        self.args=args
        self.kwargs=kwargs
    def getall(self):
        config.load_kube_config(config_file)
        v1 = client.CoreV1Api()
        if hasattr(v1,self._k8s_obj):
            ret = getattr(v1,self._k8s_obj)()
            # ret()
    # ret = v1.list_namespace(watch=False)
            return ret
        else:
            return None
