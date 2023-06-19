from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    download_dir: Path 
    downloaded_files: Path
    saparate_files: Path
    data_class_csv: Path 
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate:float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
          
@dataclass(frozen=True)
class CallbackConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path
    

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    num_epochs: int 
    batch_size: int 
    augmentation: bool
    image_size: list    

@dataclass(frozen = True)
class EvaluationConfig:
    model_path: Path
    training_data: Path
    all_params: dict 
    image_size: list
    batch_size: int      