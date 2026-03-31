def solve_product_twist(products):
    # 1. Map the frequency of each product
    counts = {}
    for p in products:
        counts[p] = counts.get(p, 0) + 1
    
    # 2. Find the highest occurrence count
    max_freq = max(counts.values())
    
    # 3. Collect all strings that appear 'max_freq' times
    # (e.g., all 4 types if 4 is the max)
    candidates = [name for name, count in counts.items() if count == max_freq]
    
    # 4. Sort alphabetically (A to Z)
    candidates.sort()
    
    # 5. Return the last one in the sorted list
    return candidates[-1]

print(solve_product_twist(["apple", "apple", "zebra", "zebra"]))
# Example: ["apple", "apple", "zebra", "zebra"]
# Max count is 2. Candidates: ["apple", "zebra"]
# Sorted: ["apple", "zebra"] -> Result: "zebra"
