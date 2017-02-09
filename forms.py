# -*- coding:utf-8 -*-
from django import forms
class ItemForm(forms.Form):
    ItemCode = forms.CharField()
    ItemName = forms.CharField()
    Remark = forms.CharField(required=False)
