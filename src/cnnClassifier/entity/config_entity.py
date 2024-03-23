#return type of class of data_ingestion -> entity
#dataclass -> decorator on python class like a python variable

from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path