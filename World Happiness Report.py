import numpy as np
import pandas as pd
# import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)

df1 = pd.read_csv("Dünya mutluluk endeksi\2015.csv")
df2 = pd.read_csv("Dünya mutluluk endeksi\2016.csv")
df3 = pd.read_csv("Dünya mutluluk endeksi\2017.csv")
df4 = pd.read_csv("Dünya mutluluk endeksi\2018.csv")
df5 = pd.read_csv("Dünya mutluluk endeksi\2019.csv")

# her sete ilişkin incelemeleri yapalım, örneğin:

df1.columns
df2.head()
df3.shape()
df4.isnull().sum()
df5.describe().T
df3.info() 

# Aynı bilgilere ait kolonlar farklı veri setlerinde farklı şekilde isimlendirilmiş.
# Veri setlerindeki isimleri df1'e göre düzenleyelim

df3.rename(columns={"Happiness.Rank": "Happiness Rank",
            "Happiness.Score": "Happiness Score",
            "Economy..GDP.per.Capita.": "Economy (GDP per Capita)",
            "Health..Life.Expectancy.": "Health (Life Expectancy)",
            "Trust..Government.Corruption.": "Trust (Government Corruption)"},inplace=True)

df4.rename(columns={"Overall rank": "Happiness Rank",
            "Score": "Happiness Score",
            "GDP per capita": "Economy (GDP per Capita)",
            "Healthy life expectancy": "Health (Life Expectancy)",
            "Freedom to make life choices": "Freedom",
            "Perceptions of corruption": "Trust (Government Corruption)",
            "Country or region": "Country"},inplace=True)

df5.rename(columns={"Overall rank": "Happiness Rank",
            "Score": "Happiness Score",
            "GDP per capita": "Economy (GDP per Capita)",
            "Healthy life expectancy": "Health (Life Expectancy)",
            "Freedom to make life choices": "Freedom",
            "Perceptions of corruption": "Trust (Government Corruption)",
            "Country or region": "Country"},inplace=True)


# setleri birleştirmeden önce hangi yıllara ait olduklarını gösteren kolonu ekleyelim

df1["Year"] = "2015"
df2["Year"] = "2016"
df3["Year"] = "2017"
df4["Year"] = "2018"
df5["Year"] = "2019"

# Aynı ülkenin ismi farklı veri setlerinde farklı yazılmış durumda. df1'e göre düzenleyelim.
#df2'de 1 ülkenin ismi farklı yazılmış
df2[df2["Country"]=="Somaliland Region"]
df2["Country"][96] = "Somaliland region"


#df3'de 4 ülkenin ismi df1 den farklı yazılmıs,onları düzelttim,cünkü listeleri birleştirdigimizde region karşılıgı gelmiyor
df3[df3["Country"]=="Taiwan Province of China"]
df3["Country"][32] = "Taiwan"

df3[df3["Country"]=="Hong Kong S.A.R., China"]
df3["Country"][70] = "Hong Kong"

df3[df3["Country"]=="South Sudan"]
df3["Country"][146] = "Sudan"

df3[df3["Country"]=="Somalia"]
df3["Country"][92] = "Somaliland region"

#df4'te 4 ülkenin ismi farklı yazılmıs onları düzelttim
df4[df4["Country"]=="Trinidad & Tobago"]
df4["Country"][37] = "Trinidad and Tobago"

df4[df4["Country"]=="Northern Cyprus"]
df4["Country"][57] = "North Cyprus"

df4[df4["Country"]=="South Sudan"]
df4["Country"][153] = "Sudan"

df4[df4["Country"]=="Somalia"]
df4["Country"][97] = "Somaliland region"

#df5'te 5 ülkenin ismi farklı yazılmıs
df5[df5["Country"]=="Trinidad & Tobago"]
df5["Country"][38] = "Trinidad and Tobago"

df5[df5["Country"]=="Northern Cyprus"]
df5["Country"][63] = "North Cyprus"

