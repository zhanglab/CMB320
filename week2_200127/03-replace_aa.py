protein = "VLSPADKTNV"
print('original protein: {}'.format(protein))
# replace valine with tyrosine
print('Replace V with Y: {}'.format(protein.replace("V", "Y")))
# we can replace more than one character
print('Replace VLS with YMT: {}'.format(protein.replace("VLS", "YMT")))
# the original variable is not affected
print('Original protein does not change after replace activity: {}'.format(protein))
