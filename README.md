# wordWrap
memoized recursive wordWrap algorithm

A basic recursive word wrap algorithm using memoized recursive function instead of DP...

It's an exhaustive(global) recusive algorithm that calculates all possible line breaks and returns with the breaks of minimal raggedness. The global optimization minimizes over the 'least raggedness'. The raggedness is defined as(according to Knut) the left space between the words in a line and the maximum line width squared. ( '12 45 78  ' max width 10 => left spaces = 2 => raggedness = squared(2) = 4 )

The algorithm is recursive, but because of the caching of the recursion-call results the optimal paths can be reused (reoccurences), which leads to a decent runtime.

