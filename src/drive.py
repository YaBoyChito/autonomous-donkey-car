"""Autonomous drive entry point scaffold for the trained model."""

from __future__ import annotations

from pathlib import Path

from config import DEFAULT_CONFIG


def drive() -> None:
    """Explain the runtime workflow for autonomous inference."""
    models_dir = DEFAULT_CONFIG.models_dir
    models_dir.mkdir(parents=True, exist_ok=True)

    print(f"Model directory: {models_dir}")
    print("TODO: load the trained Keras model and stream frames from the onboard camera.")
    print("TODO: convert predictions into steering and throttle commands for the RC controller.")


if __name__ == "__main__":
    drive()
