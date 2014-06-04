#!/usr/bin/env python3

end = 1000
ans = 0

for i in range(end):
    if (i % 3 == 0) or (i % 5 == 0):
        ans += i

print(ans)
