"""TensorFlow model definitions for the autonomous driving project."""

from __future__ import annotations

from typing import Tuple

import tensorflow as tf


def build_model(image_shape: Tuple[int, int, int] = (120, 160, 3)) -> tf.keras.Model:
    """Build a lightweight CNN for steering and throttle prediction.

    This is a practical starting point for imitation learning, derived from
    the image-to-control pattern used in Donkey Car tutorials. It is meant to
    be extended with real preprocessing, data augmentation, and tuned output
    layers for the project hardware.
    """
    inputs = tf.keras.Input(shape=image_shape)

    x = tf.keras.layers.Rescaling(scale=1.0 / 255.0)(inputs)
    x = tf.keras.layers.Conv2D(24, (5, 5), strides=(2, 2), activation="relu")(x)
    x = tf.keras.layers.Conv2D(32, (5, 5), strides=(2, 2), activation="relu")(x)
    x = tf.keras.layers.Conv2D(64, (3, 3), activation="relu")(x)
    x = tf.keras.layers.Conv2D(64, (3, 3), activation="relu")(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(100, activation="relu")(x)
    x = tf.keras.layers.Dense(50, activation="relu")(x)

    steering = tf.keras.layers.Dense(1, activation="tanh", name="steering")(x)
    throttle = tf.keras.layers.Dense(1, activation="sigmoid", name="throttle")(x)

    model = tf.keras.Model(inputs=inputs, outputs=[steering, throttle])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
        loss={
            "steering": tf.keras.losses.MeanSquaredError(),
            "throttle": tf.keras.losses.MeanSquaredError(),
        },
        loss_weights={"steering": 1.0, "throttle": 0.5},
        metrics={
            "steering": [tf.keras.metrics.MeanAbsoluteError()],
            "throttle": [tf.keras.metrics.MeanAbsoluteError()],
        },
    )
    return model
