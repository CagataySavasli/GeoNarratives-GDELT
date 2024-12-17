from src.BigQueryConnector import BigQueryConnector
from src.QueryGenerotor import QueryGenerotor
from src.WepScrapper import WebScrapper
from src.Translator import Translator

bigQueryConnector = BigQueryConnector()
queryGenerator = QueryGenerotor()

get_countries_query = queryGenerator.generate_get_country_query()
countries_code = bigQueryConnector.get_data(get_countries_query)
countries_code = countries_code.dropna().reset_index(drop=True)
countries_code = sorted(countries_code['CountryCode'].tolist())

def download_data(contry_1, contry_2, start_date, end_date, limit, path):
    query = queryGenerator.generate_query(contry_1, contry_2, start_date, end_date, limit)
    results = bigQueryConnector.get_data(query)

    results.to_csv(path, index=False)

    print(f"Data was saved to '{path}' successfully.")

def scrap_data(path, root):
    webScrapper = WebScrapper(path, root)
    data = webScrapper.get_source_text()
    data.to_csv(path, index=False)

def translate_data(path, root):
    translator = Translator(path, root)
    translator.get_translate()