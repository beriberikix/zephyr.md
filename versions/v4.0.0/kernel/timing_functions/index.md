---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/timing_functions/index.html
original_path: kernel/timing_functions/index.html
---

# Executing Time Functions

The timing functions can be used to obtain execution time of
a section of code to aid in analysis and optimization.

Please note that the timing functions may use a different timer
than the default kernel timer, where the timer being used is
specified by architecture, SoC or board configuration.

## Configuration

To allow using the timing functions, [`CONFIG_TIMING_FUNCTIONS`](../../kconfig.md#CONFIG_TIMING_FUNCTIONS "CONFIG_TIMING_FUNCTIONS")
needs to be enabled.

## Usage

To gather timing information:

1. Call [`timing_init()`](../../doxygen/html/group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47) to initialize the timer.
2. Call [`timing_start()`](../../doxygen/html/group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde) to signal the start of gathering of
   timing information. This usually starts the timer.
3. Call [`timing_counter_get()`](../../doxygen/html/group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208) to mark the start of code
   execution.
4. Call [`timing_counter_get()`](../../doxygen/html/group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208) to mark the end of code
   execution.
5. Call [`timing_cycles_get()`](../../doxygen/html/group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955) to get the number of timer cycles
   between start and end of code execution.
6. Call [`timing_cycles_to_ns()`](../../doxygen/html/group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2) with total number of cycles
   to convert number of cycles to nanoseconds.
7. Repeat from step 3 to gather timing information for other
   blocks of code.
8. Call [`timing_stop()`](../../doxygen/html/group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2) to signal the end of gathering of
   timing information. This usually stops the timer.

### Example

This shows an example on how to use the timing functions:

```c
#include <zephyr/timing/timing.h>

void gather_timing(void)
{
    timing_t start_time, end_time;
    uint64_t total_cycles;
    uint64_t total_ns;

    timing_init();
    timing_start();

    start_time = timing_counter_get();

    code_execution_to_be_measured();

    end_time = timing_counter_get();

    total_cycles = timing_cycles_get(&start_time, &end_time);
    total_ns = timing_cycles_to_ns(total_cycles);

    timing_stop();
}
```

## API documentation

[Timing Measurement APIs](../../doxygen/html/group__timing__api.md)

[Arch specific Timing Measurement APIs](../../doxygen/html/group__timing__api__arch.md)

[SoC specific Timing Measurement APIs](../../doxygen/html/group__timing__api__soc.md)

[Board specific Timing Measurement APIs](../../doxygen/html/group__timing__api__board.md)
