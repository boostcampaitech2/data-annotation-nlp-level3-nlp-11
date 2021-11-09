import os
import pandas as pd
from tqdm import tqdm
from pororo import Pororo

class SentenceNer:
    def __init__(self,args) -> None:
        self.args = args
        self.csv_path = args.output_dir + args.raw_csv 
        self.run_ner()

    def get_csv(self,csv_path=None):
        if csv_path == None:
            csv_path = self.csv_path
        return pd.read_csv(csv_path)
    

    def run_ner(self,entity_csv=None):
        if entity_csv==None:
            entity_csv = self.args.entity_csv

        df = self.get_csv()
        ner = Pororo(task="ner", lang="ko",apply_wsd=self.args.use_applywsd)

        total_array = []
        for i,sentence in enumerate(tqdm(df["sentence"])):
            result = ner(sentence)
            tmp_array = []
            count_O = 0
            for word_entity in result:
                if word_entity[1] == 'O':
                    count_O+=1
                    continue
                tmp = {}
                tmp["word"] = word_entity[0]
                tmp["type"] = word_entity[1]
                tmp["start"] = sentence.find(word_entity[0])
                tmp_array.append(tmp)
            if len(tmp_array) >= 2 and count_O!=0:
                total_array.append(tmp_array)
            else:
                total_array.append([])

        tmp_df = pd.concat([df,pd.DataFrame({"entity":total_array})],axis=1)
        tmp_df.to_csv(self.args.output_dir + self.args.entity_csv,index=False)