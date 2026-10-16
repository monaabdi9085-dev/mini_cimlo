import pandera as pa
import pandas as pd

# Datavalidering med pandera

# läsa in csv fil

df=pd.read_csv("data/ci_korningar.csv")

#print(df.columns)

schema= pa.DataFrameSchema({
    "korning_id":pa.Column(str, unique=True),
    "antal_tester":pa.Column(int,pa.Check.gt(0)),
    "byggtid_sekunder":pa.Column(float,pa.Check.gt(0), coerce=True) # corece gör så att Pandera försöker omvandla heltal till decimaltal ex 12 -> 12.0

})

schema.validate(df)
print("Datavalidering lyckades !")
# kontrollerar att datan följer reglerna 