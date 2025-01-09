import json
import pandas as pd
from tqdm import tqdm

BASE_URL = "https://arkhamdb.com/"
CARD_API = "/api/public/card/"
JSON_DATA="data_extract/all_cards.json"


def read_cards_json():
    
    df=pd.DataFrame(columns=["game_name","expansion","id","text"])
    
    with open(JSON_DATA,'r') as file:
        card_data=json.loads(file.read())
    
    for i in tqdm(range(len(card_data))):
        card=card_data[i]
        
        card_text='Game Name : Arkham Horror'
        for key in card:
            if key not in ['deck_requirements','deck_options','double_sided','octgn_id','url','imagesrc','backimagesrc','duplicated_by','alternated_by',
                           'illustrator','errata_date','restrictions','spoiler']:
                value=str(card[key])
                value=value.replace('<b>','').replace('</b>','').strip()
                card_text+=", "+key+" : "+value
        df.loc[len(df)]=['Arkham Horror',card['pack_name'],card['code'],card_text]   

    df.to_parquet('arkham_horror_card_data.parquet',index=False)

def get_card_image():
    pass

if __name__ == "__main__":
    read_cards_json()