#import curses
#import lessons


#def __init__():
#    self.l = Lesson(0)
#    start()

#l = Lesson(0)

lesson_intros = {
        0 : ["Welcome to Lesson 0, Getting started", "Why learn Dvorak? <br> If you've gotten this far, you probably already have a good understanding of what dvorak is and why people switch to it so I won't bore you too much. <br> <br> How to learn Dvorak? <br> This approach xxxyyyzzz"],
        1 : ["Welcome to Lesson 1, Review", "In this lesson, we will review common english words with no punctuation. press any key besides tab to start:"],
        2 : ["Welcome to Lesson 2, ,. <> :;", "By now, you should feel pretty smooth with normal words, eh? Time for some useful punctuation"],
        3 : ["Welcome to Lesson 3: += _-", "More tough symbols. Don't feel discouraged if you are slow! everyone is at the start. Remember to take breaks."],
        4 : ["Welcome to Lesson 4: [] {} ()", "These are the most important and also likely the most used. Master these!"],
        5 : ["Welcome to Lesson 5: Common Shell Commands", "You will likely be using these A LOT! These may need some mental re-programming."],
        6 : ["Welcome to Lesson 6: Common Vim Commands", "I recommend doing vimtutor, but these are some useful keys to refresh."],
        7 : ["Welcome to Lesson 7: Putting it all together", "At this point you are a buttery smooth Dvorak user. Try practicing on a site like coderacer.dev. I hope this program helped!"],
        }

lesson_texts = {
        0 : ["welcome"],
        1 : ["the be to of and a in that have I it for not on with he as you do at this but his by fom they we say her she or an will my one all would there their what so up out if about who get which go me when make can like time no just him know take pouple into year your good some could them see other then now look only come its over think also back after use two how our work first well way even new want because any these give day most us"],
        2 : ["var: <br> <tag> </br> </tag> i<j i>j x>f f>r r>d d<w r>i sum: max: 12; 9; 8; 0; 6; maxNum; len; sum; var; text; shell;"],
        3 : ["num+=1 sum+=2 i+1 57+900 92+1 max+1 max+=1 num+1 len+1 max=50 sum=0 number=89 snake_case_is_cool max_num sum_var modulo_var array_sum iterate_array dashed-var branch-name-ex branch-var master-branch main-branch very-important-commit"],
        4 : ["fun() init() sum() len() max() main() split() random() rand() randrange() var() func() function() gui() extension() get_max() set_max() set_num() get_num_func() get_best_typing_skills()"],
        5 : ["pwd ls cd mkdir rmdir mount df uname ps kill service batch shutdown touch cat vim cat head tail cp mv comm less ls cmp dd alias history wget iptables traceroute curl find locate grep clear echo sort sudo chmod man tar whatis help"],
        6 : ["placeholder"],
        7 : ["placeholder"]
        }

def get_text(num):
    return lesson_texts[num]

def get_intro(num):
    return lesson_intros[num]

def get_lesson_array(num):
    return lesson_texts[num][0].split(" ")
