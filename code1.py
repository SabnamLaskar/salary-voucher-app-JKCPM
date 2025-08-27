# %%
import pandas as pd

# %%
df = pd.read_excel(
    "salary voucher.xlsx",
    sheet_name="Input data(Earning & Deduction)",
    skiprows=2
)

# %%
print(type(df))

df.columns = df.columns.str.strip()

# %%
df

# %%
df = df.dropna(subset=["Cost Centre"])

# %%
df["Cost Centre"] = df["Cost Centre"].astype(int)


# %%
df

# %%
df = df.sort_values("Cost Centre")

# %%
df.head()

# %%
df.columns = df.columns.map(lambda x: str(x).strip())

# %%
df.columns

# %%
target_cols = [col for col in df.columns if "1000" in str(col) or "1003" in str(col)]

# %%
df.isnull().sum()

# %%
df["Amount"] = df[target_cols].sum(axis=1)

# %%
summary = df.groupby("Cost Centre", as_index=False)["Amount"].sum()

# %%
summary.to_excel("cost_centre_summary.xlsx", index=False)

# %%
summary.insert(0, "General Ledger", 4401010700)


# %%
summary.to_excel("cost_centre_summary.xlsx", index=False)

# %%
summary

# %%
df1=pd.read_excel('GL.xlsx')

# %%


# %%
df1 = df1.dropna()

# %%
df1.columns = df1.columns.str.strip()

# %%
df1["GL code"] = pd.to_numeric(df1["GL code"], errors="coerce")

# %%
df1["GL code"] = df1["GL code"].astype("int64")

# %%
df1.head(5)

# %%

result = df1.groupby("GL code")["Particular"].apply(lambda x: ", ".join(map(str, x))).reset_index()


# %%
result

# %%



