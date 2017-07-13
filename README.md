# z80trace

A simple (Z80) trace tool analyzer.

z80trace takes a trace of the value of a processor's program counter at
successive instructions and produces a graphical representation of the
execution.

As the name suggests, it was initially developed for the Z80 and particularly
the ZX Spectrum, but there's nothing actually Spectrum or Z80 specific about
it at the moment.

## Usage

`$ ./z80trace.py file.trace > file.dot`

This takes the trace in `file.trace` and outputs a
[Graphviz](http://www.graphviz.org/) file containing the execution graph. You
can then use Graphviz to convert that into a graphical format (e.g. via
`dot -Tpng file.dot > file.png`).

There's a (compressed) example trace file `boot.trace` which contains the trace
of a Spectrum booting to the "(c) 1982 Sinclair Research Ltd" message should
you wish to try this out. Be warned that the Graphviz rendering can take a
while.

## Trace file format

The trace file should consist of the list of PC values from the processor, one
per line, with three additions:

* `Interrupt` when an interrupt is accepted.
* `CALL` on the line *after* a CALL instruction is actually taken (as opposed
   to when something like a CALL NZ, nnnn is not taken because A was zero).
* `RET` on the line *after* a RET instruction is actually taken.

## Any questions?

Mail `philip-z80trace@shadowmagic.org.uk`.
