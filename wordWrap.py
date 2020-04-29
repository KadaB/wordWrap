'''
Created on 12.02.2020

@author KadaB
@license: GPL 3.0
'''

# recursive algorithm
# words, set of words
# maxL maximum line length
# cache to cache recursion results in cache
# starting index for word in words(including)
def lineBreak(words, maxL, cache, i):

    # generate possible linesbreaks beginning at word[i:] till length maxL
    # returns all linebreaks(/sentences) till line is full
    def getIndicesForWordsInLine(i):

        # count length of line with given set of words (sentence with words + whitespaces)
        def countLength(wordset):
            wordLengths = sum(len(word) for word in wordset)
            return wordLengths + len(wordset) - 1
    
        for k in range(i, len(words)):
            line = words[i:k + 1]
            size = countLength(line)
            
            if size > maxL and k > i:
                break
            
            score = maxL - countLength(line)
            # beginning word, index+1 till line is full, scoring spaces left till maxL square
            yield i, k + 1, score * score

    # combine scoring, since python can't add tuple...
    # a score for linebreak-path
    # b list indices for linebreak-path 
    def combineScoring(a, b):
        return (a[0] + b[0], a[1] + b[1])
    
    # save result of recursive call, works itself backwards form recursion terminal, 
    # so guaranteed to hold lowest score from there on
    def cacheOrRecurse(words, maxL, cache, l):
            cachedVal = cache.get(l)
            # return cached value, if none there, recurse
            return cachedVal if cachedVal else lineBreak(words, maxL, cache, l)
    
    # actual algorithm, gives set of possible breaks and scores   
    resultLines = [ combineScoring((score, [ (k, l) ]), cacheOrRecurse(words, maxL, cache, l)) 
                   if l < len(words)
                   else (score, [ (k, l) ])
                   
                   for k, l, score in getIndicesForWordsInLine(i) ]
    
    # pick lowest score, s = (score, path)
    result = min(resultLines, key=lambda s: s[0]) 
    cache[i] = result 
    return result
    
    
def printLineBreak(linebreakResult, words):
        score, lines = linebreakResult
        
        for i, j in lines:
            print(' '.join(words[i:j]))

            
if __name__ == '__main__':
    words = "AAA BB CC DDDDD".split();  # -> ['AAA', 'BB', 'CC', 'DDDD']
    printLineBreak(lineBreak(words, 6, {}, 0), words)
    
