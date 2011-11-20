(defn gcd [a b]
  (cond
   (= a b) a
   (> a b) (recur (- a b) b)
   :else (recur (- b a) a)))

(defn lcm [a b]
  (/ (* a b) (gcd a b)))

(reduce lcm (range 11 21))

