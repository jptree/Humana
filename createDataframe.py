import pandas as pd

def createDataframe():
    """
    Create Testing Dataframe by combining csvs
    :return: returns a pandas dataframe
    """
    df1 = pd.read_csv('Data/2020_Competition_Training1.csv', index_col=0)
    df2 = pd.read_csv('Data/2020_Competition_Training2.csv', index_col=0)
    df3 = pd.read_csv('Data/2020_Competition_Training3.csv', index_col=0)
    df4 = pd.read_csv('Data/2020_Competition_Training4.csv', index_col=0)
    df5 = pd.read_csv('Data/2020_Competition_Training5.csv', index_col=0)

    frames = [df1, df2, df3, df4, df5]

    return pd.concat(frames)