df5[df5["Country"]=="North Macedonia"]
df5["Country"][83] = "Macedonia"

df5[df5["Country"]=="South Sudan"]
df5["Country"][155] = "Sudan"

df5[df5["Country"]=="Somalia"]
df5["Country"][111] = "Somaliland region"


# Her df'de bölge sütunu olmadıgı icin yeni bir df olusturup df1'e göre Country ve Region ekleyelim
df_region = df1[["Country", "Region"]]

# df3-df4-df5'te Region kolonu yok. Veri setinden Region kolonunu düşürmek yerine olmayan setlere de ekleyelim 
df3[df3["Region"].isnull()]
df4[df4["Region"].isnull()]
df5[df5["Region"].isnull()]

df3 = pd.merge(df3, df_region, on="Country", how="left")
df3[df3["Region"].isnull()]
df4 = pd.merge(df4, df_region, on="Country", how="left")
df4[df4["Region"].isnull()]
df5 = pd.merge(df5, df_region, on="Country", how="left")
df5[df5["Region"].isnull()]

# df'lerde bazı ülkelere ait Region kısmı NaN olarak geliyor. Bunları veri setinden atabiliriz ya da ekleyebiliriz. 
# Kendimiz ekleyelim(internet araştırması ile)

df3["Region"] = {"Taiwan Province of China": "Eastern Asia", 
                "Belize": "Latin America and Caribbean",
                "Hong Kong S.A.R., China": "Eastern Asia", 
                "Somalia": "Sub-Saharan Africa",
                "South Sudan": "Sub-Saharan Africa", 
                "Namibia": "Sub-Saharan Africa"}

df4["Region"] = {"Trinidad & Tobago": "Latin America and Caribbean",
                "Belize": "Latin America and Caribbean",
                "Northern Cyprus": "Western Europe",
                "Somalia": "Sub-Saharan Africa", 
                "Namibia": "Sub-Saharan Africa",
                "South Sudan": "Sub-Saharan Africa"}

df5["Region"] = {"Trinidad & Tobago": "Latin America and Caribbean",
                 "Northern Cyprus": "Western Europe",
                 "North Macedonia": "Central and Eastern Europe",
                 "Somalia": "Sub-Saharan Africa", 
                 "Namibia": "Sub-Saharan Africa",
                 "South Sudan": "Sub-Saharan Africa", 
                 "Gambia": "Sub-Saharan Africa"}

df_region["Country"]

# Sonradan listeye giren ülkeler ve listede olup da ismi farklı olduğu için bölgesi cıkmayan ülkeler var
# bu ülkelerin de bölgelerini tanımlayalım
s1= dict(zip(df_region["Country"],df_region["Region"]))
s2= {"Belize": "Latin America and Caribbean",
     "Namibia": "Sub-Saharan Africa",
     "Gambia": "Sub-Saharan Africa"}
s1.update(s2)  #iki listeyi birleştirdik
s1
# df_region = pd.DataFrame(s1).reset_index()
country = list(s1.keys())
region = list(s1.values())
df_region = pd.DataFrame(list(zip(country, region)),
                  columns=['Country', 'Region'])

df1["Region"].unique()

#  Tekrar merge edelim

df3 = pd.merge(df3, df_region, on="Country", how="left")
#df1.loc[df1["Region"]=='Western Europe']
#df3.loc[df3["Region"]=='Western Europe']

df3[df3["Region"].isnull()]
df3.info()

df4 = pd.merge(df4, df_region, on="Country", how="left")
df5 = pd.merge(df5, df_region, on="Country", how="left")

######### Veri seti üzerinde çalışmaya başlayabiliriz
##   bölgelere göre mutluluk skorları  ##
df1.groupby("Region").agg({"Happiness Score": "mean"}).sort_values(by="Happiness Score", ascending=False)

sns.boxplot(x="Region", y="Happiness Score", data=df1)
g1= sns.boxplot(x="Region", y="Happiness Score", data=df1)
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #x deki yazıları dik yazar
plt.show()

