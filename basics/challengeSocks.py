 
 
def sockMerchant(n, ar):
    pairSocks = []
    ar.sort()
    count = 0 
    qtdPairs = 0
    enable = False
    for index, socks in enumerate(ar):
        if len(ar) != 1:
            if enable == False and socks == ar[index - 1]:
                pairSocks.append(1)
                enable = True
            else:
                enable = False               
                     
    return len(pairSocks)

if __name__ == '__main__':
    # ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    ar = [100]
    sockMerchant(1, ar)
