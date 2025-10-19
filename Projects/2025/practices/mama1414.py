import pandas as pd
import matplotlib.pyplot as plt
from random import randint
# wtf am i just coded
def main():
    amount = 10
    data = pd.DataFrame(
        {"Name" : "Male"+str(i),
        "Size" : randint(5,10)}
        for i in range(1, amount+1)
    )
    plt.plot([i for i in range(1,amount+1)], data["Size"])
    plt.axhline(data["Size"].mean(), color="red")

    plt.title("Male size")
    plt.show()
    
if __name__ == "__main__":
    main()
