from rich.console import Console
from rich.table import Table

def display_header(city_name):
    console.print(f"[white]Weather Forecast for [/white]\n [cyan]{city_name} [/cyan]", style="bold", justify="center")

def display_current_weather():
    pass

def display_hourly_weather():
    pass


console=Console()
console.print()

if __name__ == "__main__":
    display_header("London")