import System.Environment
import System.IO
import Data.Char

allSubs :: Int -> String -> [String]
allSubs n s
  | length s >= n = take n s : allSubs n (tail s)
  | otherwise = []

substringProduct :: String -> Int
substringProduct s = product $ map digitToInt s

main = do
     args <- getArgs
     let fname = args !! 0
     contents <- readFile fname
     let numString = (lines contents) !! 0
     print $ maximum $ map substringProduct $ allSubs 13 numString
