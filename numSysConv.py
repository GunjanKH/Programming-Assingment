def numSysCon(numSys,decNum):
    msg="Please provide valid inputs.binary,octal or hexadecimal"
    if(numSys.lower()=="binary"):
        return bin(decNum)
    elif(numSys.lower()=="octal"):
        return oct(decNum)
    elif(numSys.lower()=="hexadecimal"):
        return hex(decNum)
    else:
        return msg

