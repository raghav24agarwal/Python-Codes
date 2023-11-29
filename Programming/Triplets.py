def triplets(arr, target):

    arr.sort()
    n = len(arr)
    result = []

    for i in range(0, n-2):
        j = i+1
        k = n-1


        while( j < k ):
            #print("inside while")
            currentSum = arr[i] + arr[j] + arr[k]
            if (currentSum == target):
                res = [i, j, k]
                result.append(res)
            
            elif currentSum < target:
                j += 1

            else:
                k -= 1

    print(result)


if __name__ == "__main__":
    
    n = int(input("Enter size of array: "))

    arr = list(map(int, input("Enter array elements: ").split()))

    target = int(input("Enter target sum: "))

    triplets(arr, target)