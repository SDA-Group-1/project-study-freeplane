# Amirhossein Torabiardekani Personal Project Journal

## 13/04/2026

 Read the project requirements document (Project-SW_DA-2026.pdf) 
and explored the Freeplane documentation and GitHub repository 
to get familiar with the project structure and goals.

## 14/04/2026

Attended a team meeting where we discussed different options 
for splitting the work among the five members. Each member 
was assigned a specific responsibility in the project.
I got assigned to the **Dependencies** section of the 
Design Report, which involves analyzing code dependencies 
and knowledge dependencies between the Freeplane modules.

## 26/04/2026

- Cloned the project repository to the local machine 
  using VS Code.
- Started exploring the Freeplane GitHub repository 
  to get familiar with the module structure.
- Identified the main modules of the project: 
  freeplane (core), freeplane_api, freeplane_framework, 
  and several plugin modules such as freeplane_plugin_script 
  and freeplane_plugin_formula.


  ## 03/05/2026

- Cloned the Freeplane source code to the local machine.
- Wrote a Python script to analyze import statements
  across all Java source files.
- Successfully identified inter-module dependencies:
  - freeplane_api has no dependencies (base module)
  - freeplane (core) depends only on freeplane_api
  - All plugins depend on freeplane core
  - freeplane_plugin_formula has the most dependencies
- This initial exploration will serve as a starting point 
  for the dependency analysis.
