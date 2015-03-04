class Formula(object):
    
    def __init__(self, subformulas):
        self.subformulas = subformulas

    def subf(self):
        return self.subformulas

    def toString(self):
        return ""

    def eval(self, i):
        return False


class Variable(Formula):
    def __init__(self, name):
        Formula.__init__(self, [])
        self.name = name

    def toString(self):
        return self.name

    def eval(self, i):      # dopln exception
        return i[self.name]

class Negation(Formula):
    def __init__(self, formula):
        Formula.__init__(self, [formula])

    def toString(self):
        return "-"+self.originalFormula().toString()

    def originalFormula(self):
        return self.subf()[0]

    def eval(self, i):      # dopln exception
        return not self.originalFormula().eval(i)

class Disjunction(Formula):
    def __init__(self, subformulas):
        Formula.__init__(self, subformulas)

    def toString(self):
        temp = ""
        for f in self.subformulas:
            temp += f.toString()+"|"
        return "("+temp[:-1]+")"

    def eval(self, i):
        for f in self.subformulas:
            if f.eval(i):
                return True
        return False

class Conjunction(Formula):
    def __init__(self, subformulas):
        Formula.__init__(self, subformulas)

    def toString(self):
        temp = ""
        for f in self.subformulas:
            temp += f.toString()+"&"
        return "("+temp[:-1]+")"

    def eval(self, i):
        for f in self.subformulas:
            if not f.eval(i):
                return False
        return True



class BinaryFormula(Formula):
    def __init__(self, left, right):
        Formula.__init__(self, [left, right])
    def leftSide(self):
        return self.subformulas[0]
    def rightSide(self):
        return self.subformulas[1]

class Implication(BinaryFormula):
    def toString(self):
        return "("+self.leftSide().toString()+"=>"+self.rightSide().toString()+")"

    def eval(self, i):
        return not self.leftSide().eval(i) or self.rightSide().eval(i)

class Equivalence(BinaryFormula):
    def toString(self):
        return "("+self.leftSide().toString()+"<=>"+self.rightSide().toString()+")"

    def eval(self, i):
        return self.leftSide().eval(i) == self.rightSide().eval(i)
