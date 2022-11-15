#!/usr/bin/env ruby
# A regular expression that is simply matches a given pattern

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
