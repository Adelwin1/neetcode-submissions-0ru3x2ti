from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        g = defaultdict(list)
        emailtoname = {}


        for account in accounts:
            name = account[0]
            f_email = account[1]


            for email in account[1:]:
                emailtoname[email] = name

            for email in account[2:]:

                g[f_email].append(email)
                g[email].append(f_email)
        visited = set()
        result = []

        def dfs(curr, emails):

            if curr in visited:
                return 

            visited.add(curr)
            emails.append(curr)

            for nei in g[curr]:
                dfs(nei, emails) 

        

        for email in emailtoname:

            if email not in visited:
                emails = []

                dfs(email, emails)

            
                emails.sort()
                result.append([emailtoname[email]]+ emails)

        return result
        