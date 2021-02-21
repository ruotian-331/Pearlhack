import anvil.server
from anvil.tables import app_tables
import pandas as pd
anvil.server.connect("K7XKRLX7OOYMPWGVQ6ENWSBR-56CWRXFDWIEOE5Q6")

def import_csv_data(file):
    with open(file, "r") as f:
        df = pd.read_csv(f)
        for d in df.to_dict(orient="records"):
            app_tables.stocks.add_row(**d)

import_csv_data('stocks.csv')


