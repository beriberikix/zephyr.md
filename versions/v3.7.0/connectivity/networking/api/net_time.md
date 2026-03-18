---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_time.html
original_path: connectivity/networking/api/net_time.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Network time representation in the network stack

## API Reference

*group* Network time representation.
:   Defines

    NET\_TIME\_MAX
    :   The largest positive time value that can be represented by [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56).

    NET\_TIME\_MIN
    :   The smallest negative time value that can be represented by [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56).

    NET\_TIME\_SEC\_MAX
    :   The largest positive number of seconds that can be safely represented by [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56).

    NET\_TIME\_SEC\_MIN
    :   The smallest negative number of seconds that can be safely represented by [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56).

    Typedefs

    typedef int64\_t net\_time\_t
    :   Any occurrence of [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) specifies a concept of nanosecond resolution scalar time span, future (positive) or past (negative) relative time or absolute timestamp referred to some local network uptime reference clock that does not wrap during uptime and is - in a certain, well-defined sense - common to all local network interfaces, sometimes even to remote interfaces on the same network.

        This type is EXPERIMENTAL. Usage is currently restricted to representation of time within the network subsystem.

        Timed network protocols (PTP, TDMA, …) usually require several local or remote interfaces to share a common notion of elapsed time within well-defined tolerances. Network uptime therefore differs from time represented by a single hardware counter peripheral in that it will need to be represented in several distinct hardware peripherals with different frequencies, accuracy and precision. To co-operate, these hardware counters will have to be “syntonized” or “disciplined” (i.e. frequency and phase locked) with respect to a common local or remote network reference time signal. Be aware that while syntonized clocks share the same frequency and phase, they do not usually share the same epoch (zero-point).

        This also explains why network time, if represented as a cycle value of some specific hardware counter, will never be “precise” but only can be “good

        enough” with respect to the tolerances (resolution, drift, jitter) required by a given network protocol. All counter peripherals involved in a timed network protocol must comply with these tolerances.

        Please use specific cycle/tick counter values rather than [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) whenever possible especially when referring to the kernel system clock or values of any single counter peripheral.

        [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) cannot represent general clocks referred to an arbitrary epoch as it only covers roughly +/- ~290 years. It also cannot be used to represent time according to a more complex timescale (e.g. including leap seconds, time adjustments, complex calendars or time zones). In these cases you may use timespec (C11, POSIX.1-2001), timeval (POSIX.1-2001) or broken down time as in tm (C90). The advantage of [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) over these structured time representations is lower memory footprint, faster and simpler scalar arithmetic and easier conversion from/to low-level hardware counter values. Also [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) can be used in the network stack as well as in applications while POSIX concepts cannot. Converting [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) from/to structured time representations is possible in a limited way but - except for timespec - requires concepts that must be implemented by higher-level APIs. Utility functions converting from/to timespec will be provided as part of the [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) API as and when needed.

        If you want to represent more coarse grained scalar time in network applications, use time\_t (C99, POSIX.1-2001) which is specified to represent seconds or suseconds\_t (POSIX.1-2001) for microsecond resolution. Kernel [k\_ticks\_t](../../../kernel/services/timing/clocks.md#group__clock__apis_1ga9832cb0adc2d1866420e5c370a0863e2) and cycles (both specific to Zephyr) have an unspecified resolution but are useful to represent kernel timer values and implement high resolution spinning.

        If you need even finer grained time resolution, you may want to look at (g)PTP concepts, see [net\_ptp\_extended\_time](ptp_time.md#structnet__ptp__extended__time).

        The reason why we don’t use int64\_t directly to represent scalar nanosecond resolution times in the network stack is that it has been shown in the past that fields using generic type will often not be used correctly (e.g. with the wrong resolution or to represent underspecified concepts of time with unclear syntonization semantics).

        Any API that exposes or consumes [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) values SHALL ensure that it maintains the specified contract including all protocol specific tolerances and therefore clients can rely on common semantics of this type. This makes times coming from different hardware peripherals and even from different network nodes comparable within well-defined limits and therefore [net\_time\_t](#group__net__time_1gaf1da332e3909fca30de991cc2f950e56) is the ideal intermediate building block for timed network protocols.
