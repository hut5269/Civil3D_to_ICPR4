import helpers as hp
import pandas as pd
import numpy as np 
from IPython.display import clear_output


def catchments(peaking_factor):
    add_columns  = ['HydrographMethod', 'InfiltrationMethod', 'MaxAllowableQ',
                    'TimeShift', 'PctImpervious', 'PctDCIA', 'PctDirect', 
                    'Comment', 'ShapeX', 'ShapeY', 'ShapeZ', 'TextX', 'TextY', 
                    'TextZ', 'TextAngle', 'IsPlaced']
    column_order = ['Name', 'Node', 'HydrographMethod', 'InfiltrationMethod', 
                    'TimeOfConcentration', 'MaxAllowableQ', 'TimeShift',
                    'UnitHydrograph', 'PeakingFactor', 'Area', 'CurveNumber',
                    'PctImpervious', 'PctDCIA', 'PctDirect', 'RainfallName', 
                    'Comment', 'ShapeX', 'ShapeY', 'ShapeZ', 'TextX', 'TextY', 
                    'TextZ', 'TextAngle', 'IsPlaced']
    rename       = {'TC': 'TimeOfConcentration'}

    user_file = hp.file_upload("Upload Civil Catchment Data CSV File")
    df = pd.read_csv(user_file)
    df['CurveNumber'] = (df.C + 1)/0.020
    df = df.reindex(df.columns.tolist() + add_columns, axis=1)
    df = df.rename(columns=rename)
    df['Node'] = df['Name']
    df['UnitHydrograph'] = 'UH{0}'.format(peaking_factor)
    df['PeakingFactor'] = peaking_factor
    df['RainfallName'] = 'Scsiii'
    df = df[column_order]
    df = df.replace(np.nan, '0')

    df.to_csv('/content/Output/BasinDataOutput.csv', encoding='utf-8', index=False)