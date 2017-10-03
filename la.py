import vector as vc

my_vector = vc.Vector([8.218, -9.341])
my_vector2 = vc.Vector([-1.129, 2.111])

if my_vector.dimension != my_vector2.dimension:
    print ("Vectors are equal")
else:
    print ("Vectors are NOT equal")

print(my_vector != my_vector2)

print("=========================")
my_vector_sum = vc.add(my_vector, my_vector2)
print(my_vector_sum)
print("=========================")
my_vector11 = vc.Vector([7.119, 8.215])
my_vector22 = vc.Vector([-8.223, 0.878])

print("=========================")
my_vector_sub = vc.sub(my_vector11, my_vector22)
print(my_vector_sub)
print("=========================")

my_vector33 = vc.Vector([1.671, -1.012, -0.318])
scalar = 7.41
my_vector_sclrMult = vc.sclrMult(my_vector33, scalar)
print("=========================")
print(my_vector_sclrMult)

print("=========================")

my_vector44 = vc.Vector([-0.221, 7.437])
my_vector44_magnitude = my_vector44.magnitude()

print("=========================")
my_vector444 = vc.Vector([8.813, -1.331, -6.247])
my_vector444_magnitude = my_vector444.magnitude()

print("=========================")

my_vector5 = vc.Vector([5.581, -2.136])
my_vector5_unit_vector = my_vector5.direction()

print(my_vector5_unit_vector)
print("=========================")
my_vector6 = vc.Vector([1.996, 3.108, -4.554])
my_vector6_unit_vector = my_vector6.direction()

print(my_vector6_unit_vector)

vc_dot_1 = vc.Vector([7.887, 4.138])
vc_dot_2 = vc.Vector([-8.802, 6.776])
vc_dot_3 = vc.Vector([-5.955, -4.904, -1.874])
vc_dot_4 = vc.Vector([-4.496, -8.755, 7.103])

vc_angle_rad_1 = vc.Vector([3.183, -7.627])
vc_angle_rad_2 = vc.Vector([-2.668, 5.319])
vc_angle_deg_1 = vc.Vector([7.35, 0.221, 5.188])
vc_angle_deg_2 = vc.Vector([2.751, 8.259, 3.985])

vc_dot_product1 = vc.dotProduct(vc_dot_1, vc_dot_2)
vc_dot_product2 = vc.dotProduct(vc_dot_3, vc_dot_4)

print("Dot Product 1 is:{}".format(vc_dot_product1))
print("Dot Product 2 is:{}".format(vc_dot_product2))

# vc_angle_deg_1 = vc.Vector([1, 2, -1])
# vc_angle_deg_2 = vc.Vector([3, 1, 0])

vc_angle_rad_1 = vc.angleBetween(vc_angle_rad_1, vc_angle_rad_2, inRadians=True)

print("Angle in Rad is:{}".format(vc_angle_rad_1))

vc_angle_deg_1 = vc.angleBetween(vc_angle_deg_1, vc_angle_deg_2, inRadians=False)

print("Angle in Deg is:{}".format(vc_angle_deg_1))

# %pwd
