#
# Author: Igor Ivanov
# 2019
#
import time
import os
from termcolor import colored
from datetime import datetime
import colorama

colorama.init()

"""
Small print tool for implementing chat in the terminal
"""

class print_chat:

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def clear_row(self):
        print('\r' + ' ' * os.get_terminal_size().columns + '\r', end='')


    def up_on_rows(self, number):
        self.clear_row
        print(('\x1b[A\r' + ' ' * os.get_terminal_size().columns + '\r') * number, end='')


    def up_on_message(self, number):
        n = self.__get_lines(number)
        self.up_on_rows(n)


    def up_on_occupied_rows(self, len_str):
        lines = ((len_str-1) // os.get_terminal_size().columns) + 1
        self.up_on_rows(lines)


    def down_on_rows(self, number):
        self.clear_row()
        print(('\n\r' + ' ' * os.get_terminal_size().columns + '\r') * number, end='')


    def get_num_messages(self):
        return(len(self.MESSAGES))


    def get_messages_from(self, sender):
        out = ()
        for i in self.MESSAGES:
            if i['sender'] == sender:
                out.append(i)
        return out


    def get_messages(self):
        return self.MESSAGES


    def get_message(self, number):
        if number <= len(self.MESSAGES):
            return self.MESSAGES[len(self.MESSAGES) - number]


    def get_senders(self):
        out = ()
        for key in self.senders.keys():
            out.append(key)
        return out


    def get_mark(self, number):
        return self.MESSAGES[len(self.MESSAGES) - number]['mark']


    def set_colors(self, colors):
        found = False
        for color in colors:
            for i in range(len(self.senders)):
                if self.senders[i]['sender'] == color[0]:
                    self.senders[i]['color'] = color[1]
                    found = True

            if not found:
                if len(color) == 1:
                    self.senders.append({
                            'sender': color[0],
                            'color': 'grey',
                        })
                else:
                    self.senders.append({
                            'sender': color[0],
                            'color': color[1],
                        })


    def get_time(self):
        if not self.time_full:
            return datetime.today().strftime("%H:%M")
        else:
            return datetime.today().strftime("%d.%m.%y %H:%M")


    def set_header(self, text):
        self.header = text.split('\n')
        self._print_header()


    def _print_header(self):
        self._clear_screen()
        for i in self.header:
            print(i)


    # returns the number of lines that must be passed to move the cursor to the specified message
    def __get_lines(self, number):
        lines = 0
        for i in range(number):

            # counting the number of lines occupied by a message
            m = self.MESSAGES[(len(self.MESSAGES)-1) - i]
            l = (len(m['sender']) + len(m['text']) + len(m['mark']) + self.len_frame)

            # count the number of lines occupied by a skip
            s = 0
            for j in m['skip']:
                j = str(j)
                if isinstance(j, str):
                    for k in j.split('\n'):
                        s += ((len(k)-1) // os.get_terminal_size().columns) + 1
                else:
                    s += ((len(j)-1) // os.get_terminal_size().columns) + 1

            lines += (((l-1) // os.get_terminal_size().columns) + 1) + s

        return lines


    def _print_mess(self, sender, text, time, skip, mark):

        if self.is_time:
            print('[{}] '.format(time), end='')

        # color selection for printing sender name
        c0, c1 = 'white', 'grey'

        found = False
        for i in self.senders:
            if i['sender'] == sender:
                c = i['color']
                if c == 'grey':
                    c0, c1 = 'white', 'grey'
                else:
                    c0, c1 = 'grey', c
                break
                found = True
        if not found:
            self.senders.append({
                    'sender': sender,
                    'color': 'grey',
                })

        print(colored('[' + sender + ']', c0, ('on_' + c1)) + ': ', end='')
        print('{}{}'.format(text, ''.join(mark)), end='\n')
        for i in skip:
            print(i)



    def add_mark(self, number, mark):
        if not mark == '' and number > 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            m = self.MESSAGES[len(self.MESSAGES)-number]['mark']
            if not m:
                self.MESSAGES[len(self.MESSAGES)-number].update({
                        'mark': [str(mark)]
                    })
            else:
                m.append(str(mark))
                self.MESSAGES[len(self.MESSAGES)-number].update({
                        'mark': m
                    })
            self._load(number)


    def edit_mark(self, number, mark):
        if number > 0 and number <= len(self.MESSAGES):
            if mark == '':
                self.remove_mark(number)
            else:
                n = len(self.MESSAGES) - number
                self.up_on_message(number)
                self.MESSAGES[n].update({
                        'mark': [str(mark)]
                    })
                self._load(number)


    def remove_mark(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            n = len(self.MESSAGES) - number
            self.up_on_message(number)
            self.MESSAGES[n].update({
                    'mark': []
                })
            self._load(number)


    def has_mark(self, number):
        n = len(self.MESSAGES) - number
        if self.MESSAGES[n]['mark'] == []:
            return False
        else:
            return True


    def get_mark(self, number):
        n = len(self.MESSAGES) - number
        return self.MESSAGES[n]['mark']


    def add_skip(self, number, text):
        if not text == '' and number > 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            m = self.MESSAGES[len(self.MESSAGES)-number]['skip']
            if not m:
                self.MESSAGES[len(self.MESSAGES)-number].update({
                        'skip': [str(text)]
                    })
            else:
                m.append(str(text))
                self.MESSAGES[len(self.MESSAGES)-number].update({
                        'skip': m
                    })
            self._load(number)


    def edit_skip(self, number, text):
        if number > 0 and number <= len(self.MESSAGES):
            if text == '':
                self.remove_skip(number)
            else:
                self.up_on_message(number)
                self.MESSAGES[len(self.MESSAGES) - number].update({
                        'skip': [str(text)]
                    })
                self._load(number)


    def remove_skip(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            self.MESSAGES[len(self.MESSAGES) - number].update({
                    'skip': []
                })
            self._load(number)


    def has_skip(self, number):
        if self.MESSAGES[len(self.MESSAGES) - number]['skip'] == []:
            return False
        else:
            return True


    # reprints the specified number of messages
    def reload(self, number):
        if number > 0 and number < len(self.MESSAGES):
            self.up_on_message(number)
            self._load(number)
        elif number == len(self.MESSAGES):
            self._clear_screen()
            self._print_header()
            self._load(number)


    def _load(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            for m in self.MESSAGES[len(self.MESSAGES)-number:len(self.MESSAGES)]:
                self._print_mess(m['sender'], m['text'], m['time'], m['skip'], m['mark'])


    def remove(self, number):
        if number > 0 and number <= len(self.MESSAGES):
            self.up_on_message(number)
            self._load(number-1)

            self.MESSAGES.pop(len(self.MESSAGES) - number)


    def edit(self, number, text):
        if number > 0 and number <= len(self.MESSAGES):
            if text == '':
                self.remove(number)
            else:
                n = len(self.MESSAGES) - number
                self.up_on_message(number)
                self.MESSAGES[n].update({
                        'text': text
                    })
                self._load(number)


    def add_message_top(self, sender, text, time='', skip=[], mark=[], prnt=True):
        text = " ".join(str(text).split())
        if text != '':

            if time == '':
                time = self.get_time()

            self.MESSAGES.insert(0, {
                    'sender': sender,
                    'text': text,
                    'time': time,
                    'skip': skip,
                    'mark': mark,
                })

            if prnt:
                self.up_on_message(self.get_num_messages() - 1)
                self._print_mess(sender, text, time, skip, mark)
                self._load(self.get_num_messages()-1)


    def add_message(self, sender, text, time='', skip=[], mark=[]):
        text = " ".join(str(text).split())
        if text != '':

            if time == '':
                time = self.get_time()

            self.MESSAGES.append({
                    'sender': sender,
                    'text': text,
                    'time': time,
                    'skip': skip,
                    'mark': mark,
                })
            self._print_mess(sender, text, time, skip, mark)


    def close(self, clr=False):
        self.MESSAGES.clear()
        self.senders.clear()
        print('\x1b[A\r', end='')
        if clr:
            self._clear_screen()


    def __init__(self, time=False):
        self.MESSAGES = []
        self.senders = []
        self.header = []

        self.is_time = False
        self.time_full = False
        if time == 'short':
            self.len_frame = 4 + 8
            self.is_time = True
        elif time == 'full':
            self.len_frame = 4 + 8 + 9
            self.is_time = True
            self.time_full = True
        else:
            self.len_frame = 4

        self._clear_screen()
