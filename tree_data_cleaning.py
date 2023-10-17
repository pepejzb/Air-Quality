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