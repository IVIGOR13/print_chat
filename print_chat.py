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
        print('\x1b[A\r', end='')
        if clr:
            self._clear_screen()


    def up_on_rows(self, number):
        print(('\x1b[A\r' + ' ' * os.get_terminal_size().columns + '\r') * number, end='')


    def up_on_message(self, number):
        n = self.__get_lines(number)
        self.up_on_rows(n)


    def up_on_occupied_rows(self, len_str):
        lines = ((len_str-1) // os.get_terminal_size().columns) + 1
        self.up_on_rows(lines)


    def get_num_messages(self):
        return(len(self.MESSAGES))


    def get_messages(self, start, end):
        s = len(self.MESSAGES) - end + 1
        e = len(self.MESSAGES) - start + 1
        return self.MESSAGES[s:e]


    def set_colors(self, colors):
        for i in colors:
            self.sender_color[i[0]] = i[1]


    def __get_lines(self, number):
        lines = 0
        for i in range(number):
            m = self.MESSAGES[(len(self.MESSAGES)-1) - i]
            lines += (((len(m['sender']) + len(m['message']) + 4)-1) // os.get_terminal_size().columns) + 1
        return lines


    def __print_mess(self, sender, text):

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
        if number >= 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            for i in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self.__print_mess(i['sender'], i['message'])


    def load(self, number):
        if number >= 0 and number <= len(self.MESSAGES):
            for i in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self.__print_mess(i['sender'], i['message'])


    def remove(self, number):
        if number >= 0 and number <= len(self.MESSAGES):
            self.MESSAGES.pop(len(self.MESSAGES) - number)
            self.up_on_message(number)
            self.load(number-1)


    def edit(self, number, text):
        if number >= 0 and number <= len(self.MESSAGES):
            n = len(self.MESSAGES) - number
            self.MESSAGES[n].update({'sender': self.MESSAGES[n]['sender'], 'message': text})
            self.reload(number)


    def add_message(self, sender, text):
        if text != '':
            self.MESSAGES.append({'id': self.id, 'sender': sender, 'message': text})
            self.id += 1
            self.__print_mess(sender, text)


    def __init__(self, clr=True, file_name=''):
        self.id = 0
        self.MESSAGES = []
        self.sender_color = {}
        self.file_name = file_name
        if file_name != '':
            self.save_file = True
        else:
            self.save_file = False
        if clr:
            self._clear_screen()
