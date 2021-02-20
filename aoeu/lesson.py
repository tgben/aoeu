#import curses
#import lessons


#def __init__():
#    self.l = Lesson(0)
#    start()

#l = Lesson(0)

lesson_intros = {
        0 : ["Welcome to Lesson 0, Getting started", "Why learn Dvorak? <br> If you've gotten this far, you probably already have a good understanding of what dvorak is and why people switch to it so I won't bore you too much. <br> <br> How to learn Dvorak? <br> This approach xxxyyyzzz"],
        1 : ["Welcome to Lesson 0, Review", "In this lesson, we will review common english words with no punctuation. press any key besides tab to start:"],
        2 : [""],
        3 : [""],
        4 : [""],
        5 : [""],
        6 : [""],
        7 : [""],
        8 : [""],
        9 : [""],
        }

lesson_texts = {
        1 : ["the be to of and a in that have I it for not on with he as you do at this but his by fom they we say her she or an will my one all would there their what so up out if about who get which go me when make can like time no just him know take pouple into year your good some could them see other then now look only come its over think also back after use two how our work first well way even new want because any these give day most us"],
        2 : [""],
        3 : [""],
        4 : [""],
        5 : [""],
        6 : [""],
        7 : [""],
        8 : [""],
        9 : [""],
        }

def get_text(num):
    return lesson_texts[num]

def get_intro(num):
    return lesson_intros[num]
