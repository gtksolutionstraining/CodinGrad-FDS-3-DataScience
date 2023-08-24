import ydata_profiling as yp
class BasicDetails:
    def __init__(self,
                 reportDict: yp.ydata_profiling.model.BaseDescription):
        
        self.reportDict = reportDict
        self.no_datapoints = reportDict.table['n']
        self.no_features = reportDict.table['n_var']
        self.no_missing_cells = reportDict.table['n_cells_missing']
        self.no_duplicates = reportDict.table['n_duplicates']
        self.no_num_features = reportDict.table['types']['Numeric']
        self.no_cat_fetures = reportDict.table['types']['Categorical']
        self.no_text_features = reportDict.table['types']['Text']
        self.__get_num_features()
        self.__get_cat_features()

    def __get_num_features(self):

        self.num_features = list(filter(lambda x: \
                                        self.reportDict.variables[x]['type'] == \
                                        'Numeric',self.reportDict.variables.keys()))
    
    def __get_cat_features(self):
        self.cat_features = list(filter(lambda x: \
                                        self.reportDict.variables[x]['type'] == \
                                        'Categorical',self.reportDict.variables.keys()))
        
    ##TODO
    """
    getting Text features
    """
        
    