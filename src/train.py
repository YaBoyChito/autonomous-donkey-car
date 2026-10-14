"""Training script for the donkey car imitation learning model."""

from __future__ import annotations

from pathlib import Path

from config import DEFAULT_CONFIG
from model import build_model


def train_model() -> None:
    """Placeholder but realistic training entry point.

    The intention is to keep the workflow aligned with Donkey Car:
    - collect driving data
    - label steering/throttle values
    - load examples into a TensorFlow model
    - save model weights for deployment
    """
    data_dir = DEFAULT_CONFIG.data_dir
    models_dir = DEFAULT_CONFIG.models_dir
    models_dir.mkdir(parents=True, exist_ok=True)

    if not data_dir.exists():
        raise FileNotFoundError(
            f"No training dataset directory found at {data_dir}. "
            "Run data collection before training."
        )

    model = build_model((DEFAULT_CONFIG.image_height, DEFAULT_CONFIG.image_width, DEFAULT_CONFIG.image_depth))
    model_path = models_dir / "autonomous_donkey_car_model.keras"

    print(f"Training dataset directory: {data_dir}")
    print(f"Model destination: {model_path}\n")
    print("TODO: load real recorded driving data and train the model on the collected frames.")
    print("TODO: call model.save(model_path) after successful training.")


if __name__ == "__main__":
    train_model()
