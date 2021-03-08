class Solution:
    def myAtoi(self, str: str) -> int:
        str.strip() #去除前面的空格
        copy=''
        n=len(str)
        for i in range(n):
            if str[i]=='+' or str[i]=='-':
                if str[i]=='-':
                    sign=-1
                copy+=str[i]
                for j in range(i+1,n):
                    if 48<=ord(str[j])<=57:
                        copy+=str[j]
                    else:
                        break
                break
                return int(copy)
            elif 48<=ord(str[i])<=57:
                for j in range(i,n):
                    if 48 <= ord(str[j]) <= 57:
                        copy += str[j]
                    else:
                        break
                break
                return int(copy)

            elif str[i]==' ':
                continue
            else:
                break
        if copy=='' or copy=='+' or copy=='-':
            return 0
        elif abs(int(copy))>2**31-1:
            return 2147483647
        elif int(copy)<-2**31:
            return -2147483648
        return int(copy)


