#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /hbt*n/,
# which matches 'h', followed by zero or more occurrences of 'b',
# followed by 't', and ending with 'n'.
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/hbt*n/).join
