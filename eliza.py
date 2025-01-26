##############################################################################
# Mallika Lakshminarayan
# CMSC 416
# 02/05/24
# PA 1
##############################################################################

'''
Usage: 
python eliza.py

Objective:
The goal of this program is to act as a psychotherapist. It should recognize patterns in the 
user's input and transform it to respond to it. This is possible using regular 
expressions. They allow "Eliza" to spot certain words and capture parts of the sentence 
that are important in order to respond appropriately


Sample Run:
[eliza] Hi, my name is Eliza. What is your name?
[user] mallika
[eliza] Hi Mallika, how can I help you? Type 'exit' at any time to quit the program
[Mallika] I feel sad
[eliza] Tell me more about feeling sad 
[Mallika] I just feel like no one cares   
[eliza] I understand, feeling like no one cares can be complex. Try to break it down into simpler parts.
[Mallika] Well, I am very lonely
[eliza] Why are you very lonely?
[Mallika] I feel awkward in public
[eliza] Since you're feeling awkward in public, would you like to hear a joke?
[Mallika] sure   
[eliza] Okay Mallika, how much does a chimney cost?
[Mallika] I don't know
[eliza] Nothing, it's on the house ;)
[eliza] Wasn't that really funny?
[Mallika] no
[eliza] Let's get back to the main point of me being here. What else can I help you with?
[Mallika] exit
[eliza] Goodbye Mallika :)

Algorithm:

1. The program prompts the user for a name. It accepts input that is a single word long 
or the last word in a sentence of the form "My name is ...". It stores the name for use 
throughout the program

2. It then greets the user using the stored name and asks for the user to ask it a question. 

3. Then an infinite while loop runs until the user types the word "exit"

4. Inside the while loop, it first checks if 'exit' has been input, and it ends the 
program by saying "Goodbye, user :)" if it has. It then passes the username to an input handler function.

5. The input handler function checks what type of question the user is asking. I chose to 
spot for feelings, desires through the word 'want to', doubts through the phrases "I don't know", 
"confused", and "I'm not sure", auxiliary verbs like am, have or is, the user asking for a joke, 
absolute words that express black and white thinking, and concerning desires like suicide. 
These are all expressed in the first section labeled "REGEXs"

6. Once there is a REGEX match, the inputHandler function will call the appropriate function 
to handle the type of question.

7. The feeling, desire, and auxiliary verb functions all transform the input. If the user 
types "I want to cry", the program transforms it to "Why do you want to cry?" There are a couple 
of options for string responses that are shown in the section labeled "ELIZA OUTPUT STRINGS". 
The program determines which response will be chosen randomly.



'''
import re
import random
import time

# REGEXs
NAME = r"\bMy name is \S+\b|^[A-Za-z?+';.!@]+$"
FEELING = r"feel(s|ing)*"
DESIRE = r"\bwant to\b"
DOUBT = r"I do(n't| not) know|confused|I('m| am) not sure"
AUXVERB = r"(am|have|is)"
EXIT = r"\bexit\b"
NO = r"\b[Nn][oO]\b|don't want|stop"
JOKE = r"\bjoke\b"
ABSOLUTE = r"all|none|must|except|every|always|only|never"
CONCERN = r"suicid(e|al)|kill"

# ELIZA OUTPUT STRINGS
GIBBERISHR = ["I'm sorry I didn't understand that, please rephrase your question.", "Could you repeat that in a different way?", "I'm not sure how to help you, please retype your question."]
DOUBTR = ["It seems like you're going through some turmoil, expand on that.", "What is unclear in this situation?"]
FEELINGR = [["Tell me more about feeling", ""], ["I understand, feeling", "can be complex. Try to break it down into simpler parts."]]
JOKER = [["how much does a chimney cost?", "Nothing, it's on the house ;)"]]
DESIRER = [["I'm sure you want to", ", but is that the best idea?"],["I can understand wanting to", ", but how would it help you?"]]
ABSOLUTER = ["It seems that you are exhibiting signs of black and white thinking. Try to step back and think more objectively about the situation", "This is quite extreme - I'd suggest reframing this thought process.", "Is there any way you can attempt to reframe this black and white thinking pattern?"]

# function to ask for name and store it
def promptName ():
    print(f"[eliza] Hi, my name is Eliza. What is your name?")
    text = input("[user] ")
    intro = re.findall(NAME, text)
    name = intro[0].split()[-1]
    return name

# function to greet user and prompt to ask a question
def greetingPrompt (name):
    print(f"[eliza] Hi {name}, how can I help you? Type 'exit' at any time to quit the program")
    userInput = input(f"[{name}] ")
    return userInput

