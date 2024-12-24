from prophet import Prophet
from sklearn.model_selection import ParameterGrid
from sklearn.metrics import mean_squared_error

def tune_prophet_hyperparameters(data, params_grid):
    best_params = None
    best_mse = float('inf')

    for params in ParameterGrid(params_grid):
        model = Prophet(**params)
        model.fit(data)

        future = model.make_future_dataframe(periods=0)
        forecast = model.predict(future)

        current_mse = mean_squared_error(data['y'], forecast['yhat'])

        if current_mse < best_mse:
            best_params = params.copy()
            best_mse = current_mse
    
    return best_params, best_mse

def train_final_model(data, best_hyperparams):
    model = Prophet(**best_hyperparams)
    model.fit(data)
    return model
