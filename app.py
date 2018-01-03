from flask import *  # import Flask
from makeChain import Chain
from getQuote import Quote
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html") #this is the introduction, instructiosn, and button to start the quiz

@app.route('/quiz')
def organizeQuiz():
    q = Quote()
    c = Chain()

    quote = q.generateQuote()
    chain = c.genereteChain()

    #put options in different order and render template
    return render_template('question.html', quote=quote, chain=chain)

# @app.route('/user', methods=['POST','GET'])
# def findplaces():
#     username = request.args.get(key='username')
#
#
#     s = userSongs()
#     names = s.Login(username) #make it so that username is used here instead of other thing
#
#     print(username)
#     print(names)
#
#     return render_template("answers.html", names=names)

#maybe authprize in js? use spotify tuts
if __name__ == '__main__':
    app.run()
