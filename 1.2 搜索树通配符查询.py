def match(prefix,sufix,tree,rtree,term):
    p = tree
    ans = []
    len = prefix.__len__()
    for i in range(len):
        if prefix[i] in p:
            p = p[prefix[i]]
        else:
            p = {'VALUE':[]}
    ans += p['VALUE']

    p = rtree
    rans = []
    len = sufix.__len__()
    for i in range(len):
        if sufix[i] in p:
            p = p[sufix[i]]
        else:
            p = {'VALUE': []}
    rans += p['VALUE']

    result = [i for i in ans if i in rans and term[i].__len__() >= prefix.__len__() + sufix.__len__()]
    return result


if __name__ == "__main__":
    #测试用例的单词包括ab,ac,bca,cca,ccb，简单搜索树形结构如下：
    term = ['ab','ac','bca','cca','ccb']
    #        0    1     2     3     4
    all = [0,1,2,3,4]
    a_ = [0,1]
    b_ = [2]
    c_ = [3,4]
    bc_ = [2]
    cc_ = [3,4]
    tree = {'VALUE':all ,'a':{'VALUE':a_,'b':{'VALUE':[0]},'c':{'VALUE':[1]}}
                        ,'b':{'VALUE':b_,'c':{'VALUE':[2]}}
                        ,'c':{'VALUE':c_,'c':{'VALUE':cc_,'a':{'VALUE':[3]},'b':{'VALUE':[4]}}}}
    #反向
    a__ = [2,3]
    b__ = [0,4]
    c__ = [1]
    ac__ = [2,3]
    revetree = {'VALUE':all ,'a':{'VALUE':a__,'c':{'VALUE':ac__,'b':{'VALUE':[2]},'c':{'VALUE':[3]}}}
                            ,'b':{'VALUE':b__,'a':{'VALUE':[0]},'c':{'VALUE':[4]}}
                            ,'c':{'VALUE':c__}}

    prefix = 'c'
    sufix = 'b'
    ans = match(prefix,sufix,tree,revetree,term)
    print(prefix+'*'+sufix,'matches:',[term[i] for i in ans])
