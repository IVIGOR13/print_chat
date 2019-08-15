#
# Author: Igor Ivanov
# 2019
#

import time
import os
from termcolor import colored
import colorama

colorama.init()

class print_chat:

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def close(self, clr=False):
        self.MESSAGES.clear()
        self.sender_color.clear()
        print('\x1b[A', end='')
        if clr:
            self._clear_screen()
            
            
    def up_on_rows(self, number):
        print('\x1b[A' * number, end='')
        

    def up_on_occupied_rows(self, len_str):
        n = (len_str // (os.get_terminal_size().columns-1)) + 1
        print('\x1b[A' * n, end='')


    def get_num_messages(self):
        return(len(self.MESSAGES))


    def get_messages(self, start, end):
        return self.MESSAGES[len(self.MESSAGES)-end : len(self.MESSAGES)-start]


    def set_colors(self, colors):
        for i in colors:
            self.sender_color[i[0]] = i[1]


    def __get_lines(self, number):
        lines = 0
        for i in range(number):
            m = self.MESSAGES[(len(self.MESSAGES)-1) - i]
            l = ((len(m[0]) + len(m[1]) + 4) // (os.get_terminal_size().columns+1)) + 1
            m[2] = l
            lines += l
        return lines


    def __print_mess(self, sender, text, lines):

        if not sender in self.sender_color: c0, c1 = 'white', 'grey'
        else: c0, c1 = 'grey', self.sender_color[sender]

        print(colored('[' + sender + ']', c0, ('on_' + c1)) + ': ', end='')
        print(text, end='\n')

        if self.save_file:
            dt = time.strftime("%d.%m.%Y %H:%M", time.gmtime())
            str = ''
            try:
                file = open(self.file_name, 'r')
                str = file.read()
                file.close()
                file = open(self.file_name, 'w')
            except IOError:
                file = open(self.file_name, 'w')

            file.write(str + '[' + dt + '][' + sender + ']' + ': ' + text + '\n')


    def reload(self, number):
        if number > 0 and number < len(self.MESSAGES):
            print('\x1b[A\r' * self.__get_lines(number), end='')
            for i in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self.__print_mess(i[0], i[1], i[2])


    def load(self, number):
        if number > 0 and number < len(self.MESSAGES):
            for i in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self.__print_mess(i[0], i[1], i[2])


    def remove(self, number):
        if number > 0 and number < len(self.MESSAGES):
            print(('\x1b[A\r' + ' ' * os.get_terminal_size().columns + '\r') * self.__get_lines(number), end='')
            self.MESSAGES.pop(len(self.MESSAGES) - number)
            self.load(number-1)


    def edit(self, number, text):
        if number > 0 and number < len(self.MESSAGES):
            print(('\x1b[A\r' + ' ' * os.get_terminal_size().columns + '\r') * self.__get_lines(number), end='')
            self.MESSAGES[len(self.MESSAGES) - number][1] = text
            self.load(number)


    def add_message(self, sender, text):
        if text != '':
            lines = ((len(sender) + len(text) + 4) // os.get_terminal_size().columns) + 1
            self.MESSAGES.append([sender, text, lines])
            self.__print_mess(sender, text, lines)


    def __init__(self, clr=True, file_name=''):
        self.MESSAGES = []
        self.sender_color = {}
        self.file_name = file_name
        if file_name != '':
            self.save_file = True
        else:
            self.save_file = False
        if clr:
            self._clear_screen()
