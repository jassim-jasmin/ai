# TF-IDF
- Calculation
    -
    Example:
  
    Corpus D
  
        d1: A quick brown fox jumps over the lazy dog. What a fox!
        d2: A quick brown fox jumps over the lazy fox. What a fox!
  
    TF Calculation for word fox

        Number of terms in d1 (t1) = 12
        Total number of occurance of the word 'fox' in d1 (n1) = 2
  
        TF('fox', d1) = t1/n1 = 2/12 = 0.17

        Number of terms in d2 (t2) = 12
        Total number of occurance of the word 'fox' in d2 (n2) = 3

        TF('fox', d2) = t2/n2 = 3/12 = 0.25
  
    IDF Calculation for word fox
  
        idf(fox, d1) = 1 (fox is present in first document)
        idf('fox', d2) = 1 (fox is present in second document)
        idf referes to the presence only
  
        i = idf('fox', d1) + idf('fox', d2)
        number of document, n = 2
  
        IDF('fox', D) = log(i/n) = log(2/2) = 0

    TF-ID Calculation for word fox

        TFIDF('fox', d1) = TF('fox', d1) * IDF('fox', D) = 0.17 * 0 = 0
        TFIDF('fox', d2) = TF('fox', d2) * IDF('fox', D) = 0.25 * 0 = 0        TFIDF('fox', d2) = TF('fox', d2) * IDF('fox', D) = 0.25 * 0 = 0

    TFIDF can be explained as `how much information a word provide`

# Binary Term Frequency
Binary Term Frequency captures presence (1) or absence (0) of term in document. For this part, under TfidfVectorizer, 
we set binary parameter equal to true so that it can show just presence (1) or absence (0) and norm parameter equal to false.