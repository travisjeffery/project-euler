(defn primes [n]
  (loop [p 2 seq (range 2 n)]
    (if (> (* p p) n)
      seq
      (let [new-seq (filter #(or (= % p) (not= 0 (mod % p))) seq)
            new-p (first (filter #(> % p) new-seq))]
        (recur new-p new-seq)))))

(defn largest-prime-factor [n]
  (let [sqrt-of-n (int (Math/sqrt n))
        prime-factors-of-n (filter #(zero? (mod n %)) (primes sqrt-of-n))]
    (last prime-factors-of-n)))

