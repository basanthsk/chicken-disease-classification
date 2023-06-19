import os 
import pandas as pd
import urllib.request as request
import shutil
from chickenClassifier import logger
from chickenClassifier.utils.common import get_size
from chickenClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
from dotenv import load_dotenv
# from kaggle.api.kaggle_api_extended import KaggleApi

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        load_dotenv()
        
        
    def download_file(self):    
        if not os.path.exists(self.config.download_dir):
            kaggle_username = os.getenv('KAGGLE_USERNAME')
            kaggle_key = os.getenv('KAGGLE_KEY')
            from kaggle.api.kaggle_api_extended import KaggleApi
            api = KaggleApi()
            api.authenticate()
            api.dataset_download_files(self.config.source_URL, path=self.config.download_dir, unzip=True)
            logger.info(f" download data with kaggle!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.download_dir))}")
    
    def saparate_files(self):
        df = pd.read_csv(self.config.data_class_csv)
        groups = df.groupby('label')
        for name, group in groups:
            folder_name = str(name)
            folder_path = os.path.join(self.config.saparate_files, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            # Create a new column with the source file path
            group['source_path'] = group['images'].apply(lambda x: os.path.join(self.config.downloaded_files, x))
            # Create a new column with the destination file path
            group['destination_path'] = group['images'].apply(lambda x: os.path.join(folder_path, x))
    
            # Move the image file to the corresponding folder
            for index, row in group.iterrows():
                    shutil.move(row['source_path'], row['destination_path'])
    
    
    
       
                        