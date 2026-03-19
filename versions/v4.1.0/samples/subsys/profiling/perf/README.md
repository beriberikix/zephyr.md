---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/profiling/perf/README.html
original_path: samples/subsys/profiling/perf/README.html
---

# Perf tool

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/profiling/perf/README.rst/..)

This application can be used to understand how to use the [Perf](../../../../services/profiling/perf.md#profiling-perf)
tool.

## Requirements

The Perf tool is currently implemented only for RISC-V and x86\_64 architectures.

## Usage example

- Build and run the sample with:

  ```shell
  west build -b qemu_riscv64 samples/subsys/profiling/perf
  west build -t run
  ```
- After the sample has started, enter the shell command:

  ```shell
  uart:~$ perf record <duration> <frequency>
  ```

  This command will start a timer for *duration* milliseconds at *frequency* Hz.
- Wait for the completion message `perf done!`, or `perf buf override!` if
  the perf buffer size is smaller than required.
- Print the samples captured by perf in the terminal with the shell command:

  ```shell
  uart:~$ perf printbuf
  ```

  The output should be similar to:

  ```shell
  Perf buf length 2046
  0000000000000004
  00000000001056b2
  0000000000108192
  000000000010052f
  0000000000000000
    ....
  000000000010052f
  0000000000000000
  ```
- Copy the output into a file, for example `perf_buf`.
- Generate `graph.svg` with
  [scripts/profiling/stackcollapse.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/profiling/stackcollapse.py) and [FlameGraph](https://github.com/brendangregg/FlameGraph/):

  ```shell
  python scripts/perf/stackcollapse.py perf_buf build/zephyr/zephyr.elf | <flamegraph_dir_path>/flamegraph.pl > graph.svg
  ```

### Graph example

![graph example](../../../../_images/graph_example.svg)
