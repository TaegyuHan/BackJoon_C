import sys
# sys.stdin = open("./14470.txt")
key_list = [
    "cur_temperatuer",
    "wount_temperatuer",
    "ice_up",
    "cur_ice",
    "un_ice_up"    
]
T = {}
for key in key_list:
    T[key] = int(sys.stdin.readline()) 

if T["cur_temperatuer"] < 0:
    print((abs(T["cur_temperatuer"]) * T["ice_up"]) + T["cur_ice"] + (T["wount_temperatuer"] * T["un_ice_up"]))
elif T["cur_temperatuer"] > 0:
    print((T["wount_temperatuer"] - T["cur_temperatuer"]) * T["un_ice_up"])