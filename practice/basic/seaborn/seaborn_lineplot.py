import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from pathlib import Path

"""東海地方（三重・愛知・岐阜・静岡）の労働力人口を年代ごとに折れ線グラフで表示（seaborn）"""
# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）
# 調査年：1975~2020年度

# グラフの文字化け防止（日本語表示）
plt.rcParams["font.family"] = "MS Gothic"

FILE_PATH = Path(__file__).parent.parent / "data" / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands=",")
df["調査年"] = df["調査年"].str.replace("年度", "").astype(int)
print(df.dtypes)

prefs = ["三重県","愛知県","岐阜県","静岡県"]
df = df[df["地域"].isin(prefs)]

plt.figure(figsize=(11,5)) # 幅・高さ

ax = sns.lineplot(
    data=df,
    x="調査年",
    y="労働力人口",
    hue="地域",
    marker="o"
)

# y軸の数値部分をコンマ付きですべて表示
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

# y軸のラベル「労働力人口」を縦書きに変更
ax.set_ylabel("\n".join("労働力人口"), rotation=0, labelpad=20)

ax.set_xlim(1975, 2020)
plt.title("東海地方の労働力人口（1975～2020年）")
plt.show()