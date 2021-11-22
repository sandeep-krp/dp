

def solve_leet_longest_palindromic_substring(s):
        """
        :type s: str
        :rtype: str
        """
        return solve_pal(s)

def is_pal(s,rev):
    if s in rev and s == s[::-1]:
        return True
    return False

def solve_pal(s):
    longest_pal=""
    win = len(s)
    rev = s[::-1]
    while(win >=1):
        x = 0
        for y in range(win-1,len(s)+1):
            candidate = s[x:y+1]
            print('Candidate for window [{}] : {}'.format(win,candidate))
            if is_pal(candidate,rev):
                return candidate
            x += 1
        win -=1

    return longest_pal
# Taking long time. FIXME
print(solve_leet_longest_palindromic_substring('whdqcudjpisufnrtsyupwtnnbsvfptrcgvobbjglmpynebblpigaflpbezjvjgbmofejyjssdhbgghgrhzuplbeptpaecfdanhlylgusptlgobkqnulxvnwuzwauewcplnvcwowmbxxnhsdmgxtvbfgnuqdpxennqglgmspbagvmjcmzmbsuacxlqfxjggrwsnbblnnwisvmpwwhomyjylbtedzrptejjsaiqzprnadkjxeqfdpkddmbzokkegtypxaafodjdwirynzurzkjzrkufsokhcdkajwmqvhcbzcnysrbsfxhfvtodqabvbuosxtonbpmgoemcgkudandrioncjigbyizekiakmrfjvezuzddjxqyevyenuebfwugqelxwpirsoyixowcmtgosuggrkdciehktojageynqkazsqxraimeopcsjxcdtzhlbvtlvzytgblwkmbfwmggrkpioeofkrmfdgfwknrbaimhefpzckrzwdvddhdqujffwvtvfyjlimkljrsnnhudyejcrtrwvtsbkxaplchgbikscfcbhovlepdojmqybzhbiionyjxqsmquehkhzdiawfxunguhqhkxqdiiwsbuhosebxrpcstpklukjcsnnzpbylzaoyrmyjatuovmaqiwfdfwyhugbeehdzeozdrvcvghekusiahfxhlzclhbegdnvkzeoafodnqbtanfwixjzirnoaiqamjgkcapeopbzbgtxsjhqurbpbuduqjziznblrhxbydxsmtjdfeepntijqpkuwmqezkhnkwbvwgnkxmkyhlbfuwaslmjzlhocsgtoujabbexvxweigplmlewumcone'))