#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from kubernetes import client, config

config.load_kube_config("config")
v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
ret = v1.list_namespaced_pod(async=True, namespace="default")
# for i in ret.get():
#     print i.status.pod_ip
# print ret.get().items
with open("test.json", "w") as f:
    #     # for i in ret.get().items:
    f.writelines(str(ret.get().items))

# print ret.get().items[0].metadata.creation_timestamp


class My_k8s_api():
    def __init__(self, k8s_obj, *args, **kwargs):
        self._k8s_obj = k8s_obj
        self.args = args
        self.kwargs = kwargs

    def getall(self,namespace,**kwargs):
        # print self.args, "单个参数", type(self.args)
        # print self.kwargs, "多个参数"
        return namespace
# watch =False
# names={"zhang":123}
# d= My_k8s_api("obj",watch,**names)
# print d.getall()
d=My_k8s_api("obj",namespace="ingress-nginx")
f = getattr(d,"getall")
f=f(**d.kwargs)
print f