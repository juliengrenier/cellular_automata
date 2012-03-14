# -*- coding: utf-8 -*-

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

class cellular_automata(object):
    """
        Simple one-dimensional cellular automata
    """
    def __init__(self,config, rule=34):
        self.config = config
        self.rule = [int(i) for i in int2bin(rule,count=8)][::-1]

    def __call__(self, steps=None):
        if not steps:
            steps = (len(self.config)/2)+1
        for index in range(steps):
            yield self.display(self.config)
            temp = "0"+self.config + "0"
            r = [str(self.rule[int(temp[i:i+3],2)])for i in range(0,len(self.config))]
            self.config = "".join(r)

    def display(self,config):
        return u"".join([u" " if i == '0' else u"x" for i in config])


if __name__ == '__main__':
    from sys import argv
    if len(argv) == 3:
        _, rule, steps = argv
    elif len(argv) == 2:
        _,rule = argv
        steps = 50
    else:
        rule = 30
        steps = 50

    cc = cellular_automata( "0"*int(steps)+"1"+"0"*int(steps),rule=int(rule))

    for step in cc():
        print step
  