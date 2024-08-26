import os
import pandas as pd
import datetime
import psycopg2
from sqlalchemy import create_engine
from workFunctions.secrets import postgresPath


def getInfoWithFolder(folder_path):
    pathfold = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            pathfold.append(os.path.join(root, file))
    return pathfold


def setUpDate(path):
    df_main = pd.DataFrame()
    for i in range(len(path)):
        df = pd.read_table(path[i])
        df_main = pd.concat([df_main,df], ignore_index=True)
    return df_main

engine = create_engine(postgresPath)
