# Quicksort with first element as pivot

# def quickSort(A, p, r):
#     if p < r:
#         q = devide(A,p,r)
#         quickSort(A,p,q-1)
#         quickSort(A,q+1,r)

# def devide(A,p,r):
#     x = A[p]
#     i = p
#     for j in range(p+1,r+1):
#         if A[j] <= x:
#             i = i + 1
#             A[i],A[j] = A[j],A[i]
#     A[i],A[p] = A[p],A[i]
#     return i

def quickSort(lst):
    if len(lst) <= 1:
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quickSort(smaller) + [lst[0]] + quickSort(larger)



# Main Function
if __name__ == '__main__':
    A = [10,9,3,1,2,8,7,4,5,6]
    quickSort(A)
    print(A)