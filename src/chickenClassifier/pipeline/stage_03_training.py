from chickenClassifier.config.configuration import ConfigurationManager
from chickenClassifier.components.callbacks import Callback
from chickenClassifier.components.training import Training
from chickenClassifier import logger

STAGE_NAME = "Training"

class TrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        callback_config = config.get_callback_config()
        callback = Callback(config = callback_config)
        callback_list = callback.get_tb_ckpt_callbacks()
        
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list = callback_list
        )
        
    if __name__ == '__main':
        try:
            logger.info(f"**********************")
            logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
            obj = TrainingPipeline()
            obj.main()
            logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e    
            