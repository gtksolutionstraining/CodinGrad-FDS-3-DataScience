from services.internal.managers.profilerManager import(
    ProfileManager
)
from config import DATA_PATH
def main():
    print("Welcome to Data Analysis!!")
    pm = ProfileManager(DATA_PATH)
    dataset_name = pm.pandasProfiler.dataset_name
    dataset_columns = pm.pandasProfiler.columns
    print(f"Dataset Name is {dataset_name}")
    print(f"Dataset Columns are {dataset_columns}")

if __name__ == "__main__":
    main()