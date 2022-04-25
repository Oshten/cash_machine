# cash_machine

## Описание принципа работы «кассового аппарата»

### Этап 1

Предварительно нужно будет написать модель данных для товара `Item`. Модель должна содержать следующие поля.

На веб-узел `{{root}}/cash_machine` с помощью метода **POST** отправляется следующее тело запроса:

```json
{
	"items": [1, 2, 3]
}
```

где `items` это массив id товаров модели `Item`.

При этом запросе сервер должен формировать чек в формате PDF. 

Пример чека: 

![Снимок экрана 2022-04-19 в 15.12.34.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5bd878b5-0cd6-4039-93f0-12635b06df23/Снимок_экрана_2022-04-19_в_15.12.34.png)

В чек должны записываться следующие поля:

 1. Для каждой позиции товара:

- Наименование
- Общее количество
- Общая стоимость
1. Итоговая сумма 
2. Время создания чека в формате (ДД.ММ.ГГГГ Ч:М)

HTML-шаблон чека приложен к заданию. Подставить вышеуказанные поля туда можно с помощью Jinja2. Для работы с PDF рекомендуется использовать библиотеку `pdfkit` [https://pypi.org/project/pdfkit/](https://pypi.org/project/pdfkit/) 

Сформированный PDF файл нужно просто сохранять в папку `media`

Затем сервер формирует ссылку на этот PDF-файл и кодирует его в QR-код, а затем **высылает этот QR-код** **в качестве ответа на запрос.** Для работы с QR-кодами рекомендуется использовать библиотеку `qrcode`

[https://pypi.org/project/qrcode/](https://pypi.org/project/qrcode/) 

### Этап 2

При сканировании QR-код будет совершаться запрос **GET** `{{root}}/media/<наименование файла>` который в ответ будет возвращать этот файл.

Решение нужно будет загрузить на GitHub, либо Gitlab, либо Bitbucket как публичный репозиторий