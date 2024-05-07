#!/usr/bin/env ruby

# Outputs the result of scanning the first command-line argument (ARGV[0])
# for the regex pattern
# /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/.
# The pattern captures three groups of text enclosed within square brackets:
# - The first group after "from:"
# - The second group after "to:"
# - The third group after "flags:"
# The '?' after the '*' makes the '*' lazy,
# meaning it will match as few characters as possible.
# It then joins all matching occurrences into single string separated by commas.
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
