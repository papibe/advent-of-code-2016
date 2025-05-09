# Day 1 - Advent of Code 2016

## --- Day 1: No Time for a Taxicab ---

-------------------------------------

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all _fifty stars_ by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants _one star_. Good luck!

You're airdropped near _Easter Bunny Headquarters_ in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (`L`) or right (`R`) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the [street grid of the city](https://en.wikipedia.org/wiki/Taxicab_geometry), how far is the shortest path to the destination?

For example:

* Following `R2, L3` leaves you `2` blocks East and `3` blocks North, or `5` blocks away.
* `R2, R2, R2` leaves you `2` blocks due South of your starting position, which is `2` blocks away.
* `R5, L5, R5, R3` leaves you `12` blocks away.

_How many blocks away_ is Easter Bunny HQ?

Your puzzle answer was `250`.

## --- Part Two ---

-------------------------------------

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are `R8, R4, R4, R8`, the first location you visit twice is `4` blocks away, due East.

How many blocks away is the _first location you visit twice_?

Your puzzle answer was `151`.

Both parts of this puzzle are complete! They provide two gold stars: \*\*
