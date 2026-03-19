---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/profiling/perf.html
original_path: services/profiling/perf.html
---

# Perf

Perf is a profiler tool based on stack tracing. It can be used for lightweight profiling
with minimal code overhead.

## Work Principle

The `perf record` shell command starts a timer with the perf tracer function.
Timers are driven by interrupts, so the perf tracer function is called during an interruption.
The Zephyr core saves the return address and frame pointer in the interrupt stack or `callee_saved`
structure before calling the interrupt handler. Thus, the perf trace function makes stack traces by
using the return address and frame pointer.

The [scripts/profiling/stackcollapse.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/profiling/stackcollapse.py) script can be used to convert return addresses
in the stack trace to function names using symbols from the ELF file, and to prints them in the
format expected by [FlameGraph](https://github.com/brendangregg/FlameGraph/).

## Configuration

You can configure this module using the following options:

- [`CONFIG_PROFILING_PERF`](../../kconfig.md#CONFIG_PROFILING_PERF "CONFIG_PROFILING_PERF"): Enables the module. This option adds
  the `perf` command to the shell.
- [`CONFIG_PROFILING_PERF_BUFFER_SIZE`](../../kconfig.md#CONFIG_PROFILING_PERF_BUFFER_SIZE "CONFIG_PROFILING_PERF_BUFFER_SIZE"): Sets the size of the perf buffer
  where samples are saved before printing.

## Usage

Refer to the [Perf tool](../../samples/subsys/profiling/perf/README.md#profiling-perf "Send perf samples to the host with console support") sample for an example of how to use the perf tool.
