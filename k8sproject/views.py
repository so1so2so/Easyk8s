# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from k8sproject.k8sapi.allk8s import My_k8s_api
# Create your views here.
def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'page/main.html')


def login(request):
    # print request.POST
    # print request.POST.get('userName')
    # print request.POST.get('password')
    # print request.POST.get('code')
    pass

    return render(request, 'page/login/login.html')


def userinfo(request):
    return render(request, 'page/user/userInfo.html')


def page404(request):
    return render(request, 'page/404.html')


def namespace_list(request):
    get_namespace=My_k8s_api('list_namespace')
    all_name_space_things=get_namespace.getall()
    print(type(all_name_space_things))
    # print(type(all_namespace))
    return render(request, 'page/resource/namespace_list.html', locals())
def node_list(request):
    get_node=My_k8s_api('list_node')
    all_node_things=get_node.getall()
    print(type(all_node_things))
    # print(type(all_namespace))
    return render(request, 'page/resource/nodes_list.html', locals())
def getnamespace(request):
    pass

def image_list(request):
    return render(request, 'page/img/images.html')


def user_list(request):
    return render(request, 'page/user/userList.html')
def mtest_api():
    get_namespace=My_k8s_api('list_namespace')
    print(get_namespace.getall())
# mtest_api()