# Prolog Vacuum Cleaner Agent

## Overview

A simple **Vacuum Cleaner Intelligent Agent** implemented in Prolog. The agent operates in three rooms (`a`, `b`, `c`), cleans dirty rooms, moves between adjacent rooms, and stops when all rooms are clean.

## Features

* Detects dirty rooms.
* Cleans the current room.
* Moves between adjacent rooms.
* Dynamically updates room and vacuum states.
* Stops automatically when all rooms are clean.

## Environment

```text
A <----> B <----> C
```

Initially:

```prolog
dirty(a).
dirty(b).
dirty(c).
vacuum_location(a).
```

## How It Works

The agent has three actions:

```prolog
action(clean).          % Clean current room
action(move(ToRoom)).   % Move to adjacent dirty room
action(stop).           % Stop when all rooms are clean
```

Dynamic predicates `retract/1` and `assertz/1` are used to update the environment.

## Requirements

* SWI-Prolog

## Running the Program

Save the code as:

```text
vacuum_cleaner.pl
```

Load it in SWI-Prolog:

```prolog
[vacuum_cleaner].
```

Run:

```prolog
start.
```

### Expected Output

```text
Cleaning room a...
Moving from room a to room b...
Cleaning room b...
Moving from room b to room c...
Cleaning room c...
All rooms are clean. Stopping...
```

## Concepts Demonstrated

* Prolog facts and rules
* Dynamic predicates
* Logical inference
* Recursion
* `assertz/1` and `retract/1`
* Negation as failure
* Rule-based intelligent agents

## Learning Outcome

This practical demonstrates how Prolog can be used to implement a simple **rule-based intelligent agent** that observes its environment, performs actions, updates its state, and terminates when its goal is achieved.
