(defn prime? [n]
  (let [r (int (Math/sqrt n))]
    (loop [d 2]
      (cond (= n 1) false
            (> d r) true
            (zero? (rem n d)) false
            :else (recur (inc d))))))

(def primes (filter prime? (iterate inc 2)))

(defn make-seq-accumulator [[x & xs]]
  (map first (iterate
              (fn [[sum [s & more]]]
                [(+ sum s) more])
              [x xs])))

(def prime-sums
  (conj (make-seq-accumulator primes) 0))

(defn euler-50 [goal]
  (loop [c 1]
    (let [bots (reverse (take c prime-sums))
          tops (take c (reverse (take-while #(> goal (- % (last bots)))
                                            (rest prime-sums))))]
      (or (some #(when (prime? %) %)
                (map - tops bots))
          (recur (inc c))))))

