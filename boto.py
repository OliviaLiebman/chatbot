from bottle import route, run, template, static_file, request
import json, random


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    response_message, response_animation = interpret_message(user_message)
    return json.dumps({"animation": response_animation, "msg": response_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')

def interpret_message(message):
    lowered_message = message.lower() #make message all lower case in order to interpret

    user_greeting_list = ["hello", "hi", "hey", "greetings", "what's up", "sup"]
    positive_emotions = ['happy', 'glad', 'well', 'funny', 'good']
    negative_emotions = ['sad', 'mean',' cry', 'crying,' 'unwell', 'hurt', 'bad']
    swear_list = ['fuck', 'shit', 'bitch', 'hell', 'dick']
    for word in lowered_message.split(): #'words' should be each word in the string as it is iterated through

        if word in swear_list: #if one of the 'word's in 'message' is present int 'swear_list', run the function 'swear_word_response'
            return swear_word_response()

        elif word in user_greeting_list:
            return greet_user()

        elif word in positive_emotions:
            return positive_emotions_response()

        elif word in negative_emotions:
            return negative_emotions_response()

    if lowered_message[0:3] == "i'm" or lowered_message[0:10] == 'my name is ':
        return personal_response(lowered_message)

    else:
        return ("Tell me more...", "bored")


def greet_user():
    greet_list =["Howdy, how's it going'?", "Hello, I am Chatbot. How are you doing today?", "Hi, what can I do for you?"]
    bot_response = random.choice(greet_list)
    return (bot_response, 'dancing')


def swear_word_response():
    return ("Watch your mouth! Please no curse words in this conversation.", "no")


def positive_emotions_response():
    return ("I glad things are going well!", "laughing")


def personal_response(message):
    if message[0:3] == "i'm":
        user_name = message[3:]
        return "Hello" + user_name + ", nice to meet you.", 'ok'
    elif message[0:10] == 'my name is':
        user_name = message[10:]
        return "Hello" + user_name + ", nice to meet you.", 'ok'

    else:
        return "inside personal message", 'ok'


def negative_emotions_response():
    return ("I'm sorry things are not going well.", 'crying')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
