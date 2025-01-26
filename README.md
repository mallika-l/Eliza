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
