from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
# import and create a Conll extractor to use later 
extractor = ConllExtractor()

# later when you need a noun phrase extractor:
print("Hello, I am Marvin, the simple robot.\nYou can end this conversation at any time by typing 'bye'")
user_input = ""
while user_input != "bye":
    user_input = input("> ")
    user_input_blob = TextBlob(user_input, np_extractor=extractor)  # note non-default extractor specified
    np = user_input_blob.noun_phrases
    if user_input_blob.polarity <= -0.5:
        response = "Oh dear, that sounds bad. "
    elif user_input_blob.polarity <= 0:
        response = "Hmm, that's not great. "
    elif user_input_blob.polarity <= 0.5:
        response = "Well, that sounds positive. "
    elif user_input_blob.polarity <= 1:
        response = "Wow, that sounds great. "
    if len(np) != 0:
        print(response + "Can you tell me more about" , (np[0].pluralize()),  "?")
    else:
        print(response + "Can you tell me more ?")


