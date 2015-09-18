pythagProducts upto = [a * b * c |
                       a <- [1..upto],
                       b <- [a..upto],
                       let c = upto - a - b,
                       a*a + b*b == c*c]
main = print $ pythagProducts 1000 !! 0
