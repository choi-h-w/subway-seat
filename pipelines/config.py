import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

KEY_NAMES = [
    "SEOUL_KEY_HOURLY_RIDERSHIP",
    "SEOUL_KEY_CONGESTION",
    "SEOUL_KEY_ARRIVAL",
    "SEOUL_KEY_POSITION",
    "SEOUL_KEY_DISTANCE",
    "SEOUL_KEY_TIMETABLE",
    "SEOUL_KEY_STATION",
]


def get_key(name: str) -> str:
    key = os.getenv(name, "").strip()
    if not key:
        raise RuntimeError(f"{name} 값이 .env에 없습니다.")
    return key
