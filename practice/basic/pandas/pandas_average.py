import pandas as pd
from pathlib import Path

"""都道府県ごとの就業者数（男女）の平均を割り出す"""
FILE_PATH = Path(__file__).parent / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands= ",")
print(df.dtypes)

# 就業者数（男・女）列内の文字列をNaNとして処理→数字をreplaceでint型に変換して出力
labor = "就業者数"
labor_average = df.groupby("地域")[labor].mean()

labor_man = "就業者数（男）"
col_man = df[labor_man].str.replace(",", "", regex=False)
df[labor_man] = pd.to_numeric(col_man, errors="coerce")

man_average = df.groupby("地域")[labor_man].mean()

labor_woman = "就業者数（女）"
col_woman = df[labor_woman].str.replace(",", "", regex=False)
df[labor_woman] = pd.to_numeric(col_woman, errors="coerce")

woman_average = df.groupby("地域")[labor_woman].mean()

result = pd.DataFrame({
    "就業者数平均値": labor_average.map("{:,.0f}".format),
    "男性平均値": man_average.map("{:,.0f}".format),
    "女性平均値": woman_average.map("{:,.0f}".format)
})

print(result)
print(f"pandas version  {pd.__version__}")