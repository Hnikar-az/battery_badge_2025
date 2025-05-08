import csv
from pathlib import Path

from rich.prompt import Prompt

def startup(filename=Path("counter.csv")):
    if not filename.exists():
        # If the file doesn't exist, create it
        blank_dict = {"nfo": 0, "battery": 0}
        with open(filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nfo", "battery"])
            writer.writerow(blank_dict)
    else:
        # File exists on disk
        with open(filename, "r") as f:
            csv_dict = csv.DictReader(f)
        return csv_dict

def main(filename=Path("counter.csv")):
    """
    Program loop
    """
    look_for_btn = True
    with open(filename, "r") as f:
        reader = csv.DictReader(f, fieldnames=["nfo", "battery"])
        for row in reader:
            nfo_counter = int(row["nfo"])

    while look_for_btn:
        resp = Prompt.ask("NFO - Count Up (+) or Count Down (-)", choices=["+", "-"], default="+")
        if resp == "+":
            nfo_counter += 1
        else:
            nfo_counter -= 1

        print(nfo_counter)

if __name__ == "__main__":
    startup()
    main()
