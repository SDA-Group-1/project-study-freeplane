import os
from collections import defaultdict

modules = [
    "freeplane", "freeplane_api", "freeplane_framework",
    "freeplane_plugin_script", "freeplane_plugin_formula",
    "freeplane_plugin_latex", "freeplane_plugin_markdown",
    "freeplane_plugin_svg", "freeplane_plugin_bugreport",
    "freeplane_plugin_ai"
]

deps = defaultdict(set)

for module in modules:
    for root, dirs, files in os.walk(module):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("import org.freeplane"):
                            for other in modules:
                                pkg = other.replace("_", ".")
                                if pkg in line or other in line:
                                    if other != module:
                                        deps[module].add(other)

print("\n=== MODULE DEPENDENCIES ===\n")
for module in modules:
    if deps[module]:
        print(f"{module} depends on:")
        for d in sorted(deps[module]):
            print(f"  → {d}")
    else:
        print(f"{module}: no dependencies found")
    print()