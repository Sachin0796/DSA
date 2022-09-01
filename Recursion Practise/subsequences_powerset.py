ans = []
def findAllSubseq(str, index, tempAns):

    if index == len(str):
        ans.append(tempAns)
        return

    # take
    findAllSubseq(str, index + 1, tempAns + str[index])

    #not take
    findAllSubseq(str, index + 1, tempAns)

findAllSubseq('abc', 0, '')
print(ans)