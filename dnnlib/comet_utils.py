try:
    from comet_ml import Experiment
    comet_installed = True
except:
    print("Comet not installed")
    comet_installed = False
import tensorflow as tf
import json


class CometLogger():
    def __init__(self):
        self.comet_installed = comet_installed
        if self.comet_installed:
            self._experiment = Experiment()

    def log_model(self, path):
        self._experiment.log_model("Model", path)

    def log_image(self, path, name):
        self._experiment.log_image(image_data=path, name=name)
