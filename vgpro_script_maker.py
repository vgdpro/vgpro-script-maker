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

def main():
    class button_function:
        def __init__(self, button_add, button_start, button_clear):
            class add:
                def row():
                    self.step.append(0)
                    self.button_group.append([])
                    button_function.remove.button_main()
                    button = tk.Button(window, text = '-', command = lambda: button_function.remove.row(button.grid_info()['row'] - 1))
                    button.grid(row = self.row_id, column = 0)
                    self.button_group[self.row_id - 1].append(button)
                    pull_down = Combobox(window, width = 5)
                    pull_down['values'] = ('【自】', '【起】', '【永】')
                    pull_down.configure(state = 'normal')
                    pull_down.grid(row = self.row_id, column = 1)
                    button_add = tk.Button(window, text = '+', command = lambda: button_function.add.button_input(button.grid_info()['row'] - 1))
                    self.button_group[self.row_id - 1].append(button_add)
                    button_remove = tk.Button(window, text = '-', command = lambda: button_function.remove.button_input(button.grid_info()['row'] - 1))
                    self.button_group[self.row_id - 1].append(button_remove)
                    self.button_group[self.row_id - 1].append(pull_down)
                    button_add.grid(row = self.row_id, column = len(self.button_group[self.row_id - 1]) - 2)
                    button_remove.grid(row = self.row_id, column = len(self.button_group[self.row_id - 1]) - 1)
                    self.row_id += 1
                    button_function.add.button_main()
                    
                def button_main():
                    self.button_add = tk.Button(window, text = '+', command = lambda: button_function.add.row())
                    self.button_add.grid(row = self.row_id, column = 0)
                    self.button_start = tk.Button(window, text = '点击生成', command = lambda: button_function.start())
                    self.button_start.grid(row = self.row_id + 1, column = 0)
                    self.button_clear = tk.Button(window, text = '清空', command = lambda: button_function.clear())
                    self.button_clear.grid(row = self.row_id + 1, column = 1)
                    
                def button_input(row):
                    if self.step[row] == 0:
                        if len(self.button_group[row][3].get()) == 0:
                            return
                        self.step[row] += 1
                        self.button_group[row][3].configure(state = 'disable')
                        if '【永】' in self.button_group[row][3].get():
                            description = tk.Label(window, text = '区域：')
                            description.grid(row = row + 1, column = 2)
                            pull_down = Combobox(window, width = 9)
                            pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【G】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                            pull_down.grid(row = row + 1, column = 3)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            description = tk.Label(window, text = '影响：')
                            description.grid(row = row + 1, column = 4)
                            pull_down = Combobox(window, width = 7)
                            pull_down['values'] = ('影响自己', '影响所有卡')
                            pull_down.grid(row = row + 1, column = 5)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                        elif '【自】' in self.button_group[row][3].get():
                            description = tk.Label(window, text = '区域：')
                            description.grid(row = row + 1, column = 2)
                            pull_down = Combobox(window, width = 9)
                            pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                            pull_down.grid(row = row + 1, column = 3)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            description = tk.Label(window, text = '触发：')
                            description.grid(row = row + 1, column = 4)
                            pull_down = Combobox(window, width = 15)
                            pull_down['values'] = ('自己状态变化时触发', '所有卡状态变化时触发')
                            pull_down.grid(row = row + 1, column = 5)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            description = tk.Label(window, text = '时点：')
                            description.grid(row = row + 1, column = 6)
                            pull_down = Combobox(window, width = 15)
                            pull_down['values'] = ('自己状态变化时触发', '场上所有卡状态变化时触发')
                            pull_down.grid(row = row + 1, column = 7)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            description_I = tk.Label(window, text = '1回合')
                            description_I.grid(row = row + 1, column = 8)
                            pull_down = Combobox(window, width = 5)
                            pull_down['values'] = ('不限', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                            pull_down.grid(row = row + 1, column = 9)
                            description_II = tk.Label(window, text = '次')
                            description_II.grid(row = row + 1, column = 10)
                            self.button_group[row].append(description_I)
                            self.button_group[row].append(pull_down)
                            self.button_group[row].append(description_II)
                        elif '【起】' in self.button_group[row][3].get():
                            description = tk.Label(window, text = '区域：')
                            description.grid(row = row + 1, column = 2)
                            pull_down = Combobox(window, width = 9)
                            pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                            pull_down.grid(row = row + 1, column = 3)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            description_I = tk.Label(window, text = '1回合')
                            description_I.grid(row = row + 1, column = 4)
                            pull_down = Combobox(window, width = 5)
                            pull_down['values'] = ('不限', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                            pull_down.grid(row = row + 1, column = 5)
                            description_II = tk.Label(window, text = '次')
                            description_II.grid(row = row + 1, column = 6)
                            self.button_group[row].append(description_I)
                            self.button_group[row].append(pull_down)
                            self.button_group[row].append(description_II)

                    elif self.step[row] == 1:
                        for i in range(button_function.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                            if '.!combobox' in str(self.button_group[row][i]):
                                if len(self.button_group[row][i].get()) == 0:
                                    return
                        self.step[row] += 1
                        for i in range(button_function.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                            if '.!combobox' in str(self.button_group[row][i]):
                                self.button_group[row][i].configure(state = 'disable')

                        if '【永】' in self.button_group[row][3].get():
                            button = tk.Button(window, text = '数值', command = lambda: button_function.add.new_function(row, 7, 'val'))
                            button.grid(row = row + 1, column = 6)
                            text = tk.Entry(window, width = 5)
                            text.configure(state = 'disable')
                            text.grid(row = row + 1, column = 7)
                            self.button_group[row].append(button)
                            self.button_group[row].append(text)
                            button = tk.Button(window, text = '场合', command = lambda: button_function.new_function(row, 9, 'con'))
                            button.grid(row = row + 1, column = 8)
                            text = tk.Entry(window, width = 5)
                            text.configure(state = 'disable')
                            text.grid(row = row + 1, column = 9)
                            self.button_group[row].append(button)
                            self.button_group[row].append(text)
                            if '影响所有卡' in self.button_group[row][7].get():
                                description = tk.Label(window, text = '影响的自己区域：')
                                description.grid(row = row + 1, column = 10)
                                pull_down = Combobox(window, width = 5)
                                pull_down['values'] = ('【V】', '【R】', '【V/R】')
                                pull_down.grid(row = row + 1, column = 11)
                                self.button_group[row].append(description)
                                self.button_group[row].append(pull_down)
                                description = tk.Label(window, text = '影响的对手区域：')
                                description.grid(row = row + 1, column = 12)
                                pull_down = Combobox(window, width = 5)
                                pull_down['values'] = ('【V】', '【R】', '【V/R】')
                                pull_down.grid(row = row + 1, column = 13)
                                self.button_group[row].append(description)
                                self.button_group[row].append(pull_down)
                                button = tk.Button(window, text = '目标筛选', command = lambda: button_function.new_function(row, 15, 'tg'))
                                button.grid(row = row + 1, column = 14)
                                text = tk.Entry(window, width = 5)
                                text.configure(state = 'disable')
                                text.grid(row = row + 1, column = 15)
                                self.button_group[row].append(button)
                                self.button_group[row].append(text)

                    self.button_group[row][1].grid(row = row + 1, column = len(self.button_group[row]) - 2)
                    self.button_group[row][2].grid(row = row + 1, column = len(self.button_group[row]) - 1)
                
                def new_function(row, column, func):
                    new_window = tk.Toplevel()
                    new_window.title('VgPro代码生成器')
                    new_window.geometry('980x540')
                    button_group = []
                    def submit():
                        print('submit')

                    def clear():
                        button_group[0][0].configure(state = 'normal')
                        for i in range(1, len(button_group)):
                            for button in button_group[i]:
                                button.destroy()
                        del button_group[1]
                    if func == 'val':
                        def add_button():
                            if len(button_group[0][0].get()) == 0:
                                return
                            button_group[0][0].configure(state = 'disable')
                            if '数值' in button_group[0][0].get():
                                description = tk.Label(new_window, text = '力量+')
                                description.grid(row = 1, column = 0)
                                text = tk.Entry(new_window, width = 8)
                                text.grid(row = 1, column = 1)
                                text.bind('<Key>', button_function.only_numbers)
                                button_group.append([description, text])
                            elif '预设函数' in button_group[0][0].get():
                                button_group.append([])
                                pull_down = Combobox(new_window, width = 5)
                                pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【纹章区】', '【伤害区】', '【封锁区】')
                                pull_down.grid(row = 1, column = 0)
                                button_group[1].append(pull_down)
                                description = tk.Label(new_window, text = '的卡每有1张')
                                description.grid(row = 1, column = 1)
                                button_group[1].append(description)
                                description = tk.Label(new_window, text = '(卡片过滤器)：')
                                description.grid(row = 1, column = 2)
                                button_group[1].append(description)
                                button_I = tk.Button(new_window, text ='+', command = lambda: add_filter())
                                button_I.grid(row = 1, column = 3)
                                button_II = tk.Button(new_window, text ='-', command = lambda: remove_filter())
                                button_II.grid(row = 1, column = 4)
                                button_group.append([button_I, button_II])
                                description = tk.Label(new_window, text = '力量+')
                                description.grid(row = 2, column = 0)
                                button_group[1].append(description)
                                text = tk.Entry(new_window, width = 8)
                                text.grid(row = 2, column = 1)
                                text.bind('<Key>', button_function.only_numbers)
                                button_group[1].append(text)
                            elif '自定函数' in button_group[0][0].get():
                                description_I = tk.Label(new_window, text = 'function (e,tp,eg,ep,ev,re,r,rp)')
                                description_I.grid(row = 1, column = 0)
                                text = tk.Text(new_window, width = 50, height=10)
                                text.grid(row = 2, column = 0)
                                description_II = tk.Label(new_window, text = 'end')
                                description_II.grid(row = 3, column = 0)
                                button_group.append([description_I, text, description_II])

                        def add_filter():
                            return

                        def remove_filter():
                            return

                        pull_down = Combobox(new_window, width = 8)
                        pull_down['values'] = ('数值', '预设函数', '自定函数')
                        pull_down.grid(row = 0, column = 0)
                        button_add = tk.Button(new_window, text = '+', command = lambda: add_button())
                        button_add.grid(row = 0, column = 1)
                        button_submit = tk.Button(new_window, text = '提交', command = lambda: submit())
                        button_submit.grid(row = 0, column = 2)
                        button_clear = tk.Button(new_window, text = '清空', command = lambda: clear())
                        button_clear.grid(row = 0, column = 3)
                        button_group.append([pull_down, button_add, button_submit, button_clear])

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
                    button_function.remove.button_main()
                    button_function.add.button_main()
                    
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
                        for i in range(button_function.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                            self.button_group[row][i].destroy()
                        del self.button_group[row][button_function.get_range(self.button_group[row][3].get(), 1):]
                    if self.step[row] == 2:
                        self.step[row] -= 1
                        for i in range(button_function.get_range(self.button_group[row][3].get(), 1), len(self.button_group[row])):
                            if '.!combobox' in str(self.button_group[row][i]):
                                self.button_group[row][i].configure(state = 'normal')
                        for i in range(button_function.get_range(self.button_group[row][3].get(), 2), len(self.button_group[row])):
                            self.button_group[row][i].destroy()
                        del self.button_group[row][button_function.get_range(self.button_group[row][3].get(), 2):]
                    
            self.add = add
            self.remove = remove
            self.button_add = button_add
            self.button_start = button_start
            self.button_clear = button_clear
            self.button_group = []
            self.step = []
            self.row_id = 1
             
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

        def only_numbers(event):
            print(event)
            if event.keysym == 'Right'or event.keysym == 'Left' or event.keysym in ('BackSpace', 'Delete'):
                return 'continueretain'
            if not re.match(r'^[0-9]+$', event.char) or len(text_code.get()) >= 8:
                return 'break'
            return 'continueretain'
            
        def clear(self):
            if len(text_code.get()) > 0:
                text_code.delete(0, tk.END)
            for i in range(0, len(self.button_group)):
                for j in range(0, len(self.button_group[i])):
                    self.button_group[i][j].destroy()

        def start(self):
            if len(text_code.get()) <= 0:
                return
            content = '--made by vgpro-script-maker\nlocal cm,m,o=GetID()\nfunction cm.initial_effect(c)\n\tvgf.VgCard(c)'
            content += '\nend'
            create_script.write_script(text_code.get(), content)

    window = tk.Tk()
    window.title('VgPro代码生成器')
    window.geometry('1372x756')

    text_code_description = tk.Label(window, text = '卡号：')
    text_code_description.grid(row = 0, column = 0)
    text_code = tk.Entry(window, width = 8)
    text_code.grid(row = 0, column = 1)
    text_code.bind('<Key>', button_function.only_numbers)

    button_function = button_function(button_add = tk.Button(window, text = '+', command = lambda: button_function.add.row()), button_start = tk.Button(window, text = '点击生成', command = lambda: button_function.start()), button_clear = tk.Button(window, text = '清空', command = lambda: button_function.clear()))
    button_function.button_add.grid(row=1, column=0)
    
    button_function.button_start.grid(row = 2, column = 0)
    button_function.button_clear.grid(row = 2, column = 1)

    window.mainloop()
    
main()