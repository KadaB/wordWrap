# wordWrap
memoized recursive wordWrap algorithm

A basic recursive word wrap algorithm using memoized recursive function instead of DP...

It's an exhaustive(global) recusive algorithm that calculates all possible line breaks and returns with the breaks of minimal raggedness. The global optimization minimizes over the 'least raggedness'. The raggedness is defined as(according to Knut) the left space between the words in a line and the maximum line width squared. ( '12 45 78  ' max width 10 => left spaces = 2 => raggedness = squared(2) = 4 )

The algorithm is recursive, but because of the caching of the recursion-call results the optimal paths can be reused (reoccurences), which leads to a acceptable runtime.
  
  
    ['AAA', 'BB', 'CC', 'DDDD'], line width = 6
      First line:
      Possible linebreaks for line 1:  
        (1): ['AAA'], chars: 3, raggedness = square(6 - 3) = square(3) = 9
        (2): ['AAA', 'BB'] chare: 3+2+1(whitespace) = 6, raggedness = square(6-6) = square(0) = 0
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
      
    For line 2 the case (1) would be:
      (4) ['BB']
      (5) ['BB', 'CC' ]
      (6) ['BB', 'CC', 'DDDDD'], to large for the line, so only (4) and (5)
      
    And the other recursion call for (2) for Line 2:
      (7) ['CC']
      (8) ['CC', 'DDDDD'] being to large for the line, only (7)
      
    The functione getIndicesForWordsInLine(i) basically calculates all the possible words fitting in a line, till
    the maximum line width is reached (starting at index for wordset i). It doesn return the set of words themselves,
    but instead the indices. (Here in the example we will work with the sets, because it's easier to read). The
    algorithm itselt will recurse over those wordsets, it investigate itself, if the rest of the line will fit into
    a line (So every line break index for a line gets associated to a score, since it will hold the spaces left
    to the maximum line width).

    If you run a recursion and would give out the output for each level of recursion you would get something like:
    (with lvlOfRecursion: [line: scoring] )
    
    0: ['AAA': 9, 'AAA BB': 0]
        1: ['BB': 16, 'BB CC': 1]
            2: ['CC': 16]
                3: ['DDDDD': 1]
            2: ['DDDDD': 1]
        1: ['CC': 16]
            2: ['DDDDD': 1]
		
    Here your can see that the cases ['CC': 16] and ['DDDDD': 1] reoccure. Since they have the same scoring,
    every line below it will have the same optimal linebreaks, since there are no other ways to break the lines
    from there on. The recursion will calculate the exact same breaks from there on with the same scoring.
    
    If the algorithm would see ['DDDDD': 1] then he could technically simple reuse the calucation.
    
    Since ['DDDDD': 1] is the end of the recursion(recursion terminal) it means it's garuanteed that from there
    on there is no less expensive path (['DDDDD': 1] being the minimum for with least raggedness at that level).
    
    The same goes for ['CC': 16], since it's on a higher level, we spare even more recursive calls and could
    use the result, once we have encountered it and cleared all possible linebreaks from there on. When we
    go back to lvl1 ['BB CC': 1] we can chose now between ['CC': 16], ['DDDDD': 1]... ['DDDDD': 1] has the lower
    score, so we can use that. ['DDDDD': 1] also is a terminal, which means from there on there is no way
    that there is a path with a lesser score.. Which assures the minimal scoring. ['CC': 16] on the other hand
    leads to ['DDDDD': 1] and has no other paths than ['DDDDD': 1], which is a terminal, which means that there
    is no other path than the "minimal" we have chosen to this point (this principle is the core to guarantee
    that we pick the least cost for each path and is the core argument for the prove of Dijkstra's Algorithm
    - "if we had a shorter path, we would have taken it at this point", combine with the guarantee of the 
    terminal [which leaves no question if there is a more optimal path] this makes the recursive algorithm (and
    also all DP-Algorithms possible.). So the upper levels have a guarantee that they are picking between the
    lowest path and there is no other path they are missing. Which inables us to optimize over all linebreaks,
    but also enables us to cache the results when we come back from a recursion (post fix). The first time we 
    have a result for a recursion call, we can cache it. And the recursions can pick between calculating the
    new path or grapping it from the cache (which is done in the cacheOrRecurse-function). If an optimal result
    is in the cache we don't need to refill for that level, because through the terminal and backwards
    calculation we are sure to already have the optimal solution in the cache, which serves as our reoccurences.

    Effectively we could only these calls
    0: ['AAA': 9, 'AAA BB': 0]
        1: ['BB': 16, 'BB CC': 1]
            2: ['CC': 16]
                3: ['DDDDD': 1]
            2: ----
        1: ----
            2: ----
		
    Reusing these reoccurrences once we guaranteed that they are the optimal path from there on reduces
    the runtime from an exponential to a quadratic
