import pandas as pd

def other(row):
    seq = row['Sequence']
    seq4 = seq.replace("A","X").replace("T","A").replace("G","Q").replace("C","G").replace("X","T").replace("Q","C")
    return seq4

df = pd.read_csv('Book1.csv')
df['Other'] = df.apply(lambda row: other(row), axis=1)
print(df)

df.to_excel('Book2_new.xlsx',index=False)