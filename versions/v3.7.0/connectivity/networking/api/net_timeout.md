---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_timeout.html
original_path: connectivity/networking/api/net_timeout.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Network Timeout

## [Overview](#id1)

Zephyr’s network infrastructure mostly uses the millisecond-resolution uptime
clock to track timeouts, with both deadlines and durations measured with
32-bit unsigned values. The 32-bit value rolls over at 49 days 17 hours 2 minutes
47.296 seconds.

Timeout processing is often affected by latency, so that the time at which the
timeout is checked may be some time after it should have expired. Handling
this correctly without arbitrary expectations of maximum latency requires that
the maximum delay that can be directly represented be a 31-bit non-negative
number (`INT32_MAX`), which overflows at 24 days 20 hours 31 minutes 23.648
seconds.

Most network timeouts are shorter than the delay rollover, but a few protocols
allow for delays that are represented as unsigned 32-bit values counting
seconds, which corresponds to a 42-bit millisecond count.

The net\_timeout API provides a generic timeout mechanism to correctly track
the remaining time for these extended-duration timeouts.

## [Use](#id2)

The simplest use of this API is:

1. Configure a network timeout using [`net_timeout_set()`](#c.net_timeout_set).
2. Use [`net_timeout_evaluate()`](#c.net_timeout_evaluate) to determine how long it is until the
   timeout occurs. Schedule a timeout to occur after this delay.
3. When the timeout callback is invoked, use [`net_timeout_evaluate()`](#c.net_timeout_evaluate)
   again to determine whether the timeout has completed, or whether there is
   additional time remaining. If the latter, reschedule the callback.
4. While the timeout is running, use [`net_timeout_remaining()`](#c.net_timeout_remaining) to get
   the number of seconds until the timeout expires. This may be used to
   explicitly update the timeout, which should be done by canceling any
   pending callback and restarting from step 1 with the new timeout.

The [`net_timeout`](#c.net_timeout) contains a `sys_snode_t` that allows multiple
timeout instances to be aggregated to share a single kernel timer element.
The application must use [`net_timeout_evaluate()`](#c.net_timeout_evaluate) on all instances to
determine the next timeout event to occur.

[`net_timeout_deadline()`](#c.net_timeout_deadline) may be used to reconstruct the full-precision
deadline of the timeout. This exists primarily for testing but may have use
in some applications, as it does allow a millisecond-resolution calculation of
remaining time.

## [API Reference](#id3)

*group* Network long timeout primitives and helpers
:   Network long timeout primitives and helpers.

    Defines

    NET\_TIMEOUT\_MAX\_VALUE
    :   Divisor used to support ms resolution timeouts.

        Because delays are processed in work queues which are not invoked synchronously with clock changes we need to be able to detect timeouts after they occur, which requires comparing “deadline” to “now” with enough “slop” to handle any observable latency due to “now” advancing past “deadline”.

        The simplest solution is to use the native conversion of the well-defined 32-bit unsigned difference to a 32-bit signed difference, which caps the maximum delay at INT32\_MAX. This is compatible with the standard mechanism for detecting completion of deadlines that do not overflow their representation.

    Functions

    void net\_timeout\_set(struct [net\_timeout](#c.net_timeout) \*timeout, uint32\_t lifetime, uint32\_t now)
    :   Configure a network timeout structure.

        Parameters:
        :   - **timeout** – a pointer to the timeout state.
            - **lifetime** – the duration of the timeout in seconds.
            - **now** – the time at which the timeout started counting down, in milliseconds. This is generally a captured value of [k\_uptime\_get\_32()](../../../kernel/services/timing/clocks.md#group__clock__apis_1ga9253cfb7b46af4d8994349323ce9872b).

    int64\_t net\_timeout\_deadline(const struct [net\_timeout](#c.net_timeout) \*timeout, int64\_t now)
    :   Return the 64-bit system time at which the timeout will complete.

        Note

        Correct behavior requires invocation of [net\_timeout\_evaluate()](#group__net__timeout_1ga07b07966dd10929f6d3774467614f006) at its specified intervals.

        Parameters:
        :   - **timeout** – state a pointer to the timeout state, initialized by [net\_timeout\_set()](#group__net__timeout_1ga833e08b83a671d4adff799d648a12417) and maintained by [net\_timeout\_evaluate()](#group__net__timeout_1ga07b07966dd10929f6d3774467614f006).
            - **now** – the full-precision value of [k\_uptime\_get()](../../../kernel/services/timing/clocks.md#group__clock__apis_1gae3e992cd3257c23d5b26d765fcbb2b69) relative to which the deadline will be calculated.

        Returns:
        :   the value of [k\_uptime\_get()](../../../kernel/services/timing/clocks.md#group__clock__apis_1gae3e992cd3257c23d5b26d765fcbb2b69) at which the timeout will expire.

    uint32\_t net\_timeout\_remaining(const struct [net\_timeout](#c.net_timeout) \*timeout, uint32\_t now)
    :   Calculate the remaining time to the timeout in whole seconds.

        Note

        This function rounds the remaining time down, i.e. if the timeout will occur in 3500 milliseconds the value 3 will be returned.

        Note

        Correct behavior requires invocation of [net\_timeout\_evaluate()](#group__net__timeout_1ga07b07966dd10929f6d3774467614f006) at its specified intervals.

        Parameters:
        :   - **timeout** – a pointer to the timeout state
            - **now** – the time relative to which the estimate of remaining time should be calculated. This should be recently captured value from [k\_uptime\_get\_32()](../../../kernel/services/timing/clocks.md#group__clock__apis_1ga9253cfb7b46af4d8994349323ce9872b).

        Return values:
        :   - **0** – if the timeout has completed.
            - **positive** – the remaining duration of the timeout, in seconds.

    uint32\_t net\_timeout\_evaluate(struct [net\_timeout](#c.net_timeout) \*timeout, uint32\_t now)
    :   Update state to reflect elapsed time and get new delay.

        This function must be invoked periodically to (1) apply the effect of elapsed time on what remains of a total delay that exceeded the maximum representable delay, and (2) determine that either the timeout has completed or that the infrastructure must wait a certain period before checking again for completion.

        Parameters:
        :   - **timeout** – a pointer to the timeout state
            - **now** – the time relative to which the estimate of remaining time should be calculated. This should be recently captured value from [k\_uptime\_get\_32()](../../../kernel/services/timing/clocks.md#group__clock__apis_1ga9253cfb7b46af4d8994349323ce9872b).

        Return values:
        :   - **0** – if the timeout has completed
            - **positive** – the maximum delay until the state of this timeout should be re-evaluated, in milliseconds.

    struct net\_timeout
    :   *#include <net\_timeout.h>*

        Generic struct for handling network timeouts.

        Except for the linking node, all access to state from these objects must go through the defined API.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Used to link multiple timeouts that share a common timer infrastructure.

            For examples a set of related timers may use a single delayed work structure, which is always scheduled at the shortest time to a timeout event.

        uint32\_t timer\_start
        :   Time at which the timer was last set.

            This usually corresponds to the low 32 bits of [k\_uptime\_get()](../../../kernel/services/timing/clocks.md#group__clock__apis_1gae3e992cd3257c23d5b26d765fcbb2b69).

        uint32\_t timer\_timeout
        :   Portion of remaining timeout that does not exceed NET\_TIMEOUT\_MAX\_VALUE.

            This value is updated in parallel with timer\_start and wrap\_counter by [net\_timeout\_evaluate()](#group__net__timeout_1ga07b07966dd10929f6d3774467614f006).

        uint32\_t wrap\_counter
        :   Timer wrap count.

            This tracks multiples of NET\_TIMEOUT\_MAX\_VALUE milliseconds that have yet to pass. It is also updated along with timer\_start and wrap\_counter by [net\_timeout\_evaluate()](#group__net__timeout_1ga07b07966dd10929f6d3774467614f006).
