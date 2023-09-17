import itertools

def pairs(arr,target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i]+arr[j] == target):
                pairs.append((arr[i],arr[j]))
    print(pairs)


def itertools_pairs(arr,traget):
    result = [seq for i in range(len(arr), 0, -1)
          for seq in itertools.combinations(arr, i)
          if sum(seq) == target]
    print(result)

if __name__=='__main__':
    arr = [1,3,4,5,6,7,9,8,-2,-4]
    target = 6
    # pairs(arr,target)
    itertools_pairs(arr,target)