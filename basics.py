from taipy import Gui
import pandas as pd

title = "Stock Simulator"
path = "logo.jpeg"

company_name = ""
min_price = ""
max_price = ""

data = {
    "Date": pd.date_range("2024-01-01", periods=4, freq="D"),
    "Min": [-22, -19.7, 2.7, 6.5],
    "Max": [-8.6, -8.2, 12.0, 13.5],
}


def stock(state):
    print("Hey, hello stock analyst")
    print(state.company_name)
    print(state.min_price)
    print(state.max_price)

    with open("data.txt", "w") as f:
        f.write(f"{state.company_name},{state.min_price},{state.max_price}")


page = """
<|text-center |
<|{path}|image|>

<|{title}|hover_text="Welcome to Stock Screener"|>

Name of Stock: <|{company_name}|input|>

Min Price: <|{min_price}|input|>

Max Price: <|{max_price}|input|>

<|Run Simulation|button|on_action=stock|>

|>

<|{title}|hover_text="Your Simulation"|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>
"""

if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)
