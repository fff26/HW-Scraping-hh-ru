import json
from segregation import get_segregation


if __name__=='__main__':
    lst = get_segregation()
    with open('new_job.json', 'w', encoding="utf-8", newline="") as f:
        json.dump(lst, f, ensure_ascii=False, indent=2)