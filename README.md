Инструкция:

Устанавливаем бота:


pkg install git

git clone https://github.com/void990/troll-bot-low

cd troll-bot-low


Скачиваем требования:


pip3 install -r requirements.txt


Заходим и редактируем конфиг:

nano config.py

" api_id = Ваш API ID "

" api_hash = "Ваш API HASH" "


Как получить API ID и API HASH:


Заходите на сайт "my.telegram.org"

Регистрируетесь там

Заходите в раздел API DEVELOPING

Создайте приложение что бы получить (Осмысленное слово)

И скопируйте API ID и API HASH

И вставьте как показано выше


ДАЛЕЕ:


" trigger = "Ваш триггер" "

Триггер нужен для флуда.


Запускаем бота:


python3 bot.py


В боте присутствует флуд режим по триггеру


Если хотите начать флуд то укажите букву "y"


flood mode? |y/n| y


count message: Количество сообщений

chat id >> Айди чата в который вы хотите спамить

delay >> Задержка сообщений


потом отправьте ваш триггер в чат который хотите спамить.



В боте присутсвует ответ оскорблениями на сообщения собеседника.


flood mode? |y/n| n


chat id >> Айди чата

delay >> Задержка сообщений


