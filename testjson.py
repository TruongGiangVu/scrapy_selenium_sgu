import json

with open('data\\point.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data.sort(key=lambda x: x['point'], reverse=True)

# ------- rank all -------------
# rank = 0
# maxpoint = 4.1
# count = 1
# for index, student in enumerate(data):
#     point = float(student['point'])
#     if(point < maxpoint):
#         maxpoint = point
#         rank = rank + count
#         count = 1
#     else:
#         count = count + 1
#     student['rank'] = rank
# with open('data\\sort.json', 'w', encoding='utf-8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False)

# ------- rank by class -------------
listclass = []
classid = 'DCT1171'  # choose class
rank = 0
maxpoint = 4.1
count = 1
for index, student in enumerate(data):
    if(student['class'] == classid):
        point = float(student['point'])
        if(point < maxpoint):
            maxpoint = point
            rank = rank + count
            count = 1
        else:
            count = count + 1
        student['rank'] = rank
        listclass.append(student)

file = 'data\\rank_9{}.json'.format(classid)

with open(file, 'w', encoding='utf-8') as outfile:
    json.dump(listclass, outfile, ensure_ascii=False)
