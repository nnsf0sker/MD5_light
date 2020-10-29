# Tern hasher

Данный проект реализует тестовое задание, выполненное [@nnsf0sker](github.com/nnsf0sker) в марте 2019 года. Его точные условия, к сожалению, не сохранились, однако по заданию необходимо было реализовать HTTP-сервер, способный по url считать md5-хэш содержимого ссылки. Причём должны корректно обрабатываться объёмов, заметно превышающих размер оперативной памяти.

Название "Tern hasher" появилось в честь небольшой птицы, способной мигрировать на очень далёкие расстояние - полярной крачки (arctic tern). Она символизирует легковестность написанного решения, вкупе с высокой выносливостью.

## Запуск

### Установка зависимостей
Все необходимые паекты описаны в requirements.txt и устанавливаются командой
```bash
pip3 install -r requirements.txt
```

### Запуск сервера
Для того, чтобы запустить проект нужно ввести команду
```python
python3 run.py
```

## Схема работы

### API
Адрес для подключения 0.0.0.0 с портом 8000. Сервер работает с двумя типами запросов:

`/submit` - создаёт задачу, на выходе возвращает JSON с id.

`/check` - возвращает JSON c status - текущий статус задачи, так же может дополнительно возвращать url и md5.

### Хранение информации о задачах

Вместо базы данных используется папка с *.txt файлами, где имя файла является id задачи, результаты которой описаны внутри.

---
P.S. Хочется отметить, что качество кода находится на весьма низком уровне, так как это был первый неучебный проект, написанный мною на Python. В частности, в нём нет контейнеризации, тестирования, контроля код-стайла и даже соблюдения PEP8, однако несмотря на это, он интересен как минимум тем, что наглядно демонстрирует моё развитие с того времени:)
