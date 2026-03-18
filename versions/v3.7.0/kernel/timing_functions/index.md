---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/timing_functions/index.html
original_path: kernel/timing_functions/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

1. Call [`timing_init()`](#c.timing_init) to initialize the timer.
2. Call [`timing_start()`](#c.timing_start) to signal the start of gathering of
   timing information. This usually starts the timer.
3. Call [`timing_counter_get()`](#c.timing_counter_get) to mark the start of code
   execution.
4. Call [`timing_counter_get()`](#c.timing_counter_get) to mark the end of code
   execution.
5. Call [`timing_cycles_get()`](#c.timing_cycles_get) to get the number of timer cycles
   between start and end of code execution.
6. Call [`timing_cycles_to_ns()`](#c.timing_cycles_to_ns) with total number of cycles
   to convert number of cycles to nanoseconds.
7. Repeat from step 3 to gather timing information for other
   blocks of code.
8. Call [`timing_stop()`](#c.timing_stop) to signal the end of gathering of
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

*group* Timing Measurement APIs
:   Timing Measurement APIs.

    The timing measurement APIs can be used to obtain execution time of a section of code to aid in analysis and optimization.

    Please note that the timing functions may use a different timer than the default kernel timer, where the timer being used is specified by architecture, SoC or board configuration.

    Functions

    void timing\_init(void)
    :   Initialize the timing subsystem.

        Perform the necessary steps to initialize the timing subsystem.

    void timing\_start(void)
    :   Signal the start of the timing information gathering.

        Signal to the timing subsystem that timing information will be gathered from this point forward.

    void timing\_stop(void)
    :   Signal the end of the timing information gathering.

        Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

    static inline timing\_t timing\_counter\_get(void)
    :   Return timing counter.

        Returns:
        :   Timing counter.

    static inline uint64\_t timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)
    :   Get number of cycles between `start` and `end`.

        For some architectures or SoCs, the raw numbers from counter need to be scaled to obtain actual number of cycles.

        Parameters:
        :   - **start** – Pointer to counter at start of a measured execution.
            - **end** – Pointer to counter at stop of a measured execution.

        Returns:
        :   Number of cycles between start and end.

    static inline uint64\_t timing\_freq\_get(void)
    :   Get frequency of counter used (in Hz).

        Returns:
        :   Frequency of counter used for timing in Hz.

    static inline uint64\_t timing\_cycles\_to\_ns(uint64\_t cycles)
    :   Convert number of `cycles` into nanoseconds.

        Parameters:
        :   - **cycles** – Number of cycles

        Returns:
        :   Converted time value

    static inline uint64\_t timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)
    :   Convert number of `cycles` into nanoseconds with averaging.

        Parameters:
        :   - **cycles** – Number of cycles
            - **count** – Times of accumulated cycles to average over

        Returns:
        :   Converted time value

    static inline uint32\_t timing\_freq\_get\_mhz(void)
    :   Get frequency of counter used (in MHz).

        Returns:
        :   Frequency of counter used for timing in MHz.

*group* Arch specific Timing Measurement APIs
:   Arch specific Timing Measurement APIs.

    Implements the necessary bits to support timing measurement using architecture specific timing measurement mechanism.

    Functions

    void arch\_timing\_init(void)
    :   Initialize the timing subsystem.

        Perform the necessary steps to initialize the timing subsystem.

        See also

        [timing\_init()](#group__timing__api_1ga50ff9040b99d95c56f494014831e4b47)

    void arch\_timing\_start(void)
    :   Signal the start of the timing information gathering.

        Signal to the timing subsystem that timing information will be gathered from this point forward.

        See also

        [timing\_start()](#group__timing__api_1ga3c28bb4ced0467c284d33c800e070bde)

        Note

        Any call to [arch\_timing\_counter\_get()](#group__timing__api__arch_1gad7a709477650c8596a96fe080f583fdd) must be done between calls to [arch\_timing\_start()](#group__timing__api__arch_1gaf8cd88e81c2104b5eb0fbe42967b7834) and [arch\_timing\_stop()](#group__timing__api__arch_1ga566483c64f5c5d2f0465e3f969303fd3), and on the same CPU core.

    void arch\_timing\_stop(void)
    :   Signal the end of the timing information gathering.

        Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

        See also

        [timing\_stop()](#group__timing__api_1gade1584bf683c9c61905513efa4d99cf2)

        Note

        Any call to [arch\_timing\_counter\_get()](#group__timing__api__arch_1gad7a709477650c8596a96fe080f583fdd) must be done between calls to [arch\_timing\_start()](#group__timing__api__arch_1gaf8cd88e81c2104b5eb0fbe42967b7834) and [arch\_timing\_stop()](#group__timing__api__arch_1ga566483c64f5c5d2f0465e3f969303fd3), and on the same CPU core.

    timing\_t arch\_timing\_counter\_get(void)
    :   Return timing counter.

        See also

        [timing\_counter\_get()](#group__timing__api_1gaa5736c87362de09749af1d8ff30b8208)

        Note

        Any call to [arch\_timing\_counter\_get()](#group__timing__api__arch_1gad7a709477650c8596a96fe080f583fdd) must be done between calls to [arch\_timing\_start()](#group__timing__api__arch_1gaf8cd88e81c2104b5eb0fbe42967b7834) and [arch\_timing\_stop()](#group__timing__api__arch_1ga566483c64f5c5d2f0465e3f969303fd3), and on the same CPU core.

        Note

        Not all architectures have a timing counter with 64 bit precision. It is possible to see this value “go backwards” due to internal rollover. Timing code must be prepared to address the rollover (with platform-dependent code, e.g. by casting to a uint32\_t before subtraction) or by using [arch\_timing\_cycles\_get()](#group__timing__api__arch_1ga44d3a7bd8b7008c9cd6c0524e97f128c) which is required to understand the distinction.

        Returns:
        :   Timing counter.

    uint64\_t arch\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)
    :   Get number of cycles between `start` and `end`.

        See also

        [timing\_cycles\_get()](#group__timing__api_1gaa12074c7645b19578e7ca573c6aa2955)

        Note

        For some architectures, the raw numbers from counter need to be scaled to obtain actual number of cycles, or may roll over internally. This function computes a positive-definite interval between two returned cycle values.

        Parameters:
        :   - **start** – Pointer to counter at start of a measured execution.
            - **end** – Pointer to counter at stop of a measured execution.

        Returns:
        :   Number of cycles between start and end.

    uint64\_t arch\_timing\_freq\_get(void)
    :   Get frequency of counter used (in Hz).

        See also

        [timing\_freq\_get()](#group__timing__api_1gab72ed08d19630cb4cbea4977f2e6723b)

        Returns:
        :   Frequency of counter used for timing in Hz.

    uint64\_t arch\_timing\_cycles\_to\_ns(uint64\_t cycles)
    :   Convert number of `cycles` into nanoseconds.

        See also

        [timing\_cycles\_to\_ns()](#group__timing__api_1ga14a85981068350f33c63c93c4b71afe2)

        Parameters:
        :   - **cycles** – Number of cycles

        Returns:
        :   Converted time value

    uint64\_t arch\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)
    :   Convert number of `cycles` into nanoseconds with averaging.

        See also

        [timing\_cycles\_to\_ns\_avg()](#group__timing__api_1ga28b0252f3395b6e6b549cb03ea4dbef4)

        Parameters:
        :   - **cycles** – Number of cycles
            - **count** – Times of accumulated cycles to average over

        Returns:
        :   Converted time value

    uint32\_t arch\_timing\_freq\_get\_mhz(void)
    :   Get frequency of counter used (in MHz).

        See also

        [timing\_freq\_get\_mhz()](#group__timing__api_1ga65370ad32eadf61c84b90dc04ecd1d56)

        Returns:
        :   Frequency of counter used for timing in MHz.

*group* SoC specific Timing Measurement APIs
:   SoC specific Timing Measurement APIs.

    Implements the necessary bits to support timing measurement using SoC specific timing measurement mechanism.

    Functions

    void soc\_timing\_init(void)
    :   Initialize the timing subsystem on SoC.

        Perform the necessary steps to initialize the timing subsystem.

        See also

        [timing\_init()](#group__timing__api_1ga50ff9040b99d95c56f494014831e4b47)

    void soc\_timing\_start(void)
    :   Signal the start of the timing information gathering.

        Signal to the timing subsystem that timing information will be gathered from this point forward.

        See also

        [timing\_start()](#group__timing__api_1ga3c28bb4ced0467c284d33c800e070bde)

    void soc\_timing\_stop(void)
    :   Signal the end of the timing information gathering.

        Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

        See also

        [timing\_stop()](#group__timing__api_1gade1584bf683c9c61905513efa4d99cf2)

    timing\_t soc\_timing\_counter\_get(void)
    :   Return timing counter.

        See also

        [timing\_counter\_get()](#group__timing__api_1gaa5736c87362de09749af1d8ff30b8208)

        Note

        Not all SoCs have timing counters with 64 bit precision. It is possible to see this value “go backwards” due to internal rollover. Timing code must be prepared to address the rollover (with SoC dependent code, e.g. by casting to a uint32\_t before subtraction) or by using [soc\_timing\_cycles\_get()](#group__timing__api__soc_1ga97f010f79b60089b982d60d543e07660) which is required to understand the distinction.

        Returns:
        :   Timing counter.

    uint64\_t soc\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)
    :   Get number of cycles between `start` and `end`.

        See also

        [timing\_cycles\_get()](#group__timing__api_1gaa12074c7645b19578e7ca573c6aa2955)

        Note

        The raw numbers from counter need to be scaled to obtain actual number of cycles, or may roll over internally. This function computes a positive-definite interval between two returned cycle values.

        Parameters:
        :   - **start** – Pointer to counter at start of a measured execution.
            - **end** – Pointer to counter at stop of a measured execution.

        Returns:
        :   Number of cycles between start and end.

    uint64\_t soc\_timing\_freq\_get(void)
    :   Get frequency of counter used (in Hz).

        See also

        [timing\_freq\_get()](#group__timing__api_1gab72ed08d19630cb4cbea4977f2e6723b)

        Returns:
        :   Frequency of counter used for timing in Hz.

    uint64\_t soc\_timing\_cycles\_to\_ns(uint64\_t cycles)
    :   Convert number of `cycles` into nanoseconds.

        See also

        [timing\_cycles\_to\_ns()](#group__timing__api_1ga14a85981068350f33c63c93c4b71afe2)

        Parameters:
        :   - **cycles** – Number of cycles

        Returns:
        :   Converted time value

    uint64\_t soc\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)
    :   Convert number of `cycles` into nanoseconds with averaging.

        See also

        [timing\_cycles\_to\_ns\_avg()](#group__timing__api_1ga28b0252f3395b6e6b549cb03ea4dbef4)

        Parameters:
        :   - **cycles** – Number of cycles
            - **count** – Times of accumulated cycles to average over

        Returns:
        :   Converted time value

    uint32\_t soc\_timing\_freq\_get\_mhz(void)
    :   Get frequency of counter used (in MHz).

        See also

        [timing\_freq\_get\_mhz()](#group__timing__api_1ga65370ad32eadf61c84b90dc04ecd1d56)

        Returns:
        :   Frequency of counter used for timing in MHz.

*group* Board specific Timing Measurement APIs
:   Board specific Timing Measurement APIs.

    Implements the necessary bits to support timing measurement using board specific timing measurement mechanism.

    Functions

    void board\_timing\_init(void)
    :   Initialize the timing subsystem.

        Perform the necessary steps to initialize the timing subsystem.

        See also

        [timing\_init()](#group__timing__api_1ga50ff9040b99d95c56f494014831e4b47)

    void board\_timing\_start(void)
    :   Signal the start of the timing information gathering.

        Signal to the timing subsystem that timing information will be gathered from this point forward.

        See also

        [timing\_start()](#group__timing__api_1ga3c28bb4ced0467c284d33c800e070bde)

    void board\_timing\_stop(void)
    :   Signal the end of the timing information gathering.

        Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

        See also

        [timing\_stop()](#group__timing__api_1gade1584bf683c9c61905513efa4d99cf2)

    timing\_t board\_timing\_counter\_get(void)
    :   Return timing counter.

        See also

        [timing\_counter\_get()](#group__timing__api_1gaa5736c87362de09749af1d8ff30b8208)

        Note

        Not all timing counters have 64 bit precision. It is possible to see this value “go backwards” due to internal rollover. Timing code must be prepared to address the rollover (with board dependent code, e.g. by casting to a uint32\_t before subtraction) or by using [board\_timing\_cycles\_get()](#group__timing__api__board_1ga087f9f0a8915ec2f23e64c2e8b023ec8) which is required to understand the distinction.

        Returns:
        :   Timing counter.

    uint64\_t board\_timing\_cycles\_get(volatile timing\_t \*const start, volatile timing\_t \*const end)
    :   Get number of cycles between `start` and `end`.

        See also

        [timing\_cycles\_get()](#group__timing__api_1gaa12074c7645b19578e7ca573c6aa2955)

        Note

        The raw numbers from counter need to be scaled to obtain actual number of cycles, or may roll over internally. This function computes a positive-definite interval between two returned cycle values.

        Parameters:
        :   - **start** – Pointer to counter at start of a measured execution.
            - **end** – Pointer to counter at stop of a measured execution.

        Returns:
        :   Number of cycles between start and end.

    uint64\_t board\_timing\_freq\_get(void)
    :   Get frequency of counter used (in Hz).

        See also

        [timing\_freq\_get()](#group__timing__api_1gab72ed08d19630cb4cbea4977f2e6723b)

        Returns:
        :   Frequency of counter used for timing in Hz.

    uint64\_t board\_timing\_cycles\_to\_ns(uint64\_t cycles)
    :   Convert number of `cycles` into nanoseconds.

        See also

        [timing\_cycles\_to\_ns()](#group__timing__api_1ga14a85981068350f33c63c93c4b71afe2)

        Parameters:
        :   - **cycles** – Number of cycles

        Returns:
        :   Converted time value

    uint64\_t board\_timing\_cycles\_to\_ns\_avg(uint64\_t cycles, uint32\_t count)
    :   Convert number of `cycles` into nanoseconds with averaging.

        See also

        [timing\_cycles\_to\_ns\_avg()](#group__timing__api_1ga28b0252f3395b6e6b549cb03ea4dbef4)

        Parameters:
        :   - **cycles** – Number of cycles
            - **count** – Times of accumulated cycles to average over

        Returns:
        :   Converted time value

    uint32\_t board\_timing\_freq\_get\_mhz(void)
    :   Get frequency of counter used (in MHz).

        See also

        [timing\_freq\_get\_mhz()](#group__timing__api_1ga65370ad32eadf61c84b90dc04ecd1d56)

        Returns:
        :   Frequency of counter used for timing in MHz.
