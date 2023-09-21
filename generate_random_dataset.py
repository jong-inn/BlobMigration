
import numpy as np
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data")

def main(
    start_date: str,
    end_date: str,
    periods: int
):
    dates = pd.date_range(start=start_date, end=end_date, periods=periods)
    cols = ["col" + str(i) for i in range(22)]
    
    dataset = pd.DataFrame(index=dates, data=np.random.rand(periods, len(cols)), columns=cols)

    try:
        DATA_PATH.mkdir()
    except FileExistsError:
        pass

    dataset.to_csv(DATA_PATH.joinpath("random_dataset.csv"))
    print(f"Generated a random dataset.")


if __name__ == "__main__":
    start_date = "20000101"
    end_date = "20230920"
    periods = 1000000
    
    main(
        start_date=start_date,
        end_date=end_date,
        periods=periods
    )