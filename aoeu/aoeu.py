import curses
import time
import sys
import os

#from lessons.lesson import Lesson
#import lessons.lessonIntros
import lesson

scr = curses.initscr()
lessons = ['Lesson 0, Starting out', 'Lesson 1, The home row', 
            'Lesson 2, The top row', 'Lesson 3, The bottom row', 
            'Lesson 4:, ,. <> "" :: ;;',
            'Lesson 5, () {} []', 'Lesson 6: _- += |\ ',
            'Lesson 7: common shell commands', 'Lesson 8: vim commands',
            'Lesson 9: All together']

def main():

    # init
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #height, width = scr.getmaxyx()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    scr.keypad(1)
    

    menu()
    #scr.refresh()

    #c = scr.getch()


    #cleanup()
    curses.endwin()

    return

def menu():
    q = 0
    while(q==0):
        msg_welcome = "welcome to aoeu"
        msg_intro = "aoeu is made for programmers to easily switch to Dvorak and focuses on practical phrases and commands for programmers. We only briefly review the normal letters so it is recommended to practice those beforehand. <br> <br> To start, type any number to select that lesson. To quit, type tab at any time"
        #scr.clear()
        print_title()
        print_center(msg_welcome, 3)
        #print_center_stepped(msgl_intro, 6)
        height, width = scr.getmaxyx()
        y = print_paragraph(5, int(width*.1), int(width*.9), msg_intro)
        print_lessons(lessons, int(y+2), int(width*.1 + 4))
        scr.refresh()
        
        #f=Lesson(0)

        c = scr.getch()
        if c >= 48 and c <= len(lessons)+48:
            lesson_start(c)
        if c == 9:
            lesson_num = c-48
            curses.endwin()
            quit()
        else:
            print_error("please type a number or press tab to quit")
            scr.refresh()

        #time.sleep(3)

def lesson_start(c): 
    lesson_num = c-48
    intro = get_lesson_intro(lesson_num)
    scr.clear()
    print_title()
    height, width = scr.getmaxyx()

    #special intros for 0 and probably the last
    print_center_stepped([intro[0]], 3)
    #print_stepped(intro[1:], 6, 3)
    print_paragraph(5, int(width*.1), int(width*.9), intro[1])

    c = scr.getch()
    if c == 9: #tab key
        scr.clear()
        menu()
    else:
        #start test for lesson
        curses.endwin()
        quit()

# the top bar
def print_title(): 
    height, width = scr.getmaxyx()
    msg = "AOEU"
    scr.addstr(0, int(width/2)-int(int(len(msg)/2)), msg, curses.color_pair(2))
    msg = "v.0.1"
    scr.addstr(0,0, msg, curses.color_pair(1))

def print_center(msg, x=0):
    height, width = scr.getmaxyx()
    if x == 0:
        scr.addstr(int(height/2), int(width/2)-int(int(len(msg)/2)), msg)
    else:
        scr.addstr(x, int(width/2)-int(int(len(msg)/2)), msg)


def print_lessons(lessons, x_start, y_start):
    for i, lesson in enumerate(lessons):
        m = ''+str(i)+':  '+lesson
        scr.addstr(x_start, y_start, m)
        x_start+=1

def print_stepped(msgl, x_start, y):
    for msg in msgl:
        scr.addstr(x_start, y, msg)
        x_start+=1

def cleanup():
    curses.nocbreak()   # Turn off cbreak mode
    curses.echo()       # Turn echo back on
    curses.curs_set(1)  # Turn cursor back on
    scr.keypad(0) # Turn off keypad keys

def print_error(msg):
    height, width = scr.getmaxyx()
    scr.addstr(0, int(width)-int(len(msg)), msg, curses.color_pair(2))

#print intro
def get_lesson_intro(num):
    return lesson.get_intro(num)

def print_center_stepped(msgl, x_start):
    x_curr = x_start
    for msg in msgl:
        print_center(msg, x_curr)
        x_curr+=1
# print paragraph style, return num of lines used
def print_paragraph(x_start, y_start, width, msg):
    x_curr = x_start
    y_curr = y_start
    width = width
    msgl = msg.split(' ')
    for word in msgl:
        word = word + " "
        if word == "<br> ":
            x_curr += 1
            y_curr = y_start
        elif y_curr+len(word) < width:
            scr.addstr(x_curr, y_curr, word)
            y_curr += len(word)
        else:
            y_curr = y_start
            x_curr += 1
            scr.addstr(x_curr, y_curr, word)
            y_curr += len(word)

    return x_curr

main()

















