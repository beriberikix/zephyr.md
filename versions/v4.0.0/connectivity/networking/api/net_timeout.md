---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/net_timeout.html
original_path: connectivity/networking/api/net_timeout.html
---

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

1. Configure a network timeout using [`net_timeout_set()`](../../../doxygen/html/group__net__timeout.md#ga833e08b83a671d4adff799d648a12417).
2. Use [`net_timeout_evaluate()`](../../../doxygen/html/group__net__timeout.md#ga07b07966dd10929f6d3774467614f006) to determine how long it is until the
   timeout occurs. Schedule a timeout to occur after this delay.
3. When the timeout callback is invoked, use [`net_timeout_evaluate()`](../../../doxygen/html/group__net__timeout.md#ga07b07966dd10929f6d3774467614f006)
   again to determine whether the timeout has completed, or whether there is
   additional time remaining. If the latter, reschedule the callback.
4. While the timeout is running, use [`net_timeout_remaining()`](../../../doxygen/html/group__net__timeout.md#ga34e39484b19c39b3e37a4799848ad502) to get
   the number of seconds until the timeout expires. This may be used to
   explicitly update the timeout, which should be done by canceling any
   pending callback and restarting from step 1 with the new timeout.

The [`net_timeout`](../../../doxygen/html/structnet__timeout.md) contains a `sys_snode_t` that allows multiple
timeout instances to be aggregated to share a single kernel timer element.
The application must use [`net_timeout_evaluate()`](../../../doxygen/html/group__net__timeout.md#ga07b07966dd10929f6d3774467614f006) on all instances to
determine the next timeout event to occur.

[`net_timeout_deadline()`](../../../doxygen/html/group__net__timeout.md#ga3d9804474050d070fc4224e834f8cefc) may be used to reconstruct the full-precision
deadline of the timeout. This exists primarily for testing but may have use
in some applications, as it does allow a millisecond-resolution calculation of
remaining time.

## [API Reference](#id3)

[Network long timeout primitives and helpers](../../../doxygen/html/group__net__timeout.md)
