(defn palindrome? [n]
  (= (str n) (apply str (reverse (str n)))))

(apply max (filter palindrome?
                   (for [x (range 100 1000) y (range 100 1000)]
                     (* x y))))