def num_cols_distribution (numerical_dataframe):
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    for i in numerical_dataframe.columns:
        # Crea dos gráficos de Seaborn
        plt.figure(figsize=(12, 3))  # Tamaño de la figura
    
        # Primer gráfico
        plt.subplot(1, 2, 1)  
        sns.histplot(numerical_dataframe[i], bins = 50, kde = True, color = 'blue')

        # Segundo gráfico
        plt.subplot(1, 2, 2)  
        sns.boxplot(x = numerical_dataframe[i])

        plt.tight_layout()  # Ajusta el diseño para evitar superposiciones
        plt.show()  # Muestra la figura

def outliers (numerical_dataframe, upper_percentil, lower_percentil):
    import pandas as pd
    import numpy as np

    # Checking how many values will be removed if the outliers are removed
    for i in numerical_dataframe.columns:
        iqr = np.percentile(numerical_dataframe[i],upper_percentil) - np.percentile(numerical_dataframe[i],lower_percentil)
        upper_limit = np.percentile(numerical_dataframe[i],upper_percentil) + 1.5*iqr
        i, round (upper_limit, 0)


def log_transfom_clean (x):
    import numpy as np
    import pandas as pd

    if np.isfinite(x) and x!=0:
        return np.log(x)
    else:
        return np.NAN # We are returning NaNs so that we can replace them later
    
def tree_pruning (x):
    def tree_cleaning (dataset):
    import pandas as pd
    import numpy as np
    
    # Columns to be deleted
    dataset = dataset.drop (columns=['x_etrs89', 'y_etrs89', 'tipus_element', 'espai_verd', 'adreca', 'nom_castella', 'nom_catala',
                    'data_plantacio', 'tipus_aigua', 'tipus_reg', 'geom', 'catalogacio', 'codi_barri', 'nom_barri', 'codi_districte'])
    
    # Rename columns
    dataset = dataset.rename(columns={'codi': 'ID', 'latitud': 'LATITUDE',
                            'longitud': 'LONGITUDE', 'cat_especie_id': 'SPECIES_ID',
                            'nom_cientific': 'CIENTIFIC_NAME', 'categoria_arbrat': 'CATEGORY',
                            'nom_districte': 'DISTRICT'})
    
    # Checking for null values
    nulls = pd.DataFrame(round(dataset.isna().sum()/len(dataset)*100, 2))
    nulls = nulls.reset_index()
    nulls.columns = ['Column Name', 'Percentage Null Values']
    nulls.sort_values(by='Percentage Null Values', ascending = False)

    # If the resulting dataframe contains less than 1% of NaN values, they will be removed.
    for i in range (len(nulls)):
        if 0 < nulls['Percentage Null Values'].iloc[i] < 1:
            dataset.dropna(inplace=True)
        
    return dataset