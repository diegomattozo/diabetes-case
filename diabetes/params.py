import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Params:
    input_file: str
    output_file: str
    model_path: Path = Path(os.path.join("models", "final_model.pkl"))
