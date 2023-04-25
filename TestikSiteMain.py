from flask import Flask, render_template, url_for
import requests
from bs4 import BeautifulSoup
import random

frazes = ['Ээээ... Чото.. Ну вы поняли', 'Ес ай эм!', 'Инглиша не знаю и знать не хочу', 'ХАХАХАХАХАХАХА', 'Чо бобры', 'Дааа бобрята', 'Джозеф Джооостар самыый круутооой', 'СпидвагоОоун', 'Привет!', 'Панский пасаси', 'Низнаю', 'Чоо', 'Я Тестик', 'Я маленький гвынтик', 'Ямате кудасай', 'Капуста не густа, а вот кабачки это путь в рай', 'Чо ржош?!', 'Отьелло пастарался', 'ничо', 'Error', 'Два билета на Д`арби', 'made in Verde']

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    htmltxt = requests.get('https://godville.net/news')
    soup = BeautifulSoup(htmltxt.text, 'lxml')
    randomClass = random.choice(['article clearfix', 'hero clearfix', 'game clearfix', 'add clearfix', 'fc clearfix', 'news clearfix'])
    gvnews = soup.find('div', class_ = randomClass)
    return render_template('testik.html', gvnews = gvnews.text, randomfraza = random.choice(frazes))

@app.route("/obnovi")
def commandspage():
    return render_template('obnovi.html')

@app.route("/commands")
def obnovipage():
    return render_template('commands.html')

if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0', port = 5000)