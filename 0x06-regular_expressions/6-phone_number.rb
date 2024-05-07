#!/usr/bin/env ruby

# The regular expression must match a 10 digit phone number
# The ^ and $ symbols anchor the pattern to the start and end
# of the string respectively.
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/^\d{10}$/).join("")
