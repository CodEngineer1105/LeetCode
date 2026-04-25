class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        counter=0
        if dividend<0 and divisor>0:
            div = divisor
            count = 0
            while dividend+div<=0:
                dividend+=div
                div+=div
                if count>1:
                    counter+=count
                    count+=count
                else:
                    count+=2
                    counter+=1
                if dividend+div>0:
                    div = divisor
                    count = 0
            return -counter
        elif dividend>0 and divisor<0:
            div = divisor
            count = 0
            while dividend+div>=0:
                dividend+=div
                div+=div
                if count>1:
                    counter+=count
                    count+=count
                else:
                    count+=2
                    counter+=1
                if dividend+div<0:
                    div = divisor
                    count = 0
            return -counter
        elif dividend<0 and divisor<0:
            div = divisor
            count = 0
            while dividend-div<=0:
                dividend-=div
                div+=div
                if count>1:
                    counter+=count
                    count+=count
                else:
                    count+=2
                    counter+=1
                if dividend-div>0:
                    div = divisor
                    count = 0
            if counter>=2147483648:
                return 2147483647
            return counter
        else:
            div = divisor
            count = 0
            while dividend-div>=0:
                dividend-=div
                div += div
                if count>1:
                    counter+=count
                    count+=count
                else:
                    count+=2
                    counter+=1
                if dividend-div<0:
                    div = divisor
                    count = 0
            if counter>2147483647:
                return 2147483647
            return counter
        return counter
