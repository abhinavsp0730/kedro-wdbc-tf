import pandas as pd

def create_features(wdbc: pd.DataFrame) -> pd.DataFrame:
    """ preprocess the wdbc dataset

    Args:
        wdbc: Source data
    Returns:
        preprocessed the data and returns features
    """

    features = ['radius','texture', 'area_worst']
    return my_data[features]

def create_labels(wdbc: pd.DataFrame) -> pd.DataFrame:
    """ preprocess the wdbc dataset

    Args:
        wdbc: Source data
    Returns:
        preprocessed the data and returns labels
    """

    labels = ['diagnosis_numeric']
    return my_data[labels]