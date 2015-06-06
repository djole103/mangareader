from collections import Counter
from random import randrange
import math
import re
def main():

    str = "Shingeki No Kyojin"
    print(str)
    strlower = str.lower()
    print(strlower)
    finalstr = re.sub(pattern='\ ',repl='-',string=strlower)
    print(finalstr)


    # count = 0;
    # dict = {"a":1,"b":2,"c":2}
    # print(dict)
    # a = [1,2,3,4,5]
    # for x in range(1,5):
    #     print("{}".format(x))
    # #for key in dict.keys():
    # #    print(dict[key])
    # prime = True
    # for x in range(2,3):
    #     print(x)
    # N = int(input())
    # for i in range(2,N):
    #     print("Integer: {}\n".format(i))
    #     for x in range(2,math.ceil(math.sqrt(i))+1):
    #         prime = True
    #         print("Testing prime on: {}\n".format(x))
    #         if(i%x==0 and i!=x):
    #             prime = False
    #             break
    #     if prime == True:
    #         print("Prime: {}".format(i))
    #         count+=1
   # print(count)
#   randn = [randrange(10) for i in range(100)]
#   print(len(randn))
#   cntr = Counter()
#   for i in randn:
#       cntr[i]+=1
#   print(cntr)
#   print (cntr[0])



  #dict = {key: value for key,value in enumerate(cntr)}
  #print (dict)
if __name__ == "__main__":
    main()