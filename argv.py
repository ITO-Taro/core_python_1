import sys

def add_em(var_x):
	if all([i.isnumeric() for i in var_x]):
		res = sum([int(i) for i in var_x])
	else:
		res = ",".join([i for i in var_x])
	return res

print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

if __name__ == "__main__":
	print(add_em(sys.argv[1:]))
