import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
"""東海地方（三重・愛知・岐阜・静岡）の労働力人口を年代ごとに折れ線グラフで表示"""
# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）
# 調査年：1975~2020年度

#グラフの文字化け防止
plt.rcParams["font.family"] = "MS Gothic"

FILE_PATH = Path(__file__).parent.parent / "data" / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands=",")
df["調査年"] = df["調査年"].str.replace("年度", "").astype(int)

print(df.dtypes)
print(f"total: {df["労働力人口"].sum():,}")

#東海地方のdataframe
data_mie = df[df["地域"] == "三重県"]
data_aichi = df[df["地域"] == "愛知県"]
data_gihu = df[df["地域"] == "岐阜県"]
data_shizuoka = df[df["地域"] == "静岡県"]

#東海地方のx軸（調査年：1975~2020年度）
survey_year = "調査年"
x_mie = data_mie[survey_year]
x_aichi = data_aichi[survey_year]
x_gihu = data_gihu[survey_year]
x_shizuoka = data_shizuoka[survey_year]

#東海地方のy軸（労働力人口）
labor = "労働力人口"
y_mie = data_mie[labor]
y_aichi = data_aichi[labor]
y_gihu = data_gihu[labor]
y_shizuoka = data_shizuoka[labor]

plt.figure(figsize=(15,6)) #幅・高さ

plt.plot(x_mie, y_mie, label="三重県")
plt.plot(x_aichi, y_aichi, label="愛知県")
plt.plot(x_gihu, y_gihu, label="岐阜県")
plt.plot(x_shizuoka, y_shizuoka, label="静岡県")

y_total = y_mie.values + y_aichi.values + y_gihu.values + y_shizuoka.values
print(f"max: {y_total.max():,}")
print(f"min: {y_total.min():,}")

#y軸（労働力人口）の表示形式を変更。今回は百万単位の数字をコンマ付きで表示
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

plt.xlabel("調査年")
plt.ylabel("労働力人口")
plt.xlim(1975, 2020)
plt.ylim(0, 5000000)
plt.title("1975年~2020年までの東海地方の労働力人口")
plt.legend()
plt.show()