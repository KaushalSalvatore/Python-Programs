def missing_number(list_1):
    missing_elements = []
    for ele in range(list_1[0], list_1[-1]+1):
        if ele not in list_1:
            missing_elements.append(ele)
    print(missing_elements)
            
if __name__=='__main__':
    arr = [1,  2, 5,  6,  7,  8,  9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72,
            73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84,
            85, 86, 87, 88, 89, 91, 93, 94, 95, 96,
            97, 98, 99, 100
        ]
    missing_number(arr)