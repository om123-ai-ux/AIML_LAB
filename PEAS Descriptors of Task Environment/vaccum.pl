:- dynamic dirty/1.
:- dynamic vacuum_location/1.

room(a).
room(b).
room(c).

adjacent(a, b).
adjacent(b, a).
adjacent(b, c).
adjacent(c, b).

dirty(a).
dirty(b).
dirty(c).

vacuum_location(a).

action(clean) :-
    vacuum_location(Room),
    dirty(Room).

action(move(ToRoom)) :-
    vacuum_location(CurrentRoom),
    adjacent(CurrentRoom, ToRoom),
    dirty(ToRoom).

action(stop) :-
    \+ dirty(_).

perform(clean) :-
    vacuum_location(Room),
    dirty(Room),
    retract(dirty(Room)),
    format("Cleaning room ~w...~n", [Room]).

perform(move(ToRoom)) :-
    vacuum_location(CurrentRoom),
    retract(vacuum_location(CurrentRoom)),
    assertz(vacuum_location(ToRoom)),
    format("Moving from room ~w to room ~w...~n", [CurrentRoom, ToRoom]).

perform(stop) :-
    format("All rooms are clean. Stopping...~n", []).
start :-
    action(Action),
    perform(Action),
    Action \= stop,
    start.

start :-
    action(stop),
    perform(stop).

