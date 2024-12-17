from src.BigQueryConnector import BigQueryConnector
from src.QueryGenerotor import QueryGenerotor
from src.WepScrapper import WebScrapper

bigQueryConnector = BigQueryConnector()
queryGenerator = QueryGenerotor()

def download_data(contry_1, contry_2, start_date, end_date, limit, path):
    query = queryGenerator.generate_query(contry_1, contry_2, start_date, end_date, limit)
    results = bigQueryConnector.get_data(query)

    results.to_csv(path, index=False)

    print(f"Data was saved to '{path}' successfully.")

def scrap_data(path, root):
    webScrapper = WebScrapper(path, root)
    data = webScrapper.get_source_text()
    data.to_csv(path, index=False)