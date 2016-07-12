mult3or5 num = (mod num 3 == 0) || (mod num 5 == 0)
main = print $ sum $ takeWhile (< 1000) (filter mult3or5 [0..])
