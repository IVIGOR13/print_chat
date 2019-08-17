#
# Author: Igor Ivanov
# 2019
#
#
# # TODO: get_senders()
#
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
        found = False
        for color in colors:
            for i in range(len(self.senders)):
                if self.senders[i]['sender'] == color[0]:
                    self.senders[i]['color'] = color[1]
                    found = True

            if not found:
                self.senders.append({'id': self.id_sender, 'sender': color[0], 'color': color[1]})
                self.id_sender += 1


    def __get_lines(self, number):
        lines = 0
        for i in range(number):
            m = self.MESSAGES[(len(self.MESSAGES)-1) - i]
            l = (len(m['sender']) + len(m['message']) + self.len_frame)
            lines += ((l-1) // os.get_terminal_size().columns) + 1
        return lines


    def __print_mess(self, sender, text):

        a = ''
        if self.time:
            a = time.strftime("%H:%M", time.gmtime())

        for i in self.senders:
            if not i['sender'] == sender:
                c0, c1 = 'white', 'grey'
            else:
                c0, c1 = 'grey', i['color']
                break


        print('[' + a + '] ' + colored('[' + sender + ']', c0, ('on_' + c1)) + ': ', end='')
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
            text = " ".join(text.split())
            self.MESSAGES.append({'id': self.id_message, 'sender': sender, 'message': text})
            self.id_message += 1
            self.__print_mess(sender, text)

            return (self.id_message-1)


    def get_senders(self):
        return self.senders


    def __init__(self, clr=True, file_name='', time=False):
        self.time = time
        if time:
            self.len_frame = 12
        else:
            self.len_frame = 4
        self.id_message = 0
        self.id_sender = 0
        self.MESSAGES = []
        self.senders = []
        self.file_name = file_name
        if file_name != '':
            self.save_file = True
        else:
            self.save_file = False
        if clr:
            self._clear_screen()
