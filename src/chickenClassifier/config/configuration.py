from chickenClassifier.constants import * 
from chickenClassifier.utils.common import read_yaml, create_directories
import os
from chickenClassifier.entity.config_entity import (DataIngestionConfig,
                                                    PrepareBaseModelConfig,
                                                    CallbackConfig,
                                                    TrainingConfig)

class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            download_dir=config.download_dir,
            downloaded_files = config.downloaded_files,
            saparate_files=config.saparate_files
        )
        
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) ->PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path = Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model),
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
        )
        
        return prepare_base_model_config
        
    def get_callback_config(self) -> CallbackConfig:
        config = self.config.callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
             Path(config.tensorboard_root_log_dir)])
        
        callback_config = CallbackConfig(
            root_dir = Path(config.root_dir),
            tensorboard_root_log_dir = Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath = Path(config.checkpoint_model_filepath)
        )
        
        return callback_config
                
    def get_training_config(self) -> TrainingConfig:
        config = self.config.training
        base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.saparate_files,)
        create_directories([
            Path(config.root_dir)
        ])
        
        training_config = TrainingConfig(
            root_dir = Path(config.root_dir),
            trained_model_path = Path(config.trained_model_path),
            updated_base_model_path = Path(base_model.updated_base_model),
            training_data = Path(training_data),
            num_epochs = params.EPOCHS,
            batch_size = params.BATCH_SIZE,
            augmentation = params.AUGMENTATION,
            image_size = params.IMAGE_SIZE
            
        )
        
        return training_config