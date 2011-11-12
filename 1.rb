puts (1...1000).select {|x| x % 3 == 0 or x % 5 == 0}.reduce(:+)
