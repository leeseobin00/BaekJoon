import math
import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
day = math.ceil((V - A) / (A - B)) + 1

print(day)