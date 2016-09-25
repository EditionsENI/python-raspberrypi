#!/usr/bin/env python3
import curses, string

class PiCalc:
    def __init__(self, screen):
        self.screen = screen
        self.formula = ''
        self.history = ''
        self.number = ''
        self.stack = []
        self.accepted_chars = string.digits + '+/-*=.CcFf'
        self.screen_y, self.screen_x = self.screen.getmaxyx()
        self.screen.keypad(1)
        self.draw_calc()
        self.parse_input()

    def draw_calc(self):
        self.screen.clear()

        self.calc_y = 30
        self.calc_x = 60
        self.calc = curses.newwin(
                        self.calc_y, 
                        self.calc_x, 
                        int(self.screen_y / 2) - int(self.calc_y / 2),
                        int(self.screen_x / 2) - int(self.calc_x / 2)
                    )

        self.calc.box()
        self.screen.refresh()

        line = '-' * self.calc_x
        char_pos = int(int(self.calc_x / 4) / 1.25)
        instructions = 'Nettoyer (C ou c) - Fermer (F ou f)'

        self.calc.addstr(4, 0, line)
        self.calc.addstr(6, (self.calc_x - 5) - len(instructions), instructions)
        self.calc.addstr(8, 0, line)

        self.calc.addstr(12, char_pos,     '7')
        self.calc.addstr(12, char_pos * 2, '8')
        self.calc.addstr(12, char_pos * 3, '9')
        self.calc.addstr(12, char_pos * 4, '/')

        self.calc.addstr(16, char_pos,     '4')
        self.calc.addstr(16, char_pos * 2, '5')
        self.calc.addstr(16, char_pos * 3, '6')
        self.calc.addstr(16, char_pos * 4, '*')

        self.calc.addstr(20, char_pos,     '1')
        self.calc.addstr(20, char_pos * 2, '2')
        self.calc.addstr(20, char_pos * 3, '3')
        self.calc.addstr(20, char_pos * 4, '-')

        self.calc.addstr(24, char_pos,     '0')
        self.calc.addstr(24, char_pos * 2, '.')
        self.calc.addstr(24, char_pos * 3, '=')
        self.calc.addstr(24, char_pos * 4, '+')

        self.calc.refresh()

    def update_result(self, key):
        self.calc.addstr(2, (self.calc_x - 4) - len(key), key)
        self.calc.refresh()

    def parse_input(self):
        while True:
            key = self.screen.getkey().strip()
            if key == '':
                key = '='
            if key in self.accepted_chars:
                if key == '=':
                    if len(self.stack) == 0:
                        continue
                    if len(self.history) > 0 and self.history[-1] in '+/-*':
                        continue
                    self.stack.append(self.number)
                    result = eval(''.join(self.stack))
                    self.draw_calc()
                    self.update_result(str(result))
                    self.history = key
                    self.stack = []
                    self.number = ''
                    self.formula = ''
                if key in '+/-*':
                    if len(self.history) == 0:
                        continue
                    if len(self.history) > 0 and self.history[-1] in '+/-*=':
                        continue
                    self.stack.append(self.number)
                    self.stack.append(key)
                    self.number = ''
                    self.formula = self.formula + key
                    self.update_result(self.formula)
                    self.history = self.history + key
                if key in string.digits + '.':
                    if len(self.history) > 0 and self.history[-1] == '=':
                        self.draw_calc()
                        self.history = ''
                    self.formula = self.formula + key
                    self.number = self.number + key
                    self.history = self.history + key
                    self.update_result(self.formula)
                if key in 'Cc':
                    self.history = ''
                    self.formula = ''
                    self.number = ''
                    self.draw_calc()
                if key in 'Ff':
                    break

curses.wrapper(PiCalc)
