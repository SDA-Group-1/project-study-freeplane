# Freeplane: System Overview

## 1. Purpose of the System and Main Stakeholders

**Purpose of the System**
The purpose of the Freeplane system is to provide, within a modular and open-source application, a specialized set of tools for mind mapping and navigating mapped information. It enables users to model complex cognitive concepts through non-linear structures, acting as a central hub for knowledge management with broad support for data import and export formats.

**Main Stakeholders**

**1. Primary Users (End Users)**
This category interacts directly with the application's interface.
* **Students, Project Managers, and Planners:** This category encompasses any daily user of the application who relies on a responsive interface and stable data storage to organize ideas, study materials, and project work breakdown structures.

**2. Developers and Maintainers (Maintainers & Contributors)**
Fundamental technical stakeholders for the evolution, testing, and sustainability of the software ecosystem.
* **Developers:** Primarily responsible for developing new plugins, managing the core architecture, and ensuring system stability and performance.
* **Community Contributors:** Primarily dedicated to bug fixing or extending add-ons; they are volunteers distinguishable from the main group of developers, heavily relying on the modular architecture to contribute safely.
* **Localizers and Editors:** Also volunteers, but non-technical, who are responsible for developing the application's documentation or translating the interface via property files.

**3. Architectural Entities and External Ecosystem (External Context)**
* **Data Consumers (External Systems):** Software tools and workflows that rely on Freeplane's standardized export capabilities. By converting internal tree structures into open formats (like XML, HTML, or Markdown), Freeplane ensures its data can be ingested by external word processors, web browsers, or project management suites.

## 2. System Description and Basic Code Statistics

Freeplane is a multi-platform desktop application designed around a robust, highly modular architecture based on the OSGi (Open Services Gateway initiative) framework. This dynamic module system allows components to hide their internal implementations and export only necessary public interfaces. This architectural pattern strictly divides the software into a lightweight central core and a rich ecosystem of independent plugins, ensuring low coupling: a failure or an unhandled exception in a peripheral module is isolated and will not crash the entire application.

**The Central Core**
The foundation of the application resides in the `freeplane` directory, which is compiled into the `org.freeplane.core` OSGi bundle. It is responsible for the essential operations: managing the primary data structures in memory, handling the main Java Swing-based Graphical User Interface (GUI), and orchestrating XML file input/output operations for data persistence. Furthermore, the core implements the underlying event-handling mechanisms that allow plugins to dynamically hook into user actions (like keystrokes or menu clicks) without requiring any modification to the central codebase.

**The Plugin Ecosystem (Modules)**
The functionality of the core is dynamically extended through a total of 18 distinct modules and plugins. While some of these act as minor internal utilities or test dependencies, the most architecturally significant components identified in the repository include:
* **freeplane_api:** Provides the stable public interfaces used for safe external extension development.
* **freeplane_framework:** The component responsible for bootstrapping the Knopflerfish OSGi framework.
* **freeplane_mac:** Contains system integrations and native behaviors specific to Apple macOS environments.
* **JOrtho_0.4_freeplane:** An integrated module handling advanced spell-checking features directly within the text nodes.
* **freeplane_plugin_script:** The Groovy engine for executing custom user-defined scripts.
* **freeplane_plugin_latex:** An advanced rendering system for displaying mathematical formulas.
* **freeplane_plugin_markdown:** Handles text formatting and native Markdown export.
* **freeplane_plugin_jsyntaxpane:** Provides syntax highlighting for the internal scripting editor.
* **freeplane_plugin_grpc:** Integrates an RPC server to allow remote control and network automation.

**Build, Dependency, and Quality Management**
The entire modular structure is orchestrated using Gradle. It resolves complex dependencies, compiles each plugin into an individual JAR file, and dynamically injects OSGi manifests (containing directives like `Bundle-Activator` and `Import-Package`) to ensure proper sandboxing at runtime.

| Metric | Detected Value |
| :--- | :--- |
| **Top Contributors (Core Team)** | Dimitry Polivaev (12,650 commits), Volker Boerchers (864 commits), Felix Natter (447 commits) |
| **Total Source Files** | 3,271 |
| **Total Lines of Code** | 377,097 |
| **Modules / Plugins** | 18 |
| **Packages** | 180 |

### 2.1 Code Distribution by Programming Language

Static analysis of the codebase reveals that the ecosystem is almost entirely developed in Java. The secondary languages present are strictly limited to operating system-specific integrations or automation scripts.

| Language | Files | Lines of Code (LOC) |
| :--- | :--- | :--- |
| **Java** | 2,289 | 211,985 |
| **Objective-C++ (C)** | 38 | 26,879 |
| **Groovy** | 2 | 881 |
| **Etc.** | 12 | 1,103 |
| **Total (Programming Only)** | **2,341** | **240,848** |
