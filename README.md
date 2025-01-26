# Eliza - Psychotherapist Program

## Objective
The goal of this program is to act as a psychotherapist. It recognizes patterns in the user's input and transforms responses accordingly using **regular expressions**. These allow "Eliza" to spot specific words and capture important parts of a sentence to respond appropriately.

---

## Sample Run
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

---

## Algorithm

1. **Greeting and Name Input**  
   The program prompts the user for their name. It accepts:  
   - A single word input (e.g., "Mallika").  
   - The last word in sentences like "My name is ...".  
   The name is stored for personalized responses throughout the session.

2. **User Interaction**  
   Eliza greets the user by name and prompts them to ask a question or share their thoughts.

3. **Main Loop**  
   An infinite `while` loop runs until the user types "exit". Within the loop:  
   - The program checks for "exit". If detected, it ends the session by saying goodbye.  
   - Otherwise, the input is passed to the `inputHandler` function.

4. **Input Handling**  
   The `inputHandler` function analyzes the user's input using predefined **REGEX patterns**. It identifies:  
   - **Feelings** (e.g., "I feel sad").  
   - **Desires** (e.g., "I want to ...").  
   - **Doubts** (e.g., "I don't know", "I'm not sure", "confused").  
   - **Auxiliary Verbs** (e.g., "am", "is", "have").  
   - **Requests for Humor** (e.g., "Tell me a joke").  
   - **Absolute Thinking** (e.g., "always", "never").  
   - **Concerning Desires** (e.g., mentions of self-harm).  

5. **Response Generation**  
   Once a pattern is matched, the program calls an appropriate function to generate a response:  
   - **Feelings, desires, and auxiliary verbs**: Transform user input into questions.  
     - Example: "I want to cry" → "Why do you want to cry?"  
   - Multiple response options are defined in the **ELIZA OUTPUT STRINGS** section. Responses are selected randomly.

6. **Session Termination**  
   When the user types "exit", Eliza bids farewell using the stored username.

---