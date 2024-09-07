def find_nth_occurrence(string, char, nth):
    count = 0
    for i, char_ in enumerate(string):
        if char_ == char:
            count+=1
        if count == nth:
            return i
        
with open('text.txt', 'r') as file:
    res = file.read()
    
arr_res = res.split('}')
# print(arr_res[74:88])
result = ''
for txt in arr_res:
    try:
        colin_ind = find_nth_occurrence(txt, ':', 5)
        stop_ind = txt[colin_ind+2:].find('"')
        # print(colin_ind)
        # print(stop_ind)
        # print(txt[colin_ind+2:colin_ind+2+stop_ind])
        result = result+ txt[colin_ind+2:colin_ind+2+stop_ind]
        # print(txt.index('"'))
    except TypeError:
        break
        

result = result.replace(r'\n', "\n")
print(result)