
from mlflow.models.signature import infer_signature


def log_results_to_mlflow(best_params, best_mse, mlflow):
    mlflow.log_params(best_params)
    mlflow.log_metric("best_mse", best_mse)
    
    mlflow.log_artifact('predict/forecast_plot.png')
    mlflow.log_artifact('predict/forecast_components.png')

    print("Plots saved successfully.")

def deploy_model_to_mlflow(final_model, registered_model_name, mlflow):
    # Prepare an example input for the model
    example_input = final_model.make_future_dataframe(periods=5) 

    # Create an example output
    example_output = final_model.predict(example_input)

    # Infer the model signature based on the example input and output
    signature = infer_signature(example_input, example_output)

    # Log the model with input example and signature
    mlflow.prophet.log_model(
        final_model, 
        artifact_path="model",
        registered_model_name=registered_model_name,
        signature=signature, 
        input_example=example_input  
    )

    print("Model saved successfully.")