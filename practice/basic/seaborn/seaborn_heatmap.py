import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from pathlib import Path

"""東海地方（三重・愛知・岐阜・静岡）の労働力人口数（男・女）をヒートマップで表示（seaborn）"""
# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）
# 調査年：1975~2020年度

# グラフの文字化け防止（日本語表示）
plt.rcParams["font.family"] = "MS Gothic"

FILE_PATH = Path(__file__).parent.parent / "data" / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands=",")
print(df.dtypes)
print(f"\n{df.columns.tolist()}")

labor_man = "労働力人口（男）"
total_man = df.groupby("地域")[labor_man].sum()
print(f"\n{total_man}")

labor_woman = "労働力人口（女）"
total_woman = df.groupby("地域")[labor_woman].sum()
print(f"\n{total_woman}")

data = pd.DataFrame({
    "労働力人口（男性）": total_man,
    "労働力人口（女性）": total_woman
})

print(f"\n{data}")

plt.figure(figsize=(7,5)) # 幅・高さ
plt.title("1975～2020年度の労働力人口（性別）の総数")

ax = sns.heatmap(
    data,
    annot=True,
    fmt=",.0f",
    cmap="Blues",
)

# y軸の項目を横並びで表示
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
# y軸のラベル「地域」を非表示
ax.set_ylabel("")

plt.show()