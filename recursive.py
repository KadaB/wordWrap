'''
Created on 12.02.2020

@author: farnsworth
'''
from prompt_toolkit.key_binding.bindings.named_commands import self_insert

class WordWrap(object):
    '''
    classdocs
    '''

    def __init__(self, Text, maxL):
        '''
        Constructor
        '''
        self.maxL = maxL
        self.text = Text
        self.words = Text.split();
        
        self.memo = {}
        
    def printLineBreak(self):
        score, lines = self.lineBreak(0)
        
        for i, j in lines:
            print(' '.join(self.words[i:j]))
            
    def getIndicesForWordsInLine(self, i):
        def countLength(words):
            wordLengths = sum( len(word) for word in words )
            return wordLengths + len(words) - 1
        
        for k in range(i, len(self.words)):
            line = self.words[i:k+1]
            size = countLength(line)
            
            if size > self.maxL and k > i:
                break
            
            score = self.maxL - countLength(line)
            yield i, k+1, score * score
    
    def lineBreak(self, i):
        def combineScoring(a, b):
            return (a[0] + b[0], a[1] + b[1])
        
        def memoize(l):
            memoized = self.memo.get(l)
            if memoized:
                return memoized
            else:
                return self.lineBreak(l)
            
        resultLines = [ combineScoring( (score, [ (k, l) ]), memoize(l) ) 
                       if l < len(self.words)
                       else ( score, [ (k, l) ])
                       
                       for k, l, score in self.getIndicesForWordsInLine(i) ]
        
        result = min(resultLines, key = lambda b: b[0])
        self.memo[i] = result
        return result
    
    def stackLineBreak(self, i):
        def combineScoring(a, b):
            return (a[0] + b[0], a[1] + b[1])
               
        stack = [ i ]
        while stack:
            l = stack.pop()
            
        return None

if __name__ == '__main__':
    Text = "AAA BB CC DDDDD"
    maxW= 6
    WordWrap(Text, maxW).printLineBreak()
    