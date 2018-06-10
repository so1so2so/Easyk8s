# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe


# Create your models here.


class Menu(models.Model):
    """菜单"""
    name = models.CharField(max_length=32)
    url_type_choices = ((0, 'alias'), (1, 'absolute_url'))
    url_type = models.SmallIntegerField(choices=url_type_choices)
    url_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "菜单"
        verbose_name = "菜单"


class namespace(models.Model):
    namespace_name = models.CharField(max_length=32, verbose_name="命名空间")

    # result_from_api_name = models.TextField(max_length=10240, verbose_name="所有返还结果")

    def __unicode__(self):
        return self.namespace_name

    class Meta:
        verbose_name_plural = "命名空间"
        verbose_name = "命名空间"


class All_api_for_k8s(models.Model):
    api_name = models.CharField(max_length=128)
    menu_name = models.ForeignKey("Menu", verbose_name="菜单名称")
    # namespace_type = models.ForeignKey("namespace", verbose_name="所属命名空间")

    # result_from_api_name = models.TextField(max_length=10240, verbose_name="所有返还结果")
    def __unicode__(self):
        return self.api_name

    class Meta:
        verbose_name_plural = "api名称"
        verbose_name = "api名称"


class result(models.Model):
    api = models.ForeignKey("All_api_for_k8s")
    namespace = models.ForeignKey("namespace")
    result_from_api_name = models.TextField(max_length=10240, verbose_name="所有返还结果",null=True,blank=True)

    def __unicode__(self):
        return "结果"

    class Meta:
        verbose_name_plural = "返还结果"
        verbose_name = "返还结果"


class Show_content(models.Model):
    content_name = models.CharField(max_length=32)
    menu_name = models.ForeignKey("Menu", verbose_name="菜单名称")

    def __unicode__(self):
        return self.content_name

    class Meta:
        verbose_name_plural = "需要显示的行"
        verbose_name = "需要显示的行"


class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=32, unique=True)
    menus = models.ManyToManyField("Menu", blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "角色"


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        self.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """账号表"""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )
    password = models.CharField(_('password'), max_length=128, help_text=mark_safe("""<a href="password">修改密码</a>"""))
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    roles = models.ManyToManyField("Role", blank=True)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):  # __unicode__ on Python 2
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        permissions = (
            ('show_table', '查看table'),

        )
