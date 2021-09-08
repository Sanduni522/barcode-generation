import random
import pandas as pd

def whole(row):
    seq1 = row['Sequence']
    seq2 = row['Other']
    reverse = ''.join(reversed(seq2))
    p = 'GGAAAC'
    q = 'CUUCGG'
    a = 'AAA'
    t = 'TTT'
    g = 'GGG'
    c = 'CCC'
    x = random.randint(0,1)
    if x < 0.5:
        whole1 = seq1 + p + reverse
        y = random.randint(1,5)
        if y <= 2:
            whole11 = whole1 + a
            return whole11
        elif y >= 2 and y <= 3:
            whole12 = whole1 + t
            return whole12
        elif y >= 3 and y <= 4:
            whole13 = whole1 + g
            return whole13
        elif y >= 4:
            whole14 = whole1 + c
            return whole14
    else:
        whole2 = seq1 + q + reverse
        y = random.randint(1, 5)
        if y <= 2:
            whole21 = whole2 + a
            return whole21
        elif y >= 2 and y <= 3:
            whole22 = whole2 + t
            return whole22
        elif y >= 3 and y <= 4:
            whole23 = whole2 + g
            return whole23
        elif y >= 4:
            whole24 = whole2 + c
            return whole24

df = pd.read_excel('Book2.xlsx')
df['Whole'] = df.apply(lambda row: whole(row), axis=1)
print(df)

df.to_excel('Book3_new.xlsx',index=False)
