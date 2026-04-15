class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def h(c, o, e):

            if len(c)== 2*n:
                result.append(c)
                return 
            if o<n:
                h(c+"(", o+1, e)
            if e<o:
                h(c+")", o, e+1)
        h("", 0, 0)
        return result
            
        