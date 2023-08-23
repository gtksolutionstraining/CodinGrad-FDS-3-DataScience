from services.external.profilers.pandasProfiler.profiler import(
    PandasProfiler
)

class ProfileManager:
    def __init__(self,dataPath):
        self.pandasProfiler = PandasProfiler(dataPath)
    