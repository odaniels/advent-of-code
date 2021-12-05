from datetime import date
from pathlib import Path
import shutil

dir_name = str(date.today())[-2:]

curr_dir = Path(__file__).parent
new_dir = curr_dir / dir_name
try:
    shutil.copytree(curr_dir / "template", new_dir)
except FileExistsError:
    pass

print(f"Created: {(new_dir / '__main__.py').resolve()}")