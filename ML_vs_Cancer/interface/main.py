import pandas as pd
import numpy as np
from ML_vs_Cancer.ml_logic.data import load_data_to_bq, get_data_with_cache
#from pathlib import Path

def preprocess() -> None:
    """
    - Query the raw dataset from Le Wagon's BigQuery dataset
    - Cache query result as a local CSV if it doesn't exist locally
    - Process query data
    - Store processed data on your personal BQ (truncate existing table if it exists)
    - No need to cache processed data as CSV (it will be cached when queried back from BQ during training)
    """
    query = ""

    # data_query_cache_path = Path(LOCAL_DATA_PATH).joinpath("raw", f"query_{min_date}_{max_date}_{DATA_SIZE}.csv")
    data_query_cache_path = ""
    data_query = get_data_with_cache(
        query=query,
        gcp_project="",
        cache_path=data_query_cache_path,
        data_has_header=True
    )

    # TODO Process data

    data_processed_with_timestamp = None
    load_data_to_bq(
        data_processed_with_timestamp,
        gcp_project="",
        bq_dataset="",
        table=f'processed_{""}',
        truncate=True
    )
