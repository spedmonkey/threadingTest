import pandas as pd
import numpy as np


class data():
    task_list = [
        {"scene": "003mob", "shot": "0010"},
        {"scene": "003mob", "shot": "0020"},
        {"scene": "003mob", "shot": "0030"},
        {"scene": "003mob", "shot": "0040"},
        {"scene": "003mob", "shot": "0050"},
        {"scene": "003mob", "shot": "0060"},
        {"scene": "003mob", "shot": "0070"},
        {"scene": "003mob", "shot": "0010"},
        {"scene": "003mob", "shot": "0020"},
        {"scene": "002aac", "shot": "0010"},
        {"scene": "002aac", "shot": "0020"},
        {"scene": "002aac", "shot": "0030"},
        {"scene": "002aac", "shot": "0040"},
        {"scene": "002aac", "shot": "0010"},
        {"scene": "002aac", "shot": "0020"},
        {"scene": "002aac", "shot": "0030"},
        {"scene": "002aac", "shot": "0040"},
    ]

    df = pd.DataFrame(task_list, columns=['scene', 'shot',
                                          'scene_check_state',
                                          'shot_check_state',
                                          'regex',
                                          'resolve'])
    df = df.drop_duplicates()
    scenes = df['scene'].unique()
    shots = df['shot'].unique()

    # print df.loc[df['scene'] == "003mob", 'shot'].unique()
    # print df.loc[df['scene'] == "002aac", 'shot'].unique()


data = data()

# print a.df

for scene in data.df['scene'].unique():
    shot = data.df.loc[data.df['scene'] == scene, 'shot'].unique()
    print scene, shot
