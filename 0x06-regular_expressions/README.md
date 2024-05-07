# Regular Expressions

Regular expressions (regex or regexp) are powerful tools for pattern matching and manipulation of text. They are widely used in various programming languages and tools for tasks such as searching, validation, and text transformation.

## Table of Contents

- [Introduction](#introduction)
- [Syntax Basics](#syntax-basics)
- [Common Patterns](#common-patterns)
- [Modifiers](#modifiers)
- [Character Classes](#character-classes)
- [Anchors](#anchors)
- [Quantifiers](#quantifiers)
- [Grouping and Capturing](#grouping-and-capturing)
- [Assertions](#assertions)
- [Examples](#examples)
- [Resources](#resources)

## Introduction

Regular expressions are sequences of characters that define a search pattern. They can contain a mix of literal characters and special symbols called metacharacters, which represent classes of characters or specify operations.

## Syntax Basics

A simple regex consists of literal characters that match themselves. For example, the regex `hello` matches the string "hello" in its entirety.

## Common Patterns

- `\d` matches any digit.
- `\w` matches any alphanumeric character.
- `\s` matches any whitespace character.
- `.` matches any character except newline.

## Modifiers

Modifiers are flags that modify the behavior of a regex pattern. Common modifiers include:

- `i`: Case-insensitive matching.
- `g`: Global matching (find all matches, not just the first).
- `m`: Multiline mode (treats beginning (^) and end ($) characters as working across multiple lines).

## Character Classes

Character classes are used to match one character from a set of characters. They are enclosed in square brackets ([]). For example:

- `[aeiou]` matches any vowel.
- `[0-9]` matches any digit.

## Anchors

Anchors are used to specify the position of a match within the text. Common anchors include:

- `^`: Matches the start of a line.
- `$`: Matches the end of a line.
- `\b`: Matches a word boundary.

## Quantifiers

Quantifiers specify the number of occurrences of the preceding element. Common quantifiers include:

- `*`: Matches zero or more occurrences.
- `+`: Matches one or more occurrences.
- `?`: Matches zero or one occurrence.
- `{n}`: Matches exactly n occurrences.
- `{n,}`: Matches n or more occurrences.
- `{n,m}`: Matches between n and m occurrences.

## Grouping and Capturing

Parentheses are used for grouping and capturing subpatterns. They can be used to apply quantifiers to multiple characters or to extract substrings from the matched text.

## Assertions

Assertions are conditions that must be met for a match to occur but do not consume any characters from the input string. Common assertions include:

- `(?=...)`: Positive lookahead (matches if ... is followed by the pattern).
- `(?!...)`: Negative lookahead (matches if ... is not followed by the pattern).
- `(?<=...)`: Positive lookbehind (matches if ... is preceded by the pattern).
- `(?<!...)`: Negative lookbehind (matches if ... is not preceded by the pattern).

## Examples

Here are some examples of regular expressions:

- Matching an email address: `/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/`
- Matching a URL: `/(https?|ftp):\/\/[^\s/$.?#].[^\s]*/`
- Matching a phone number: `/\d{3}-\d{3}-\d{4}/`

## Resources

- [Regex101](https://regex101.com/): Online regex tester and debugger.
- [MDN Web Docs - Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions): Documentation on regular expressions in JavaScript.
- [Regexr](https://regexr.com/): Another online regex tester and debugger.

Feel free to explore more resources and experiment with different regular expressions to become proficient in using them for your specific needs.
