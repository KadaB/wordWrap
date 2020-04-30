# wordWrap
memoized recursive wordWrap algorithm

A basic recursive word wrap algorithm using memoized recursive function instead of DP...

It's an exhaustive(global) recusive algorithm that calculates all possible line breaks and returns with the breaks of minimal raggedness. The global optimization minimizes over the 'least raggedness'. The raggedness is defined as(according to Knut) the left space between the words in a line and the maximum line width squared. ( '12 45 78  ' max width 10 => left spaces = 2 => raggedness = squared(2) = 4 )

The algorithm is recursive, but because of the caching of the recursion-call results the optimal paths can be reused (reoccurences), which leads to a acceptable runtime.
  
  ['AAA', 'BB', 'CC', 'DDDD'], line width = 6
  First line:
    Possible linebreaks for line 1:
    
    (1): ['AAA'], chars: 3, raggedness = square(6 - 3) = square(3) = 9
    (2): ['AAA', 'BB'] chare: 3+1+2 = 6, raggedness = square(6-6) = square(0) = 0
    (3): ['AAA', 'BB', 'CC'], wouldn't fit into line => use the previous combinations
    
    [ (1), (2) ] = [ ['AAA'], ['AAA', 'BB'] ]
      
    Now from here on, we do the same for the second line, except that depending if we proceed with (1) or (2),
    we proceed with the words left, in case of 

      (1) = ['AAA']
      rest1 = ['BB', 'CC', 'DDDDD']. 

    In case of 

      (2) = ['AAA', 'BB']
      rest2 = ['CC', 'DDDDD']

    And that is where the recurion comes in...
    For which we solve the line breaks again, once for (1) and once for (2) which in term create
    new combinations themselves... Depending on the linebreaks you can make you got alternatives which give you
    different scores. The end score is the scores on the lines combined. The linebreaks with least score(raggedness) is
    chosen.
