def check_in_k(docID,poslist1,poslist2,ans,k):
    initial = 0
    for m in range(len(poslist1)):
        for n in range(initial,len(poslist2)):
            if abs(poslist1[m] - poslist2[n]) <= k:
                ans.append([docID,poslist1[m],poslist2[n]])
            elif poslist2[n] - poslist1[m] > k:
                break
            elif poslist1[m] - poslist2[n] > k:
                initial = n + 1
    return

def merge(p1, p2, k):
    ans = []
    i = 0
    j = 0
    while(i < p1['DF'] and j < p2['DF']):
        if(p1['doclist'][i]['docID'] == p2['doclist'][j]['docID']):
            check_in_k(p1['doclist'][i]['docID'],p1['doclist'][i]['poslist'],p2['doclist'][j]['poslist'],ans,k)
            i += 1
            j += 1
        elif(p1['doclist'][i]['docID'] < p2['doclist'][j]['docID']):
            i += 1
        else:
            j += 1
    return ans

if __name__ == "__main__":
    #
    test1 = {'term':'test1',
             'DF':3,
             'doclist':[{'docID':1,'frequency':4,'poslist':[1,7,10,19]},
                        {'docID':3,'frequency':3,'poslist':[3,9,13]},
                        {'docID':4,'frequency':5,'poslist':[3,4,24,25,26]}]
             }

    test2 = {'term':'test2',
             'DF':2,
             'doclist':[{'docID':1,'frequency':4,'poslist':[4,15,20,30]},
                        {'docID':4,'frequency':3,'poslist':[7,9,20]}]
             }
    ans = merge(test1,test2,4)
    print(ans)