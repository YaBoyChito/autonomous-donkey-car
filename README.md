# Autonomous Donkey Car

A camera-based autonomous RC car project using Donkey Car, Python, and TensorFlow. This repository provides a startup scaffold for collecting driving data, training an imitation-learning model, and preparing for autonomous deployment.

## Project overview

This project explores how machine learning connects visual perception with vehicle control. Instead of hardcoding a fixed route, the goal is to collect examples of human driving, train a model from that data, and verify performance on the track.

## Objectives

- Build the RC chassis and onboard electronics integration.
- Collect driving demonstrations with labeled steering and throttle.
- Train a TensorFlow model from camera observations.
- Evaluate autonomous driving performance and iterate on data quality.
- Document hardware, software, and training workflow.

## Repository structure

- `src/config.py` — default project settings and directories
- `src/model.py` — TensorFlow CNN model scaffold
- `src/data_utils.py` — utilities for listing and loading recorded data
- `src/data_collection.py` — data collection workflow helper
- `src/train.py` — training entry point
- `src/drive.py` — drive-time inference scaffold
- `requirements.txt` — Python dependencies
- `data/` — raw training data and labels
- `models/` — trained model outputs
- `logs/` — logs and diagnostics

## Quick start

1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Collect driving data in `data/`.

4. Train the model:
   ```bash
   python src/train.py
   ```

5. Run the drive scaffold:
   ```bash
   python src/drive.py
   ```

## Next steps

- Connect and verify camera and motor control hardware.
- Record training laps with steering and throttle labels.
- Improve the dataset quality before training.
- Tune the CNN and training pipeline for better lane following.
- Integrate the trained model into the vehicle runtime stack.

## Current status

This repository is a working foundation for the project. The code is intentionally scaffolded and needs real hardware, dataset capture, and training tuning before autonomous performance can be verified.
