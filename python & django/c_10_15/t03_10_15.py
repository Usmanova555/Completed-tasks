from contextlib import contextmanager
class Inf:
    def __init__(self, name, summ):
        self.name = name
        self.summ = summ
@contextmanager
def check(p):
    f = None
    try:
        f = open(p, 'r')
        l = []
        for prov in f:
            if int(prov.split()[1]) > 1000: l.append(prov)
        yield l
    except IOError as e: raise e
    finally:
        if f: f.close()
@contextmanager
def write(n):
    f = None
    try:
        f = open(n, 'w')
        yield f
    except IOError as e: raise e
    finally:
        if f: f.close()
a = []
with check('in.txt') as check1:
    for ss in check1:
        sum = 0
        k = ss.split()
        for i in [int(item) for item in k[1:]]: sum += i/7  
        a.append(Inf(k[0], round(sum)))
with write('out.txt') as write1:
    for ss in a: write.write('{ss.name} {ss.summ}')
