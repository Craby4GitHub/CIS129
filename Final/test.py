usersNum = [-40,-40,-40]
genNum = ['Empty', 'Empty', 'Empty']

totalLoop = 0
fileOpen = open('c:\\users\\wrcrabtree\\desktop\\testfile.txt', 'w')


def triangle():

    fourth = '({})  [{}]  ({})'.format(genNum[0], usersNum[1], genNum[2])
    second = '[{}]'.format(usersNum[2]).center(int(len(fourth)/2), ' ')
    third = '[{}]'.format(usersNum[0]).center(int(len(fourth)/2), ' ')
    first = '({})'.format(genNum[1]).center(int(len(second) + len(third)), ' ')

    #print(genNum[1])
    fileOpen.write('        ' + str(genNum[1]) + '\n')
    fileOpen.write('     ' + str(usersNum[0]) + '   ' + str(usersNum[2]) + '\n')
    fileOpen.write(str((genNum[0], usersNum[1], genNum[2])) + '\n' + '\n')

outer = -40
inner = -40
inner2 = -40

while outer <= 40:
    usersNum[0] = outer
    outer += 1
    if usersNum[0] == 40:
        while inner <= 40 and outer != 0:
            usersNum[1] = inner
            inner += 1
            outer = 0
            if usersNum[1] == 40:
                while inner2 <= 40 and inner != 0:
                    usersNum[2] = inner2
                    inner2 += 1
                    inner = 0

    totalSum = int(sum(usersNum))/2
    for yes in range(3):
        floatCheck = totalSum - int(usersNum[yes])

        if isinstance(floatCheck, int):
            genNum[yes] = floatCheck
    #print(totalSum)
    triangle()

    totalLoop += 1
print(totalLoop)

