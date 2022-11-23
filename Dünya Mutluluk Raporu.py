"""
About Dataset
Context
The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012, the second in 2013, the third in 2015, and the
fourth in the 2016 Update. The World Happiness 2017, which ranks 155 countries by their happiness levels, was released at the United Nations at an event celebrating 
International Day of Happiness on March 20th. The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness
indicators to inform their policy-making decisions. Leading experts across fields – economics, psychology, survey analysis, national statistics, health, public policy 
and more – describe how measurements of well-being can be used effectively to assess the progress of nations. The reports review the state of happiness in the world today
and show how the new science of happiness explains personal and national variations in happiness.

Content
The happiness scores and rankings use data from the Gallup World Poll. The scores are based on answers to the main life evaluation question asked in the poll. This 
question, known as the Cantril ladder, asks respondents to think of a ladder with the best possible life for them being a 10 and the worst possible life being a 0 and 
to rate their own current lives on that scale. The scores are from nationally representative samples for the years 2013-2016 and use the Gallup weights to make the 
estimates representative. The columns following the happiness score estimate the extent to which each of six factors – economic production, social support, life 
expectancy, freedom, absence of corruption, and generosity – contribute to making life evaluations higher in each country than they are in Dystopia, a hypothetical 
country that has values equal to the world’s lowest national averages for each of the six factors. They have no impact on the total score reported for each country, 
but they do explain why some countries rank higher than others.

Inspiration
What countries or regions rank the highest in overall happiness and each of the six factors contributing to happiness? How did country ranks or scores change between 
the 2015 and 2016 as well as the 2016 and 2017 reports? Did any country experience a significant increase or decrease in happiness?

What is Dystopia?

Dystopia is an imaginary country that has the world’s least-happy people. The purpose in establishing Dystopia is to have a benchmark against which all countries can 
be favorably compared (no country performs more poorly than Dystopia) in terms of each of the six key variables, thus allowing each sub-bar to be of positive width. 
The lowest scores observed for the six key variables, therefore, characterize Dystopia. Since life would be very unpleasant in a country with the world’s lowest 
incomes, lowest life expectancy, lowest generosity, most corruption, least freedom and least social support, it is referred to as “Dystopia,” in contrast to Utopia.

What are the residuals?

The residuals, or unexplained components, differ for each country, reflecting the extent to which the six variables either over- or under-explain average 2014-2016 
life evaluations. These residuals have an average value of approximately zero over the whole set of countries. Figure 2.2 shows the average residual for each country 
when the equation in Table 2.1 is applied to average 2014- 2016 data for the six variables in that country. We combine these residuals with the estimate for life 
evaluations in Dystopia so that the combined bar will always have positive values. As can be seen in Figure 2.2, although some life evaluation residuals are quite 
large, occasionally exceeding one point on the scale from 0 to 10, they are always much smaller than the calculated value in Dystopia, where the average life is rated 
at 1.85 on the 0 to 10 scale.

What do the columns succeeding the Happiness Score(like Family, Generosity, etc.) describe?

The following columns: GDP per Capita, Family, Life Expectancy, Freedom, Generosity, Trust Government Corruption describe the extent to which these factors contribute 
in evaluating the happiness in each country.
The Dystopia Residual metric actually is the Dystopia Happiness Score(1.85) + the Residual value or the unexplained value for each country as stated in the previous 
answer.

If you add all these factors up, you get the happiness score so it might be un-reliable to model them to predict Happiness Scores.
"""

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


