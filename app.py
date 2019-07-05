from flask import Flask
app = Flask(__name__)

from nltk.chat.util import Chat, reflections
import datetime
import questions


pairs = [
    [
        "how are you",
        ["I'm doing good\nHow about You ?", ]
    ],
]

arr = []
file = open('umt.txt','r').readlines()

for n in file:
    arr.append(n)




count =arr.__len__()

for y in range(0,count-1):
    arr[y]=arr[y].rstrip()

while("" in arr) :
    arr.remove("")


def addspaces(txt):
    s = txt.split(' ')
    for x, y in enumerate(s):
        if x % 12 == 0:
            s.insert(x, '\n')
    text = ' '.join(s)
    return text





count =arr.__len__()

for i in range(0,count-1,2):
    arr[i]=arr[i].replace('-','')
    arr[i]=arr[i].rstrip()
    arr[i]=arr[i].strip()
    arr[i+1]=arr[i+1].replace('-','')
    arr[i+1] = arr[i+1].rstrip()
    arr[i+1]=arr[i+1].strip()
    que = []
    ans = []
    que.append(arr[i])
    val = arr[i+1]
    ans.append(val)
    que.append(ans)
    pairs.append(que)


pairs[1][0] = "what is umt"


def converser(self,input,quit="quit"):
    user_input = input
    while user_input != quit:
        user_input = quit
        try:
            user_input = input
        except EOFError:
            print(user_input)
        if user_input:
            while user_input[-1] in "!.":
                user_input = user_input[:-1]
            return (self.respond(user_input))
            break



def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        print('Good Morning!')

    if currentH >= 12 and currentH < 18:
        print('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        print('Good Evening!')



from flask import Flask , render_template , request , jsonify

app = Flask(__name__)



@app.route("/")
def code():
    val = request.args.get('text')
    chat = Chat(pairs, reflections)
    actual = questions.questionpredict(val)
    actual = actual.strip()
    text = converser(chat, actual)
    return render_template('main.html',text=text)


@app.route("/bot/",methods=['GET'])
def get():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    chat = Chat(pairs, reflections)
    actual = questions.questionpredict(id)
    actual = actual.strip()
    values = converser(chat, actual)
    answer = {"text":values}
    return jsonify(answer)

