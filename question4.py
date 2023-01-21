### Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# length of it_companies set
print("length of it_companies set : ", len(it_companies))
# adding company to it_company
it_companies.add("Twitter")
# removing company from it_company
it_companies.discard("Oracle")
print("it companies : ", it_companies)
print(""" remove vs discard : 
remove deletes the element from the list if not present it returns Key error, 
discard deleted the element from the list otherwise return None""")
# joining A and B sets
print("Join of A and B : ", A.union(B))
# intersection of A and B sets
print("Intersection of A and B : ",A.intersection(B))
# checking if A is subset of B
print("Is A subset of B : ", A.issubset(B))
# check if A is disjoint of B
print("Is A disjoint of B : ", A.isdisjoint(B))
# A union B and B union A
print("A union B : ", A.union(B))
print("B union A : ", B.union(A))
# symmetric difference between two sets
print("set A difference with set B : ",A.difference(B))
# deleting sets A and B
A.clear()
B.clear()
# converting age list to set
set_ages = set(age)
# comparing length of list and length of set
print("Is length of age list same of length of age set : ", len(age) == len(set_ages))
