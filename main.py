from mlflowProject import logger
from mlflowProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlflowProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
#from mlflowProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
#from mlflowProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
#from mlflowProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e