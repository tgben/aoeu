#!/usr/bin/env python3
# NOT USED RIGHT NOW
import curses
import time
import sys
import os

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

