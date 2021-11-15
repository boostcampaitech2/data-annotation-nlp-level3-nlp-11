import json
import os
import pandas as pd

with open('annotations-legend.json', "r") as j:
    annotation_info = json.load(j)

path_html = './plain.html/pool/'
path_json = './ann.json/master/pool'

dir_list = os.listdir(path_json)

jk = 0

datafordf = []
for folder in dir_list:
    if folder[0] == '.':
        continue
    now_json = os.path.join(path_json,folder)
    now_html = os.path.join(path_html,folder)
    
    file_list = os.listdir(now_json)
    for file_name in file_list:
        if file_name[0] == '.' or file_name[-4:] != 'json':
            continue
        json_name = os.path.join(now_json,file_name)
        html_name = os.path.join(now_html,'.'.join(file_name.split('.')[:-2]))+'.plain.html'
        
        with open(json_name,'r') as j:
            data_info = json.load(j)
        
        
        with open(html_name, 'r') as j:
            sentence = j.readlines()
            sentence = ''.join(sentence).split('content')[2]
            sentence = sentence.replace('&quot;','"')
        
            sentence = sentence.split('</pre>')[0]
            sentence = sentence.split('>')[2]
  
        if len(data_info['entities']) != 2:
            print('==============')
            print('엔티티 수가 이상함')
            print(sentence)
            print('================')
            continue
        nowdic = {'sentence' : None, 'OBJ' : '', 'SUB' : '' } 
        for i in range(2):
            info = data_info['entities'][i]
            offset_info = info['offsets'][0]
            start = offset_info['start'] + i*7
            end = start + len(offset_info['text'])
            entity_type = annotation_info[info['classId']].split('_')
            nowdic[entity_type[0]] = entity_type[1]
            if offset_info['text'] != sentence[start:end]:
                print('=======코드 처리 필요: 이것들의 위치가 맞지 않음==========')
                print(start,end,sentence[start:end],"|||||||",offset_info['text'])
                print(sentence)
                break
            sentence = sentence[:start] + f'<{entity_type[0]} :{offset_info["text"]}>' + sentence[end:]
        nowdic['sentence'] = sentence
        datafordf.append(nowdic)

        
df = pd.DataFrame(datafordf)
df.to_csv('output.csv')

print('Done')