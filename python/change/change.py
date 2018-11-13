
'''
minv = 99999
min_list = []
def backtrack_sol_slow(balance_change , coins_avail , used_coins):
    #Exponential Solution
    if(balance_change < 0):return
    if(balance_change == 0):
        global minv
        if(len(used_coins) < minv):
            global min_list
            minv = len(used_coins)
            min_list = used_coins
    if(len(coins_avail) == 0):return

    for i in range(0,(balance_change // coins_avail[-1] )+ 1):
        backtrack_sol(balance_change - (i * coins_avail[-1]) , coins_avail[:-1] , (used_coins + ([coins_avail[-1]] * i)) )
'''
def backtrack_sol_fast(coins_avail, amount):
    coin_used = [ [] for i in range( amount + 1) ]
    dp = [-1 for i in range ( amount + 1) ]
    dp[0] = 0
    for i in range(1,amount + 1):
        for j in coins_avail:
            if( j > i ):continue
            subsol = dp[ i - j ]
            if( subsol != -1  and  ( dp[i] == -1 or  dp[i] > subsol + 1 )  ):
                dp[i] = subsol + 1
                coin_used[i] = coin_used[i - j] + [j]
    return coin_used[amount]

def find_minimum_coins(total_change, coins):
    if(total_change < 0):raise ValueError("Negaive Amounts are not allowed")
    ans = backtrack_sol_fast(coins , total_change)
    if(len(ans) == 0 and total_change != 0):raise ValueError("Error Change cannot be Made")
    return sorted(ans)
