from pathlib import Path

path1 = Path(r"c:\Program Files")
print(path1)
print(path1.absolute())
print(path1.home())
print(path1.is_file())
print(path1.exists())