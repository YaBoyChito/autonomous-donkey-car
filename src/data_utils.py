"""Utilities for loading and preparing driving data."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Tuple

import numpy as np


def list_image_files(data_dir: Path) -> List[Path]:
    """Return image files under a data directory."""
    if not data_dir.exists():
        raise FileNotFoundError(f"Data directory was not found: {data_dir}")

    files = [p for p in data_dir.rglob("*") if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
    return sorted(files)


def load_labels(label_file: Path) -> dict:
    """Load a simple CSV label file in the form: image_path,steering,throttle.

    This placeholder expects a structured dataset and is intentionally simple.
    Real Donkey Car datasets typically use the native record format generated
    by the data collection tool and can be converted as needed.
    """
    labels: dict = {}
    if not label_file.exists():
        return labels

    with label_file.open("r", encoding="utf-8") as handle:
        next(handle, None)  # Skip header if present.
        for line in handle:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) < 3:
                continue
            image_path, steering, throttle = parts[0], parts[1], parts[2]
            labels[image_path] = (float(steering), float(throttle))
    return labels


def ensure_dataset_dirs(base_dir: Path) -> None:
    """Create the basic directory structure expected by the project."""
    for rel_path in ["data", "models", "logs"]:
        (base_dir / rel_path).mkdir(parents=True, exist_ok=True)
