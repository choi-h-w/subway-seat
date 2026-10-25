import sys
import json
from pathlib import Path

import requests

sys.path.append(str(Path(__file__).resolve().parents[1]))
from config import get_key

key = get_key("SEOUL_KEY_POSITION")
line = "2호선"
url = f"http://swopenAPI.seoul.go.kr/api/subway/{key}/json/realtimePosition/0/5/{line}"

res = requests.get(url, timeout=10)
print("상태 코드:", res.status_code)

data = res.json()
print("최상위 키:", list(data.keys()))
print(json.dumps(data, ensure_ascii=False, indent=2)[:2500])
