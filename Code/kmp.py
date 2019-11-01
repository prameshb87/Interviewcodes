def kmp(string, pattern):





def create_array(pattern):
    j, i, arr_helper = 0, 1, [0 for _ in range(len(pattern)+1)]
    while i <= len(pattern):
        if pattern[i] != pattern[j]:
            if j == 0:
                arr_helper[i] = 0
                i+=1
            else:
                j = 0:
                if pattern[i] != pattern[j]:
                    arr_helper[i] = 0
                    i+=1
                else:
                    arr_helper[i] = j+1
                    i+=1
                    j+=1
        else:
            arr_helper[i] = j+1
            i+=1
            j+=1
    return arr_helper
