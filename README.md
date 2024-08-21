# Проект виджета банковских операций

## Описание:

Проект виджета банковских операций - бэкэнд-проект, направленный на 
подготовку данных для отображения в новом виджете, который показывает 
несколько последних успешных банковских транзакций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:varyadolgikh94/test_poetry.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Чтобы воспользоваться функцией маскировки, перейдите в src/widget.py, 
вызовите функцию Mask_account_card и передайте ей соответствующие данные 
в форме «ваша_карта_имя_номер_карты» для карт или «Счет account_number» 
для учетных записей. Не забудьте распечатать результат:
```
your_card = "your_card_name card_number"
print(mask_account_card("your card"))
your_account = "Счет account_number"
print(mask_account_card("your account"))
```
4. Перейдите в src/processing.py и создайте список dicts, содержащий информацию 
о ваших последних операциях в форме {"id": Operation_id, 
"state": "EXECUTED"/"CANCELED", "date": "operation_date"} . 
Передайте эти данные в функцию filter_by_state, чтобы видеть только 
«ИСПОЛНЕННЫЕ» операции, или укажите состояние фильтрации, передав второй 
параметр state="CANCELED". Вызовите функцию sort_by_date, чтобы просмотреть 
свои операции в нисходящем хронологическом порядке (от самых последних к самым 
ранним). Чтобы просмотреть операции в порядке возрастания, передайте второй 
параметрparameter="False":
```
operations_data = [
{"id": operation1_id, "state": "EXECUTED", "date": "operation1_date"}, 
{"id": operation2_id, "state": "CANCELED", "date": "operation2_date"}
]
print(filter_by_state(operations_data)) # выводит только выполненные операции
print(filter_by_state(operations_data, state="CANCELED")) # выводит только отмененные операции
print(sort_by_date(operations_data)) # выводит операции в хронологическом порядке от самых последних к более ранним
print(sort_by_date(operations_data, parameter=False)) # выводит операции от более ранних до самых последних
```

## Использование:

1. Функция маскировки:
```
# Card usage example
Visa Platinum 7000 7922 8960 6361  # input data
Visa Platinum 7000 79** **** 6361  # output data

# Account usage example
Счет 73654108430135874305  # input data
Счет **4305  # output data
```
2. Функция фильтрации
```
# Вывод функции с состоянием по умолчанию 'EXECUTED'
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
] 

# Function output with 'CANCELED' passed as the second argument
[
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
```
3. Функция сортировки:
```
# Вывод функции (сортировка по убыванию, т.е. от самых последних операций)
[
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]
```
## Тесты:
Проект протестирован 47 различными способами, что обеспечивает 100% покрытие кода. 
Тестирование проекта выполняется с помощью pytest. Чтобы запустить тесты,
установите pytest в группу разработки и напишите соответствующую команду в своем терминале:

```
poetry add --group dev pytest
pytest
```
Чтобы просмотреть статистику покрытия кода, установите pytest-cov поэзию, 
добавьте --group dev pytest-cov и введите pytest --cov в своем терминале.


