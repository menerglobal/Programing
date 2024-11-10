def bacterial_growth(initial, growth_rate, max_bact):
    
    N = initial
    hours = 0
    threshold = 0.9 * max_bact

    while N < threshold:
        delta_N = growth_rate * N * (max_bact - N) / max_bact
        N += delta_N
        hours += 1
        
        if N >= max_bact:
            break
        if hours > 10000:
            return -1

    return hours

initial_bacteria = 100
growth_rate = 0.1
max_bacteria = 1000

result = bacterial_growth(initial_bacteria, growth_rate, max_bacteria)
print(f"Time taken to reach 90% of max population: {result} hours")
