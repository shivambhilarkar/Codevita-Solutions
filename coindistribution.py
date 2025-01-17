# Problem Statement
# Find the minimum number of coins required to form any value between 1 to N,both inclusive.Cumulative value of coins should not exceed N. Coin denominations are 1 Rupee, 2 Rupee and 5 Rupee.Let’s Understand the problem using the following example. Consider the value of N is 13, then the minimum number of coins required to formulate any value between 1 and 13, is 6. One 5 Rupee, three 2 Rupee and two 1 Rupee coins are required to realize any value between 1 and 13. Hence this is the answer.However, if one takes two 5 Rupee coins, one 2 rupee coin and two 1 rupee coin, then too all values between 1 and 13 are achieved. But since the cumulative value of all coins equals 14, i.e., exceeds 13, this is not the answer.

# Input Format:
# A single integer value.
 

# Output Format:
# Four space separated integer values.
# 1st – Total number of coins.
# 2nd – number of 5 Rupee coins.
# 3rd – number of 2 Rupee coins.
# 4th – number of 1 Rupee coins.
 

# Constraints:
# 0 < n < 1000
# Refer the sample output for formatting

# Sample Input

#     13

# Sample Output

#    6 1 3 2

# Explanation

# The minimum number of coins required is 6 with in it:
# minimum number of 5 Rupee coins = 1
# minimum number of 2 Rupee coins = 3
# minimum number of 1 Rupee coins = 2
# Using these coins, we can form any value with in the given value and itself, like below:

# Here the given value is 13

# For 1 = one 1 Rupee coin
# For 2 = one 2 Rupee coin
# For 3 = one 1 Rupee coin and one 2 Rupee coins
# For 4 = two 2 Rupee coins
# For 5 = one 5 Rupee coin
# For 6 = one 5 Rupee and one 1 Rupee coins
# For 7 = one 5 Rupee and one 2 Rupee coins
# For 8 = one 5 Rupee, one 2 Rupee and one 1 Rupee coins
# For 9 = one 5 Rupee and two 2 Rupee coins
# For 10 = one 5 Rupee, two 2 Rupee and one 1 Rupee coins
# For 11 = one 5 Rupee, two 2 Rupee and two 1 Rupee coins
# For 12 = one 5 Rupee, three 2 Rupee and one 1 Rupee coins
# For 13 = one 5 Rupee, three 2 Rupee and two 1 Rupee coins


number = int (input ())
five = int ((number - 4) / 5)
one=1
two = ((number - 5 * five - one)//2)
if ((number - 5 * five) % 2)== 0:
    one = 2
else:
    two = ((number - 5 * five - one)//2)
    one = 1
    two = ((number - 5 * five - one)//2)
print (one + two + five)
# print (one + two + five, five, two, one)