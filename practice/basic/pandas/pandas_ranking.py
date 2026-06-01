import pandas as pd
from pathlib import Path
"""東海地方（三重・愛知・岐阜・静岡）の全労働力人口・就業者数を合計し、ランキング付けする"""

# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）
# 調査年：1975~2020年度

FILE_PATH = Path(__file__).parent / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands=",")


# 労働力人口
labor = "労働力人口"
labor_total = df.groupby("地域")[labor].sum()

# 就業者数
employees = "就業者数"
employees_total = df.groupby("地域")[employees].sum()

result = pd.DataFrame({
    "労働力人口": labor_total,
    "就業者数": employees_total
})

sorted_result = result.sort_values(["労働力人口", "就業者数"], ascending=False).reset_index()
sorted_result.index = range(1, len(sorted_result) + 1)
sorted_result.index.name = "順位"

# reset_index()で数字が文字列になるため、数字カラムだけに絞って.map()を適用
for col in [labor, employees]:
    sorted_result[col] = sorted_result[col].map("{:,.0f}".format)
    
print(result.dtypes)
print(len(sorted_result))
print(f"\n{sorted_result}")
