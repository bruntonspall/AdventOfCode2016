def find_solution(cogs):
    # find x where (for n in cogs, (offset+time)%size == 0 )
    for x in range(10000000):
        passed = 0
        for cog, (size, offset) in enumerate(cogs):
            if (offset+cog+x+1) % size == 0:
                passed += 1
        if passed == len(cogs):
            return x
