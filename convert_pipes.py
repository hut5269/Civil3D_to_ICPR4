import helpers as hp
import pandas as pd
from IPython.display import clear_output


def pipes():
    user_file = hp.file_upload("Upload Civil 3D Pipe Data CSV File")
    df = pd.read_csv(user_file)
    df['UsInvert'],df['DsInvert']=np.where(df['UsInvert']<df['DsInvert'],
        (df['DsInvert'],df['UsInvert']),(df['UsInvert'],df['DsInvert']))
    df.to_csv('/content/Output/LinkPipeOutput.csv', encoding='utf-8', index=False)
    clear_output()