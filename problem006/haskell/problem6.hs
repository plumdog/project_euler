sumOfSquares n = sum $ map (\a -> a^2) [1..n]
squareOfSums n = b * b
  where b = sum [1..n]
result n = (squareOfSums n) - (sumOfSquares n)

main = print $ result 100
