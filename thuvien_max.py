# Dữ liệu mẫu để test
# Sau này thay bằng danh sách của nhóm
scores_easy = []
scores_medium = []
scores_hard = []


def diem_cao_nhat(scores):
    if len(scores) == 0:
        return 0
    return max(scores)


def lay_diem_3_level():
    easy = diem_cao_nhat(scores_easy)
    medium = diem_cao_nhat(scores_medium)
    hard = diem_cao_nhat(scores_hard)

    return easy, medium, hard

def luu_diem(level, diem):
    if level == "Easy":
        scores_easy.append(diem)
    elif level == "Medium":
        scores_medium.append(diem)
    elif level == "Hard":
        scores_hard.append(diem)