# function to spot desires
def desire(inp, userName):
    # isolate desire
    parts = re.split(DESIRE, inp)
    des = parts[-1].strip(' ')

    # choose a random desire response
    num = random.randint(0, len(DESIRER)-1)
    if(num >= 0 and num <len(DESIRER)):
        print(f"[eliza] {DESIRER[num][0]} {des}{DESIRER[num][1]}")
    return 0

# function to tell a joke
def tellJoke(answer, userName):
    if re.search(NO, answer):
        print(f"[eliza] Okay, well how else can I help you then?")
    elif re.search(EXIT, answer):
        exit()
    else:
        ind = random.randint(0, len(JOKER)-1)
        print(f"[eliza] Okay {userName}, {JOKER[ind][0]}")
        a = input(f"[{userName}] ")
        if re.search(NO, a):
            print(f"[eliza] Okay, well how else can I help you then?")
        elif re.search(EXIT, answer):
            exit()
        else:
            print(f"[eliza] {JOKER[ind][1]}")
            time.sleep(2)
            print(f"[eliza] Wasn't that really funny?")
            input(f"[{userName}] ")
            print(f"[eliza] Let's get back to the main point of me being here. What else can I help you with?")

# function to respond to feelings
def feeling(inp, userName):
    # isolate feeling
    parts = re.split(FEELING, inp)
    feel = parts[-1].strip(' ')

    # choose a random feeling response
    num = random.randint(0, len(FEELINGR))
    if(num >= 0 and num <len(FEELINGR)):
        print(f"[eliza] {FEELINGR[num][0]} {feel} {FEELINGR[num][1]}")
    else:
        #joke function
        print(f"[eliza] Since you're feeling {feel}, would you like to hear a joke?")
        answer = input(f"[{userName}] ")
        # print(f"[eliza] joke")
        tellJoke(answer, userName)
    return 0

# function to handle auxiliary verbs
def auxVerbs(inp, userName):
    match = re.search(AUXVERB, inp)
    parts = re.split(AUXVERB, inp)
    parts = [x.strip(' ') for x in parts]
    if parts[0] == 'I' or 'i':
        parts[0] = "you"
        if parts[1] == "am":
            parts[1] = "are"
    if parts[1]=="have":
        print(f"[eliza] Why do {parts[0]} {parts[1]} {parts[2]}?")
    else:
        print(f"[eliza] Why {parts[1]} {parts[0]} {parts[2]}?")
    return 0

def doubt(userName):
    num = random.randint(0, len(DOUBTR)-1)
    print(f"[eliza] {DOUBTR[num]}")
    return 0

def absolute():
    num = random.randint(0, len(ABSOLUTER)-1)
    print(f"[eliza] {ABSOLUTER[num]}")
    return 0

def handleGibberish():
    num = random.randint(0, len(GIBBERISHR)-1)
    print(f"[eliza] {GIBBERISHR[num]}")
    return 0    

# function to handle general input
def inputHandler(userInput, userName):
    if re.search(EXIT, userInput):
        exit()
    elif re.search(CONCERN, userInput):
        concern(userName)
    elif re.search(FEELING, userInput):
        feeling(userInput, userName)     
    elif re.search(DESIRE, userInput):
        desire(userInput, userName)
    elif re.search(DOUBT, userInput):
        doubt(userName)
    elif re.search(AUXVERB, userInput):
        auxVerbs(userInput, userName)
    elif re.search(JOKE, userInput) and (re.search(NO, userInput) is None):
        tellJoke("yes", userName)
    elif re.search(ABSOLUTE, userInput):
       absolute()
    else:
        handleGibberish()
    return 0

# function to respond to concerning input
def concern(userName):
    print(f"[eliza] {userName}, if you're struggling it's okay to seek help. Please take care of yourself. You are loved. What exactly is on your mind?")
    return 0

# function to handle gibberish
def gibberish():
    print(f"[eliza] I'm not exactly sure what you mean by that. Try typing your question again.")
    return 0
    
# main method where program starts
def main():
    try:
        userName = promptName().capitalize()
        userInput = greetingPrompt(userName)
        while(True):
            if re.search(EXIT, userInput):
                exit()
            inputHandler(userInput, userName)
            userInput = input(f"[{userName}] ")
    except SystemExit:
        print(f"[eliza] Goodbye {userName} :)")
    except:
        print(f"[eliza] Please enter your question in correct format.")

if __name__ == "__main__":
    main()
