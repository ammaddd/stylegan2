from comet_ml import Experiment
import tensorflow as tf
import json

class CometLogger():
    def __init__(self,comet_config):
        with open(comet_config, "r") as content:
            content=json.load(content)
            self.experiment = Experiment(content['api_key'],content['project_name'],content['workspace'])

    #Logging parameters
    def log_parameters(self,hyper_parameters):
        self.experiment.log_parameters(hyper_parameters)

    def log_model(self, path):
        self.experiment.log_model("Model", path)

    def log_image(self, path, name):
        self.experiment.log_image(image_data=path,name=name)