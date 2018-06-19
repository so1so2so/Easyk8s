#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from k8sproject.k8sapi.allk8s import My_k8s_api
from k8sproject import models
import pickle, json, os
from Easyk8s.settings import STATICFILES_DIRS


# config_file = os.path.join(os.path.join(os.path.join(BASE_DIR, 'keys'), ), 'config')


# Create your views here.
def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'page/main.html')


def login(request):
    return render(request, 'page/login/login.html')


def userinfo(request):
    return render(request, 'page/user/userInfo.html')


def page404(request):
    return render(request, 'page/404.html')


def namespace_list(request):
    get_namespace = My_k8s_api('list_namespace')
    all_name_space_things = get_namespace.getall()
    all_api = models.All_api_for_k8s.objects.values("api_name")

    return render(request, 'page/resource/namespace_list.html', locals())


def node_list(request):
    if request.method == "GET":
        get_node = My_k8s_api('list_node')
        all_node_things = get_node.getall()
        return render(request, 'page/resource/nodes_list.html', locals())


def node_info(request, node_ip):
    all = models.result.objects.filter(api__api_name='list_node')
    for i in all:
        result_pidkle = i.result_from_api_name
        # result=all[0]['result_from_api_name']
        all_node_things = pickle.loads(result_pidkle)
    # if request.method == "GET":
    #     get_node = My_k8s_api('list_node')
    #     # print(node_ip)
    #     all_node_things = get_node.getall()
    return render(request, 'page/resource/node_info.html', locals())


def pod_list(request):
    if request.method == "GET":
        get_pod = My_k8s_api('list_pod_for_all_namespaces')
        namespace = request.GET.get("namespace", None)
        # print(namespace)
        if namespace:
            get_pod = My_k8s_api('list_namespaced_pod', namespace=namespace)
            # print(get_pod)
        all_pod_things = get_pod.getall()
        get_namespace = My_k8s_api('list_namespace')
        all_name_space_things = get_namespace.getall()
        return render(request, 'page/resource/pod_list.html', locals())


def pod_info(request, pod_name):
    if request.method == "GET":
        get_pod = My_k8s_api('list_pod_for_all_namespaces')
        namespace = request.GET.get("namespace", None)
    if namespace:
        get_pod = My_k8s_api('list_namespaced_pod', namespace=namespace)
        # print(get_pod)
    all_pod_things = get_pod.getall()
    get_namespace = My_k8s_api('list_namespace')
    all_name_space_things = get_namespace.getall()
    # print(pod_name)
    return render(request, 'page/resource/pod_info.html', locals())


def cs_list(request):
    get_cs = My_k8s_api("list_component_status")
    all_cs = get_cs.getall()
    return render(request, 'page/resource/cs_list.html', locals())


def config_map(request):
    get_config_map = My_k8s_api("list_config_map_for_all_namespaces")
    namespace = request.GET.get("namespace", None)
    if namespace:
        get_config_map = My_k8s_api('list_namespaced_config_map', namespace=namespace)
    get_all_config_map = get_config_map.getall()
    get_namespace = My_k8s_api('list_namespace')
    all_name_space_things = get_namespace.getall()
    return render(request, 'page/resource/config_map_info.html', locals())


def config_map_info(request, map_name):
    get_config_map = My_k8s_api("list_config_map_for_all_namespaces")
    namespace = request.GET.get("namespace", None)
    if namespace:
        get_config_map = My_k8s_api('list_namespaced_config_map', namespace=namespace)
    get_all_config_map = get_config_map.getall()
    get_namespace = My_k8s_api('list_namespace')
    all_name_space_things = get_namespace.getall()
    return render(request, 'page/resource/config_map_info.html', locals())


def endpoints_list(request):
    get_ep = My_k8s_api("list_endpoints_for_all_namespaces")
    namespace = request.GET.get("namespace", None)
    if namespace:
        get_ep = My_k8s_api('list_namespaced_config_map', namespace=namespace)
    get_all_ep = get_ep.getall()
    return render(request, 'page/resource/config_map_info.html', locals())


def image_list(request):
    return render(request, 'page/img/images.html')


def user_list(request):
    return render(request, 'page/user/userList.html')


def create_menu(request):
    menu = {}
    menu["contentManagement"] = []
    menu_all = models.Menu.objects.all()
    for menus in menu_all:
        menu_name = menus.name
        center = {}
        apiname = models.All_api_for_k8s.objects.filter(menu_name__name=menu_name)
        for i in apiname:
            # api___name=None
            children = False
            if i.api_name.find("namespaced") == -1:
                api___name = i.api_name
                center["title"] = menu_name
                center["icon"] = "icon-text"
                center["href"] = "/k8s/show/%s" % api___name
                center["spread"] = False
        menu["contentManagement"].append(center)

    key_path = os.path.join(os.path.join(STATICFILES_DIRS[0], "json"), "menu.json")
    # print(key_path)
    import codecs
    # print menu.__len__()
    with codecs.open(key_path, "w", 'utf8')as men:
        men.write(json.dumps(menu))
    # STATICFILES_DIRS
    return HttpResponse(json.dumps(menu))


def show_part(request, api_name):
    all_namespace=models.namespace.objects.all()
    namespace = request.GET.get("namespace", None)
    all = models.result.objects.filter(api__api_name=api_name)
    if namespace:
        name_api = api_name.split("_")[1]
        start_str = 'list_namespaced_'
        new_api_name = ''.join([start_str, name_api])
        all = models.result.objects.filter(api__api_name=new_api_name).filter(namespace__namespace_name=namespace)
    for i in all:
        result_pidkle = i.result_from_api_name
        # result=all[0]['result_from_api_name']
        result = pickle.loads(result_pidkle)
    return render(request, 'page/resource/show_part.html', locals())
