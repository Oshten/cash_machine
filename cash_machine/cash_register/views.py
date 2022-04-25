import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, FileResponse

from rest_framework import views
from rest_framework.response import Response

from jinja2 import Environment, FileSystemLoader

from cash_register import function
from cash_register import models
from cash_machine import settings


class MakeChek(views.APIView):
    """Представление кассового аппарата"""
    def get(self, request):
        return Response('Отправте POST запрос со списком товаров')

    def post(self, request):
        list_items = request.data['items']
        all_items = models.Item.objects.all()
        count_items = function.counting_items(list_items=list_items)
        items = [item for item in all_items if item.id in set(list_items)]
        total_sum = function.total_sum(list_items=items, count_items=count_items)
        content = {'items': items, 'count_items': count_items, 'total_sum': total_sum}
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('cash_register/jinja2/receipt.html')
        pdf_template = template.render(content)
        full_name_pdf, name_pdf = function.get_file_name(name='chek', extension='pdf', path=settings.MEDIA_DIR)
        function.make_pdf(file=pdf_template, name=full_name_pdf)
        full_name_img, name_img = function.get_file_name(name='image', extension='png', path=settings.STATIC_DIR)
        url = f'{settings.ALLOWED_HOSTS[0]}:{settings.PORT}/media/{name_pdf}'
        function.make_qr_code(url=url, name=full_name_img)
        return render(request, 'index.html', context={'image': name_img})


def get_chek(request, name):
    file_list = os.listdir(settings.MEDIA_DIR)
    if file_list:
        for file in file_list:
            print(file)
            if file == name:
                full_name = os.path.join(settings.MEDIA_DIR, name)
                return FileResponse(open(full_name, 'rb'), content_type='application/pdf')
    return HttpResponseNotFound()
