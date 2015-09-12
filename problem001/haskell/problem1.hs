mult3or5 num = (mod num 3 == 0) || (mod num 5 == 0)
lessthan a b = a > b

problem1 upto = sum $ takeWhile (lessthan upto) (filter mult3or5 [0..])

main = print $ problem1 1000
