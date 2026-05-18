# Amirhossein Torabiardekani Personal Project Journal

## 13/04/2026

Read the project requirements and the Freeplane documentation
to get familiar with the project structure and goals.

## 14/04/2026

Had a meeting with the team to discuss splitting the work.
I was assigned the Dependencies section of the Design Report.

## 26/04/2026

Cloned the project repository and explored the Freeplane
GitHub repository to understand the module structure.
Identified the main modules: freeplane (core), freeplane_api,
freeplane_framework, and several plugin modules.

## 03/05/2026

Cloned the Freeplane source code and wrote a Python script
to analyze import statements across all Java source files.
Identified the main inter-module dependencies and added
the initial results to the design report.

## 07/05/2026

Had a meeting with the team to update each other on progress
and agreed on a deadline for completing individual parts.
Started working on the analysis section of the design report,
explaining why the identified dependencies exist and their
impact on maintainability.

## 11/05/2026

Continued working on the analysis section. Added deeper
explanations about which modules have the most and least
dependencies and why. Added a link to real source code
to confirm the findings.

## 18/05/2026

Wrote two additional Python scripts to analyze knowledge
dependencies by examining the 1,000 most recent commits.
Found that freeplane core and freeplane_plugin_ai co-changed
44 times, making it the strongest knowledge dependency
dependencies. Updated the design report with co-change
tables and deeper explanations. Added all three scripts
to the extra-material folder.
