import pyarrow.parquet as pq
import pandas as pd
from rich import print
import json
from pathlib import Path

datasetPath=Path(__file__).parent
filename="alpaca.parquet"

def parquet2jsn(filename:str):
    dataPath=datasetPath.joinpath(filename)
    alpaca = pq.read_table(dataPath.__str__())
    df:pd.DataFrame=alpaca.to_pandas()
    with datasetPath.joinpath(filename.split(".")[0]+".json").open(
        'w',encoding='utf8'
    ) as jsn:
        json.dump(df.to_dict(),jsn,ensure_ascii=False,indent=2)


if __name__=='__main__':
    parquet2jsn(filename)
