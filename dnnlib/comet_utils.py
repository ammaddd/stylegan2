from comet_ml import Experiment

class CometLogger():
    def __init__(self,api_key,project_name,workspace):
        self.experiment = Experiment(api_key,project_name,workspace)

    #Logging parameters
    def log_parameters(self,hyper_parameters):
        self.experiment.log_parameters(hyper_parameters)