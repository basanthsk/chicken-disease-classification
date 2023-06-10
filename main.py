from chickenClassifier import logger
from chickenClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chickenClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started<<<<<")
    data_ingestion =DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<stage {STAGE_NAME} completed >>>>>>>>>>\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started<<<<<")
    data_ingestion =PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<<<<stage {STAGE_NAME} completed >>>>>>>>>>\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e
    