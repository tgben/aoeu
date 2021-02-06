import curses
import time
import sys
import os

import lessons.lesson1

def main():

    # init
    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #height, width = scr.getmaxyx()
    
    lessons = ['Lesson 0, Starting out', 'Lesson 1, The home row']

    q = 0
    while(q==0):
        print_title(scr)
        print_center(scr, "welcome to aoeu", 3)
        print_lessons(scr, lessons)
        #c = scr.getch()
        curses.curs_set(0)
        scr.refresh()

        time.sleep(10)
        q = 1
    #scr.refresh()

    #c = scr.getch()


    #cleanup()
    curses.endwin()

    return

# the top bar
def print_title(scr): 
    height, width = scr.getmaxyx()
    msg = "AOEU"
    scr.addstr(0, int(width/2)-int(int(len(msg)/2)), msg, curses.color_pair(2))
    msg = "v.0.1"
    scr.addstr(0,0, msg, curses.color_pair(1))

def print_center(scr, msg, x=0):
    height, width = scr.getmaxyx()
    if x == 0:
        scr.addstr(int(height/2), int(width/2)-int(int(len(msg)/2)), msg)
    else:
        scr.addstr(x, int(width/2)-int(int(len(msg)/2)), msg)


def print_lessons(scr, lessons):
    x_start = 8
    y_start = 4
    for i, lesson in enumerate(lessons):
        m = ''+str(i)+':  '+lesson
        scr.addstr(x_start, y_start, m)
        x_start+=1


def cleanup():
    curses.nocbreak()   # Turn off cbreak mode
    curses.echo()       # Turn echo back on
    curses.curs_set(1)  # Turn cursor back on
    scr.keypad(0) # Turn off keypad keys

main()

















