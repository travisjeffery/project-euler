main = do
  let fibs = map fst $ iterate(\(a, b) -> (b, a+b)) (1,2)
  print $ sum(takeWhile(< 4000000) (filter even fibs))
