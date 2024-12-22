from pathlib import Path


def load_file(day: int = 0) -> str:
    file_path = Path(f"data/{day:02d}_input.txt")
    return file_path.read_text()
