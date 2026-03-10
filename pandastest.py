import pandas as pd
a=pd.Series([12,45,67,89])
print(a)
a=pd.Series([66,88,99],index=["math","it","cs"])
print(a)
print(a["math"])
d={"ali":65,"khan":87,"jawad":99}
da=pd.Series(d)
print(da)
s=pd.Series([10,20,30,40,50],index=["a","b","c","d","e"])
print(s.values)
print(s.index)
print(s.dtype)
print(s.shape)
print(s.size)
print(len(s))
print(s.sum())
print(s.mean())
print(s.max())
print(s.min())
print(s.std())
print(s.describe())
s2=s*2
print(s2)
print(s[s>20])

d=pd.DataFrame({
"name":["ali","usman","jawad"],
 "age":[23,24,21],"dept":["it","cs","datscience"],
 "salry":[2200,6000,5000]
})
print(d)
print(d.shape)
print(d.dtypes)
print(d.columns)
print(d.index)
print(d.describe())
print(d.describe(include="all"))
print(d.info())

# dataset

df=pd.read_csv("airline_ticket_prices_dataset.csv")
print(df.describe())
df.info()
print(df.head())
print(df[["Airline","Class"]])

d=pd.DataFrame({
"name":["ali","usman","jawad"],
 "age":[23,24,21],"dept":["it","cs","datscience"],
 "salry":[2200,6000,5000]
})
d.index=["r0","r1","r2"]
print(d.loc["r0":"r1"])
print(d.loc["r1","salry"])
d=d.reset_index(drop=True)
print(d.iloc[0])
h=d[d["salry"]>3000]
print(h)
s=d[d["dept"].isin(["it"])]
print(s)
d2=d.set_index("name")
print(d2.loc["jawad"])
d3=d.reset_index("name")
d4_m=d.set_index(["name","dept"])
print(d4_m.loc["cs"])






df=pd.read_csv("airline_ticket_prices_dataset.csv")
print(df.head())
print(df.tail(2))
print(df.sample())
print(df.shape)
print(df.describe())
print(df.columns.tolist())
print(df.index.tolist())
print(df["Class"].unique())
print(df["Class"].nunique())
print(df["Class"].value_counts(normalize=True))
d=df.sort_values("Price_USD",ascending=False)
print(d.head())
print(df.nlargest(2,"Price_USD"))
print(df.nsmallest(2,"Price_USD"))
df["Airline"]=df["Airline"].apply(str.upper)
print(df.head())
def label_Price_USD(columns):
    if columns["Price_USD"]>=5349.65:
        return "high"
    elif columns["Price_USD"]>=2070.30:
        return "midlle"
    else:
        return "low"
df["b"]=df.apply(label_Price_USD,axis=1)
print(df[["b"]])



import pandas as pd
import numpy as np
df=pd.read_csv("winequalityN.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(np.mean(df["alcohol"]))
good=df[df["quality"]>6]
print(good.head())
print(df["quality"].max())





# import pandas as pd
import numpy as np
df=pd.read_csv("loan_dataset_20000.csv")
print(df.head())
print(df.isnull().sum())
print(np.mean(df["monthly_income"]))
approved=df[df["loan_paid_back"]== 1]
print(approved)
print(approved.shape[0])




# superstore
# import pandas as pd
import numpy as np
df=pd.read_csv("train.csv")
print(df.head())
print(df["Sales"].sum())
print("avrege",np.mean(df["Sales"]))
print(df.loc[df["Sales"].idxmax()])
highsales=df[df["Sales"]>1000]
print(highsales.head())




# Titanic
import pandas as pd
import numpy as np
df=pd.read_csv("tested.csv")
print(df.head())
print(df["Survived"].value_counts())
print("age average",np.mean(df["Age"]))
print(df.columns)
female=df[df["Sex"]=="female"]
print(female.head())
age=df[df["Age"]>30]
print(age.head())
print(df.groupby("Sex")["Survived"].mean())
femalesurvivor=df[(df["Sex"]=="female")&(df["Survived"]==1) ]
print("femalesurvivor" ,femalesurvivor.head())
print(df.shape)


df=pd.read_csv("data.csv")
print(df.head()) #5 rows
print(df.shape)   #column and rows
print(df.tail)     #last 5 rows
print(df.sample)     #random rows
print(df.info())        #info
print(df.dtypes)
print(df.describe())   #statatistical data
print(df["price"].mean())
print(df["price"].max())
print(df["price"].min())
print(df["price"].std())
print(df[df["price"]>50000])
print(df[df["bedrooms"]>3])
print(df[(df["price"]>500000)& (df["bedrooms"]>3)])
print(df["price"])
print(df.sort_values("price",ascending=True))
print(df.isnull().sum())
df=df.fillna(0)
print(np.mean(df["price"]))
print(np.median(df["price"]))
print(np.sqrt(df["price"]))
print(df.duplicated().sum())
print(np.percentile(df["price"],25))
print(np.log(df["price"]))



# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("tested.csv")
sns.histplot(df["Age"], kde=True)

plt.show()
sns.countplot(x="Survived", data=df)
plt.show()


sns.boxplot(x="Pclass", y="Age", data=df)
plt.show()


sns.scatterplot(x="age",y="Fare",data=df)
plt.show()