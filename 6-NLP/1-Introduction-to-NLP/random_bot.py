import random as rd

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]
inp = ""
print("Hello, I am Marvin, the simple robot.\nYou can end this conversation at any time by typing 'bye'")
while inp != "bye":
    inp = input()
    resp = rd.choice(random_responses)
    print(resp)