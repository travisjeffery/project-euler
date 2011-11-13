class Fibonacci
  include Enumerable

  def initialize(boundary)
    @boundary = boundary
    @index = 0
    @sequence = {0 => 1, 1 => 1}
  end

  def each 
    @index += 1
    while fibonacci(@index) < @boundary
      yield fibonacci(@index) if block_given?
      @index += 1
    end
  end

  def fibonacci(n)
    if n < 2
      n
    else
      if @sequence.has_key?(n)
        @sequence[n]
      else
        @sequence[n] = fibonacci(n-1) + fibonacci(n-2)
      end
    end
  end
end

puts Fibonacci.new(4_000_000).select {|fibonacci| fibonacci % 2 == 0}.reduce(:+)
