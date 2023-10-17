Remove the NaN value

df2 = pd.DataFrame(df)
df2.replace([np.inf, -np.inf], np.nan, inplace=True)
df2 = df2.fillna(0)
df2
