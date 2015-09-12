import Data.List
import qualified Data.Map as Map
import Data.Numbers.Primes

frequency :: Ord a => [a] -> Map.Map a Int
frequency list = Map.fromList $ map (\l -> (head l, length l)) (group (sort list))

factorsMaps n = map (frequency . primeFactors) [2..n]
resultFactorCounts n = Map.unionsWith max $ factorsMaps n
resultFactors n = map (\a -> fst a ^ snd a) $ Map.toList (resultFactorCounts n)
result n = product $ resultFactors n

main = print $ result 20
