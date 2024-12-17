class QueryGenerotor:
    query = """
    SELECT 
        {columns}
    FROM 
        `gdelt-bq.gdeltv2.events`
    WHERE 
        (Actor1CountryCode = '{contry_1}' OR Actor2CountryCode = '{contry_1}')
        AND (Actor1CountryCode = '{contry_2}' OR Actor2CountryCode = '{contry_2}')
        AND PARSE_DATE('%Y%m%d', CAST(SQLDATE AS STRING)) BETWEEN DATE('{start_date}') AND DATE('{end_date}')
    ORDER BY 
        SQLDATE ASC
    LIMIT {limit};
    """

    get_country_query = """
    SELECT Actor1CountryCode AS CountryCode
    FROM `gdelt-bq.gdeltv2.events`
    UNION DISTINCT
    SELECT Actor2CountryCode AS CountryCode
    FROM `gdelt-bq.gdeltv2.events`;
    """
    def generate_query(self, contry_1: str, contry_2: str, start_date: str, end_date: str, limit: int, columns_list:list = None) -> str:
        columns = ", ".join(columns_list) if not columns_list is None else "*"
        query = self.query.format(columns=columns, contry_1=contry_1, contry_2=contry_2, start_date=start_date,
                                  end_date=end_date, limit=limit)
        return query

    def generate_get_country_query(self) -> str:
        query = self.get_country_query
        return query