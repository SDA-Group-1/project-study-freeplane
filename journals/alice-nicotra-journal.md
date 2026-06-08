# Alice Nicotra Personal Project Journal

## 14/04/2026
- I took a look at the documentation and the Freeplane project on github, in order to have an idea about the amount of work we have to do.
- We had a group meeting to decide how to split the work. I was assigned the Design Pattern part and we decide to have a weekly meeting to update each other about the work progress.

## 21/04/2026
- I studied the Design Patterns documentation. This will allow me to perform a more effective code inspection in the coming days.

## 22/04/2026
- I started analyzing Freeplane source code, searching for keywords like 'Abstract' to pinpoint potential design patterns within the architecture.

## 06/05/2026
- I focused my analysis on `NodeModel.java`, which serves as a core component of the Freeplane architecture. I identified the Composite Design Pattern within this class, which is used to manage the hierarchical structure of the mind map. In this implementation, NodeModel acts as both a 'Component' and a 'Composite', allowing individual nodes and entire branches to be treated uniformly. I studied how this pattern facilitates recursive operations, such as rendering or searching through the tree structure, ensuring that the system can handle complex nested maps efficiently.

## 07/05/2026
- Had a meeting with the group to update each other on the current work. Set a deadline for the final work.

## 12/05/2026
- Conducted a comprehensive design pattern inspection within Freeplane's core architecture.
- Identified and analyzed four additional patterns:
    - *Observer Pattern*: Located in `MapModel.java` and `INodeChangeListener`, decoupling data updates from the Swing presentation layer (MapView).
    - *Command Pattern*: Isolated in `UndoHandler.java` and `IActor`, reifying user actions into standalone execution blocks to implement memory-efficient Undo/Redo history tracking.
    - *Singleton Pattern*: Discovered a thread-safe registry variation in `Controller.java` (features.mode) providing single-point global access to sub-systems.
    - *Abstract Factory Pattern*: Spotted in `IconFactory.java`, managing environment-dependent components to allow headless batch execution without UI rendering crashes.
- Drafted the concise report sections for all five extracted patterns (Composite, Observer, Command, Singleton, Abstract Factory) to finalize formatting and word count requirements.

## 22/05/2026
- Reviewed the text of the Design Patterns section and inserted all the links to the source code.
- Pulled the 'design' branch to integrate the Dependencies section with the Design Patterns section.
- Read the Dependencies section and added the summary of the design report. Then, committed the full text (pending a final review once the word count script is available).

## 25/05/2026
- Started figuring out which diagrams/images would best visualize the implemented design pattern.

## 08/06/2026
- Finalized Design Report Section: Integrated the custom-generated UML design pattern diagrams into the design.md file, ensuring precise alignment between the architectural theory and the actual Freeplane implementation.
- Conducted a comprehensive proofreading of the entire Design section, cross-referencing it with the Overview and Architecture chapters to ensure consistent terminology and logical flow across the project documentation.
- Refined the pattern analysis (specifically updating the Singleton and Composite sections) to include critical architectural trade-offs and detailed dependency observations, ensuring that identified violations are accurately reported.
- Performed a final word count check using the provided utility script to confirm that the entire document remains within the 2500-word constraint, ensuring all technical requirements for the report submission are met.
