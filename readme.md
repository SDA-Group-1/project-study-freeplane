# Group 1 Project Repository — SDA (Politecnico di Torino)

This is the project directory of **Group 1** for the **Software Design and Architecture Course** at **Politecnico di Torino**.  
Our group decided to study **Freeplane** as the reference project.

## Structure

```text
.
├── journals/
│   ├── fateme-hemmati-journal.md
│   ├── sergio-maestrale-journal.md
│   ├── niccolo-nannucci-journal.md
│   ├── alice-nicotra-journal.md
│   └── amirhossein-torabiardekani-journal.md
├── deliverables/
│   ├── overview.md
│   ├── design.md
│   └── architecture.md
└── extra-material/
	└── *.md
```

- **journals**: personal journals where each member reports our activities, with a maximum frequency of once every two weeks (preferably more frequent). Naming convention: `<name>-<surname>-journal.md`.
- **deliverables**: the three required project documents:
	- **overview**: 1000 words
		- purpose of the system, main stakeholders, short system description, and basic code statistics.
	- **design**: 2500 words
		- code and knowledge dependency analysis, at least 4 pattern instances with roles/problem/alternatives, and a summary.
	- **architecture**: 2500 words
		- C4 levels 1-2-3 (context/container/component), tools used, relation to Clean Architecture, SOLID observations, and key architectural qualities.
	- word limits refer to text only (diagrams excluded).
- **extra-material**: extra materials we produce mainly for personal use and to share resources within the group.

## Branching

We decided not to introduce significant branch-management overhead.  
Each member will create a simple personal branch, for example:

- `overview-s`

Pull requests targeting `main` should be reviewed by at least one other team member when possible. More importantly, they should be kept small, frequent, and closed as quickly as possible so that `main` always contains most of the current work.
It is therefore acceptable to close them without extensive verification from the whole group, as the priority is to keep the shared content on `main` up to date.

## Members

- Hemmati Fateme
- Maestrale Sergio
- Nannucci Niccolò
- Nicotra Alice
- Torabiardekani Amirhossein
