#Function for to check LCS
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)

    # Create a DP table (2D list)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    lcs_str = ''.join(lcs)

    # Print results
    print("\n--- LCS Result ---")
    print("String 1:", str1)
    print("String 2:", str2)
    print("LCS Length:", dp[m][n])
    print("LCS:", lcs_str)

# --- Get input from user ---
str1 = input("Enter first string: ").strip()
str2 = input("Enter second string: ").strip()

# Call function
longest_common_subsequence(str1, str2)

#output ->>>
#Enter first string: Avinash
#Enter second string: vaishnav

#--- LCS Result ---

#String 1: Avinash
# String 2: vaishnav
# LCS Length: 4
# LCS: vash
