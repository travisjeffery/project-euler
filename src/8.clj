(use '[clojure.contrib.duck-streams :only (read-lines)])

(def digits
  (map #(Integer/parseInt (str %)) (reduce str (read-lines "8-digits.txt"))))

(loop [p digits acc []]
  (if (seq p)
    (recur (drop 1 p) (conj acc (apply * (take 5 p))))
    (apply max acc)))
