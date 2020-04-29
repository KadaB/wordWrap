# wordWrap
memoized recursive wordWrap algorithm

A basic recursive word wrap algorithm using memoized recursive function instead of DP...

It's an exhaustive(global) recusive algorithm that calculates all possible line breaks and returns with the breaks of minimal raggedness. The global optimization minimizes over the 'least raggedness'. The raggedness is defined as(according to Knut) the left space of the words including whitespaces to the maximum line width squared.

The algorithm is recursive, but because of the caching of the recursion-call results the optimal paths can be reused (reoccurences).

