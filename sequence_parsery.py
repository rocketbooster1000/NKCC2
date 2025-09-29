import pandas as pd

# df = pd.read_csv("D/D-filtered.csv")
df = pd.read_csv("F/F-filtered.csv", usecols=["seq"])
df2 = pd.DataFrame(columns=["id", "seq"])

i = 0
for s in df["seq"]:
    s_array = s.split("/")
    df2 = df2._append({"id": i, "seq": s_array[1]}, ignore_index=True)
    i += 1
df2.to_csv("F/F-sequence_parsed.csv", index=False)
