#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /hbt+n/,
# which matches 'h', followed by 'b',
# followed by one or more occurrences of 't', and ending with 'n'.
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/hbt+n/).join
