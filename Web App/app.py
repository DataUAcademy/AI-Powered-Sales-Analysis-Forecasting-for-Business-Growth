import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import plotly.graph_objects as go
import joblib

# Load your trained model and scaler
model = load_model('lstm_model.h5')
sc = joblib.load('scaler.pkl')

# Function to split the dataset into train and test sets
def train_test_split(df, train_end, test_end):
    train_end = pd.to_datetime(train_end)
    test_end = pd.to_datetime(test_end)
    
    train_set = df[df.index <= train_end]
    test_set = df[(df.index > train_end) & (df.index <= test_end)]
    return train_set, test_set

# Function to create lookback dataset
def lookback(df, window):
    X, Y = [], []
    for i in range(window, len(df)):
        X.append(df[i-window:i, 0])
        Y.append(df[i,0])
    return np.array(X), np.array(Y)

# Streamlit UI
st.title('Sales Forecasting using LSTM')
data = pd.read_hdf('final_data.h5', key = 'df')

# Pre-set dates for splitting data
train_end = '2018-04-30'
test_end = '2018-08-29'

# Split the data without user input
train_df, test_df = train_test_split(data, train_end, test_end)

train_df_scaled = sc.fit_transform(train_df[['total_amount']])
test_df_scaled = sc.transform(test_df[['total_amount']])

# Lookback
window = 1  # Replace with your desired window size
X_train, y_train = lookback(train_df_scaled, window)
X_test, y_test = lookback(test_df_scaled, window)

# Reshape X for LSTM
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Reshape X for LSTM
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

# Generate predictions
y_pred = model.predict(X_test)

y_test_actual = sc.inverse_transform(y_test.reshape(-1, 1))
y_pred_actual = sc.inverse_transform(y_pred)

# ... previous code ...

# Forecast future values
def forecast_future(model, last_window, n_days):
    future_predictions_scaled = []
    current_batch = last_window[-window:].reshape(1, window, 1)

    for i in range(n_days):
        # Get the next prediction
        future_pred = model.predict(current_batch)
        future_predictions_scaled.append(future_pred[0, 0])
        
        # Update batch to include the next prediction and drop first value
        current_batch = np.append(current_batch[:, 1:, :], [[future_pred[0]]], axis=1)

    return np.array(future_predictions_scaled)

# Number of days to forecast
st.title("Forecast Input after test set")
forecast_days = st.number_input("Enter number of days to forecast:", min_value=1, value=121, max_value = 150)
extended_index = pd.date_range(start=test_df.index[-1], periods=forecast_days)

# Plotting actual vs predicted values
fig = go.Figure()
fig.add_trace(go.Scatter(x=test_df.index, y=y_test_actual.flatten(), mode='lines', name='Actual'))
fig.add_trace(go.Scatter(x=test_df.index, y=y_pred_actual.flatten(), mode='lines', name='Predicted'))
# Plotting actual vs predicted values with forecast
fig.add_trace(go.Scatter(x=extended_index, y=y_pred_actual.flatten(), mode='lines', name='Forecast', line=dict(color='red')))
fig.update_layout(title='Actual vs Predicted Values',
                  xaxis_title='Date',
                  yaxis_title='Value',
                  legend_title='Legend')
st.plotly_chart(fig)