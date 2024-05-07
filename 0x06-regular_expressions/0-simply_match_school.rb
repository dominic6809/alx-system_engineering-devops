#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /School/,
# and joins all matching occurrences into a single string.
puts ARGV[0].scan(/School/).join
