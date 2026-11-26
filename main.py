import os

LINE = (
    "At 2 a.m. after my first night shift, I lifted the plate off my father's "
    "scallion-oil noodles, steaming, and ate standing up, coat still on, "
    "slurping so as not to wake him asleep at the table."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
