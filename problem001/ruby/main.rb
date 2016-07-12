#!/usr/bin/ruby
puts (1...1000).select { |i| (i % 3).zero? or (i % 5).zero? }.reduce(0, :+)
