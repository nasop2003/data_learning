import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from pathlib import Path

"""東海地方（三重・愛知・岐阜・静岡）の労働力人口数（男・女）を棒グラフで表示（seaborn）"""
# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）
# 調査年：1975~2020年度

# グラフラベルの文字化け防止
plt.rcParams["font.family"] = "MS Gothic"

FILE_PATH = Path(__file__).parent.parent / "data" / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands= ",")
print(df.dtypes)
print(f"\n{df.columns}")
print(f"\n{df.index}")
print(f"\n{df.values}")

labor_man = "労働力人口（男）"
total_man = df.groupby("地域")[labor_man].sum()
print(f"\n{total_man.map("{:,.0f}".format)}")

labor_woman = "労働力人口（女）"
total_woman = df.groupby("地域")[labor_woman].sum()
print(f"\n{total_woman.map("{:,.0f}".format)}")

data = pd.DataFrame({
    "男性": total_man,
    "女性": total_woman
})

# DataFrameを縦持ち（long format）に変換
data_long = data.reset_index().melt(
    id_vars="地域",
    value_vars=["男性", "女性"],
    var_name="性別",
    value_name="労働力人口"
)

print(data_long)

plt.figure(figsize=(10,5)) # 幅・高さ
plt.title("1975～2020年度までの東海地方の労働力人口（性別）")

ax = sns.barplot(
    data=data_long,
    x="地域",
    y="労働力人口",
    hue="性別"
)

# y軸のラベル「労働力人口」を縦書きに変更（縦に読めるように）
ax.set_ylabel("\n".join("労働力人口"), rotation=0, labelpad=20)

# y軸の数値をコンマ付きですべて表示
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

plt.show()