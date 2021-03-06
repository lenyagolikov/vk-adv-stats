# Сбор статистики объявлений рекламных кампаний в VK
#### Скачивание репозитория, создание и активация виртуального окружения
    git clone https://github.com/lenyagolikov/vk-adv-stats.git
    cd vk-adv-stats && python3 -m venv env
    source env/bin/activate
#### Установка зависимостей
    pip install -r requirements.txt
#### Создайте файл .env в корне проекта, скопируйте содержимое .template.env и вставьте его в .env, заполнив нужные поля
#### token: токен от VK приложения (строка), account_id: id от личного кабинета рекламной кампании (целое число), adv_ids: id's объявлений через запятую, либо одно объявление
    token = 'token'
    account_id = id
    adv_ids = '12345', '56789', '2133123'
#### Дополнительная информация
* VK позволяет просматривать статистику в личном кабинете, но только по дням. Скрипт можно настроить через планировщика (crontab), чтобы он запускался ежечасно, тогда вы сможете узнать лучше, в какое именно время больше прироста просмотров, кликов и потраченных денег на рекламу.
* Статистика будет отображена в excel-файле со значениями: ID объявления, просмотры, клики, потрачено денег, время запуска скрипта.
* Во втором файле (delta.xlsx) та же самая информация, но с учетом дельты (текущая статистика - предыдущая статистика).
* Настройки под себя можно найти в [документации VK](https://vk.com/dev/ads.getStatistics) и прописать их в файле config.py
