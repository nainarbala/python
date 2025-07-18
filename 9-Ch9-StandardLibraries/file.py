from pathlib import Path
import shutil

path = Path("8-Ch8-Modules/ecommerce/shopping/sales1.py")
print(path.read_text())

shutil.copy("8-Ch8-Modules/ecommerce/shopping/sales1.py", "8-Ch8-Modules/ecommerce/shopping/sales1_1.py")

