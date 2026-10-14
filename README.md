# Autonomous Donkey Car

This repository is a practical starting point for a camera-based autonomous RC car project using Donkey Car and TensorFlow.

## Current status

The repository now contains:
- a basic Python project structure
- a reusable configuration module
- a TensorFlow CNN model scaffold for steering and throttle prediction
- training and driving entry points
- a lightweight data collection and project layout guide

## Quick start

1. Create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Prepare a training dataset in `data/`.

4. Train the model:
   python src/train.py

5. Run the driving scaffold:
   python src/drive.py

## Project structure

- `src/config.py` - runtime configuration values
- `src/model.py` - TensorFlow CNN model definition
- `src/data_utils.py` - dataset helpers
- `src/data_collection.py` - collection workflow scaffold
- `src/train.py` - training entry point
- `src/drive.py` - autonomous driving entry point
- `data/` - captured examples and labels
- `models/` - trained model artifacts
- `logs/` - training logs and diagnostics

## Next steps

- Connect the camera and RC hardware
- Capture manual driving data
- Review and clean the dataset
- Tune the CNN to improve steering stability
- Integrate real Donkey Car vehicle control on the target hardware
