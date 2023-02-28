# Notes

## Author

Trevor F. Freeman

## Purpose

Just a place for some quick notes and thoughts on the book *Mastering Python for Bioinformatics* (O'Reilly, 2021, ISBN 9781098100889).

## Critiques

### Testing

This book does a fantastic job of introducing readers to testing, and especially test driven development (TDD).
However, overall I am not a fan of Youens-Clark's treatment of TDD.

My biggest critize is that I find the author recommends a style of TDD that does far too much of what I have heard called integration testing, although I am not sure if this is an official technical term.
In Chapter 6, Solution 2: Creating a Unit Test, the author writes, "The `hamming()` function is a good unit of code, and it belongs in a function with a test. In a much larger program, this would be one of perhaps dozens to hundreds of other functions, and each should be encapsulated, documented, and tested."
On its face, it makes sense to test every unit of code (read function) to make sure the expected output is produced, edge cases are handled, etc.
And it does make sense here with a very simple function such as one that computes Hamming distance which essentially only has to compare each positon of two strings and determine whether they are the same character.
However, in practice this does not make much sense for even slightly more complex functions, and to explain what I mean, I will use an example:

Consider the problem from chapter 5 of computing the GC content (percent of residues that are G or C) of a DNA sequence.
A straightfoward solution to this problem is to break it up into two steps: first count the number of GC residues, then divide the GC count by the length of the DNA sequence to get the GC content.
This could be implemented a number of ways.
Say that the first idea is to stick to the [single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle) very strictly, so these two responsibilities are put into separate functions: `count_gc()` and `compute_gc_content()`.
By Youens-Clark's usage of TDD, where every function is tested as a separate unit, the developer should write two tests: `test_count_gc()` and `test_compute_gc_content()`.
The developer writes the tests and then writes the functions so that they pass the test.
However, in benchmarking the project manager is not happy with the performance and thinks that making repeated calls to `count_gc()` from within `compute_gc_content()` is introducting unnecessary overhead, so it's worth moving the logic from `count_gc()` into `compute_gc_content()`.
The developer makes this change, cuts `count_gc()`, runs the test suite to verify everything passes, but the tests fail because `test_count_gc()` is still attempting to run `count_gc()`.

Herein lies the problem: **implementations change frequently, so writing tests at the implementation level means the test suite as to change frequently too**.
This is the case **even when the overall behavior of the program remains the same**.
So in the example where we're computing GC content, the behavior of the program is static: all we care about is computing GC content.
But the implementation could be dynamic: we might choose different ways of breaking the problem down, or different ways of reporting GC content, or have to update code when dependencies change.
If we test each unit at the implementation level, this impedes development speed for no real benefit, because since we are also testing at the level of behavior (i.e. testing that we compute the correct GC content) we are inherently checking the implementations as well.

In short, I prefer TDD targeted at testing behavior.
A principle in OOP is to program to an interface, and when it comes to TDD I prefer testing to behaviors.
