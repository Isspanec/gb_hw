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


# ������-3: �������� ��������, ����������� ������ ������������� ������ �������
# � ��������� �� -100 �� 100. � ������ ������ ���� n - ���������.
# ���������:
# ��� ��������� ���������� ����� ����������� ������� randint() ������ random


# ������-4: ��� ������, ����������� ������������� ������ �������.
# �������� ����� ������, ���������� �������� �����: 
# �) ��������������� �������� ��������� ������:
# ��������, lst = [1, 2, 4, 5, 6, 2, 5, 2], ����� �������� lst2 = [1, 2, 4, 5, 6]
# �) �������� ��������� ������, ������� �� ����� ����������:
# ��������, lst = [1 , 2, 4, 5, 6, 2, 5, 2], ����� �������� lst2 = [1, 4, 6]