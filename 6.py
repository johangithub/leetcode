"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        d={}
        for i in range(numRows):
            d[i] = ''
        i=0
        while i < len(s):
            if i % (numRows + numRows-2) ==0:
                tmp = s[i:i+numRows]
                for j in range(len(tmp)):
                    d[j]+= tmp[j]
                i += numRows
                # print(tmp)
            else:
                row = numRows - 1 -i % (numRows-1)
                # print(s[i], row)
                d[row].append(s[i])
                i += 1
        ans = ''
        # print(d)
        for i in range(numRows):
            ans += ''.join(d[i])
        return ans

    # @pharrellyhy
    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)