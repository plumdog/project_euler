import System.Environment
import System.IO


sumNums :: [String] -> Integer
sumNums lines = sum $ map (\n -> (read n :: Integer)) lines
firstDigits :: Integer -> Int -> Int
firstDigits n d = (read $ take d $ show $ n :: Int)

main = do
     args <- getArgs
     let fname = args !! 0
     contents <- readFile fname
     print $ firstDigits (sumNums (lines contents)) 10
