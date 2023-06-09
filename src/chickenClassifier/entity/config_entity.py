from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    download_dir: Path 
    downloaded_files: Path
    saparate_files: Path 
    