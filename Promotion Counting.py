'''
Description:

Bessie the cow is helping Farmer John run the USA Cow Olympiad (USACO), an on-line contest where participants answer challenging questions to demonstrate their mastery of bovine trivia.
In response to a wider range of participant backgrounds, Farmer John recently expanded the contest to include four divisions of difficulty: bronze, silver, gold, and platinum.
All new participants start in the bronze division, and any time they score perfectly on a contest they are promoted to the next-higher division.
It is even possible for a participant to be promoted several times within the same contest.
Farmer John keeps track of a list of all contest participants and their current divisions, so that he can start everyone out at the right level any time he holds a contest.
When publishing the results from his most recent contest, Farmer John wants to include information on the number of participants who were promoted from bronze to silver, from silver to gold, and from gold to platinum.
However, he neglected to count promotions as they occurred during the contest.
Bessie, being the clever bovine she is, realizes however that Farmer John can deduce the number of promotions that occurred solely from the number of participants at each level before and after the contest.
Please help her perform this computation!

Input:

Input consists of four lines, each containing two integers in the range 0..1,000,000.
The first line specifies the number of bronze participants registered before and after the contest.
The second line specifies the number of silver participants before and after the contest.
The third line specifies the number of gold participants before and after the contest.
The last line specifies the number of platinum participants before and after the contest.

Output:

Please output three lines, each containing a single integer.
The first line should contain the number of participants who were promoted from bronze to silver.
The second line should contain the number of participants who were promoted from silver to gold.
The last line should contain the number of participants who were promoted from gold to platinum.
'''

first = input()
second = input()
third = input()
fourth = input()

# b=bronze before, B=bronze after, same for Silver, Gold, and Platinum

b,B = map(int, first.split())
s,S = map(int, second.split())
g,G = map(int, third.split())
p,P = map(int, fourth.split())

# Silver= number of contestants advanced to silver, Gold = number of contestants advanced to Gold, Platinum = number of contestants advanced to Platinum

Silver = S-s
Gold = G-g
Platinum = P-p

print(Silver+Gold+Platinum)
print(Gold+Platinum)
print(Platinum)
