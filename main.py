
def algoritm(x,roadstr):

    fixes = False

    if len(roadstr) == 0 :
       roadnew = ''

    else:

        firstfind = roadstr.find('0')

        if firstfind > -1:
           # st  =roadstr[firstfind:x]
            fixes = True
            roadnew = roadstr[firstfind+x:]
    #    else:
    #        roadnew = ''

    return [roadnew,fixes]


x = int(input('x= '))
road = []
road.append(input('road ( . or 0) = '))
s = 0#int(input('s= ') )
fixes = 0

while len(road[-1]) != 0:
    ls =  algoritm(x,road[-1])
    if  ls[1]:
        fixes += 1
    road.append(ls[0])


print(f'fixes = ',fixes)
print(road)