# 10, 12, 6,37

def duplicate_number(arr):
    duplicate_value=[]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if(arr[i]==arr[j]):
                duplicate_value.append(arr[i])
    return duplicate_value
            


if __name__=='__main__':
    arr = [1,  2, 5,  6,  7,  8,  9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            49, 50, 51, 52, 53, 54, 12, 56, 57, 58, 59, 60,
            61, 62, 37, 64, 65, 66, 67, 68, 70, 71, 72,
            73, 74, 75, 76, 78, 79, 80, 81, 10, 83, 84,
            85, 86, 6, 88, 89, 91, 93, 94, 95, 96,
            97, 98, 99, 100
        ]
    print(duplicate_number(arr))