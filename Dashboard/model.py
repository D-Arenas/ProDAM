import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

    
def evaluate_model(y_pred, y_test):
    # Calculate evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Print evaluation metrics
    print("Mean Squared Error:", mse)
    print("R^2:", r2)

def train_sweing():

    df = pd.read_csv('../Data Engineering/datoslimpios.csv')
    df = df[df['department'] == 'sweing']
    X = df[['incentive']]
    y = df['actual_productivity']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Get the input shape from the training data
    input_dim = X_train.shape[1]

    # Create a sequential model
    model = Sequential()

    # Add layers to the model
    model.add(Dense(64, activation='relu', input_shape=(input_dim,)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])

    # Train the model
    model.fit(X_train, y_train, epochs=100, batch_size=32)

    # Evaluate the model
    y_pred = model.predict(X_test)

    print("Sweing Department")
    evaluate_model(y_pred, y_test)

    return model

def train_finishing():

    df = pd.read_csv('../Data Engineering/datoslimpios.csv')
    df = df[df['department'] == 'finishing']
    X = df[['smv' ]]
    y = df['actual_productivity']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Get the input shape from the training data
    input_dim = X_train.shape[1]

    # Create a sequential model
    model = Sequential()

    # Add layers to the model
    model.add(Dense(64, activation='relu', input_shape=(input_dim,)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile the model
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])

    # Train the model
    model.fit(X_train, y_train, epochs=100, batch_size=32)

    # Evaluate the model
    y_pred = model.predict(X_test)

    print("Finishing Department")
    evaluate_model(y_pred, y_test)

    return model

sewing_model = train_sweing()
finishing_model = train_finishing()

def predict_productivity(department, input_data):
    # input_data es incentive para sweing y smv para finishing
    input_data = np.array([[input_data]])
    if department == 'sweing':
        result = sewing_model.predict(input_data)
    elif department == 'finishing':
        result = finishing_model.predict(input_data)
    return result[0][0]

