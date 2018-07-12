
# We take in a number array arr and a potential pair sum k.
# If we fina d pair we return True, False otherwise.
def pair_sum(arr, k):
    s = set()
    for a in arr:
        if k-a in s:
            return True
        else:
            s.add(a)
        print(s)
    return False


print(pair_sum([10, 15, 3, 7],17))
