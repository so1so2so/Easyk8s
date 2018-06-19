#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from kubernetes import client, config
# from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

config.load_kube_config("config")
v1 = client.CoreV1Api()
v2 = client.ExtensionsV1beta1Api()
body = client.V1DeleteOptions()
ret = v1.delete_namespaced_pod(name='nginx-ingress-controller-7494c4c66d-f4mc6',namespace='ingress-nginx',body=body)
v2.create_namespaced_deployment()
print(ret)
# ret2 = v1.list_node(async=True)
# for i in ret.get():
#     print i.status.pod_ip
# print ret.get().items
# # print(ret)
# print ret.get(), ret2.get()
# print(ret.get().items)
# with open("test.json", "w") as f:
#     # for i in ret.get().items:
#     f.writelines(str(ret.get().items))
    # f.writelines(str(ret.items))


# api_response = api_instance.list_namespaced_endpoints(namespace, pretty=pretty, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
#     pprint(api_response)
# print ret.get().items[0].metadata.creation_timestamp


class My_k8s_api():
    def __init__(self, k8s_obj, *args, **kwargs):
        self._k8s_obj = k8s_obj
        self.args = args
        self.kwargs = kwargs

    def getall(self, namespace, **kwargs):
        # print self.args, "单个参数", type(self.args)
        # print self.kwargs, "多个参数"
        return namespace
# watch =False
# names={"zhang":123}
# d= My_k8s_api("obj",watch,**names)
# print d.getall()
# d=My_k8s_api("obj",namespace="ingress-nginx")
# f = getattr(d,"getall")
# f=f(**d.kwargs)
# print f
# from k8sproject import models
# models.result.objects.filter(api__api_name='list_node')
