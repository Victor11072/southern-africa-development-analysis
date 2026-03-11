import pandas as pd
#Rank fucntion for indicator
def indicator_rank(df, start_row, step, countries, col_position=-1):
    values = []
    
    for i in range(len(countries)):
        value = df.iloc[start_row + i*step, col_position]
        values.append(value)
        
    result = pd.DataFrame(values, columns=["2024_GDP"])
    result["country"] = countries
    result.set_index("country", inplace=True)
    # Rank values (largest = rank 1)
    result["rank"] = result["2024_GDP"].rank(ascending=False)
    return result
