from rich.console import Console
from rich.table import Table
from rich.align import Align
import pandas as pd
import matplotlib.pyplot as plt

def display_header(city_name):
    console.print(f"[white]Weather Forecast for [/white]\n [cyan]{city_name} [/cyan]", style="bold", justify="center")

def display_current_weather(current_weather):
    table= Table(title="Current Weather", show_header=True, header_style="bold cyan")

    display_current=current_weather.copy()
    display_current.rename(columns={"time": "Time", "temperature_2m": "Temperature (°C)","apparent_temperature":"Apparent Temperature (°C)", "precipitation":"Percipitation (mm)", "cloud_cover":"Cloud Cover (%)", "wind_speed_10m":"Wind Speed (mph)", "wind_direction_10m":"Wind Direction (°)", "soil_temperature_0cm":"Soil Temperature (°C)"}, inplace=True)

    for key in display_current.columns:
        table.add_column(key, style="", justify="left")

    for index, row in current_weather.iterrows():
        table.add_row(*[str(v) for v in row.tolist()])

    console.print(Align.center(table))

def display_hourly_weather(hourly_weather):
    table= Table(title="Hourly Weather", show_header=True, header_style="bold cyan", row_styles=["white", "color(8)"])

    display_hourly=hourly_weather.copy()
    display_hourly.rename(columns={"time": "Time", "temperature_2m": "Temperature (°C)","cloud_cover":"Cloud Cover (%)", "wind_speed_10m": "Wind Speed (mph)" ,"precipitation": "Percipitation (mm)"}, inplace=True)

    for key in display_hourly.columns:

        table.add_column( key, style="", justify="left")

    for index, row in hourly_weather.iterrows():
        table.add_row(*[str(v) for v in row.tolist()])

    console.print(Align.center(table))

def display_graphs(hourly_weather):
    fig, ax = plt.subplots(2,2)

    ax[0,0].plot(hourly_weather["time"].str[11:16], hourly_weather["temperature_2m"], color="red")
    ax[0,0].set_title("Temperature (°C)")
    ax[0,0].set_xlabel("Time")
    ax[0,0].set_ylabel("Temperature (°C)")

    ax[0,1].plot(hourly_weather["time"].str[11:16], hourly_weather["cloud_cover"], color="blue")
    ax[0,1].set_title("Cloud Cover (%)")
    ax[0,1].set_xlabel("Time")
    ax[0,1].set_ylabel("Cloud Cover (%)")

    ax[1,0].plot(hourly_weather["time"].str[11:16], hourly_weather["wind_speed_10m"], color="green")
    ax[1,0].set_title("Wind Speed (mph)")
    ax[1,0].set_xlabel("Time")
    ax[1,0].set_ylabel("Wind Speed (mph)")

    ax[1,1].plot(hourly_weather["time"].str[11:16], hourly_weather["precipitation"], color="purple")
    ax[1,1].set_title("Percipitation (mm)")
    ax[1,1].set_xlabel("Time")
    ax[1,1].set_ylabel("Percipitation (mm)")
    

    plt.show()





console=Console()


if __name__ == "__main__":
    test_current_weather = pd.DataFrame([{
    "time": "2026-09-14T09:15",
    "interval": 900,
    "temperature_2m": 19.7,
    "apparent_temperature": 20.9,
    "precipitation": 0.0,
    "cloud_cover": 94,
    "wind_speed_10m": 10.1,
    "wind_direction_10m": 231,
    "soil_temperature_0cm": 21.5
    }])
    test_hourly_weather = pd.DataFrame({
    "time": ["2026-09-14T00:00", "2026-09-14T01:00", "2026-09-14T02:00", "2026-09-14T03:00"],
    "temperature_2m": [17.6, 17.3, 17.3, 17.2],
    "cloud_cover": [100, 100, 82, 100],
    "wind_speed_10m": [6.5, 5.8, 6.5, 6.5],
    "precipitation": [0.0, 0.0, 0.0, 0.0]
})
    display_header("London")
    display_current_weather(test_current_weather)
    display_hourly_weather(test_hourly_weather)
    display_graphs(test_hourly_weather)