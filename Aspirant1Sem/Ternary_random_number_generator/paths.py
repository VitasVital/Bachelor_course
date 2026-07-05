# paths.py
from pathlib import Path

# Корневая папка проекта (туда, где лежит этот файл)
PROJECT_ROOT = Path(__file__).parent.resolve()

# Папка для всех выходных данных
OUTPUT_DIR = PROJECT_ROOT / "output"

def ensure_output_dir():
    """Создаёт папку output, если её нет."""
    OUTPUT_DIR.mkdir(exist_ok=True)