from services.internal.managers.profilerManager import(
    ProfileManager
)
def display_basic_details(pm: ProfileManager):
    print(f" dataset no features: {pm.pandasProfiler.basicDetails.no_features}")
    print(f" dataset no datapoints: {pm.pandasProfiler.basicDetails.no_datapoints}")
    print(f" dataset no duplicate datapoints: {pm.pandasProfiler.basicDetails.no_duplicates}")
    print(f" dataset no missing cells: {pm.pandasProfiler.basicDetails.no_missing_cells}")
    print(f" dataset no numerical features: {pm.pandasProfiler.basicDetails.no_num_features}")
    print(f" dataset no categorical features: {pm.pandasProfiler.basicDetails.no_cat_fetures}")
    print(f" dataset no text features: {pm.pandasProfiler.basicDetails.no_text_features}")

def display_features(pm: ProfileManager,type):
    if type == "Numeric":
        print(f" dataset numerical features are: {pm.pandasProfiler.basicDetails.num_features}")
    elif type =="Categorical":
        print(f" dataset categorical features are: {pm.pandasProfiler.basicDetails.cat_features}")