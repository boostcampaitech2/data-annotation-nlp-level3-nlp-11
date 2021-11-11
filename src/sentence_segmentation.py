
import os
import pandas as pd
from tqdm import tqdm
from kss import split_sentences
from src.morph_filter import morph_filter

class SentenceSagmentation:
    def __init__(self,args) -> None:
        self.args = args
        self.data_to_csv()

    def get_data(self,data_path=None):
        if data_path == None:
            data_path = self.args.data_path

        file_list = os.listdir(data_path)
        print(f'총 파일 리스트 \n{file_list}')
        return file_list

    def data_to_csv(self,data_path=None):
        if data_path == None:
            data_path = self.args.data_path

        file_list = self.get_data()

        df = pd.DataFrame()
        
        for i in tqdm(range(len(file_list))):
            f = open(data_path+'/'+file_list[i])
            txt = f.read()
            sentence_array = []
            result = split_sentences(
                text= txt,
                use_heuristic= False,
                use_quotes_brackets_processing=True,
                # backend="mecab",
            )
            result = morph_filter(result)
            for sentence in result:
                sentence_array.append(sentence)
            
            df = pd.concat([pd.DataFrame({"doc":file_list[i].split('.')[0],"sentence": sentence_array}),df])

        df.to_csv(self.args.output_dir + self.args.raw_csv,index=False,encoding="utf-8-sig")