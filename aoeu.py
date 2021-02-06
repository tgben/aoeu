#!/usr/bin/env python3

import curses
import time
import sys
import os


#text = sys.stdin.read().strip().replace('\t', '').replace('\n', '')

# dirty hack to make sys.stdin and curses work together
# https://stackoverflow.com/a/4000997
#f=open("/dev/tty")
#os.dup2(f.fileno(), 0)

def main():

    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    scr.addstr(0, 0, "This string gets printed at position (0, 0)")

    scr.refresh()

    curses.napms(2000)
    curses.endwin()

    return
    
main()
'''
def draw_window(stdscr):
    
    k = 0
    cursor_x = 0
    cursor_y = 0

    iteration = 0

    error_string = []

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    START_TIMER = False

    height, width = stdscr.getmaxyx()

    captions = len(text) // width + 5

    max_length = height * width - width * 2

   # input string too large
    if len(text) > max_length:
        exit()

    while k != 27:

        stdscr.clear()
        stdscr.refresh()

        # header
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(0, 0, "LET'S GO! WHAT ARE YOU WAITING FOR?".center(width))
        stdscr.attroff(curses.color_pair(3))

        # put together three parts of text
        correct_part = text[:cursor_x+(cursor_y*width)-len(error_string)]
        error_part = ''.join(error_string)
        future_part = text[cursor_x+(cursor_y*width):]

        # print correct_part
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(2, 0, correct_part)
        stdscr.attroff(curses.color_pair(1))

        # print error_part
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(len(correct_part) // width + 2, len(correct_part) % width, error_part)
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # print future_part
        stdscr.addstr(len(correct_part + error_part) // width + 2, len(correct_part + error_part) % width, future_part)

        stdscr.move(cursor_y + 2, cursor_x)

        # wait keypress
        k = stdscr.getch()

        if not START_TIMER:
            start = time.time()
            START_TIMER = True
        
        # CORRECT BRANCH
        if chr(k) == text[iteration] and not error_string:
            cursor_x += 1
            iteration += 1

            error_string.clear()

            # exit if text ended
            if iteration == len(text):
                end = time.time()

                overal_time = end - start
                overal_time_in_mins = overal_time / 60

                speed = int(len(text) / overal_time_in_mins)

                if 0 <= speed <= 150: s = "Common! Use both hands!"
                if 150 <= speed <= 350: s = "Not great, not terrible."
                if 350 <= speed <= 10000: s = "WTF... A u typewriter?"
                
                stdscr.addstr(captions, 0, f"Time: {round(overal_time, 2)} seconds")
                stdscr.addstr(captions+1, 0, f"cpm: {speed}, wpm: {int(speed / 4.7)}")
                stdscr.addstr(captions+2, 0, f"{s}")
                
                stdscr.refresh()

                time.sleep(5)
                break

        # INCORRECT BRANCH
        elif chr(k) != text[iteration] and k != curses.KEY_BACKSPACE or error_string and k != curses.KEY_BACKSPACE:

            error_string.append(chr(k))
            cursor_x += 1

        # BACKSPACE BRANCH
        elif k == curses.KEY_BACKSPACE and error_string:
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
'''

