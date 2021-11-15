import pandas as pd    

class ReplaceEntity:
    def __init__(self,args) -> None:
        self.args = args
        self.entity_csv_path = args.output_dir + args.entity_csv
        self.replace_entity()

    def replace_entity(self):
        df = pd.read_csv(self.entity_csv_path)
        pattern = []
        pattern.append(r"""'type': 'OCCUPATION'""")
        pattern.append(r"""'type': 'PERSON'""")
        pattern.append(r"""'type': '(CIVILIZATION|ARTIFACT|COUNTRY|THEORY|LOCATION|EVENT|TIME|MATERIAL|CITY)'""")
        pattern.append(r"""'type': 'NONE'""")
        pattern.append(r"""{'word': '[^']*', 'type': '(DISEASE|ANIMAL|PLANT)', 'start': [0-9]*},?""")
        pattern.append(r'')

        df["entity"].replace(pattern[0],pattern[1], regex=True, inplace=True)
        df["entity"].replace(pattern[2],pattern[3], regex=True, inplace=True)
        df["entity"].replace(pattern[4],pattern[5], regex=True, inplace=True)
        df.to_csv(self.entity_csv_path,index=False,encoding="utf-8-sig")