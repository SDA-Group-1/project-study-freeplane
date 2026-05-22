# Design Report

## 1. Dependencies

### Method

Three Python scripts were developed to analyze dependencies
in the Freeplane codebase.

**Script 1 — Code Dependency Analysis:**
A Python script scanned all 2,288 Java source files, extracting
inter-module import statements and mapping each import to its
corresponding module. This produced a complete map of which
modules depend on which others at the source code level.

**Script 2 — Knowledge Dependency Analysis:**
A second script analyzed the 1,000 most recent commits using
Git command-line tools. For each commit, the script identified
which modules contained changed files. Pairs of modules that
appeared together in the same commit were counted as co-changed,
revealing implicit knowledge dependencies not visible in source
code imports.

**Script 3 — Module-Level Co-change Analysis:**
A third script extended the knowledge dependency analysis by
grouping changed files by their parent module and counting how
often pairs of modules appeared together in the same commit,
providing a higher-level view of knowledge dependencies.

All scripts are available in the `extra-material` folder.

### Results: Code Dependencies

| Module                     | Depends On                         |
| -------------------------- | ---------------------------------- |
| freeplane_api              | — (no dependencies)                |
| freeplane                  | freeplane_api                      |
| freeplane_framework        | freeplane, freeplane_api           |
| freeplane_plugin_script    | freeplane, freeplane_api           |
| freeplane_plugin_formula   | freeplane, freeplane_plugin_script |
| freeplane_plugin_latex     | freeplane, freeplane_api           |
| freeplane_plugin_markdown  | freeplane                          |
| freeplane_plugin_svg       | freeplane                          |
| freeplane_plugin_bugreport | freeplane                          |
| freeplane_plugin_ai        | freeplane                          |

### Dependency Diagram

![Freeplane Module Dependencies](freeplane-dependencies.png)

### Key Findings

- **freeplane_api** has no dependencies, serving as the stable
  contract layer that all other modules depend on.
- **freeplane** (core) depends only on `freeplane_api`, keeping
  its coupling minimal and allowing independent maintenance and
  testing.
- **All plugins depend on core**, but not on each other, making
  the system highly extensible — adding or removing a plugin
  does not affect any other plugin.
- **freeplane_plugin_formula** is the most coupled plugin,
  depending on both core and `freeplane_plugin_script`, justified
  by its need to execute Groovy scripts during formula evaluation.
- The overall structure follows a clean layered architecture with
  no circular dependencies.

### Analysis

#### Why these dependencies exist

Freeplane follows a layered architecture designed to maximize
modularity and minimize coupling. `freeplane_api` defines the
public interfaces that all modules rely on, ensuring that plugins
never depend on internal implementation details. This is
consistent with the Dependency Inversion Principle: both the
core and the plugins depend on the abstraction layer, not on
each other's internals.

`freeplane_framework` depends on both `freeplane` and
`freeplane_api` because it coordinates application startup and
plugin lifecycle, requiring access to both the API contracts and
the core implementation through the OSGi framework.

All plugins depend on core because they extend its functionality.
For example, `freeplane_plugin_script` requires access to the
node model to manipulate mind maps through Groovy scripts, and
`freeplane_plugin_latex` needs node content to render LaTeX
formulas. This is confirmed directly in the source code:
[Activator.java](https://github.com/freeplane/freeplane/blob/1.13.x/freeplane_plugin_script/src/main/java/org/freeplane/plugin/script/Activator.java)
in `freeplane_plugin_script` imports both
`org.freeplane.api.Controller` and
`org.freeplane.features.mode.ModeController`.

#### Which modules have the most dependencies and why?

`freeplane_plugin_formula` depends on both core and
`freeplane_plugin_script` because evaluating a formula may
require executing a Groovy script. `freeplane` core is the most
frequently changed module (787 out of 1,000 commits analyzed),
reflecting its central role. `freeplane_plugin_ai` is the second
most changed (217 commits), as it is a recently added feature
still under active development.

#### Which modules have the least dependencies and why?

`freeplane_api` has no dependencies by design: as the contract
layer, any dependency on another module would create a circular
dependency. Modules like `freeplane_plugin_markdown`,
`freeplane_plugin_svg`, and `freeplane_plugin_bugreport` depend
only on core because their functionality is self-contained —
they only need to read or render node content. Their low commit
frequencies (2 and 1 respectively) confirm that they are stable,
mature components.

#### Are these dependencies consistent and logical?

Yes. No circular dependencies were found. Plugins do not depend
on each other, with the single justified exception of
`freeplane_plugin_formula` depending on
`freeplane_plugin_script`. All modules depend on the API layer
rather than on internal implementations, and the layered
structure (api → core → framework → plugins) is consistently
respected across the entire codebase.

#### Impact on maintainability

Because plugins depend on the API rather than on core internals,
the core team can refactor implementation details without
breaking the plugin interface. The high change frequency of core
(787 commits) introduces a potential risk, but this is mitigated
by the stable `freeplane_api` layer: changes to core that do not
affect the API require no updates in the plugins. The active
development of `freeplane_plugin_ai` (217 commits, 44 co-changes
with core) suggests this plugin is still being deeply integrated,
and its co-change frequency is expected to decrease as it matures.

### Knowledge Dependencies (Co-change Analysis)

The commit history was analyzed using a Python script examining
1,000 recent commits out of 16,777 total.

#### Module Co-change Frequency

| Times | Module 1            | Module 2                |
| ----- | ------------------- | ----------------------- |
| 44x   | freeplane           | freeplane_plugin_ai     |
| 8x    | freeplane           | freeplane_framework     |
| 5x    | freeplane           | freeplane_plugin_script |
| 4x    | freeplane_plugin_ai | freeplane_plugin_script |
| 3x    | freeplane_api       | freeplane_plugin_script |
| 2x    | freeplane_api       | freeplane_plugin_ai     |
| 2x    | freeplane           | freeplane_api           |

#### Module Change Frequency

| Commits | Module                    |
| ------- | ------------------------- |
| 787     | freeplane (core)          |
| 217     | freeplane_plugin_ai       |
| 13      | freeplane_framework       |
| 6       | freeplane_plugin_script   |
| 4       | freeplane_api             |
| 2       | freeplane_plugin_latex    |
| 1       | freeplane_plugin_markdown |

#### Key Findings

- **freeplane** core is the most frequently changed module (787
  commits), reflecting its central role.
- **freeplane_plugin_ai** is under active development (217
  commits), explaining its high co-change frequency with core.
- Most knowledge dependencies are consistent with code
  dependencies — modules that import each other tend to change
  together.

#### Inconsistencies between Code and Knowledge Dependencies

- `freeplane_api` and `freeplane_plugin_script` co-changed 3
  times despite no direct import relationship, suggesting a
  **hidden dependency**: API changes sometimes require adjustments
  in the script plugin.
- `freeplane_plugin_ai` and `freeplane_plugin_script` co-changed
  4 times with no code dependency, possibly indicating shared
  behavioral assumptions.

## 2. Patterns

_(To be completed by Alice)_

## 3. Summary

_(To be completed)_
