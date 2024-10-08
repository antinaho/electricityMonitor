import sys
import os
import pandas as pd

from dotenv import load_dotenv

from energy.energy import EnergySlice, EnergyType
from utils.db import DatabaseConnection, ConnectionParams

from datetime import datetime, timedelta
from urllib.parse import quote
from utils.sql_helper import execute_sql_file, batch_execute, execute_command


def get_property_data() -> pd.DataFrame:
    url = "https://helsinki-openapi.nuuka.cloud/api/v1.0/Property/List"

    try:
        r = pd.read_json(url)
        return r
    except os.error as e:
        print(f"Error, {e}")
        sys.exit(1)

def insert_to_property_table(c) -> None:
    properties = get_property_data()
    properties = properties.dropna()

    params = [tuple(row) for row in properties.values]

    batch_execute(c, "sql/property/insert_property_data.sql", params)


def clean_property_table(c) -> None:
    execute_sql_file(c, "sql/property/transform_property_data.sql")

def extract_electricity_data(c) -> None:
    head = "https://helsinki-openapi.nuuka.cloud/api/v1.0/EnergyData/"

    time_slice = "Hourly"

    daily_e = EnergySlice(datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), EnergyType.ELECTRICITY)
    reporting_group = f"ReportingGroup={daily_e.energy_type.value}"
    start_time = f"StartTime={daily_e.start_date}"
    end_time = f"EndTime={daily_e.end_date}"

    execute_command(c, "SELECT location_name FROM location.property_clean")

    locations = c.fetchall()
    for loc in locations:
        location_name = f"SearchString={quote(loc[0])}"
        tail = f"{time_slice}/ListByProperty?Record=LocationName&{location_name}&{reporting_group}&{start_time}&{end_time}"
        url = head + tail
        try:
            df = pd.read_json(url)
            df = df[df['timestamp'] != daily_e.end_date]

            params = [tuple(row) for row in df.values]

            batch_execute(c, "sql/energy/insert_electricity_data.sql", params)
        except os.error as e:
            pass

def clean_electricity_data(c) -> None:
    execute_sql_file(c, "sql/energy/transform_electricity_data.sql")

def get_warehouse_creds() -> ConnectionParams:
    return ConnectionParams(
        db=os.getenv('POSTGRES_DB', ''),
        user=os.getenv('POSTGRES_USER', ''),
        password=os.getenv('POSTGRES_PASSWORD', ''),
        host=os.getenv('POSTGRES_HOST', ''),
        port=int(os.getenv('POSTGRES_PORT', 5432)),
    )

def main() -> None:
    load_dotenv('env')
    with DatabaseConnection(get_warehouse_creds()).connection() as c:
        insert_to_property_table(c)

        clean_property_table(c)

        extract_electricity_data(c)

        clean_electricity_data(c)


if __name__ == '__main__':
    main()
