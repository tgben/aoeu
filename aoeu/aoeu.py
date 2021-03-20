import curses
import time
import sys
import os
#from lessons.lesson import Lesson
#import lessons.lessonIntros
import lesson
import random

ALIAS_TAB = 9
ALIAS_BACKSPACE = 127

scr = curses.initscr()
lessons = ['Lesson 0, Starting out', 'Lesson 1, Review',
        'Lesson 2:, ,. <> :;', 'Lesson 3: _- +='
            'Lesson 4, () {} []',
            'Lesson 5: common shell commands', 'Lesson 6: vim commands',
            'Lesson 7: All together']

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
        #scr.addstr(30,20,str(int(c)))
        #scr.refresh()
        #time.sleep(3)
        if c >= 48 and c <= len(lessons)+48:
            lesson_start(c)
        if c == ALIAS_TAB:
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

    print_center_stepped([intro[0]], 3)
    #print_stepped(intro[1:], 6, 3)
    print_paragraph(5, int(width*.1), int(width*.9), intro[1])

    c = scr.getch()
    if c == ALIAS_TAB:
        scr.clear()
        menu()
    else:
        #start test for lesson
        run_test(get_lesson_text(lesson_num))
        c = scr.getch()
        scr.clear() 
        lesson_start(lesson_num+48)

def run_test(text):
    k, cursor_x, cursor_y, i = 0,0,0,0
    y = 3
    error_string = []
    timer = False
    height, width = scr.getmaxyx()
    width = int(width * 0.8)
    captions = len(text) // width + 5
    max_length = height * width - width * 2

   # input string too large
    if len(text) > max_length:
        exit()

    while k != ALIAS_TAB:
        scr.clear()
        scr.refresh()
        print_title()

        # put together three parts of text
        correct_part = text[:cursor_x+(cursor_y*width)-len(error_string)]
        error_part = ''.join(error_string)
        future_part = text[cursor_x+(cursor_y*width):]

        # print correct_part
        scr.attron(curses.color_pair(1))
        scr.addstr(y, 0, correct_part)
        scr.attroff(curses.color_pair(1))

        # print error_part
        scr.attron(curses.color_pair(2))
        scr.attron(curses.A_BOLD)
        scr.addstr(len(correct_part) // width + y, len(correct_part) % width, error_part)
        scr.attroff(curses.color_pair(2))
        scr.attroff(curses.A_BOLD)

        # print future_part
        scr.addstr(len(correct_part + error_part) // width + y, len(correct_part + error_part) % width, future_part)

        scr.move(cursor_y + 2, cursor_x)

        # wait keypress
        k = scr.getch()

        if not timer:
            start = time.time()
            timer = True

        # CORRECT BRANCH
        if chr(k) == text[i] and not error_string:
            cursor_x += 1
            i += 1

            error_string.clear()

            # exit if text ended
            if i == len(text):
                end = time.time()

                overal_time = end - start
                overal_time_in_mins = overal_time / 60

                speed = int(len(text) / overal_time_in_mins)


                scr.addstr(captions, 0, f"Time: {round(overal_time, 2)} seconds")
                scr.addstr(captions+1, 0, f"cpm: {speed}, wpm: {int(speed / 4.7)}")

                scr.refresh()

                break

        # INCORRECT BRANCH
        elif (chr(k) != text[i] and k != ALIAS_BACKSPACE) or (error_string and k != ALIAS_BACKSPACE):

            error_string.append(chr(k))
            cursor_x += 1

        # BACKSPACE BRANCH
        elif k == ALIAS_BACKSPACE and error_string:
            error_string.pop()
            cursor_x -= 1


        if cursor_x >= width:
            cursor_x = 0
            cursor_y += 1

        if cursor_x < 0:
            cursor_x = width - 1
            cursor_y -= 1

        cursor_x = max(0, cursor_x)
        cursor_y = max(0, cursor_y)


def get_lesson_text(num):
    max_words = 20
    text = ""
    i=0
    text_ar = lesson.get_lesson_array(num)
    for i in range(max_words):
        x = random.randrange(0, len(text_ar))
        text += text_ar[x]
        if i != max_words-1:
            text += " "
    return text


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
















