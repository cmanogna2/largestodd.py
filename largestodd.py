s = input().strip()

result = ""

# Traverse from the end to find the last odd digit
for i in range(len(s) - 1, -1, -1):
    if int(s[i]) % 2 == 1:
        result = s[:i + 1]
        break

print(result)
