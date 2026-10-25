from config import KEY_NAMES, get_key

for name in KEY_NAMES:
    try:
        k = get_key(name)
        print(f"{name:30s} OK  길이={len(k)}  앞4자={k[:4]}****")
    except RuntimeError:
        print(f"{name:30s} 없음")
