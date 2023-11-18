def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:  # проверка на пустой список
        return ""

    result = ""
    result = ""
    l = 0
    while True:
        if l >= len(strs[0]):
            return result
        prefix = strs[0][:l+1]
        for i in range(1, len(strs)):
            if strs[i][:l+1] != prefix:
                return result  # возвращаем результат сразу после того, как найден несоответствующий префикс
        result = prefix
        l += 1
    return result


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
