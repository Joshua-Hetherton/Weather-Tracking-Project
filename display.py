from rich.console import Console
from rich.table import Table
import pandas as pd

def display_header(city_name):
    console.print(f"[white]Weather Forecast for [/white]\n [cyan]{city_name} [/cyan]", style="bold", justify="center")

def display_current_weather(current_weather):
    table= Table(title="Current Weather", show_header=True, header_style="bold cyan")

    for key in current_weather.columns:
        table.add_column(key, style="dim", justify="left")

    for index, row in current_weather.iterrows():
        table.add_row(*[str(v) for v in row.tolist()])

    console.print(table)

def display_hourly_weather(hourly_weather):
    table= Table(title="Current Weather", show_header=True, header_style="bold cyan")

    for key in hourly_weather.columns:
        table.add_column(key, style="dim", justify="left")

    for index, row in hourly_weather.iterrows():
        table.add_row(*[str(v) for v in row.tolist()])

    console.print(table)


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