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