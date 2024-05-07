#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /^h.n$/,
# which matches 'h' at the start of the string,
# followed by any single character, and ending with 'n'.
# The ^ and $ symbols anchor the pattern to the start and end
# of the string respectively.
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/^h.n$/).join
