import Data.Char

properDivisors num = filter (\a -> num `mod` a == 0) [2..halfnum]
    where halfnum = quot num 2

sumProperDivisors num = 1 + sum (properDivisors num)

isAmicable num = (num /= sumProp) && (sumProperDivisors sumProp == num)
    where sumProp = sumProperDivisors num

main = print $ sum $ filter isAmicable [0..10000]

