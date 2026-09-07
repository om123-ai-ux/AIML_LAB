% Home Security Monitoring Expert System

:- dynamic alarm_status/1.
:- dynamic motion_detected/1.
:- dynamic door_status/2.

% Initial alarm status
alarm_status(off).

% Security sensor facts
motion_detected(yes).
door_status(front_door, open).
door_status(back_door, closed).

% Rule: Turn ON alarm when motion is detected
action(turn_on) :-
    motion_detected(yes),
    alarm_status(off).

% Rule: Turn ON alarm when any door is open
action(turn_on) :-
    door_status(_, open),
    alarm_status(off).

% Rule: Turn OFF alarm when there is no threat
action(turn_off) :-
    motion_detected(no),
    door_status(front_door, closed),
    door_status(back_door, closed),
    alarm_status(on).

% Stop when no further action is required
action(stop) :-
    \+ action(turn_on),
    \+ action(turn_off).

% Turn ON the alarm
perform(turn_on) :-
    retract(alarm_status(off)),
    assertz(alarm_status(on)),
    format("Security threat detected: Turning ON alarm...~n", []).

% Turn OFF the alarm
perform(turn_off) :-
    retract(alarm_status(on)),
    assertz(alarm_status(off)),
    format("No security threat detected: Turning OFF alarm...~n", []).

% Stop the system
perform(stop) :-
    format("All security conditions are safe. Stopping...~n", []).

% Main execution loop
start :-
    action(Action),
    perform(Action),
    Action \= stop,
    start.
