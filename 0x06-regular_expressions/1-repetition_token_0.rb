#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /hbt{2,5}n/,
# which matches 'h', followed by 2 to 5 occurrences of 'b',
# and ending with 'n'.
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/hbt{2,5}n/).join
