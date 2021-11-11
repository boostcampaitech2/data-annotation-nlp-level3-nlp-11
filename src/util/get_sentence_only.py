import pandas as pd
import math

class GetSentencenly:
    def __init__(self,args) -> None:
        self.args = args
        self.entity_csv_path = args.output_dir + args.entity_csv
        self.get_sentence()
        

    def get_sentence(self):
        df = pd.read_csv(self.args.output_dir+"entity_data_all.csv")
        df["sentence"].to_csv(self.args.output_dir+"entity_data_all_sentence.csv",index=False,encoding="utf-8-sig")

    def split_sentence(self,n):
        df = pd.read_csv(self.args.output_dir+"entity_data_all_sentence.csv")
        amount = int(math.ceil(len(df)/n))
        for i in range(n):
            start_index = i*amount
            end_index = ((i+1)*amount) -1
            if i==n-1:
                df["sentence"][start_index:].to_csv(f'{self.args.output_dir}split_{i+1}.csv',index=False,encoding="utf-8-sig")
            else:
                df["sentence"][start_index:end_index].to_csv(f'{self.args.output_dir}split_{i+1}.csv',index=False,encoding="utf-8-sig")