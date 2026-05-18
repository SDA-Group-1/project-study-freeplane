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
