import pandas as pd


def generate_calendar(start_date, end_date):

    dates = pd.date_range(
        start=start_date,
        end=end_date
    )


    df = pd.DataFrame({
        "date": dates
    })


    df["weekday"] = (
        df["date"]
        .dt
        .day_name()
    )


    df["month"] = (
        df["date"]
        .dt
        .month
    )

    df["year"] = df["date"].dt.year

    df["season"] = df["month"].apply(
        get_season
    )


    df["is_weekend"] = (
        df["weekday"]
        .isin(
            [
                "Saturday",
                "Sunday"
            ]
        )
    )


    return df



def get_season(month):

    if month in [12,1,2]:
        return "Winter"

    if month in [3,4,5]:
        return "Spring"

    if month in [6,7,8]:
        return "Summer"

    return "Fall"
