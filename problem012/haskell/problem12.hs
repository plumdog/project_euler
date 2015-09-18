import Data.List
import Data.Numbers.Primes
import qualified Data.Map as Map

frequencyCounts list = map length $ group (sort list)
numDivisors n = product [count + 1 | count <- frequencyCounts $ primeFactors n]
triangle n = n * (n + 1) `quot` 2

main = print $ (dropWhile (\n -> numDivisors n <= 500) $ map triangle [1..]) !! 0
