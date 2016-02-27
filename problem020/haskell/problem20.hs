import Data.Char

sumDigits x = sum $ map digitToInt (show x)
main = print $ sumDigits (product [1..100])
