# Greedy algorithm
# Slightly different version compared to John Guttag's book

# Each item has a name, value and weight
# We also calculate the raw value, value density and inverse of the weight
# We are trying to fit as many things as possible with the constraints that we have 
class Item(object):
    
    def __init__(self,nam, val, wgt):
        self.name = nam
        self.value = val
        self.weight = wgt
    
    def getname(self):
        return self.name
    
    def getvalue(self):
        return self.value

    def getweight(self):
        return self.weight
    
    def __str__(self):
        result = '{ ' + self.name + ' & ' + str(self.value) + ' & ' + str(self.weight) + ' }' 
        return result
    
    def weightinv(self):
        return 1.0/self.getweight()

    def density(self):
        return self.getvalue()/self.getweight()


def greedy(items, maxweight, keyfunction):
    cp_items = sorted(items, key = keyfunction, reverse = True)
    #want to create a new list rather than mutate the existing one.
    result = []
    totalvalue = 0.0
    totalweight = 0.0
    for i in range( len(cp_items) ):
        if (totalweight + cp_items[i].getweight() ) <= maxweight:
            result.append(cp_items[i]) #add to your list
            totalweight = totalweight + cp_items[i].getweight()
            totalvalue =  totalvalue + cp_items[i].getvalue()
    
    return (result, totalvalue)

def createlist(names, values, weights):
    finallist = []
    for i in range(len(values)):
        finallist.append(Item(names[i], values[i], weights [i]))
    return finallist

def testgreedy(items, maxweight, keyfunction):
    taken, val = greedy(items, maxweight, keyfunction)
    print('Total value is ', val)
    for item in taken:
        print('  ', item)

#Function to test everything
def testfunction(items, maxweight = 20):  
    print('By Size:')
    testgreedy(items, maxweight, Item.getvalue)
    
    print('By Weight:')
    testgreedy(items, maxweight, Item.weightinv)
    
    print('By Density:')
    testgreedy(items, maxweight, Item.density)

#Test it out
names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
values = [175, 90, 20, 50, 10, 200]
weights = [10, 9, 4, 2, 1, 20]
items = createlist(names, values, weights)
testfunction(items, 30)