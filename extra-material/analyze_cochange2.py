import subprocess
from collections import defaultdict

modules = [
    "freeplane", "freeplane_api", "freeplane_framework",
    "freeplane_plugin_script", "freeplane_plugin_formula",
    "freeplane_plugin_latex", "freeplane_plugin_markdown",
    "freeplane_plugin_svg", "freeplane_plugin_bugreport",
    "freeplane_plugin_ai"
]

def get_module(filepath):
    for m in modules:
        if filepath.startswith(m + "/"):
            return m
    return None

result = subprocess.run(
    ["git", "log", "--pretty=format:%H", "--no-merges"],
    capture_output=True, text=True
)
commits = result.stdout.strip().split("\n")
print(f"Total commits analyzed: {len(commits[:1000])}")

module_cochange = defaultdict(int)
module_change_count = defaultdict(int)

for commit in commits[:1000]:
    result = subprocess.run(
        ["git", "diff-tree", "--no-commit-id", "-r", "--name-only", commit],
        capture_output=True, text=True
    )
    files = result.stdout.strip().split("\n")
    mods = set()
    for f in files:
        m = get_module(f)
        if m:
            mods.add(m)
    for m in mods:
        module_change_count[m] += 1
    mods = list(mods)
    for i, m1 in enumerate(mods):
        for m2 in mods[i+1:]:
            pair = tuple(sorted([m1, m2]))
            module_cochange[pair] += 1

print("\n=== MODULE CO-CHANGE (Knowledge Dependencies) ===\n")
sorted_pairs = sorted(module_cochange.items(), 
                     key=lambda x: x[1], reverse=True)
for pair, count in sorted_pairs:
    print(f"{count}x: {pair[0]} <-> {pair[1]}")

print("\n=== MODULE CHANGE FREQUENCY ===\n")
for m, count in sorted(module_change_count.items(), 
                       key=lambda x: x[1], reverse=True):
    print(f"{count} commits: {m}")