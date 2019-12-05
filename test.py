import hashlib
import time
import sys


# UserInput = 'text'
# Difficult_Level = 3

def sha256(UserInput):
    hashResult = hashlib.sha256(UserInput.strip().encode('utf-8')).hexdigest()
    return hashResult

def CalGN(InsN, Difficult_Level, UserInput, i):
    start = time.time()
    for nonce in range(int(i), pow(2, 32), int(InsN)):
        result = sha256(sha256(UserInput + bin(nonce)[2::]))
        if result[0:int(Difficult_Level)] == '0'*int(Difficult_Level):
            end = time.time()
            t_time = end - start
            print("Text Found!!! \nNonce is: %s" % nonce)
            print("Text is: %s" % result)
            print("Total Running Time:", t_time, "seconds")
            break

if __name__ == '__main__':
    if len(sys.argv) == 5:
        CalGN(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        # CalGN(3, 4, 'text', 1)
    else:
        print("Fail: Check the argument input format!")

# def bytesToInt(bytes):
#     result = 0
#     for b in bytes:
#         result = result * 256 + int(b)
#     return result
#
#
# hash_obj = UserInput.strip().encode('utf-8')
# start = time.time()
# for counter in range (0,4294967296):
#     # Transfer the bytes to the int
#     hash_objdec = bytesToInt(hash_obj)
#     output = counter + hash_objdec
#     test = hex(output)
#     testResult = sha256(sha256(test))
#     print('trying text %d ===>', testResult)
#     counter += 1
#     end = time.time()
#     t_time = end - start
#
#     if testResult == result:
#         print("Text Found!!! Text is: %s" % test)
#         print("Total Running Time:", t_time, "seconds")
#         time.sleep(10)
#         break
# else:
#     print("Text not Found")




# 2cbb4a15c1f6b6088te1ee02676a78710635ebb12a348b593c9763277e0763ce92