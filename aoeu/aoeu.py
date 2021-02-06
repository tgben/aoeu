import curses
import time
import sys
import os

from lessons.lesson import Lesson
import lessons.lesson0

def main():

    # init
    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #height, width = scr.getmaxyx()
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    scr.keypad(1)
    
    lessons = ['Lesson 0, Starting out', 'Lesson 1, The home row']

    q = 0
    while(q==0):
        msg_welcome = "welcome to aoeu"
        print_title(scr)
        print_center(scr, msg_welcome, 3)
        print_center(scr, "aoeu is made for programmers to easily switch to dvorak.", 5)
        print_center(scr, "to start, type any number to select that lesson", 6)
        print_center(scr, "We recommed working through linearly but that decision is left to you", 7)
        print_lessons(scr, lessons)

        f=Lesson(0)

        scr.refresh()

        c = scr.getch()
        #print_center(scr, chr(c), 9)
        if c >= 48 and c <= len(lessons)+48:
            route_lesson(0)
        else:
            print_error(scr, "please type a number or press esc to quit")
        
        scr.refresh()
        time.sleep(3)
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
    x_start = 10
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

def print_error(scr, msg):
    height, width = scr.getmaxyx()
    scr.addstr(0, int(width)-int(len(msg)), msg, curses.color_pair(2))

def route_lesson(num):
    if num == 0:
        scr.addscr(lessons.lesson0)


main()

















