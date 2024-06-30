class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def len_of_set(results_set: set) -> int:
            len_list = list()
            for s in results_set:
                len_list.append(len(s))
            
            return max(len_list)

        # Solve empty str case:
        if s == "":
            return 0
        
        n = len(s)
        results_set = set()
        i = 0
        
        while i < n:
            # Create a new list each time:
            results_str = str()

            #If in last element, add to results_set and break loop:
            if i > n-1:
                results_set.add(results_str)
                break
            # If not in last element, check characters uniquenes in str:
            else:
                j = i
                while s[j] not in results_str:

                    results_str += s[j]
                    j += 1
                    # If at end of the str:
                    if j > n-1:
                        break
                

                results_set.add(results_str)
                print(results_str)
            i += 1
        longest_substring_lenght = len_of_set(results_set=results_set)
        return longest_substring_lenght
    

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(s="pwwkew"))

    x=1