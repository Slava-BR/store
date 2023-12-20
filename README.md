## Как запустить docker

После скачивания репозитория зайди в корневую папку проекта. Открой её через терминал,
и напиши команду: docker-compose up -d

## ENDPOINT
 ip/main/ - json содержащий список товара
![img_1.png](img_1.png)
ip/detail/slug/ - json содержащий всю информацию о товаре
![img.png](img.png)
ip/collection/?collections= - json список товара из коллекции, которая будет указа в get-запросе
![img_2.png](img_2.png)
ip/field/slug/ - поле товара определенного товара
![img_3.png](img_3.png)

field - любое поле товара(image, price, title, size, textile, material, collection, type)

slug - сформированный индекс для каждого товара по его названию


