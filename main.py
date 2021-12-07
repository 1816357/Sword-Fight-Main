# numList = [1, 5, 3, 11, 15]
#
# newNuM = map(lambda n:n+10, numList )
# print(list(newNuM))
#
# import rooms as R1
#
# print(rooms.room)
# print(R1)

hero1 = {'Name':'Salah', 'Health': 10 }
enemy1 = {'Name':'Bob', 'Health': 10}

import random
insults = ["You fight like a dairy Farmer!", "This is the END for you, you gutter crawling cur!", "I've spoken with apes more polite than you!",]

combacks = ["How appropriate. You fight like a cow!", "And I've got a little TIP for you, get the POINT?"," I'm glad to hear you attended your family reunion!"]

gameState = 1
while gameState == 1:

    print(random.choice(insults))
    user_input = input('What your response?\n:')

    if user_input == "And I've got a little TIP for you, get the POINT?":
        hero1['Health']
        pass

    if user_input == "I'm glad to hear you attended your family reunion!":
        pass

    if user_input == "How appropriate. You fight like a cow!":
        pass

    if user_input == "No U!":
        print('You win')
        gameState = 2

    # if random.choice(combacks) == random.choice(combacks):
    #     pass
    #
    # if random.choice(combacks) == "How appropriate. You fight like a cow!":
    #     gameState = 2
    #     print("I WIN")



