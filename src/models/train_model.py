from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pickle
from sklearn.neural_network import MLPClassifier


# Function to train the model
def train_Nmodel(X, y):
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=123, stratify=y)
    # Scale the data using MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(X_train)
    # Now transform xtrain and xtest
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    # Train the logistic regression model
    # fit/train the model. Check batch size.
    model = MLPClassifier(hidden_layer_sizes=(3,3), batch_size=50, max_iter=200, random_state=123).fit(X_train_scaled,y_train)
    
    # Save the trained model
    with open('models/Neural_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model, X_test_scaled, y_test