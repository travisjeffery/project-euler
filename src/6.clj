(use 'clojure.contrib.generic.math-functions)

(- (sqr (reduce + (range 1 101))) (reduce + (map sqr (range 1 101))))
