"""Example data collection script scaffold for the project."""

from __future__ import annotations

from config import DEFAULT_CONFIG


def collect_data() -> None:
    """Prepare the data directories and explain the collection workflow."""
    data_dir = DEFAULT_CONFIG.data_dir
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"Driving data folder: {data_dir}")
    print("Collect data by recording camera frames and steering/throttle commands while driving.")
    print("Recommended structure:")
    print("  data/raw/      -> captured images")
    print("  data/labels.csv -> image_path,steering,throttle")
    print("  data/validated/ -> reviewed high-quality examples")


if __name__ == "__main__":
    collect_data()
