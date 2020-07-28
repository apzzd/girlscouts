from browser import document, alert,ajax,html
from random import *
import browser
import json

def clear():
    document['nottext'].text = ''



def on_complete(req):
   if req.status == 200 or req.status == 0:
      browser.console.log(document['nottext'].text)
      clear()
      opennote()
      document['nottext'] <= html.P("WARNING: I've got some of your information already!")
      document['nottext'] <= html.P('Browser Online:' + str(document.nav.onLine))
      document['nottext'] <= html.P('Platform:' + document.nav.platform)
      document['nottext'] <= html.P('Where you live: ' + json.loads(req.text)['city'] + ', ' + json.loads(req.text)['region'])
      document['nottext'] <= html.P('Internet Sevice Provider: ' + json.loads(req.text)['org'])

req = ajax.Ajax()
req.bind('complete', on_complete)
req.open('GET', 'https://ipapi.co/json/', True)
##req.set_header('content-type', 'application/x-www-form-urlencoded')
# send data as a dictionary
req.send()




def print_loc(loc):
    print(loc)
    


def click(ev):
    if document['name'].value and document['age'].value and document['anim'].value and document['hobb'].value:
        clear()
        opennote()
        document['nottext'] <= 'Hey: I can save this information, you know. Now I know that your name is ' + document['name'].value + ' and that you are ' + document['age'].value + ' years old.'
        showunames()
        showpass()
        document.getElementById("myDIV").style.visibility = 'visible'
    else:
        alert('You must fill out the form first.')
    

def showunames():
    if document['name'].value and document['age'].value and document['hobb'].value and document['anim'].value and document['color'].value and document['food'].value:
        un1 = document['name'].value + document['anim'].value + document['age'].value + str(randint(0,9)) + str(randint(0,9))
        un2 = document['hobb'].value + document['name'].value + document['age'].value + str(randint(0,9)) + str(randint(0,9))
        un3 = document['hobb'].value + document['anim'].value + document['age'].value + str(randint(0,9)) + str(randint(0,9))
        un4 = document['food'].value + document['anim'].value + document['age'].value + str(randint(0,9)) + str(randint(0,9))
        un5 = document['color'].value + document['anim'].value + document['age'].value + str(randint(0,9)) + str(randint(0,9))
        un6 = document['anim'].value + document['food'].value + document['age'].value + str(randint(0,9)) + str(randint(0,9))
        
        document['unames'] <= html.P(un1)
        document['unames'] <= html.P(un2)
        document['unames'] <= html.P(un3)
        document['unames'] <= html.P(un4)
        document['unames'] <= html.P(un5)
        document['unames'] <= html.P(un6)
    else:
        alert('You must fill out the form first')
        
def showpass():
    adj = ['cool', 'cute', 'fluffy', 'evil', 'awesome', 'purple', 'orange']
    nouns = ['pandas', 'kittenz', 'manat33s', 'crocodiles', 'doggos', 'id3as', 'toes']
    noun = ['panda', 'kitten', 'manat33', 'crocodile', 'doggo', 'id3a', 'toe']
    food = ['pizza', 'cupcakes', 'sandwitch', 'burrito', 'tofu', 'marshmallow', 'corndogs']
    verb = ['eat', 'playwith', 'greet', 'impeach', 'kick', 'siton']
    number = [str(i) for i in range(0,9)]
    
    p1 = choice(adj) + choice(nouns) + choice(verb) + choice(nouns)
    p2 = choice(adj) + choice(adj) + choice(food) + choice(noun)
    p3 = choice(adj) + choice(nouns) + 'eat' + choice(food)
    p4 = choice(adj) + choice(noun) + 'eats' + choice(number) + choice(adj) + choice(food)
    p5 = choice(number) + choice(adj) + choice(nouns) + choice(verb) + choice(nouns)
    p6 = choice(number) + choice(adj) + choice(food) + choice(nouns)
    
    document['pass'] <= html.P(p1)
    document['pass'] <= html.P(p2)
    document['pass'] <= html.P(p3)
    document['pass'] <= html.P(p4)
    document['pass'] <= html.P(p5)
    document['pass'] <= html.P(p6)
 
def uselect(ev):
    ##alert(ev.target)
    t = document.getSelection().toString()
    clear()
    opennote()
    document['nottext'] <= "Uh oh! Don't use this username. Now I know one of your possible usernames: " + str(t) + '.'
    
def pselect(ev):
    ##alert(ev.target)
    t = document.getSelection().toString()
    clear()
    opennote()
    document['nottext'] <= "Uh oh! Don't use this password. Now I know one of your possible passwords: " + str(t) + '.'

    
def opennote():
    document["notices"].style.visibility = 'visible'
    
def closenote(ev):
    document["notices"].style.visibility = 'hidden'

# bind event 'click' on button to function echo
document["submit"].bind("click", click)
document['unames'].bind('copy', uselect)
document['pass'].bind('copy', pselect)
document['bluebtn'].bind('click', closenote)
