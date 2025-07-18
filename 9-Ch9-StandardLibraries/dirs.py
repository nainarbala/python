from pathlib import Path

path = Path()

print(path.home())
print(path.is_dir())

print(path.iterdir())

# for dir in path.iterdir():
#     print(dir)

dirs = [p for p in path.iterdir() if p.is_dir()]
print(dirs)

py_files = [p for p in path.glob("**/*.py")]
print(py_files)