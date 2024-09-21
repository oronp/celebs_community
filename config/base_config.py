import os
from pathlib import Path
from dataclasses import dataclass, field


@dataclass(frozen=True)
class BaseConfig:
    CONFIG_DIR: str = os.path.dirname(os.path.abspath(__file__))
    MAIN_DIR: str = str(Path(CONFIG_DIR).resolve().parent)
    DATA_DIR: str = os.path.join(MAIN_DIR, 'data')
