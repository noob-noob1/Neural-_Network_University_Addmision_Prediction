import pandas as pd

def load_and_preprocess_data(data_path):
    
    # Import the data from 'credit.csv'
    df = pd.read_csv(data_path)

    # Impute all missing values in all the features
    df['Admit_Chance']=(df['Admit_Chance'] >=0.8).astype(int)

    # Drop 'Serial_No' variable from the data
    df = df.drop(['Serial_No'], axis=1)
    
    # Change dtypes
    df['University_Rating'] = df['University_Rating'].astype('object')
    df['Research'] = df['Research'].astype('object')

    return df