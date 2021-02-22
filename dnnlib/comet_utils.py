try:
    from comet_ml import Experiment
    comet_installed = True
except:
    comet_installed = False

class CometLogger():
    def __init__(self):
        global comet_installed
        self._logging = False
        if comet_installed:
            try:
                self._experiment = Experiment()
                self._logging = True
            except:
                print("Comet not configured properly")
        else:
            print("Comet is not installed")

    def log_model(self, path):
        if self._logging:
            self._experiment.log_model("Model", path)

    def log_image(self, path, name):
        if self._logging:
            self._experiment.log_image(image_data=path, name=name)
