import subprocess
from collections import defaultdict

# Get all commits
result = subprocess.run(
    ["git", "log", "--pretty=format:%H", "--no-merges"],
    capture_output=True, text=True
)
commits = result.stdout.strip().split("\n")
print(f"Total commits: {len(commits)}")

# For each commit, get changed files
cochange = defaultdict(int)
file_count = defaultdict(int)

for i, commit in enumerate(commits[:500]):  # limit to 500 commits
    result = subprocess.run(
        ["git", "diff-tree", "--no-commit-id", "-r", "--name-only", commit],
        capture_output=True, text=True
    )
    files = [f for f in result.stdout.strip().split("\n") 
             if f.endswith(".java")]
    
    for f in files:
        file_count[f] += 1
    
    for i, f1 in enumerate(files):
        for f2 in files[i+1:]:
            pair = tuple(sorted([f1, f2]))
            cochange[pair] += 1

# Show top 20 co-changed pairs
print("\n=== TOP 20 CO-CHANGED FILE PAIRS ===\n")
sorted_pairs = sorted(cochange.items(), key=lambda x: x[1], reverse=True)
for pair, count in sorted_pairs[:20]:
    print(f"{count}x: {pair[0].split('/')[-1]} <-> {pair[1].split('/')[-1]}")