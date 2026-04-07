print("chai aur python")

def chai(n):
    print(n)

chai("leamon tea")

chai_one = "leamon tea"
chai_two = "ginger tea"
chai_three = "masala chai"


import copy

chai = [[chai_one, chai_two, chai_three]]

chai_copy = copy.deepcopy(chai)
print(chai)
print(chai_copy)
chai_copy[0][0] = "green tea"
print(chai)
print(chai_copy)
chai_shallow_copy = copy.copy(chai)
chai_shallow_copy[0][0] = "black tea"
print(chai)
print(chai_shallow_copy)


a =[[1,2,3],[4,5,6]]

b = copy.deepcopy(a)  #deep copy
c = copy.copy(a)  #shallow copy

a[0][0] = 999
print(a)
print(b)
print(c)

