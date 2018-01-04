from flask import *  # import Flask
from makeChain import Chain
from getQuote import Quote
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html") #this is the introduction, instructiosn, and button to start the quiz

@app.route('/about')
def serveAbout():
    return render_template("about.html")

@app.route('/quiz')
def organizeQuiz():
    q = Quote()
    c = Chain()

    quote = q.generateQuote()
    chain = c.genereteChain()

    pos = random.randint(1,2)
    #put options in different order and render template
    return render_template('question.html', quote=quote, chain=chain, answerpos=pos)

@app.route('/correct')
def serveCorrect():
    return render_template("correct.html")

@app.route('/wrong')
def serveWrong():
    return render_template("wrong.html")

if __name__ == '__main__':
    app.run()
