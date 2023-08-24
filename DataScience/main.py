from services.internal.managers.profilerManager import(
    ProfileManager
)
from utils.displayUtils import(
    display_basic_details,
    display_features
)
from config import DATA_PATH

def main():
    print("Welcome to Data Analysis!!")
    pm = ProfileManager(DATA_PATH)
    display_basic_details(pm)
    display_features(pm,"Numeric")
    display_features(pm,"Categorical")
    
if __name__ == "__main__":
    main()