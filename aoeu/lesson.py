#import curses
#import lessons


#def __init__():
#    self.l = Lesson(0)
#    start()

#l = Lesson(0)

lesson_intros = {
        0 : ["Welcome to Lesson 0, Getting started",
            "Why learn Dvorak?", 
            "",
            "If you've gotten this far, you probably already have a good understanding",
            "of what dvorak is and why people switch to it so I won't bore you too much.",
            "",
            "How to learn Dvorak?",
            ""
            "This approach"],
        1 : [""],
        2 : [""],
        3 : [""],
        4 : [""],
        5 : [""],
        6 : [""],
        7 : [""],
        8 : [""],
        9 : [""],
        }

def get_intro(num):
    return lesson_intros[num]

