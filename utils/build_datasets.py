# Build datasets
import siconfipy
import pandas as pd
import os

# Build br_cods dataset
df = siconfipy.get_info()

# Fix Type: `capital` to numeric type
df.astype({"capital": "int32"})

# Fix `regiao`: for `uf` == 'TO' replace `regiao` to 'NO'
df.loc[df["uf"] == "TO", "regiao"] = "NO"

# Fix `regiao`: for `cod_ibge == 17` replace `regiao` to 'NO'
df.loc[df["cod_ibge"] == 17, "regiao"] = "NO"

# Save csv
df.to_csv(os.getcwd() + "/siconfipy/data/" + "br_cods.csv", index=False)
