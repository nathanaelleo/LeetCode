def minOperations(logs: list[str]) -> int:
    depth = 0
    for log in logs:
        if log == "../":
            depth -= 1
        elif log == "./":
            depth == depth
        else:
            depth += 1
    return print(depth)

logs = ["d1/","d2/","./","d3/","../","d31/"]

minOperations(logs)


#Input: logs = ["d1/","d2/","../","d21/","./"]
#Output: 2

#Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
#Output: 3


