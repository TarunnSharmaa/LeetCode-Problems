# https://leetcode.com/problems/fizz-buzz/submissions/

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        answer = []

        # Loop for the range provided
        for i in range(1, n+1):

            if (i%3 == 0 and i%5 == 0):
                print(i)
                answer.append('FizzBuzz')

            elif i%3 == 0:
                answer.append('Fizz')

            elif i%5 == 0:
                answer.append('Buzz')

            else:
                answer.append(str(i))

        
        return answer


