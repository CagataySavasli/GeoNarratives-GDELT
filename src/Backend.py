from src.BigQueryConnector import BigQueryConnector
from src.QueryGenerotor import QueryGenerotor

bigQueryConnector = BigQueryConnector()
queryGenerator = QueryGenerotor()

def download_data(contry_1, contry_2, start_date, end_date, limit):
    query = queryGenerator.generate_query(contry_1, contry_2, start_date, end_date, limit)
    results = bigQueryConnector.get_data(query)

    csv_filename = "outputs/data.csv"
    results.to_csv(csv_filename, index=False)

    print(f"Data was saved '{csv_filename}' successfully.")