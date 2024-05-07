#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /hb?t?n/,
# which matches 'h', followed by an optional 'b',
# followed by an optional 't', and ending with 'n'.
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/hb?t?n/).join

# This script takes one argument from the command line and outputs
# all occurrences of the pattern 'hb?t?n' in that argument.
