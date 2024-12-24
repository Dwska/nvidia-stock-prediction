import os
from notebook.src.data_processing import load_and_preprocess_data

def test_load_and_preprocess_data():
    mock_data = "Date,Close\n2022-01-01,100\n2022-01-02,101"
    file_path = "mock_data.csv"
    with open(file_path, "w") as f:
        f.write(mock_data)

    data = load_and_preprocess_data(file_path)
    assert data.shape[1] == 2, "Data should have exactly 2 columns"
    assert "ds" in data.columns and "y" in data.columns, "Columns should be renamed correctly"

    os.remove(file_path)
