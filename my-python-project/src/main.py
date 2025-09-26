# Contents of /my-python-project/my-python-project/src/main.py

import sys
from utils import load_config, log_message
from services.data_service import DataService

def main():
    config = load_config('config.json')
    log_message('Application started with config: {}'.format(config))
    
    data_service = DataService()
    data = data_service.fetch_data()
    log_message('Fetched data: {}'.format(data))

if __name__ == '__main__':
    main()