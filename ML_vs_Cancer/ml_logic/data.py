import pandas as pd
from pathlib import Path
from google.cloud import bigquery

def get_data_with_cache(
    gcp_project: str,
    query: str,
    cache_path: Path,
    data_has_header = True
) -> pd.DataFrame:
    """
    Retrieve `query` data from BigQuery, or from `cache_path` if the file exists
    Store at `cache_path` if retrieved from BigQuery for future use
    """
    if cache_path.is_file():
        df = pd.read_csv(cache_path, header='infer' if data_has_header else None)
    else:
        client = bigquery.Client(project=gcp_project)
        query_job = client.query(query)
        result = query_job.result()
        df = result.to_dataframe()
        
        # Store as CSV if the BQ query returned at least one valid line
        if df.shape[0] > 1:
            df.to_csv(cache_path, header=data_has_header, index=False)
            
    return df

def load_data_to_bq(
    data: pd.DataFrame,
    gcp_project: str,
    bq_dataset: str,
    table: str,
    truncate: bool
) -> None:
    """
    - Save the DataFrame to BigQuery
    - Empty the table beforehand if `truncate` is True, append otherwise
    """
    
    assert isinstance(data, pd.DataFrame)
    full_table_name = f"{gcp_project}.{bq_dataset}.{table}"

    data.columns = [f"_{column}" if not str(column)[0].isalpha() and not str(column)[0] == "_" else str(column) for column in data.columns]
    
    client = bigquery.Client()
    
    write_mode = "WRITE_TRUNCATE" if truncate else "WRITE_APPEND"
    job_config = bigquery.LoadJobConfig(write_disposition=write_mode)

    job = client.load_table_from_dataframe(data, full_table_name, job_config=job_config)
    result = job.result()
