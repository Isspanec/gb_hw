# ������-1:
# ��� ������, ����������� ������������� ������ �������, �������� ����� ������,
# ���������� �������� ����� ���������� ����� ��������� ��������� ������,
# �� ������ ���� ���������� ���������� ����� �� ����� ���������� ����� �
# ���� ����� ������ ������ ����� �������
# ������: ����: [2, -5, 8, 9, -25, 25, 4]   ���������: [3, 5, 2]

try:
    num_lst = input("������� ������ ����� �����, �������� �������� �������� ��� ���������: ")
    num_lst = list(map(int, num_lst.replace(',', ' ').split()))
    print(f"����: {num_lst}")
    num_lst_new = []
    for num in num_lst:
        if num >= 0:  # ���� �� ����� ����� ������� �� ����������� ���������� ������
            square_root = num ** 0.5
            if square_root - int(square_root) == 0:  # ���� ���������� ���������� ����� �� ����� ���������� �����
                num_lst_new.append(int(square_root))
    print(f"���������: {num_lst_new}")
except ValueError:
    print("�� ����� �������� ������")

# ������-2: ���� ���� � ������� dd.mm.yyyy, ��������: 02.11.2013.
# ���� ������ ������� ���� � ��������� ����, ��������: ������ ������ 2013 ����.
# ���������� ���������� (2000 ����, 2010 ����)

MONTH = {
    1: "������",
    2: "�������",
    3: "�����",
    4: "������",
    5: "���",
    6: "����",
    7: "����",
    8: "�������",
    9: "��������",
    10: "�������",
    11: "������",
    12: "�������",
}
DAY = {
    1: "������",
    2: "������",
    3: "������",
    4: "��������",
    5: "�����",
    6: "������",
    7: "�������",
    8: "�������",
    9: "�������",
    10: "�������",
    11: "������������",
    12: "�����������",
    13: "�����������",
    14: "�������������",
    15: "�����������",
    16: "������������",
    17: "������������",
    18: "��������������",
    19: "�������������",
    20: "���������",
    21: "��������������",
    22: "��������������",
    23: "��������������",
    24: "����������������",
    25: "�������������",
    26: "��������������",
    27: "���������������",
    28: "���������������",
    29: "���������������",
    30: "���������",
    31: "��������������"
}
date = input("������� ���� � ������� dd.mm.yyyy: ")
try:
    date = list(map(int, date.split(".")))  # ��������� ������ ���� [dd, mm, yyyy]
    print(f"{DAY[date[0]]} {MONTH[date[1]]} {date[2]} ����")
except ValueError:
    print("�� ����� �������� ������")
except KeyError:
    print("�� ����� �������� ������")

# ������-3: �������� ��������, ����������� ������ ������������� ������ �������
# � ��������� �� -100 �� 100. � ������ ������ ���� n - ���������.
# ���������:
# ��� ��������� ���������� ����� ����������� ������� randint() ������ random

import random
try:
    n = int(input("������� �������� ���������� ��������� ������: "))
    lst = [random.randint(-100, 100) for x in range(0, n)]
    print(f"��������������� ������: {lst}")
except ValueError:
    print("�� ����� �������� ������")

# ������-4: ��� ������, ����������� ������������� ������ �������.
# �������� ����� ������, ���������� �������� �����: 
# �) ��������������� �������� ��������� ������:
# ��������, lst = [1, 2, 4, 5, 6, 2, 5, 2], ����� �������� lst2 = [1, 2, 4, 5, 6]
# �) �������� ��������� ������, ������� �� ����� ����������:
# ��������, lst = [1 , 2, 4, 5, 6, 2, 5, 2], ����� �������� lst2 = [1, 4, 6]

try:
    num_lst = input("������� ������ ����� �����, �������� �������� �������� ��� ���������: ")
    num_lst = list(map(int, num_lst.replace(',', ' ').split()))
    print(f"�������� ������: {num_lst}")
    lst_a = list(set(num_lst))
    print(f"�) ��������������� �������� ��������� ������: {lst_a}")
    lst_b = [x for x in num_lst if num_lst.count(x) == 1]
    print(f"�) �������� ��������� ������, ������� �� ����� ����������: {lst_b}")
except ValueError:
    print("�� ����� �������� ������")