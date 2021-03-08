class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        making_decimal = 10**(len(digits)-1)
        number = 0
        i = 0
        while making_decimal > 0:
            number = number + (digits[i] * making_decimal)
            making_decimal = making_decimal // 10
            i+=1
        number+=1
        return list(map(int,list(str(number))))
        