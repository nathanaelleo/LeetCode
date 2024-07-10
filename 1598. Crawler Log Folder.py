def minOperations(logs: list[str]) -> int:
    depth = 0
    for log in logs:
        if log == "../" and depth > 0:
            depth -= 1
        elif log == "./" or log == "../":
            depth == depth
        else:
            depth += 1
    return print(depth)

logs = ["./","../"]

minOperations(logs)

#https://leetcode.com/problems/crawler-log-folder/submissions/1316767629?envType=daily-question&envId=2024-07-10

#Input: logs = ["d1/","d2/","../","d21/","./"]
#Output: 2

#Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
#Output: 3


