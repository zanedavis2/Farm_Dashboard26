import numpy as np


def classify_weather(temp, rain):

    if rain >= 0.50:
        return "Rainy"

    elif temp >= 90:
        return "Hot"

    elif temp >= 75:
        return "Sunny"

    elif temp >= 55:
        return "Mild"

    else:
        return "Cold"


def generate_weather(calendar):

    df = calendar.copy()

    temperatures = []
    rainfalls = []
    conditions = []

    previous_temp = None

    for month in df["month"]:

        # Seasonal averages

        if month in [12, 1, 2]:
            seasonal_temp = 35
            avg_rain = 0.18

        elif month in [3, 4, 5]:
            seasonal_temp = 60
            avg_rain = 0.20

        elif month in [6, 7, 8]:
            seasonal_temp = 85
            avg_rain = 0.08

        else:
            seasonal_temp = 70
            avg_rain = 0.15

        # First day

        if previous_temp is None:

            temp = np.random.normal(
                seasonal_temp,
                3
            )

        else:

            temp = (
                previous_temp
                + np.random.normal(0, 2)
            )


            temp += (
                seasonal_temp
                - temp
            ) * 0.10

        temp = round(temp, 1)

        rain = round(
            max(
                0,
                np.random.normal(avg_rain, 0.15)
            ),
            2
        )

        condition = classify_weather(
            temp,
            rain
        )

        temperatures.append(temp)
        rainfalls.append(rain)
        conditions.append(condition)

        previous_temp = temp

    df["temperature"] = temperatures
    df["rainfall"] = rainfalls
    df["weather_condition"] = conditions

    return df[
        [
            "date",
            "temperature",
            "rainfall",
            "weather_condition"
        ]
    ]
