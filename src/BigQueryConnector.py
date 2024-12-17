from google.cloud import bigquery
class BigQueryConnector:
    service_account_path = "services_accounts/services_accounts_file.json"
    def __init__(self, ):
        self.client = bigquery.Client.from_service_account_json(self.service_account_path)

    def get_data(self, query):
        query_job = self.client.query(query)
        return query_job.result().to_dataframe()