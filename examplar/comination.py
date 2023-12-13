import pandas as pd
import numpy as np
import itertools
import tkinter as tk

class combination:
    def __init__(self):
        self.collection = {
            'name': ['adarsha', 'vinay', 'Amith', 'janani'],
            'age': [20, 21, 22, 23],
            'adress': ['mulluru', 'lakshmipuram', 'vijaynagar', 'mulluru']
        }

        self.df = pd.DataFrame(self.collection)

        self.df_name = self.df.loc[:, 'name']
        self.df_adress = self.df.loc[:, 'adress']
        self.df_tool = self.df[['name', 'adress']]

        self.lists = self.df_tool.values.tolist()

        self.unique_list = []
        for item in self.lists:
            for ele in item:
                if ele not in self.unique_list:
                    self.unique_list.append(ele)

        self.result = {}
        for itr in range(0, len(self.unique_list)):
            sets = set()
            for items in self.lists:
                if self.unique_list[itr] in items:
                    sets.update(items)
            self.result[self.unique_list[itr]] = sets

    def combinator(self, item):
        related_items = self.result[item]
        possible_list = []
        for i in range(1, len(related_items) + 1):
            possible_list.extend(itertools.combinations(related_items, i))
        return possible_list

    def funct_to_convert(self, combinations):
        root = tk.Tk()
        frame = tk.Frame(root)

        frame.pack()

        for item in combinations:
            set_items = ', '.join(item)
            label = tk.Label(frame, text=set_items)
            label.pack()

        root.mainloop()

# This block will only run if this script is executed directly, not if it's imported as a module
if __name__ == "__main__":
    cmb = combination()
    combinations_data = cmb.combinator("adarsha")
    cmb.funct_to_convert(combinations_data)
