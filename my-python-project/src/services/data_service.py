class DataService:
    def __init__(self, data_source):
        self.data_source = data_source

    def fetch_data(self):
        # Logic to fetch data from the data source
        print(f"Fetching data from {self.data_source}")
        # Example return value
        return {"data": "sample data"}

    def save_data(self, data):
        # Logic to save data to the data source
        print(f"Saving data to {self.data_source}: {data}")
        # Example return value
        return True