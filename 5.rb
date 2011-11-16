n = 20
n += 20 until (1..20).all? {|i| n % i == 0} 
puts n

