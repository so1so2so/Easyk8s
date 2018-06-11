#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from k8sproject.k8sapi.allk8s import My_k8s_api
from k8sproject import models
from django.shortcuts import render, HttpResponse
import pickle


def get_all_to_databases(request):
    all_api = models.All_api_for_k8s.objects.values("api_name")
    for api_name in all_api:
        api_names = api_name['api_name']
        # print(api_names)
        api_obj = models.All_api_for_k8s.objects.filter(api_name=api_names)[0]
        # print(api_obj)
        # if api_names != 'list_endpoints_for_all_namespaces':  # 这个api有问题
        print(api_names)
        if api_names == "list_namespace":
            for name in My_k8s_api(api_names, async=True).getall().get().items:
                name_space = name.metadata.name
                models.namespace.objects.update_or_create(namespace_name=name_space)
        else:
            try:
                get_all = My_k8s_api(api_names, async=True).getall()
                if get_all and len(get_all.get().items) > 0:
                    # print(get_all.getall())
                    # result = get_all.items[0]
                    # result = str(get_all.get().items)
                    result = pickle.dumps(get_all.get().items)
                    name_space_obj = models.namespace.objects.filter(namespace_name="all")[0]
                    print(api_obj)
                    models.result.objects.update_or_create(
                        result_from_api_name=result,
                        api=api_obj,
                        namespace=name_space_obj,
                    )
            except TypeError:
                all_namespace = models.namespace.objects.values("namespace_name").exclude(namespace_name='all')
                for name_space in all_namespace:
                    name_space_name = name_space["namespace_name"]
                    print(name_space_name)
                    name_space_obj = models.namespace.objects.filter(namespace_name=name_space_name)[0]
                    get_all = My_k8s_api(api_names, namespace=name_space_name, async=True).getall()
                    print(get_all, name_space_name, api_names)
                    # d = get_all.getall()
                    try:
                        if get_all and len(get_all.get().items) > 0:
                            # print(get_all.getall())
                            # result = str(get_all.get().items)
                            result = pickle.dumps(get_all.get().items)
                            models.result.objects.update_or_create(
                                api=api_obj, namespace=name_space_obj,
                                result_from_api_name=result, )
                    except:
                        print ("请检查api名称是否正常", api_names)
                        continue
            except:
                print ("请检查api名称是否正常", api_names)
                continue
    return HttpResponse("配置入库成功")
