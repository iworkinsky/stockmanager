# -*- coding:utf-8 -*-
from django import forms
class ItemForm(forms.Form):
    ItemCode = forms.CharField(max_length=10,label=u'物料编码',error_messages={'invalid':u'必填项'})
    #ItemCode = forms.CharField(label=u'零件编码',max_length=10)
   # ItemName = forms.CharField(label=u'物料名称',error_messages=u'必填项')
    ItemName = forms.CharField(label=u'零件名称')
    Remark = forms.CharField(label=u'备注',required=False,widget=forms.Textarea)
