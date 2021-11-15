import pandas as pd
import ast

class Eda:
    def __init__(self,args) -> None:
        self.args = args
        self.csv_path = args.output_dir + args.raw_csv
        self.entity_csv_path = args.output_dir + args.entity_csv
        print("All entity count \n")
        self.get_entity_count()
        print("All word in entitiy \n")
        self.get_entity_word()

    def get_entity_count(self):
        df = pd.read_csv(self.entity_csv_path)
        all_entity_array = []
        for i,entity in enumerate(df["entity"]):
            entity = ast.literal_eval(entity)
            all_entity_array.extend(entity)

        dic = {}

        for entity in all_entity_array:
            if entity["type"] in dic:
                dic[entity["type"]] +=1
            else:
                dic[entity["type"]] = 0
        print(dic)

    def get_entity_word(self):
        df = pd.read_csv(self.entity_csv_path)
        all_entity_array = []
        for i,entity in enumerate(df["entity"]):
            entity = ast.literal_eval(entity)
            all_entity_array.extend(entity)

        dic = {}

        for entity in all_entity_array:
            if entity["type"] in dic:
                dic[entity["type"]].append(entity["word"])
            else:
                dic[entity["type"]] = []
        
        for i in dic:
            dic[i] = list(set(dic[i]))
        print(dic)