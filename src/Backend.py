from src.BigQueryConnector import BigQueryConnector
from src.QueryGenerotor import QueryGenerotor
from src.WepScrapper import WebScrapper
from src.Translator import Translator

bigQueryConnector = BigQueryConnector()
queryGenerator = QueryGenerotor()

f = open("src/CodesDicts/CAMEO.country_codes2text.py", "r")
countries_code2name = eval(f.read())
f.close()

get_countries_query = queryGenerator.generate_get_country_query()
countries_code = bigQueryConnector.get_data(get_countries_query)
countries_code = countries_code.dropna().reset_index(drop=True)
countries_code = sorted(countries_code['CountryCode'].tolist())
countries_code = [country + " : " + countries_code2name[country] if country in countries_code2name else country for
                  country in countries_code]


def download_data(contry_1, contry_2, start_date, end_date, limit, path):
    contry_1 = contry_1.split(" : ")[0]
    contry_2 = contry_2.split(" : ")[0]
    query = queryGenerator.generate_query(contry_1, contry_2, start_date, end_date, limit)
    results = bigQueryConnector.get_data(query)

    results.to_csv(path, index=False)

    print(f"Countries: {contry_1} and {contry_2}",
          f"Date Range: {start_date} - {end_date}",
          f"Limit: {limit}",
          f"Data was saved to '{path}' successfully.")
    #print(f"Data was saved to '{path}' successfully.")


def scrap_data(path, root):
    webScrapper = WebScrapper(path, root)
    data = webScrapper.get_source_text()
    data.to_csv(path, index=False)


def translate_data(path, root):
    translator = Translator(path, root)
    translator.get_translate()


def all_in_one(contry_1, contry_2, start_date, end_date, limit, path, root):
    download_data(contry_1, contry_2, start_date, end_date, limit, path)
    scrap_data(path, root)
    translate_data(path, root)
