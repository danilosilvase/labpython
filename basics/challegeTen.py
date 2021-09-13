
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    n = int(input().strip())
    s = 0
    t = 0
    while n > 0:
        rem = n % 2
        n = n // 2
        if rem == 1:
            s = s + 1
            if s >= t:
                t = s 
        else:
            s = 0
    print(t)





# if __name__ == '__main__':

#     n = int(input().strip())
#     # print(bin(n))
#     lista = list((bin(n)))
#     # print(type(lista))
#     count = 1
#     bigger = 0
#     binarios=[1]
#     separator = ", "
#     for indice, valor in enumerate(lista):
#         # if indice > 1:
#             if valor == lista[indice-1] and int(valor) != 0 :
#                 count = count + 1
#                 if count > bigger:
#                     # print("valor: {}".format(valor))
#                     binarios.append(valor)
#                     bigger = count
#             else:
#                 count = 1
    
#     result = [str(integer) for integer in binarios]
#     print(result)
#     a_result = "".join(result)
#     print(a_result)
#     b_result = int(a_result, 2)
#     print(b_result)
#     print(count)
    
# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     n = int(input())

#     rmd = []
    
#     while n > 0:
#         rm = n % 2
#         n = n//2
#         rmd.append(rm)
    
#     count,result = 0,0
    
#     for i in range(0,len(rmd)):
#         if rmd[i] == 0:
#             count = 0
#         else:
#             count +=1
#             result = max(result,count)
    
#     print(result)
    
    
