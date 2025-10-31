from datetime import datetime

with open("last_commit.txt", "w") as f:
    f.write(f"Last commit: {datetime.now()}\n")
