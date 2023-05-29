#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Octal:
    def __init__(self, size):
        if size <= 0 or size > 100:
            raise ValueError()
        self.digits = [0] * size

    def __str__(self):
        octal_string = ''.join(map(str, self.digits[::-1]))
        return octal_string

    def __add__(self, rhs):
        if not isinstance(rhs, Octal):
            raise ValueError()

        size = max(len(self.digits), len(rhs.digits))
        result = Octal(size)
        self.add_lenght(rhs)

        carry = 0
        for i, item in enumerate(result):
            sum_digits = self.digits[i] + rhs.digits[i] + carry
            result.digits[i] = sum_digits % 8
            carry = sum_digits // 8

        if carry > 0:
            result.digits.append(carry)

        return result

    def __lt__(self, rhs):
        if not isinstance(rhs, Octal):
            raise ValueError()

        size = max(len(self.digits), len(rhs.digits))
        self.add_lenght(rhs)

        for i in range(size - 1, -1, -1):
            if self.digits[i] < rhs.digits[i]:
                return True
            elif self.digits[i] > rhs.digits[i]:
                return False

        return False

    def __eq__(self, rhs):
        if not isinstance(rhs, Octal):
            raise ValueError()

        self.add_lenght(rhs)
        return self.digits == rhs.digits

    def __getitem__(self, index):
        if 0 <= index <= len(self.digits):
            return self.digits[index]
        else:
            raise IndexError("Index out of range")

    def add_lenght(self, rhs):
        while len(self.digits) != len(rhs.digits):
            if len(self.digits) > len(rhs.digits):
                rhs.digits.append(0)
            if len(self.digits) < len(rhs.digits):
                self.digits.append(0)


if __name__ == '__main__':
    num1 = Octal(4)
    num1.digits = [7, 5, 3, 1]
    print(f"num1: {num1}")

    num2 = Octal(3)
    num2.digits = [2, 4, 6]
    print(f"num2: {num2}")

    num3 = Octal(3)
    num3.digits = [7, 3, 5]
    print(f"num3: {num3}")

    sum_num = num1 + num2
    print(f"num1 + num2: {sum_num}")

    print(num2 > num3)
    print(num2 == num3)
