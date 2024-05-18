def solution(n, arr1, arr2):
    text = []

    for i, j in zip(arr1, arr2):
        num = str(format(i | j, 'b'))
        num = num.rjust(n, '0')

        num = num.replace('0', ' ')
        num = num.replace('1', '#')

        text.append(num)
        
    return text