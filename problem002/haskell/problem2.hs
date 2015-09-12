fibs = 0:1:zipWith (+) fibs (tail fibs)
problem2 upto = sum $ takeWhile (upto >) (filter even fibs)
main = print $ problem2 4000000
