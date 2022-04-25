import os
from collections import defaultdict

import pdfkit
import qrcode


def get_file_name(path, name, extension):
    """Формирование полного имени файла"""
    list_file = os.listdir(path)
    if list_file:
        file_name = f'{name}_{len(list_file) + 1}.{extension}'
    else:
        file_name = f'{name}_1.{extension}'
    full_name = os.path.join(path, file_name)
    return full_name, file_name


def make_pdf(file, name):
    """Формирование чека в формате PDF"""
    config = pdfkit.configuration(wkhtmltopdf=r'D:/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(file, name, configuration=config)


def make_qr_code(url, name):
    """Формирование QR кода"""
    img = qrcode.make(url)
    img.save(name)


def counting_items(list_items):
    """Подстчет количества товаров"""
    dict_items = defaultdict(int)
    for item in list_items:
        dict_items[item] += 1
    return dict_items


def total_sum(list_items, count_items):
    """Подсчет итоговой суммы"""
    total_sum = 0
    for item in list_items:
        total_sum += item.price * count_items[item.id]
    return total_sum

