import pandas as pd
from src.model_training import tune_prophet_hyperparameters

def test_tune_prophet_hyperparameters():
    data = pd.DataFrame({
        'ds': pd.date_range(start='2022-01-01', periods=10, freq='D'),
        'y': [100 + i for i in range(10)]
    })
    params_grid = {
        'changepoint_prior_scale': [0.001, 0.01],
        'seasonality_prior_scale': [0.01, 0.1]
    }

    best_params, best_mse = tune_prophet_hyperparameters(data, params_grid)
    assert best_params is not None, "Best parameters should not be None"
    assert best_mse > 0, "Best MSE should be greater than 0"
