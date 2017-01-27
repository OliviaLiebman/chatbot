"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json, random


@route('/', method='GET')
def index():
    return template("chatbot.html")

#pull first word in string of user sentence and make first if statement in interpret_message func
#this way this functionality will run first, and can get user name that way
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

    swear_list = ['fuck', 'shit', 'bitch', 'hell', 'dick']
    for word in lowered_message.split(): #'words' should be each word in the string as it is iterated through

        if word in swear_list: #if one of the 'word's in 'message' is present int 'swear_list', run the function 'swear_word_response'
            return swear_word_response()

    if (lowered_message[0] == 'h'):
        return greet_user()

    else:
        return ("default response", "bored")

def greet_user():
    greet_list =["Howdy, how's it going'?", "Hello, I am Chatbot. How are you doing today?", "Hi, what can I do for you?"]
    bot_response = random.choice(greet_list)
    return (bot_response, 'dancing')

def swear_word_response():
    return ("Watch your mouth! Please no curse words in this conversation.", 'no')

def main():
    run(host='localhost', port=7500)

if __name__ == '__main__':
    main()
