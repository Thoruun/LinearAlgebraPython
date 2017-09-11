import vector as vc

my_vector = vc.Vector([8.218, -9.341])
my_vector2 = vc.Vector([-1.129, 2.111])

if my_vector.dimension != my_vector2.dimension:
    print ("Vectors are equal")
else:
    print ("Vectors are NOT equal")

print(my_vector != my_vector2)

my_vector_sum = vc.add(my_vector, my_vector2)
print(my_vector_sum)

my_vector11 = vc.Vector([7.119, 8.215])
my_vector22 = vc.Vector([-8.223, 0.878])

my_vector_sub = vc.sub(my_vector11, my_vector22)
print(my_vector_sub)

my_vector33 = vc.Vector([1.671, -1.012, -0.318])
scalar = 7.41
my_vector_sclrMult = vc.sclrMult(my_vector33, scalar)
print(my_vector_sclrMult)
# %pwd
