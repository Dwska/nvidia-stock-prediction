
def log_results_to_mlflow(best_params, best_mse, mlflow):
    mlflow.log_params(best_params)
    mlflow.log_metric("best_mse", best_mse)
    
    mlflow.log_artifact('predict/forecast_plot.png')
    mlflow.log_artifact('predict/forecast_components.png')
    
    # Display success message
    print("Plots saved successfully.")