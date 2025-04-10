import pandas as pd

# create dummy features
def create_dummy_vars(df):
    # Create dummy variables for all 'object' type variables except 'Loan_Status'
    df = pd.get_dummies(df, columns=['University_Rating','Research'],dtype='int')

    # store the processed dataset in data/processed
    df.to_csv('data/processed/Processed_UCLA_Neural.csv', index=None)

    # Separate the input features and target variable
    X = df.drop(['Admit_Chance'], axis=1)
    y = df['Admit_Chance']

    return X, y