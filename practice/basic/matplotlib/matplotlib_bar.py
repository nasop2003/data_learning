import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path
"""東海地方（三重・愛知・岐阜・静岡）の労働力人口（男・女）数を棒グラフで表示"""
# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）
# 調査年：1975~2020年度

#グラフラベルの文字化け防止
plt.rcParams["font.family"] = "MS Gothic"

FILE_PATH = Path(__file__).parent.parent / "data" / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands=",")
print(df.dtypes)

#東海地方すべての男性労働力人口
labor_man = "労働力人口（男）"
total_man = df.groupby("地域")[labor_man].sum()
print(f"\n{total_man.map("{:,.0f}".format)}")

#東海地方すべての女性労働力人口
labor_woman = "労働力人口（女）"
total_woman = df.groupby("地域")[labor_woman].sum()
print(f"\n{total_woman.map("{:,.0f}".format)}")

data = pd.DataFrame({
    "男性": total_man,
    "女性": total_woman
})

ax = data.plot(kind="bar", stacked=False, figsize=(5,5))

#x軸の文字を横向きに変更、y軸の表示形式を変更（コンマ付きで全桁表示）
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))

plt.title("1975～2020の労働力人口数（性別）")
plt.tight_layout()
plt.show()