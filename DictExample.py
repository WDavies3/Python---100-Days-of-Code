word = 'aabacccaabbbbbbdd'
freqTable = {}
for c in word:
    freqTable[c] = freqTable[c] + 1 if c in freqTable else 1
for key in freqTable:
    print(key)
for key,val in freqTable.items():
    print(f'{key}: {val}')
