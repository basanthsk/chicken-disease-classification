import os 
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
        # Iterate over each file in the source directory
        for filename in os.listdir(self.config.downloaded_files):
            # Extract the filename without extension
            file_name, file_extension = os.path.splitext(filename)
            directory_name = file_name.split('.')[0]
            
            # Check if the file is an image file (you can add more extensions if needed)
            if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                # Create the folder based on the filename if it doesn't exist
                folder_path = os.path.join(self.config.saparate_files, directory_name)
                os.makedirs(folder_path, exist_ok=True)
                
                # Move the image file to the corresponding folder
                source_file_path = os.path.join(self.config.downloaded_files, filename)
                destination_file_path = os.path.join(folder_path, filename)
                shutil.move(source_file_path, destination_file_path)
                        