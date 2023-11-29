def pairs(arr, target):
	
	bucket = set()

	for i in arr:
		if (target-i) in bucket:
			result = [i, target-i]
			break
		else:
			bucket.add(i)

	if len(result) != 0:
		print("Pair is", result)
	else:
		print("Pair not found")

    
if __name__ == "__main__":

	n = int(input("Enter size of array "))

	arr = list(map(int, input("Enter array elemets: ").strip().split()))
	target = int(input("Enter target sum "))

	pairs(arr, target)