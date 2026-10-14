"""Project configuration for the autonomous Donkey Car project."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectConfig:
    project_root: Path = Path(__file__).resolve().parent.parent
    data_dir: Path = project_root / "data"
    models_dir: Path = project_root / "models"
    logs_dir: Path = project_root / "logs"

    # Donkey Car settings
    image_width: int = 160
    image_height: int = 120
    image_depth: int = 3
    batch_size: int = 32
    epochs: int = 10

    # Vehicle-specific settings
    steering_scale: float = 1.0
    throttle_scale: float = 1.0


DEFAULT_CONFIG = ProjectConfig()
