
in_str = input("input id.. \n")
in_pw = input("input pw.. \n")
real_id_1 = "11"
real_id_2 = "12"

if real_id_1 == in_str or real_id_2 == in_str:
    print("Hello!!")
elif real_id_1 == in_str and real_id_2 == in_str:
    print("same all")
else:
    print("who are youuuu? ")

real_id_1_pw = "1234"
if real_id_1 == in_str:
    if real_id_1_pw == in_pw:
        print("Hello!! id and pw is correct!")
    else:
        print(real_id_1 + " pwd is failed")
else:
    print("abnormal connection")

