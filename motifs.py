
2. # Insert your Count(Motifs) function here from the last Code Challenge.

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
             profile[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            profile[symbol][j] += 1/(t)
    # insert your code here
    return profile

def Consensus(Motifs):
    # insert your code here
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus=""
    for j in range(k):
        m=0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus+=frequentSymbol
    return consensus
    
def Count(Motifs):
    count = {}
    # your code here
    k = len(Motifs[0])
    for symbol in "ACGT": 
            count[symbol]=[]
            for i in range(k):
                count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Score(Motifs):
    # Insert code here
    consensus=Consensus(Motifs)
    count= Count(Motifs)
    k =len(consensus)
    j= len(count)
    t=len(Motifs)
    mscore =0
    score =0
    for i in range(k):
        mscore= t - count[consensus[i]][i]
        score+=mscore
    return score

def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

def ProfileMostProbablePattern(Text, k, Profile):
    p_dict = {}
    for i in range(len(Text)- k +1):
        p = Pr(Text[i: i+k], Profile)
        p_dict[i] = p
    m = max(p_dict.values())
    keys = [k for k,v in p_dict.items() if v == m]
    ind = keys[0]
    return Text[ind: ind +k]


def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def CountWithPseudocounts(Motifs):
    count = {}
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    for symbol in "ACGT": 
            count[symbol]=[]
            for i in range(k):
                count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count