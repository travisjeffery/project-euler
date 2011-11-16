; another solution i'd better interested is using the fact that every
; 3rd fibonacci is even...

(defn even-fibonacci []
  (filter even? (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1]))))

(apply + (take-while #(< % 4000000) (even-fibonacci)))
