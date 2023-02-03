from prophet import Prophet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet.plot import plot_plotly, plot_components_plotly

    
past_data = pd.DataFrame(pd.read_excel("Dados.xlsx"))

past_data.columns = ['ds', 'y']

model = Prophet()
model.fit(past_data)

future_days = pd.date_range(start='2023-01-21', end='2023-01-25')

df_future_days = pd.DataFrame(future_days)
df_future_days.columns = ['ds']

forecast = model.predict(df_future_days)

forecast[['ds','yhat','yhat_lower','yhat_upper']]

fig = plot_plotly(model, forecast)

fig.show()
