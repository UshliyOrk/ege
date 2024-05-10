from itertools import product, permutations


for elem in product("10" , repeat=6):
	elem = "".join(elem)
	print(elem, elem[:3], elem[3:], sep ="..")