# GDP ekleyelim
df1_ = df1.groupby("Region").agg({"Happiness Score": "mean","Economy (GDP per Capita)": "mean"}).\
    sort_values(by="Happiness Score", ascending=False)
df1_.reset_index()

sns.scatterplot(x="Happiness Score",y="Economy (GDP per Capita)",hue="Region",style=None,data=df1_)

# 2015 de mutluluk sıralamasındaki ilk 10 ülke
df1_10 = df1.groupby("Country").agg({"Happiness Score": "mean", "Health (Life Expectancy)": "mean"}).\
    sort_values(by="Happiness Score", ascending=False).head(10)

sns.scatterplot(x="Happiness Score",y="Health (Life Expectancy)",hue="Country",style=None,data=df1_10)

#2019 da mutluluk sıralamasındaki ilk 10 ülke
df5_10= df5.groupby("Country").agg({"Happiness Score": "mean", "Health (Life Expectancy)": "mean"}).\
    sort_values(by="Happiness Score", ascending=False).head(10)

sns.scatterplot(x="Happiness Score",y="Health (Life Expectancy)",hue="Country",style=None,data=df5_10)

#######  Bütün yılları birleştirelim
df = pd.concat([df1,df2,df3,df4,df5],axis=0,ignore_index = True)  #axis=0 alt alta birlestirir
df.head()

df = df[["Country", "Region", "Happiness Rank", "Happiness Score", "Economy (GDP per Capita)", "Health (Life Expectancy)", "Freedom", "Trust (Government Corruption)", "Generosity", "Year"]]
df.info()

# yıllara görefarklı skorlara bakalım
dff1 = df.groupby("Year").agg({"Happiness Score": "mean"})
dff1.plot()

dff2 = df.groupby("Year").agg({"Economy (GDP per Capita)": "mean"})
dff2.plot()

dff3 = df.groupby("Year").agg({"Trust (Government Corruption)": "mean"})
dff3.plot()

dff4 = df.groupby("Year").agg({"Health (Life Expectancy)": "mean"})
dff4.plot()

# Bölgelere göre incelemeler
df.groupby(["Region", "Year"]).agg({"Happiness Score": "mean"})
df.groupby("Region").agg({"Happiness Score": "mean"})
sns.boxplot(x="Happiness Score", y="Region",  data=df)

df.groupby("Region")["Economy (GDP per Capita)"].mean().sort_values(ascending=False).reset_index()
sns.boxplot(x="Economy (GDP per Capita)", y="Region",  data=df)

dfr = df.groupby("Region")["Economy (GDP per Capita)", "Happiness Score"].mean().sort_values(by="Happiness Score", ascending=False).reset_index()
sns.scatterplot(x="Happiness Score",y="Economy (GDP per Capita)",hue="Region",style=None,data=dfr)

# Distopyadaki ülkeler
# df.groupby("Country")["Happiness Score"].mean().sort_values(ascending=True).reset_index().head(15)

# Para mutluluk getiriyor mu?
df_happines = df.groupby("Country").agg({"Happiness Score": "mean", "Economy (GDP per Capita)": "mean"}).sort_values(by="Economy (GDP per Capita)", ascending=False).reset_index().head(10)
sns.scatterplot(x="Happiness Score",y="Economy (GDP per Capita)",hue="Country",style=None,data=df_happines)
# df["Happiness Score"].mean()

# Hükümete güven
df_trust = df.groupby("Country").agg({"Happiness Score": "mean", "Trust (Government Corruption)": "mean"}).sort_values(by="Trust (Government Corruption)", ascending=False).reset_index().head(10)
sns.scatterplot(x="Happiness Score",y="Trust (Government Corruption)",hue="Country",style=None,data=df_trust)
#burada dikkatimi ceken Rwanda en mutsuz 4.ülke,ama Trust (Government Corruption) 'da 1.sırada

