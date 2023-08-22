from services.external.profilers.pandasProfiler import(
    PandasProfiler
)

class ProfileManager:
    def __init__(self,data):
        self.pandasProfiler = PandasProfiler(data)
    