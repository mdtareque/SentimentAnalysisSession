import os
def crunch(basefolder):
    newlines = []
    newlabels = []
    for file in os.listdir(basefolder):
        if file.endswith(".txt"):
            lines = [x.strip().split('##') for x in open(basefolder+file).readlines()]
            print len(lines)
            for line in lines:
                try:
                    ispos = False
                    isneg = False
                    if '+' in line[0]:
                        ispos = True
                    if '-' in line[0]:
                        isneg = True
                    if ispos and not isneg:
                        newlines.append(line[1])
                        newlabels.append(1)
                    if not ispos and isneg:
                        newlines.append(line[1])
                        newlabels.append(0)
                except:
                    print line
    print len(newlines)
    liu = open("liu_simple.txt", "w")
    for i, line in enumerate(newlines):
        liu.write(line+'\t'+str(newlabels[i])+'\n')
    liu.close()

if __name__ == '__main__':
    crunch('../../resources/bingliu data/')