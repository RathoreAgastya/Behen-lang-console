"""
Behen-lang v0.0.0
Copyright (c) - RathoreAgastya, Coolstormaction (Github) 2022
All rights reserved.
"""

from rich.console import Console
from error_handler import StructureError, IndentError, ValueException, ArgError, NotDefinedException
import functoolsbh as tools, sys

console = Console()
command_list = ["trigger behen", "bye behen"]
variables = list(tools.allocate.keys())
console.print("helo, bhaio. [red3]Ye language beheno ke lea nahi he.[/] made with [red3]:heart:[/]  by agastya and debarka bhai\n")

def process_code():
    global command_list
    try:
        command_list.remove("trigger behen")
        command_list.remove("bye behen")
    except Exception: pass

    for idx, i in enumerate(command_list):
        if i.startswith("behen ye hai "):
            spl = i.split()
            if len(spl) < 3: raise StructureError("Variable name and value required.")
            if len(spl) > 3 and not spl.__contains__('='): raise StructureError("Variable value required.")
            if len(spl) == 6 and spl.__contains__('='): tools.allocate_data(spl[3], spl[5])
        if i.startswith('bol behen '):
            spl = i.split() 
            if len(spl) < 3: raise StructureError("String not given for task.")
            if len(spl) > 3: spl = [' '.join(spl[2:len(spl)])]; print(' '.join(spl[:2]).replace("'", ''))
            if len(spl) == 3 and spl[2].startswith("'") and spl[len(spl) - 1].endswith("'") or spl[-1].isnumeric() or spl[-1].__contains__('.') and spl[-1].count('.') == 1: spl = [' '.join(spl[2:len(spl)])]; print(' '.join(spl[:2]).replace("'", ''))
            if len(spl) == 3 and spl[-1].count('.') > 1: raise ValueException("Float value cannot contain more than 1 decimal points.")
            if len(spl) == 3 and not spl[2].startswith("'") or not spl[len(spl) - 1].endswith("'"):
                for k, v in tools.allocate.items(): 
                    if k == spl[-1]: print(tools.allocate[k].replace("'", ''))
                    else: raise NotDefinedException("Variable not defined.")

            if len(spl) == 3 and spl[2].startswith("'") and spl[len(spl) - 1].endswith("'") and spl.endswith(variables):
                for key, value in tools.allocate.items():
                    if key == spl[-1]: print(tools.allocate[key].replace("'", ''))
                    else: raise NotDefinedException("Variable not defined.")

        

console.print("apna code yaha likhe bhai [red3]:heart:[/]\n")

def save_progress(c : list, name):
    with open(name, "w") as f:
        f.write(f"{c}\n")

while True:
    line = input()
    if line != "run":
        command_list.append(line)

    else:
        saveProgress = console.input("Do you want to save your code/progress? Y/N - ")
        if saveProgress.lower() == "y":
            fname = console.input("Please enter a filename - ")
            if fname.endswith(".bl"): console.print("Thanks for your confirmation"); save_progress(command_list, fname); process_code(); break
            else: fname += ".bl"; console.print("Thanks for your confirmation"); save_progress(command_list, fname); process_code(); break
        else : process_code(); break
