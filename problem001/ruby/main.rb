#!/usr/bin/ruby

result = (1...1000).select do |i|
    (i % 3 == 0) or (i % 5 == 0)
end
puts result.reduce(0, :+)
