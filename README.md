# **DRF**
> ## Подготовка проекта
>> - установить зависимости проекта, выполнить команду: \
poetry install
>> - добавить .env с переменными окружения (.env_example) \

> ### Выполнено:
> Создан новый Django-проект, подключен DRF в настройках проекта.
> 
> Созданы модели: Пользователь, Курс, Урок.
> 
> Описан CRUD для моделей курса и урока. Для реализации CRUD для курса использован Viewsets, а для урока - Generic-классы.
> 
> Для модели курса добавлен в сериализатор поле вывода количества уроков. Поле выполнено с помощью SerializerMethodField().
> 
> Добавлена модель: Платежи.
> 
> Для сериализатора модели курса добавлено поле вывода уроков, вывод с помощью сериализатора для связанной модели.
> 
> Настроена фильтрация для эндпоинта вывода списка платежей с возможностями:
> - менять порядок сортировки по дате оплаты,
> - фильтровать по курсу или уроку,
> - фильтровать по способу оплаты.
> 
> Реализован CRUD для пользователей, в том числе регистрацию пользователей, настройка в проекте с использованием JWT-авторизации и закрыт каждый эндпоинт авторизацией.
> 
> Создана группа модераторов и созданы для нее права работы с любыми уроками и курсами, но без возможности их удалять и создавать новые. Заложен функционал такой проверки в контроллеры.
> 
> Созданы права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.
> 