

def find_freq(s, k):
    n = len(s)
    
    squence_freq={}

    for i in range(n-k+1):
        subs = s[i:i+k]

        if subs in squence_freq:
            squence_freq[subs] += 1
        else:
            squence_freq[subs] = 1

    
        
    for subs, freq  in squence_freq.items():
        if freq > 1:
            print(f"{subs} - {freq}")



str = "256489256472392564"
k = 4
print(find_freq(str,k))