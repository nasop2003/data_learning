import pandas as pd
from pathlib import Path

# データ出典：総務省統計局「労働力調査」（e-Stat）
# 取得データ：調査年,地域,労働力人口,労働力人口（男）,労働力人口（女）,就業者数,就業者数（男）,就業者数（女）

"""東海地方の労働人口・就業者数を割合で表示する"""
FILE_PATH = Path(__file__).parent / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands= ",")
print(df.dtypes)

#都道府県ごとに労働力人口・労働者数（性別）を割合で集計

#男性（労働力人口・就業者数）
labor_man = df.groupby("地域")["労働力人口（男）"].sum()
ratio_labor_man = labor_man / labor_man.sum() * 100

#CSV内の就業者数（男）に文字列「***」が入っているため、to_numericでNaNに変換して合計
#数字にコンマが入っているので、replaceでコンマ除去（to_numericでNaNにならないように）
df["就業者数（男）"] = df["就業者数（男）"].str.replace(",", "", regex=False)
df["就業者数（男）"] = pd.to_numeric(df["就業者数（男）"], errors="coerce")
employees_man = df.groupby("地域")["就業者数（男）"].sum()

ratio_employees_man = employees_man / employees_man.sum() * 100
print(f"labor_man : {labor_man.dtype}")

#女性（労働力人口・就業者数）
labor_woman = df.groupby("地域")["労働力人口（女）"].sum()
ratio_woman = labor_woman / labor_woman.sum() * 100

#CSV内の就業者数（女）に文字列「***」が入っているため、to_numericでNaNに変換して合計
#数字にコンマが入っているので、replaceでコンマ除去（to_numericでNaNにならないように）
df["就業者数（女）"] = df["就業者数（女）"].str.replace(",", "", regex=False)
df["就業者数（女）"] = pd.to_numeric(df["就業者数（女）"], errors="coerce")
employees_woman = df.groupby("地域")["就業者数（女）"].sum()
ratio_employees_woman = employees_woman / employees_woman.sum() * 100

print(f"labor_woman : {labor_woman.dtype}")

result_man = pd.DataFrame({
    "労働力人口（男）": labor_man.map("{:,.0f}".format),
    "割合（労働力人口）（％）": ratio_labor_man.round(1),
    "就業者数（男）": employees_man.map("{:,.0f}".format),
    "割合（就業者数）（％）": ratio_employees_man.round(1)
})

relust_woman = pd.DataFrame({
    "労働力人口（女）": labor_woman.map("{:,.0f}".format),
    "割合（労働力人口）（％）": ratio_woman.round(1),
    "就業者数（女）": employees_woman.map("{:,.0f}".format),
    "割合（就業者数）（％）": ratio_employees_woman.round(1)
})

print(result_man)
print(relust_woman)
print(f"pandas version  {pd.__version__}")