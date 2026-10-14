"""Autonomous driving entry point for running a trained model on the RC car."""

from config import DEFAULT_CONFIG


def drive() -> None:
    """Placeholder autonomous driving routine.

    In a full implementation, this function would:
    - load a trained model
    - capture frames from the camera
    - run inference
    - send steering/throttle commands to the vehicle controller
    """
    print("TODO: connect to the RC car hardware and camera stream.")
    print(f"Configured model directory: {DEFAULT_CONFIG.models_dir}")


if __name__ == "__main__":
    drive()
