## union

set1={1,2,3,4,5}
set2={2,6,7,8,9}
print(set1.union(set2))

print(set1 | set2)

set3={5,6,7,8,9}
print(set1.union(set2,set3))
print(set1 | set2 | set3)

sample={1,2,3,4,5,5,4,3}
print(len(sample))

## if there is only either needed we use union operation combines all unique elements

who_knows_python={'sha','naja','imma','shony'}
who_knows_django={'yaseen','sha','imma','uppa'}
print(who_knows_python | who_knows_django)


## intersection

print(set1.intersection(set2))
print(set1.intersection(set2,set3))
print(set1 & set2)
print(set1 & set2 & set3)

print(who_knows_python & who_knows_django)
print()

## intersection update
set2.intersection_update(set1)
print(set2)

## difference
print(set1.difference(set2))
print(set1 - set2)
print(set2 - set1)

## difference update

set1.difference_update(set2)
print(set1)

## symmetric difference

set3={2,3,4,6,8}
set4={2,3,1,2,3}
print(set3.symmetric_difference(set4))

set3.symmetric_difference_update(set4)
print(set3)


## set methods

## issubset

set5={6}
print(set5.issubset(set1))    ## here set1 is parent class and set 5 is child class

set6={2}
print(set6.issubset(set3))
print(set3)

##issuperset

print(set5.issuperset(set6))   ## here set5 is parent and set 6 is child class

##isdisjoint
print(set1.isdisjoint(set2))     ## no common elements = true and common elements = false



