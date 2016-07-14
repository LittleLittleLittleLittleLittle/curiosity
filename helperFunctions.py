


def findSubSequence(seq, thresold):
    n = len(seq)
    currSum = 0
    startIndex = []
    for i in range(1, n):
        if seq[i] >= seq[i-1]:
            currSum += 1
            if currSum == thresold:
                startIndex += [i]
                currSum = 0
                continue
        else:
            currSum = 0

    return startIndex


### test
# seq = [1,3,7,22,4,15,17,17,18,20,3,5,6,2,4,2,5,6,3,4,5,6,7,8,9]
# ind = findSubSequence(seq, 5)
# for i in ind:
#     print seq[i]