import pandas as pd
import math

class GetSentencenly:
    def __init__(self,args) -> None:
        self.args = args
        self.entity_csv_path = args.output_dir + args.entity_csv
        name = args.entity_csv.split('.')[0]
        self.entity_sentenc_result_path = args.output_dir + name + '_sentence.csv'
        self.get_sentence()
        

    def get_sentence(self):
        df = pd.read_csv(self.entity_csv_path)
        df["sentence"].to_csv(self.entity_sentenc_result_path,index=False,encoding="utf-8-sig")

    def split_sentence(self,n):
        df = pd.read_csv(self.entity_sentenc_result_path)
        amount = int(math.ceil(len(df)/n))
        for i in range(n):
            start_index = i*amount
            end_index = ((i+1)*amount) -1
            if i==n-1:
                df["sentence"][start_index:].to_csv(f'{self.args.output_dir}split_{i+1}.csv',index=False,encoding="utf-8-sig")
            else:
                df["sentence"][start_index:end_index].to_csv(f'{self.args.output_dir}split_{i+1}.csv',index=False,encoding="utf-8-sig")