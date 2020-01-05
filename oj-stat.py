import json
from importlib import import_module
import prettytable as pt

'''
Statcode:
AC 1
PE 2
WA 3
OLE 4
TLE 5
MLE 6
RE 7
CE 8
JE 9
NONE 10
ERR 11
UNV 12
'''

def change_statcode_to_str(statcode):
    maps = ["","AC","PE","WA","OLE","TLE","MLE","RE","CE","JE","NONE","ERR","UNV"]
    return maps[statcode]

config = {}
with open("config.json","r") as f:
    try:
        config = json.loads(f.read())
    except json.decoder.JSONDecodeError as e:
        print("[Error] can't parse config file.")
        print(e)
        exit()

#result_table = []
oj_class = {}
problems = []
ojlist = []

for oj in config["ojlist"]:
    try:
        oj_class[oj] = import_module("oj."+oj)
    except ImportError:
        print("[Error] no module name: "+oj)
    else:
        ojlist.append(oj)

for problem in config["problems"]:
    if ":" not in problem:
        print("[Error] problem name format error: "+problem)
        continue
    oj = problem.split(":")[0]
    pid = problem.split(":")[1]
    if not oj in ojlist:
        print("[Error] OJ not found: "+oj+" in "+problem)
        continue
    problems.append({"oj":oj,"pid":pid})

result_table = pt.PrettyTable(["Name"]+[problem for problem in [p["oj"]+":"+p["pid"] for p in problems]])
#result_table.field_names = ["Name"]
'''
for problem in config["problems"]:
    result_table.field_names.append(problem)
'''

for user in config["users"]:
    user_res = [user["name"]]
    for problem in problems:
        oj = problem["oj"]
        pid = problem["pid"]
        user_oj = user["oj"][oj]
        if user_oj == "":
            user_res.append("-")
            continue
        stat = oj_class[oj].get_stat(user_oj,pid)
        user_res.append(change_statcode_to_str(stat))
        '''
        if stat:
            user_res.append("Yes")
        else:
            user_res.append("No")
            '''
    result_table.add_row(user_res)

print(result_table)
