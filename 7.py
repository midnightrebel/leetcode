    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        rev = 0
        while x != 0:
            last_digit = x % 10
            x = x // 10
            rev = rev * 10 + last_digit

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev