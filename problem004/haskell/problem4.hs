productsThreeDigits :: [Int]
productsThreeDigits = [x * y | x <- [100..999], y <- [x..999]]

isPalindrome :: Int -> Bool
isPalindrome x = (reverse $ show x) == show x

main = print $ maximum $ filter isPalindrome productsThreeDigits
