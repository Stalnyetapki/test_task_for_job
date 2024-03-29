# test_task_for_job, pytest + selenium

1. Для запуска тестов используется тест-раннер Pytest
Это сторонняя библиотека, поэтому ее необходимо скачать:

pip install pytest

2. Окружение, которое использовалось для запуска тестов описано в файле requirements.txt

3. Для того чтобы  достать все пакеты из файла requirements.txt, нужно создать окружение, активировать его и после выполнить команду:

  pip install -r requirements.txt
  
4. Инициализация и финализация браузера находится в специальном файле conftest.py, в рамках фикстуры driver. При запуске, инициализация и финализация браузера применяется к каждой функции в рамках тестового модуля. Файл conftest.py должен располагаться в корневом каталоге (как в репозитории). В нем хранятся фикстуры и настройки.

5. По умолчанию запуск тестов производится с помощью команды:

pytest test_task.py

6. Для того чтобы pytest не перехватывал стандартный вывод Python (print не выводится в консоль) необходимо указывать флаг -s:

pytest -s test_task.py

7. Для того  чтобы в отчёт добавилась дополнительная информация со списком тестов и статусом их прохождения, 
необходимо указать параметр -v:

pytest -v test_task.py

8. В файле conftest.py добавлена возможность выбирать браузер для запуска тестов, с помощью параметра --browser_name. Добавлена возможность выбора браузера между Chrome и Firefox. По умолчанию выбран Chrome. Для того чтобы явно выбрать браузер, то в качестве значения параметра необходимо внести либо 

chrome, либо firefox. 
Например:

pytest -s -v --browser_name=chrome test_task.py

pytest -s -v --browser_name=firefox test_task.py

Соответственно для запуска требуются скачать драйвера для браузеров (требуется скачивание в зависимости от версии браузера, который вы используете)
Можно его не указывать, тогда тест запуститься в браузере Chrome:

pytest -s -v test_task.py
