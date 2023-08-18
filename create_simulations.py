import helpers as hp
import pandas as pd


def simulations():
    user_file = hp.file_upload("Upload Atlas 14 Rainfall Data CSV File")
    atlas_df = pd.read_csv(user_file, sep=',', usecols=[0,1,2,3,4,5],
                            header=0, skiprows=13, nrows=10)
    atlas_df.drop(atlas_df.head(4).index, inplace=True)

    list = []

    for index in range(atlas_df.shape[0]):
        if index > 0:
            columnSeriesObj = atlas_df.iloc[:, index]
            list1 = columnSeriesObj.tolist()
            list.extend(list1)

    rain_df = pd.DataFrame({'RainfallAmount':list})
    rain_df['RainfallAmount'] += (rain_df['RainfallAmount'] * 0.10)
    return rain_df