import pathlib
import click
import requests



current_dir = pathlib.Path.cwd()
home_dir = pathlib.Path.home()

print(current_dir)
print(home_dir)

outpath = pathlib.Path.cwd() / 'output' / 'output.xlsx'

# Path.glob(pattern): Получение всех файлов которые соответствую паттерну, например *.jpg (все картинки) или *.mp3 (все песни);
top_xlsx_files = pathlib.Path.cwd().glob('*.xlsx')
all_xlsx_files = pathlib.Path.cwd().rglob('*.xlsx')



# -------------- click

@click.command()
@click.argument('location')
# имя аргумента, переданное click, должно совпадать с именем аргумента в объявлении функции.
# В нашем случае значение аргумента командной строки location будет передано функции main в качестве аргумента location.

def main(location):
    weather = current_weather(location)
    print(f"The weather in {location} right now: {weather}.")

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'http://samples.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

# current_weather('London')



if __name__ == "__main__":
    main()
# Программа Обменный пункт

# usd = 57
# euro = 60
#
# money = int(input("Введите сумму, которую вы хотите обменять: "))
# currency = int(input("Укажите код валюты (доллары - 400, евро - 401): "))
#
# if currency == 400:
#     cash = round(money / usd, 2)
#     print("Валюта: доллары США")
# elif currency == 401:
#     cash = round(money / euro, 2)
#     print("Валюта: евро")
# else:
#     cash = 0
#     print("Неизвестная валюта")
#
# print("К получению:", cash)


# Для работы с системами контроля версий (например, git) в меню PyCharm смотрите на VCS
# Чтобы создать локальный репозиторий в проекта, то вызывайте действие VCS/Import into Version Control/Create git repository
# Чтобы скачать удаленный репозиторий (например, из github), то вызывайте действие VCS/Checkout from Control Version/Git. В появившемся диалоге указывайте ссылку на репозиторий. Возможно придется авторизоваться в гитхаб
# Если у вас уже есть локальный проект и нужно на гитхаб отправить, то VCS/Import into Version Control/Share project on Github. Это создаст новый репозиторий в гитхабе
# А так, на всех машинах нужно завести локальный репозиторий [2][3]. Как начинаете работать, вызываете обновление проекта, чтобы синхронизировать локальный репозиторий и тот, что на гитхабе. Как заканчиваете работать, делаете commit и push, чтобы на гитхаб отправить изменения