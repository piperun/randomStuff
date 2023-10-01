import matplotlib.pyplot as plt
import string
import random


def test_supermany(maxnum, percent):
    refdoc = {}
    basedoc = {}
    unique_list = []
    normal_list = []

    for i in range(0, maxnum):
        if random.randint(1, 100) < percent:
            continue
        else:
            val = ''.join(random.choice(string.ascii_lowercase)
                          for _ in range(20))
            if val not in unique_list:
                unique_list.append(val)

    print(len(unique_list))
    print(unique_list)
    print(refdoc)
    return len(unique_list), maxnum


pass


def test_many(maxnum, percent):
    refdoc = {}
    lists = []
    for i in range(0, maxnum):
        if random.randint(1, 100) < percent:
            continue


def gen_list(maxnum, percent):
    list_nums = []
    for i in range(0, maxnum):
        if random.randint(1, 100) < percent:
            continue
        else:
            list_nums.append(i)
    return list_nums


def gen_dict(maxnum, percent, users, Oflag=False):
    otm = {}
    for i in range(0, users):
        if(not Oflag):
            seed = random.randint(10, maxnum)
        else:
            seed = maxnum
        otm[''.join(random.choice(string.ascii_lowercase) for _ in range(10))] = len(gen_list(seed, percent))
    return otm

def getlen(maxnum, users, percent):
    tmp = gen_dict(maxnum, users, percent)
    diclen = 0
    for key, val in tmp.items():
        diclen += tmp[key]
    return diclen

def plotit(maxnum, Oflag=False):
    ots = []
    otm = []
    users = random.randint(1, 20)
    for i in range(100):
        ots.append(len(gen_list(maxnum, 30) * users))
        otm.append(getlen(maxnum, users, 30))
    
    print(ots)
    print(otm)
    plt.plot(ots, c='#8f9805')
    plt.plot(otm)
    plt.show()
    pass


plotit(100)
# test_supermany(100, 30)


'''
def blabla():
        for i in range(0, maxnum):
        chance = random.randint(1, 100)
        if chance < percent:
            refdoc[i] = unique_list[chance - 1]
        else:
            refdoc[i] = ''.join(random.choice(string.ascii_uppercase)
                                for _ in range(20))
    pass
'''
