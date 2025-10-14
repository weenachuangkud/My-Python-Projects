import numpy as np
import matplotlib.pyplot as matplot
import pandas as pd
from random import randint, choice

def main():
    names : list[list[str]] = [
        ["Iphone", "Mobile Phone"],
        ["Keyboard", "Computer Equipments"],
        ["Doll", "Toy"]
    ]
    data = np.array([
        [item, catagory, randint(1, 100) if item == "Doll" else randint(1000,10000)]
        for item, catagory in [choice(names) for _ in range(10)]
    ])
    df = pd.DataFrame(data, columns=["Names", "Categorys", "Prices"])
    print(df)
    print(df.dtypes)
    df["Prices"] = df["Prices"].astype(int)
    sorted_df = df.sort_values(by="Prices")
    matplot.figure(figsize=(10,6))
    matplot.bar(sorted_df["Names"], sorted_df["Prices"], color=["skyblue" if x != "Doll" else 'pink' for x in sorted_df["Names"]], width=0.5)
    matplot.title("Random Item Prices")
    matplot.xlabel("Item")
    matplot.ylabel("Price")
    matplot.show()

if __name__ == "__main__":
    main()
