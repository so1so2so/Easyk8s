#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
from kubernetes import client, config
from Easyk8s.settings import MASTER_IP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(os.path.join(os.path.join(BASE_DIR, 'keys'), MASTER_IP), 'config')


# print(config_file)


class My_k8s_api():
    def __init__(self, k8s_obj, *args, **kwargs):
        self._k8s_obj = k8s_obj
        self.args = args
        self.kwargs = kwargs

    def getall(self, *args, **kwargs):
        config.load_kube_config(config_file)
        v1 = client.CoreV1Api()
        if hasattr(v1, self._k8s_obj):
            k8s_instance_obj = getattr(v1, self._k8s_obj)
            ret = k8s_instance_obj(**self.kwargs)
            # ret = v1.list_namespace(watch=False)
            return ret
        else:
            return None
# k8s_obj = My_k8s_api("list_namespaced_pod")
# name = k8s_obj.getall("default")
# for i in name.items:
#     print i.status.pod_ip,">>>>>>>>>",i.status.host_ip
