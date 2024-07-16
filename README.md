## Задача 
#### Необходимо организовать асинхронное скачивание файлов с сайта биржи (https://spimex.com/markets/oil_products/trades/results/), а также последующий парсинг и загрузку данных в БД. Для подключения к PostgreSQL необходимо использовать асинхронный сессии.

Достает из бюллетени необходимые столбцы (забрать только данные из таблицы «Единица измерения: Метрическая тонна», где по столбцу «Количество Договоров, шт.» значения больше 0):
1) Код Инструмента (exchange_product_id)
2) Наименование Инструмента (exchange_product_name)
3) Базис поставки (delivery_basis_name)
4) Объем Договоров в единицах измерения (volume)
5) Объем Договоров, руб. (total)
6) Количество Договоров, шт. (count)

Сохраняет полученные данные в таблицу «spimex_trading» со следующей структурой:
1) id
2) exchange_product_id
3) exchange_product_name
4) oil_id - exchange_product_id[:4]
5) delivery_basis_id - exchange_product_id[4:7]
6) delivery_basis_name
7) delivery_type_id - exchange_product_id[-1]
8) volume
9) total
10) count
11) date
12) created_on
13) updated_on

* Необходимо создать базу данных, которая будет хранить информацию по итогам торгов начиная с 2023 года (для облегчения проверки скрипта дата с 10.07.2024).
* Возможный дополнительный перечень библиотек для реализации задания: pandas, xlrd, openpyxl, urllib, ssl.


## Основные используемые библиотеки:
- aiofiles==24.1.0
- aiohttp==3.9.5
- asyncpg==0.29.0
- beautifulsoup4==4.12.3
- lxml==5.2.2
- pandas==2.2.2
- python-dotenv==1.0.1
- SQLAlchemy==2.0.31
- xlrd==2.0.1