from ast import Delete
import os
import tkinter as tk
from tkinter.ttk import Combobox
import re

class create_script:
    def create_folder(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def write_script(code, content):
        create_script.create_folder('./script')
        with open('./script/c' + code + '.lua', 'w', encoding='utf-8') as f:
            f.write(content)
        print('c' + code + '.lua has been writed')

class main_window:
    def __init__(self):
        class add:
            def row():
                self.step.append(0)
                self.button_group.append([])
                self.remove.button_main()
                button = tk.Button(self.window, text = '-', command = lambda: self.remove.row(button.grid_info()['row'] - 1))
                button.grid(row = self.row_id, column = 0)
                self.button_group[self.row_id - 1].append(button)
                pull_down = Combobox(self.window, width = 5)
                pull_down['values'] = ('【自】', '【起】', '【永】')
                pull_down.configure(state = 'normal')
                pull_down.grid(row = self.row_id, column = 1)
                button_add = tk.Button(self.window, text = '+', command = lambda: self.add.button_input(button.grid_info()['row'] - 1))
                self.button_group[self.row_id - 1].append(button_add)
                button_remove = tk.Button(self.window, text = '-', command = lambda: self.remove.button_input(button.grid_info()['row'] - 1))
                self.button_group[self.row_id - 1].append(button_remove)
                self.button_group[self.row_id - 1].append(pull_down)
                button_add.grid(row = self.row_id, column = len(self.button_group[self.row_id - 1]) - 2)
                button_remove.grid(row = self.row_id, column = len(self.button_group[self.row_id - 1]) - 1)
                self.row_id += 1
                self.add.button_main()
                    
            def button_main():
                self.button_add = tk.Button(self.window, text = '+', command = lambda: self.add.row())
                self.button_add.grid(row = self.row_id, column = 0)
                self.button_start = tk.Button(self.window, text = '点击生成', command = lambda: self.start())
                self.button_start.grid(row = self.row_id + 1, column = 0)
                self.button_clear = tk.Button(self.window, text = '清空', command = lambda: self.clear())
                self.button_clear.grid(row = self.row_id + 1, column = 1)
                    
            def button_input(row):
                if self.step[row] == 0:
                    if len(self.button_group[row][3].get()) == 0:
                            return
                    self.step[row] += 1
                    self.button_group[row][3].configure(state = 'disable')
                    if '【永】' in self.button_group[row][3].get():
                        description = tk.Label(self.window, text = '区域：')
                        description.grid(row = row + 1, column = 2)
                        pull_down = Combobox(self.window, width = 9)
                        pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【G】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                        pull_down.grid(row = row + 1, column = 3)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)
                        description = tk.Label(self.window, text = '影响：')
                        description.grid(row = row + 1, column = 4)
                        pull_down = Combobox(self.window, width = 7)
                        pull_down['values'] = ('影响自己', '影响所有卡')
                        pull_down.grid(row = row + 1, column = 5)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)
                    elif '【自】' in self.button_group[row][3].get():
                        description = tk.Label(self.window, text = '区域：')
                        description.grid(row = row + 1, column = 2)
                        pull_down = Combobox(self.window, width = 9)
                        pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                        pull_down.grid(row = row + 1, column = 3)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)
                        description = tk.Label(self.window, text = '触发：')
                        description.grid(row = row + 1, column = 4)
                        pull_down = Combobox(self.window, width = 15)
                        pull_down['values'] = ('自己状态变化时触发', '所有卡状态变化时触发')
                        pull_down.grid(row = row + 1, column = 5)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)
                        description = tk.Label(self.window, text = '时点：')
                        description.grid(row = row + 1, column = 6)
                        pull_down = Combobox(self.window, width = 15)
                        pull_down['values'] = ('Call到圆阵时', '攻击时', '战斗结束时')
                        pull_down.grid(row = row + 1, column = 7)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)
                        description_I = tk.Label(self.window, text = '1回合')
                        description_I.grid(row = row + 1, column = 8)
                        pull_down = Combobox(self.window, width = 5)
                        pull_down['values'] = ('不限', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                        pull_down.grid(row = row + 1, column = 9)
                        description_II = tk.Label(self.window, text = '次')
                        description_II.grid(row = row + 1, column = 10)
                        self.button_group[row].append(description_I)
                        self.button_group[row].append(pull_down)
                        self.button_group[row].append(description_II)
                    elif '【起】' in self.button_group[row][3].get():
                        description = tk.Label(self.window, text = '区域：')
                        description.grid(row = row + 1, column = 2)
                        pull_down = Combobox(self.window, width = 9)
                        pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                        pull_down.grid(row = row + 1, column = 3)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)
                        description_I = tk.Label(self.window, text = '1回合')
                        description_I.grid(row = row + 1, column = 4)
                        pull_down = Combobox(self.window, width = 5)
                        pull_down['values'] = ('不限', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                        pull_down.grid(row = row + 1, column = 5)
                        description_II = tk.Label(self.window, text = '次')
                        description_II.grid(row = row + 1, column = 6)
                        self.button_group[row].append(description_I)
                        self.button_group[row].append(pull_down)
                        self.button_group[row].append(description_II)

                elif self.step[row] == 1:
                    for i in range(self.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                        if '.!combobox' in str(self.button_group[row][i]):
                            if len(self.button_group[row][i].get()) == 0:
                                    return
                    self.step[row] += 1
                    for i in range(self.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                        if '.!combobox' in str(self.button_group[row][i]):
                            self.button_group[row][i].configure(state = 'disable')

                    if '【永】' in self.button_group[row][3].get():
                        button = tk.Button(self.window, text = '数值', command = lambda: new_window().main(row, 7, 'val'))
                        button.grid(row = row + 1, column = 6)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 7)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                        button = tk.Button(self.window, text = '场合', command = lambda: new_window().main(row, 9, 'con'))
                        button.grid(row = row + 1, column = 8)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 9)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                        if '影响所有卡' in self.button_group[row][7].get():
                            description = tk.Label(self.window, text = '影响的自己区域：')
                            description.grid(row = row + 1, column = 10)
                            pull_down = Combobox(self.window, width = 5)
                            pull_down['values'] = ('【V】', '【R】', '【V/R】')
                            pull_down.grid(row = row + 1, column = 11)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            description = tk.Label(self.window, text = '影响的对手区域：')
                            description.grid(row = row + 1, column = 12)
                            pull_down = Combobox(self.window, width = 5)
                            pull_down['values'] = ('【V】', '【R】', '【V/R】')
                            pull_down.grid(row = row + 1, column = 13)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            button = tk.Button(self.window, text = '目标筛选', command = lambda: new_window().main(row, 15, 'tg'))
                            button.grid(row = row + 1, column = 14)
                            text = tk.Entry(self.window, width = 5)
                            text.configure(state = 'disable')
                            text.grid(row = row + 1, column = 15)
                            self.button_group[row].append(button)
                            self.button_group[row].append(text)
                    elif '【自】' in self.button_group[row][3].get():
                        button = tk.Button(self.window, text = '费用', command = lambda: new_window().main(row, 7, 'cost'))
                        button.grid(row = row + 1, column = 11)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 12)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                        button = tk.Button(self.window, text = '场合', command = lambda: new_window().main(row, 9, 'con'))
                        button.grid(row = row + 1, column = 13)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 14)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                        button = tk.Button(self.window, text = '执行', command = lambda: new_window().main(row, 9, 'op'))
                        button.grid(row = row + 1, column = 15)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 16)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                    elif '【起】' in self.button_group[row][3].get():
                        button = tk.Button(self.window, text = '费用', command = lambda: new_window().main(row, 7, 'cost'))
                        button.grid(row = row + 1, column = 7)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 8)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                        button = tk.Button(self.window, text = '场合', command = lambda: new_window().main(row, 9, 'con'))
                        button.grid(row = row + 1, column = 9)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 10)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)
                        button = tk.Button(self.window, text = '执行', command = lambda: new_window().main(row, 9, 'op'))
                        button.grid(row = row + 1, column = 11)
                        text = tk.Entry(self.window, width = 5)
                        text.configure(state = 'disable')
                        text.grid(row = row + 1, column = 12)
                        self.button_group[row].append(button)
                        self.button_group[row].append(text)

                self.button_group[row][1].grid(row = row + 1, column = len(self.button_group[row]) - 2)
                self.button_group[row][2].grid(row = row + 1, column = len(self.button_group[row]) - 1)

        class remove:
            def row(r):
                if not isinstance(r, int):
                    r = self.row_id - 2
                if r < 0:
                    return
                for button in self.button_group[r]:
                    button.destroy()
                del self.button_group[r]
                del self.step[r]
                for i in range(r, len(self.button_group)):
                    for j in range(0, len(self.button_group[i])):
                        self.button_group[i][j].grid(row = i + 1, column = self.button_group[i][j].grid_info()['column'])
                self.row_id -= 1
                self.remove.button_main()
                self.add.button_main()
                    
            def button_main():
                self.button_add.destroy()
                self.button_start.destroy()
                self.button_clear.destroy()
                    
            def button_input(row):
                if len(self.button_group[row][3].get()) == 0 or self.step[row] == 0:
                    return
                if self.step[row] == 1:
                    self.step[row] -= 1
                    self.button_group[row][3].configure(state = 'normal')
                    for i in range(self.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                        self.button_group[row][i].destroy()
                    del self.button_group[row][self.get_range(self.button_group[row][3].get(), 1):]
                if self.step[row] == 2:
                    self.step[row] -= 1
                    for i in range(self.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                        if '.!combobox' in str(self.button_group[row][i]):
                            self.button_group[row][i].configure(state = 'normal')
                    for i in range(self.get_range(self.button_group[row][3].get(), 2), len(self.button_group[row])):
                        self.button_group[row][i].destroy()
                    del self.button_group[row][self.get_range(self.button_group[row][3].get(), 2):]
                
        self.add = add
        self.remove = remove
        self.window = None
        self.text_code = None
        self.button_add = None
        self.button_start = None
        self.button_clear = None
        self.button_group = []
        self.step = []
        self.row_id = 1

    def main(self):
        self.window = tk.Tk()
        self.window.title('VgPro代码生成器')
        self.window.geometry('1372x756')

        text_code_description = tk.Label(self.window, text = '卡号：')
        text_code_description.grid(row = 0, column = 0)
        self.text_code = tk.Entry(self.window, width = 8)
        self.text_code.grid(row = 0, column = 1)
        self.text_code.bind('<Key>', other.only_numbers)
        self.button_add = tk.Button(self.window, text = '+', command = lambda: self.add.row())
        self.button_add.grid(row=1, column=0)
        self.button_start = tk.Button(self.window, text = '点击生成', command = lambda: self.start())
        self.button_start.grid(row = 2, column = 0)
        self.button_clear = tk.Button(self.window, text = '清空', command = lambda: self.clear())
        self.button_clear.grid(row = 2, column = 1)

        self.window.mainloop()

    def get_range(self, selected, step):
        if step == 1:
            return 4
        if step == 2:
            if '【自】' in selected:
                return 13
            elif '【起】' in selected:
                return 9
            elif '【永】' in selected:
                return 8
        
    def clear(self):
        if len(self.text_code.get()) > 0:
            self.text_code.delete(0, tk.END)
        for i in range(0, len(self.button_group)):
            for j in range(0, len(self.button_group[i])):
                self.button_group[i][j].destroy()

    def start(self):
        if len(self.text_code.get()) <= 0:
            return
        content = '--made by vgpro_script_maker\nlocal cm,m,o=GetID()\nfunction cm.initial_effect(c)\n\tvgf.VgCard(c)'
        content += '\nend'
        create_script.write_script(self.text_code.get(), content)

class new_window:
    def __init__(self):
        class add:
            def button_main(func):
                if len(self.button_group[0][0].get()) == 0:
                    return
                if func == 'val':
                    self.button_group[0][0].configure(state = 'disable')
                    if '数值' in self.button_group[0][0].get():
                        description = tk.Label(self.window, text = '力量+')
                        description.grid(row = 1, column = 0)
                        text = tk.Entry(self.window, width = 8)
                        text.grid(row = 1, column = 1)
                        text.bind('<Key>', other.only_numbers)
                        self.button_group.append([description, text])
                    elif '预设函数' in self.button_group[0][0].get():
                        self.button_group.append([])
                        button = tk.Button(self.window, text = '+', command = lambda: self.add.card_filter_group())
                        button.grid(row = 3, column = 1)
                        self.button_group[1].append(button)
                        pull_down = Combobox(self.window, width = 5)
                        pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【纹章区】', '【伤害区】', '【封锁区】')
                        pull_down.grid(row = 1, column = 0)
                        self.button_group[1].append(pull_down)
                        description = tk.Label(self.window, text = '的卡每有1张')
                        description.grid(row = 1, column = 1)
                        self.button_group[1].append(description)
                        description = tk.Label(self.window, text = '力量+')
                        description.grid(row = 1, column = 2)
                        self.button_group[1].append(description)
                        text = tk.Entry(self.window, width = 8)
                        text.grid(row = 1, column = 3)
                        text.bind('<Key>', other.only_numbers)
                        self.button_group[1].append(text)
                        description = tk.Label(self.window, text = '(卡片过滤器)：')
                        description.grid(row = 2, column = 0)
                        self.button_group[1].append(description)
                    elif '自定函数' in self.button_group[0][0].get():
                        description_I = tk.Label(self.window, text = 'function (e,tp,eg,ep,ev,re,r,rp)')
                        description_I.grid(row = 1, column = 0)
                        text = tk.Text(self.window, width = 50, height=10)
                        text.grid(row = 2, column = 0)
                        description_II = tk.Label(self.window, text = 'end')
                        description_II.grid(row = 3, column = 0)
                        self.button_group.append([description_I, text, description_II])

            def card_filter_group():
                row = self.button_group[1][0].grid_info()['row']
                column = self.button_group[1][0].grid_info()['column']
                self.button_group[1][0].grid(row = row + 1, column = column)
                button = tk.Button(self.window, text = '-', command = lambda: self.remove.card_filter_group(button.grid_info()['row']))
                button.grid(row = row, column = column)
                self.button_group.append([])
                self.button_group[row - 1].append([button])
                button = tk.Button(self.window, text = '+', command = lambda: self.add.card_filter(button.grid_info()['row'], button.grid_info()['column']))
                self.button_group[row - 1][0].append(button)
                button = tk.Button(self.window, text = '-', command = lambda: self.remove.card_filter(button.grid_info()['row']))
                self.button_group[row - 1][0].append(button)
                self.add.card_filter(row, column + 1)
                print(self.button_group)

            def card_filter(row, column):
                def is_button(i):
                    return not isinstance(i, str)
                t = []
                pull_down = Combobox(self.window, width = 8)
                if len(self.button_group) >= row - 1:
                    pull_down['values'] = ('and' ,'or', 'not', 'and not', 'or not')
                else:
                    pull_down['values'] = ('not')
                pull_down.grid(row = row, column = column)
                t.append(pull_down)
                pull_down = Combobox(self.window, width = 8)
                pull_down['values'] = ('1')
                t.append(pull_down)
                pull_down.grid(row = row, column = column + 1)
                description = tk.Label(self.window, text = '参数')
                description.grid(row = row, column = column + 2)
                t.append(description)
                text = tk.Entry(self.window, width = 8)
                text.grid(row = row, column = column + 3)
                t.append(text)
                self.button_group[row - 1].append(t)
                self.button_group[row - 1][0][1].grid(row = row, column = column + 4)
                self.button_group[row - 1][0][2].grid(row = row, column = column + 5)
                print(column + 4)

        class remove:
            def button_main():
                self.button_group[0][0].configure(state = 'normal')
                for i in range(1, len(self.button_group)):
                    for j in range(0, len(self.button_group[i])):
                        if isinstance(self.button_group[i][j], list):
                            for button in self.button_group[i][j]:
                                button.destroy()
                        else:
                            self.button_group[i][j].destroy()
                self.button_group = [self.button_group[0]]

            def card_filter_group(row):
                for group in self.button_group[row - 1]:
                    for button in group:
                        button.destroy()
                del self.button_group[row - 1]
                ct = 0
                for i in range(row - 1, len(self.button_group)):
                    if i <= 1:
                        continue
                    ct += 1
                    for j in range(0, len(self.button_group[i])):
                        for button in self.button_group[i][j]:
                            button.grid(row = button.grid_info()['row'] - 1, column = button.grid_info()['column'])
                self.button_group[1][0].grid(row = row + ct, column = 1)

            def card_filter(row):
                for button in self.button_group[row - 1][len(self.button_group[row - 1]) - 1]:
                    button.destroy()
                del self.button_group[row - 1][len(self.button_group[row - 1]) - 1]
                if len(self.button_group[row - 1]) == 1:
                    self.remove.card_filter_group(row)
                else:
                    column = (len(self.button_group[row - 1]) - 1) * 5 + 1
                    self.button_group[row - 1][0][1].grid(row = self.button_group[row - 1][0][1].grid_info()['row'], column = column)
                    self.button_group[row - 1][0][2].grid(row = self.button_group[row - 1][0][2].grid_info()['row'], column = column + 1)

        self.window = None
        self.button_group = []
        self.add = add
        self.remove = remove
        
    def main(self, row, column, func):
        self.window = tk.Toplevel()
        self.window.title('VgPro代码生成器')
        self.window.geometry('980x540')
        pull_down = Combobox(self.window, width = 8)
        pull_down['values'] = (self.select_list(func))
        pull_down.grid(row = 0, column = 0)
        button_add = tk.Button(self.window, text = '+', command = lambda: self.add.button_main(func))
        button_add.grid(row = 0, column = 1)
        button_clear = tk.Button(self.window, text = '-', command = lambda: self.remove.button_main())
        button_clear.grid(row = 0, column = 2)
        button_submit = tk.Button(self.window, text = '提交', command = lambda: self.submit())
        button_submit.grid(row = 0, column = 3)
        self.button_group.append([pull_down, button_add, button_clear, button_submit])

    def submit(self):
        print('submit')
    
    def select_list(self, func):
        if func == 'val':
            return ['数值', '预设函数', '自定函数']

class other:
    def only_numbers(event):
        print(event)
        if event.keysym == 'Right'or event.keysym == 'Left' or event.keysym in ('BackSpace', 'Delete'):
            return 'continueretain'
        if not re.match(r'^[0-9]+$', event.char):
            return 'break'
        return 'continueretain'

def main():
    main_window().main()

main()