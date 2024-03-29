from datetime import date
from pathlib import Path
import shutil
import sys

if __name__ == "__main__":
    try:
        dir_name = "day" + sys.argv[1]
    except IndexError:
        dir_name = "day" + str(date.today())[-2:]

    curr_dir = Path(__file__).parent
    new_dir = curr_dir.parent / dir_name
    try:
        shutil.copytree(curr_dir / "template", new_dir)
    except FileExistsError:
        pass

    print(f"Created: {(new_dir / '__main__.py').resolve()}")