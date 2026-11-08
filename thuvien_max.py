import json
import os

FILE_DIEM = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diem_cao.json")

scores_easy = []
scores_medium = []
scores_hard = []


def doc_file():
    if not os.path.exists(FILE_DIEM):
        return
    try:
        with open(FILE_DIEM, "r", encoding="utf-8") as f:
            data = json.load(f)
        scores_easy.extend(data.get("Easy", []))
        scores_medium.extend(data.get("Medium", []))
        scores_hard.extend(data.get("Hard", []))
    except (json.JSONDecodeError, OSError):
        pass


def ghi_file():
    data = {"Easy": scores_easy, "Medium": scores_medium, "Hard": scores_hard}
    with open(FILE_DIEM, "w", encoding="utf-8") as f:
        json.dump(data, f)


def diem_cao_nhat(scores):
    if len(scores) == 0:
        return 0
    return max(scores)


def lay_diem_3_level():
    return diem_cao_nhat(scores_easy), diem_cao_nhat(scores_medium), diem_cao_nhat(scores_hard)


def luu_diem(level, diem):
    if level == "Easy":
        scores_easy.append(diem)
    elif level == "Medium":
        scores_medium.append(diem)
    elif level == "Hard":
        scores_hard.append(diem)
    ghi_file()


doc_file()   # chạy 1 lần lúc import