clc
%������ � �������
%���� �������� � ������� ������������� � ���������� ������� ����� ������
%��� �������.
format short
v1=[-2 3 7]
v2=[7 7 1]
v=[v1 v2]
%k=kz:h:kz
k=-2:0.5:1
k=-2:5 %��� 1
k=-2.9:5
A=[1 2 7; 9 2 2; 2 4 6]
%������������ �������� � ������
m=3
n=5
zeros(m,n) %������� m �� n �� �����
ones(m,n) %������� m �� n �� ������
eye(m,n) %��������� �������, �� ������� ��������� ��������
rand(m,n) %������� m �� n �� ��������� ����� ���������� �������������� �� 0 �� 1
randn(m,n) %������� m �� n �� ��������� �����
A=[1 2 3 4 5 6; 7 8 9 10 11 12; 13 14 15 16 17 18]
fliplr(A) %������������ ������� ������� A ������������ ������������ ���
flipud(A) %������������ ������ ������� � ������������ ��������������� ���
rot90(A) %������������ ������� �� 90 �������� ������ ������� �������
k=2
l=9
reshape(A,k,l) %�������� ������� k �� l ������������ ��������� �������� 
%������� A �� �������� � ������������ ������������� 
%���� ��������� �� l �������� ������ �� ������� �������� k ���������
%��� ���� ����� ��������� ������ ��������� k �� l
tril(A) %������� ������ ����������� ������� �� ������ ������� A 
%���������� ��������� ���� ������� ���������
triu(A) %������� ������� ����������� ������� �� ������ ������� A 
%���������� ��������� ���� ������� ���������
x=[-5 6 2 4]
diag(x) %��������� ��� ��������� ��������� ��������. ���� x- ������, 
%������� ���������� ������� � �������� x �� ������� ���������.
%����� ���������� �������� ������ �� ������ ��������� ��� ��������� �
%�������� ���������� ������� ��� ���� �������� ����� �����. ��� �����
%���������.

diag(x,-2)
%���� x �������, �� ������� diag ������� ������ �������, ������� ������� ��
%��������� ������� ��������� �������� ������� A

%1 ������� ������ ������ ��������� �� 70 ����� � ����� ������� �� 50 ������
v1=zeros(1,70)
z2=ones(50,1)
%������� ������� ��������� �� ��������� ����� 10 �� 10 � ��� ������� �����
%��������� �� 180 �������� �� ������� ������� � ������� ������ �����������
v=randn(10,10)
tril(rot90(rot90(v)))
