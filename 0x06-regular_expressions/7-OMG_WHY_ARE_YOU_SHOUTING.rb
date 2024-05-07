#!/usr/bin/env ruby

# The regular expression matches only: capital letters
# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern /[A-Z]*/,
# which matches zero or more occurrences of uppercase letters (A-Z).
# It then joins all matching occurrences into a single string.
puts ARGV[0].scan(/[A-Z]*/).join
