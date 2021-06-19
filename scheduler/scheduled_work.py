from scrappers.uslugi.yandex_uslugi_scrapper import scrap_yandex_uslugi_data
from scrappers.yodo.youdo_scrapper import scrap_youdo_data

counter = 0


def test_job_function():
    global counter
    counter += 1

    print('loool' + str(counter))
    text_file = open("meow.txt", "a")
    text_file.write("meow_brr" + str(counter) + '\n')
    text_file.close()


def scheduled_work():
    scrap_youdo_data()
    scrap_yandex_uslugi_data()
