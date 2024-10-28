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
                    pull_down = Combobox(window)
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
                    print(self.button_group)
                    
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
                            description = tk.Label(window, text = '发动位置：')
                            description.grid(row = row + 1, column = 2)
                            pull_down = Combobox(window)
                            pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【G】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                            pull_down.grid(row = row + 1, column = 3)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                        else:
                            description = tk.Label(window, text = '发动位置：')
                            description.grid(row = row + 1, column = 2)
                            pull_down = Combobox(window)
                            pull_down['values'] = ('【V】', '【R】', '【后列的R】', '【前列的R】', '【V/R】', '【手牌】', '【灵魂】 ', '【弃牌区】', '【指令区】', '【封锁区】')
                            pull_down.grid(row = row + 1, column = 3)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            
                        if '【永】' in self.button_group[row][3].get():
                            description = tk.Label(window, text = '影响：')
                            description.grid(row = row + 1, column = 4)
                            pull_down = Combobox(window)
                            pull_down['values'] = ('影响自己', '影响所有卡')
                            pull_down.grid(row = row + 1, column = 5)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                        elif '【自】' in self.button_group[row][3].get():
                            description = tk.Label(window, text = '触发：')
                            description.grid(row = row + 1, column = 4)
                            pull_down = Combobox(window)
                            pull_down['values'] = ('自己状态变化时触发', '所有卡状态变化时触发')
                            pull_down.grid(row = row + 1, column = 5)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                            
                        if '【自】' in self.button_group[row][3].get():
                            description = tk.Label(window, text = '时点：')
                            description.grid(row = row + 1, column = 6)
                            pull_down = Combobox(window)
                            pull_down['values'] = ('自己状态变化时触发', '场上所有卡状态变化时触发')
                            pull_down.grid(row = row + 1, column = 7)
                            self.button_group[row].append(description)
                            self.button_group[row].append(pull_down)
                    elif self.step[row] == 1:
                        for i in range(4, len(self.button_group[row])):
                            if '.!combobox' in str(self.button_group[row][i]):
                                if len(self.button_group[row][i].get()) == 0:
                                    return
                        self.step[row] += 1
                        for i in range(4, len(self.button_group[row])):
                            if '.!combobox' in str(self.button_group[row][i]):
                                self.button_group[row][i].configure(state = 'disable')
                        description = tk.Label(window, text = '费用：')
                        description.grid(row = row + 1, column = 6)
                        pull_down = Combobox(window)
                        pull_down['values'] = ('自己状态变化时触发', '场上所有卡状态变化时触发')
                        pull_down.grid(row = row + 1, column = 7)
                        self.button_group[row].append(description)
                        self.button_group[row].append(pull_down)

                    self.button_group[row][1].grid(row = row + 2, column = len(self.button_group[row]) - 2)
                    self.button_group[row][2].grid(row = row + 2, column = len(self.button_group[row]) - 1)
                    print("选中的值:", self.button_group[row][3].get())

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
                    print(self.button_group)
                    
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
                        for i in range(4, len(self.button_group[row])):
                            self.button_group[row][i].destroy()
                        del self.button_group[row][4:]
                    
            self.add = add
            self.remove = remove
            self.button_add = button_add
            self.button_start = button_start
            self.button_clear = button_clear
            self.button_group = []
            self.step = []
            self.row_id = 1
             
        def lock_pull_down_list(self, row, i):
            print(self.step[row], i) 

        def only_numbers(event):
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
            content = 'local cm,m,o=GetID()\nfunction cm.initial_effect(c)\n\tvgf.VgCard(c)'
            content += '\nend'
            create_script.write_script(text_code.get(), content)

    window = tk.Tk()
    window.title('VgPro代码生成器')
    window.geometry('1000x600')

    text_code_description = tk.Label(window, text = '卡号：')
    text_code_description.grid(row = 0, column = 0)
    text_code = tk.Entry(window)
    text_code.grid(row = 0, column = 1)
    text_code.bind('<Key>', button_function.only_numbers)

    button_function = button_function(button_add = tk.Button(window, text = '+', command = lambda: button_function.add.row()), button_start = tk.Button(window, text = '点击生成', command = lambda: button_function.start()), button_clear = tk.Button(window, text = '清空', command = lambda: button_function.clear()))
    button_function.button_add.grid(row=1, column=0)
    
    button_function.button_start.grid(row = 2, column = 0)
    button_function.button_clear.grid(row = 2, column = 1)

    window.mainloop()
    
main()