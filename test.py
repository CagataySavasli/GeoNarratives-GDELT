from src.BigQueryConnector import BigQueryConnector
from src.QueryGenerotor import QueryGenerotor

bigQueryConnector = BigQueryConnector()
queryGenerator = QueryGenerotor()

contry_1 = input("İlk ülke kodunu girin: ")
contry_2 = input("İkinci ülke kodunu girin: ")
start_date = input("Başlangıç tarihini girin (YYYY-MM-DD): ")
end_date = input("Bitiş tarihini girin (YYYY-MM-DD): ")

query = queryGenerator.generate_query(contry_1, contry_2, start_date, end_date, 1000)
print(f"Query: {query}")
results = bigQueryConnector.get_data(query)

csv_filename = "outputs/data.csv"
results.to_csv(csv_filename, index=False)

print(f"Veri başarıyla '{csv_filename}' dosyasına kaydedildi.")
