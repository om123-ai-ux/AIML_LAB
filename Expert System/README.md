# Home Security Monitoring Expert System

A rule-based expert system implemented in SWI-Prolog for monitoring a small home-security environment. The system evaluates motion and door sensors, controls an alarm, and stops when no further action is required.

## Problem Statement

Build an intelligent security agent that can:

- Detect motion in the monitored area.
- Detect whether the front or back door is open.
- Turn the alarm on when a security threat is detected.
- Turn the alarm off when all monitored conditions are safe.
- Stop when no action is needed.

## Expert-System Architecture

| Component | Implementation |
| Knowledge base | Facts describing alarm, motion, and door states |
| Inference engine | Prolog rules defined by `action/1` |
| Working memory | Dynamic predicates for alarm and sensor state |
| Actuator | `perform/1`, which changes the alarm status |
| Control loop | `start/0`, which repeatedly observes, decides, and acts |

## Knowledge Representation

The initial state is represented with Prolog facts:

```prolog
alarm_status(off).
motion_detected(yes).
door_status(front_door, open).
door_status(back_door, closed).
```

The predicates are declared dynamic so the system can update the alarm and sensor state while it runs.

## Inference Rules

The inference engine selects an action from the current working memory:

1. **Turn on the alarm:** if motion is detected while the alarm is off.
2. **Turn on the alarm:** if any door is open while the alarm is off.
3. **Turn off the alarm:** if no motion is detected, both doors are closed, and the alarm is on.
4. **Stop:** if neither an alarm-on nor alarm-off action can be inferred.

The alarm actions update the knowledge base with `retract/1` and `assertz/1`. The `start/0` predicate continues the observe-decide-act cycle until `stop` is selected.

## PEAS Description

| PEAS element | Description |
| --- | --- |
| **Performance measure** | Detect threats quickly, maintain the correct alarm state, and stop when no action is needed |
| **Environment** | A home with front-door and back-door sensors plus a motion sensor |
| **Actuators** | Turn the security alarm on or off |
| **Sensors** | Motion status and the state of each monitored door |

## Requirements

- [SWI-Prolog](https://www.swi-prolog.org/)

## How to Run

1. Open a terminal in this directory.
2. Run the program directly:

   ```text
   swipl -q -s expert.pl -g start -t halt
   ```

   Or open the SWI-Prolog prompt and load it manually:

   ```prolog
   [expert].
   start.
   ```

3. Exit the interactive prompt with `halt.`.

### Expected Output

```text
Security threat detected: Turning ON alarm...
All security conditions are safe. Stopping...
```

## Project Structure

```text
.
├── expert.pl
├── README.md
└── Screenshot 2026-08-28 115617.png
```

- [`expert.pl`](expert.pl): Facts, inference rules, actions, and the main execution loop.
- `Screenshot 2026-08-28 115617.png`: Practical output or reference screenshot.

## Concepts Demonstrated

- Rule-based expert-system design
- Knowledge representation with Prolog facts
- Inference using multiple condition rules
- Dynamic state updates with `assertz/1` and `retract/1`
- Variables and anonymous variables in relational rules
- Negation as failure with `\+/1`
- Recursive observe-decide-act execution

## Limitations

This is an educational simulation. It assumes reliable sensor values, a fixed set of monitored doors, and no external alarm hardware or notification service. Sensor facts must be updated manually or by another program before the system can react to new events.

## Learning Outcome

This project demonstrates how an expert system can encode security knowledge as facts and rules, infer decisions from sensor conditions, update its working memory, and control an actuator represented by the alarm state.
