class Solution:
    def genWord(self, num, bel, tens):
        num = int(num)
        div = num // 100
        res = ''
        if div > 0:
            res += bel[div - 1] + ' Hundred '
        rem = num % 100
        if rem > 0:
            if rem < 20:
                res += bel[rem - 1] + ' '
            else:
                div = rem // 10
                one = rem % 10
                res += tens[div - 2] + ' '
                if one != 0:
                    res += bel[one - 1] + ' '
        return res.strip()

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below20 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
                   'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 
                   'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        pre = ['', 'Thousand', 'Million', 'Billion']
        res = ''
        i = 0
        while num > 0:
            temp = num % 1000
            if temp > 0:
                resTemp = self.genWord(temp, below20, tens)
                if i > 0:
                    res = resTemp + ' ' + pre[i] + ' ' + res
                else:
                    res = resTemp + res
            num = num // 1000
            i += 1
        return res.strip()
