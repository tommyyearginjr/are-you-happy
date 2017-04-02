import os

question = input("What do you want to do now? ")
for char in str(";.?:,!"):
    question = question.replace(char, "")
question = (question.lower()).split(" ")

possibleBadResponse = ['sad', 'unhappy', 'hurt', 'upset', 'angry', 'resent', 'fear', 'anger', 'anxious']

os.system('clear')

if len(question) == 1:
    print("You're a man of few words.")
else:
    print("I see. Try relaxing by taking {} deep breaths.".format(len(question)+1))

for val in question:
    if val in possibleBadResponse:
        happinessIndex = 1
    else:
        happinessIndex = 0
        
if happinessIndex != 1:
    print('\nREMEMBER: Enlightenment is the key to happiness.\n')
else:
    print('\nREMEMBER: You are not your thoughts.\n')
