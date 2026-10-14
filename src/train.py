"""Training entry point for the Donkey Car imitation learning pipeline."""

from pathlib import Path

from config import DEFAULT_CONFIG


def train_model() -> None:
    """Placeholder training entry point.

    In a full implementation, this function would:
    - load the collected driving data
    - preprocess camera images and steering/throttle labels
    - train a TensorFlow model
    - save the trained model to the models directory
    """
    data_dir = DEFAULT_CONFIG.data_dir
    models_dir = DEFAULT_CONFIG.models_dir

    if not data_dir.exists():
        raise FileNotFoundError(
            f"Training data directory does not exist yet: {data_dir}. "
            "Collect driving data before running training."
        )

    models_dir.mkdir(parents=True, exist_ok=True)
    print(f"Training data source: {data_dir}")
    print(f"Model output directory: {models_dir}\n")
    print("TODO: integrate Donkey Car training pipeline and TensorFlow model definition.")


if __name__ == "__main__":
    train_model()
