---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/timeutil.html
original_path: kernel/timeutil.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Time Utilities

## Overview

[Uptime](services/timing/clocks.md#kernel-timing-uptime) in Zephyr is based on the a tick counter. With
the default [`CONFIG_TICKLESS_KERNEL`](../kconfig.md#CONFIG_TICKLESS_KERNEL "CONFIG_TICKLESS_KERNEL") this counter advances at a
nominally constant rate from zero at the instant the system started. The POSIX
equivalent to this counter is something like `CLOCK_MONOTONIC` or, in Linux,
`CLOCK_MONOTONIC_RAW`. [`k_uptime_get()`](services/timing/clocks.md#c.k_uptime_get "k_uptime_get") provides a millisecond
representation of this time.

Applications often need to correlate the Zephyr internal time with external
time scales used in daily life, such as local time or Coordinated Universal
Time. These systems interpret time in different ways and may have
discontinuities due to [leap seconds](https://what-if.xkcd.com/26/) and
local time offsets like daylight saving time.

Because of these discontinuities, as well as significant inaccuracies in the
clocks underlying the cycle counter, the offset between time estimated from
the Zephyr clock and the actual time in a “real” civil time scale is not
constant and can vary widely over the runtime of a Zephyr application.

The time utilities API supports:

- [converting between time representations](#timeutil-repr)
- [synchronizing and aligning time scales](#timeutil-sync)

For terminology and concepts that support these functions see
[Concepts Underlying Time Support in Zephyr](#timeutil-concepts).

## Time Utility APIs

### Representation Transformation

Time scale instants can be represented in multiple ways including:

- Seconds since an epoch. POSIX representations of time in this form include
  `time_t` and `struct timespec`, which are generally interpreted as a
  representation of [“UNIX Time”](https://tools.ietf.org/html/rfc8536#section-2).
- Calendar time as a year, month, day, hour, minutes, and seconds relative to
  an epoch. POSIX representations of time in this form include `struct tm`.

Keep in mind that these are simply time representations that must be
interpreted relative to a time scale which may be local time, UTC, or some
other continuous or discontinuous scale.

Some necessary transformations are available in standard C library
routines. For example, `time_t` measuring seconds since the POSIX EPOCH is
converted to `struct tm` representing calendar time with [gmtime()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/gmtime.html).
Sub-second timestamps like `struct timespec` can also use this to produce
the calendar time representation and deal with sub-second offsets separately.

The inverse transformation is not standardized: APIs like `mktime()` expect
information about time zones. Zephyr provides this transformation with
`timeutil_timegm()` and [`timeutil_timegm64()`](#c.timeutil_timegm64).

*group* Time Representation APIs
:   Functions

    int64\_t timeutil\_timegm64(const struct [tm](#c.timeutil_timegm64) \*tm)
    :   Convert broken-down time to a POSIX epoch offset in seconds.

        See also

        [http://man7.org/linux/man-pages/man3/timegm.3.html](http://man7.org/linux/man-pages/man3/timegm.3.html)

        Parameters:
        :   - **tm** – pointer to broken down time.

        Returns:
        :   the corresponding time in the POSIX epoch time scale.

### Time Scale Synchronization

There are several factors that affect synchronizing time scales:

- The rate of discrete instant representation change. For example Zephyr
  uptime is tracked in ticks which advance at events that nominally occur at
  [`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") Hertz, while an external time
  source may provide data in whole or fractional seconds (e.g. microseconds).
- The absolute offset required to align the two scales at a single instant.
- The relative error between observable instants in each scale, required to
  align multiple instants consistently. For example a reference clock that’s
  conditioned by a 1-pulse-per-second GPS signal will be much more accurate
  than a Zephyr system clock driven by a RC oscillator with a +/- 250 ppm
  error.

Synchronization or alignment between time scales is done with a multi-step
process:

- An instant in a time scale is represented by an (unsigned) 64-bit integer,
  assumed to advance at a fixed nominal rate.
- [`timeutil_sync_config`](#c.timeutil_sync_config) records the nominal rates of a reference
  time scale/source (e.g. TAI) and a local time source
  (e.g. [`k_uptime_ticks()`](services/timing/clocks.md#c.k_uptime_ticks "k_uptime_ticks")).
- [`timeutil_sync_instant`](#c.timeutil_sync_instant) records the representation of a single
  instant in both the reference and local time scales.
- [`timeutil_sync_state`](#c.timeutil_sync_state) provides storage for an initial instant, a
  recently received second observation, and a skew that can adjust for
  relative errors in the actual rate of each time scale.
- [`timeutil_sync_ref_from_local()`](#c.timeutil_sync_ref_from_local) and
  [`timeutil_sync_local_from_ref()`](#c.timeutil_sync_local_from_ref) convert instants in one time scale
  to another taking into account skew that can be estimated from the two
  instances stored in the state structure by
  [`timeutil_sync_estimate_skew()`](#c.timeutil_sync_estimate_skew).

*group* Time Synchronization APIs
:   Functions

    int timeutil\_sync\_state\_update(struct [timeutil\_sync\_state](#c.timeutil_sync_state) \*tsp, const struct [timeutil\_sync\_instant](#c.timeutil_sync_instant) \*inst)
    :   Record a new instant in the time synchronization state.

        Note that this updates only the latest persisted instant. The skew is not adjusted automatically.

        Parameters:
        :   - **tsp** – pointer to a [timeutil\_sync\_state](#structtimeutil__sync__state) object.
            - **inst** – the new instant to be recorded. This becomes the base instant if there is no base instant, otherwise the value must be strictly after the base instant in both the reference and local time scales.

        Return values:
        :   - **0** – if installation succeeded in providing a new base
            - **1** – if installation provided a new latest instant
            - **-EINVAL** – if the new instant is not compatible with the base instant

    int timeutil\_sync\_state\_set\_skew(struct [timeutil\_sync\_state](#c.timeutil_sync_state) \*tsp, float skew, const struct [timeutil\_sync\_instant](#c.timeutil_sync_instant) \*base)
    :   Update the state with a new skew and possibly base value.

        Set the skew from a value retrieved from persistent storage, or calculated based on recent skew estimations including from [timeutil\_sync\_estimate\_skew()](#group__timeutil__sync__apis_1gac4c25a1ed054a8a06c87d4df9c25ffc6).

        Optionally update the base timestamp. If the base is replaced the latest instant will be cleared until [timeutil\_sync\_state\_update()](#group__timeutil__sync__apis_1gaa6926a23d1c4fbb61584e957d157bd62) is invoked.

        Parameters:
        :   - **tsp** – pointer to a time synchronization state.
            - **skew** – the skew to be used. The value must be positive and shouldn’t be too far away from 1.
            - **base** – optional new base to be set. If provided this becomes the base timestamp that will be used along with skew to convert between reference and local timescale instants. Setting the base clears the captured latest value.

        Returns:
        :   0 if skew was updated

        Returns:
        :   -EINVAL if skew was not valid

    float timeutil\_sync\_estimate\_skew(const struct [timeutil\_sync\_state](#c.timeutil_sync_state) \*tsp)
    :   Estimate the skew based on current state.

        Using the base and latest syncpoints from the state determine the skew of the local clock relative to the reference clock. See [timeutil\_sync\_state::skew](#structtimeutil__sync__state_1a39454807d207dddb2564d766c8ec2ea3).

        Parameters:
        :   - **tsp** – pointer to a time synchronization state. The base and latest syncpoints must be present and the latest syncpoint must be after the base point in the local time scale.

        Returns:
        :   the estimated skew, or zero if skew could not be estimated.

    int timeutil\_sync\_ref\_from\_local(const struct [timeutil\_sync\_state](#c.timeutil_sync_state) \*tsp, uint64\_t local, uint64\_t \*refp)
    :   Interpolate a reference timescale instant from a local instant.

        Parameters:
        :   - **tsp** – pointer to a time synchronization state. This must have a base and a skew installed.
            - **local** – an instant measured in the local timescale. This may be before or after the base instant.
            - **refp** – where the corresponding instant in the reference timescale should be stored. A negative interpolated reference time produces an error. If interpolation fails the referenced object is not modified.

        Return values:
        :   - **0** – if interpolated using a skew of 1
            - **1** – if interpolated using a skew not equal to 1
            - **-EINVAL** –

              - the times synchronization state is not adequately initialized
              - `refp` is null
            - **-ERANGE** – the interpolated reference time would be negative

    int timeutil\_sync\_local\_from\_ref(const struct [timeutil\_sync\_state](#c.timeutil_sync_state) \*tsp, uint64\_t ref, int64\_t \*localp)
    :   Interpolate a local timescale instant from a reference instant.

        Parameters:
        :   - **tsp** – pointer to a time synchronization state. This must have a base and a skew installed.
            - **ref** – an instant measured in the reference timescale. This may be before or after the base instant.
            - **localp** – where the corresponding instant in the local timescale should be stored. An interpolated value before local time 0 is provided without error. If interpolation fails the referenced object is not modified.

        Return values:
        :   - **0** – if successful with a skew of 1
            - **1** – if successful with a skew not equal to 1
            - **-EINVAL** –

              - the time synchronization state is not adequately initialized
              - `refp` is null

    int32\_t timeutil\_sync\_skew\_to\_ppb(float skew)
    :   Convert from a skew to an error in parts-per-billion.

        A skew of 1.0 has zero error. A skew less than 1 has a positive error (clock is faster than it should be). A skew greater than one has a negative error (clock is slower than it should be).

        Note that due to the limited precision of `float` compared with `double` the smallest error that can be represented is about 120 ppb. A “precise” time source may have error on the order of 2000 ppb.

        A skew greater than 3.14748 may underflow the 32-bit representation; this represents a clock running at less than 1/3 its nominal rate.

        Returns:
        :   skew error represented as parts-per-billion, or INT32\_MIN if the skew cannot be represented in the return type.

    struct timeutil\_sync\_config
    :   *#include <timeutil.h>*

        Immutable state for synchronizing two clocks.

        Values required to convert durations between two time scales.

        Note

        The accuracy of the translation and calculated skew between sources depends on the resolution of these frequencies. A reference frequency with microsecond or nanosecond resolution would produce the most accurate tracking when the local reference is the Zephyr tick counter. A reference source like an RTC chip with 1 Hz resolution requires a much larger interval between sampled instants to detect relative clock drift.

        Public Members

        uint32\_t ref\_Hz
        :   The nominal instance counter rate in Hz.

            This value is assumed to be precise, but may drift depending on the reference clock source.

            The value must be positive.

        uint32\_t local\_Hz
        :   The nominal local counter rate in Hz.

            This value is assumed to be inaccurate but reasonably stable. For a local clock driven by a crystal oscillator an error of 25 ppm is common; for an RC oscillator larger errors should be expected. The timeutil\_sync infrastructure can calculate the skew between the local and reference clocks and apply it when converting between time scales.

            The value must be positive.

    struct timeutil\_sync\_instant
    :   *#include <timeutil.h>*

        Representation of an instant in two time scales.

        Capturing the same instant in two time scales provides a registration point that can be used to convert between those time scales.

        Public Members

        uint64\_t ref
        :   An instant in the reference time scale.

            This must never be zero in an initialized [timeutil\_sync\_instant](#structtimeutil__sync__instant) object.

        uint64\_t local
        :   The corresponding instance in the local time scale.

            This may be zero in a valid [timeutil\_sync\_instant](#structtimeutil__sync__instant) object.

    struct timeutil\_sync\_state
    :   *#include <timeutil.h>*

        State required to convert instants between time scales.

        This state in conjunction with functions that manipulate it capture the offset information necessary to convert between two timescales along with information that corrects for skew due to inaccuracies in clock rates.

        State objects should be zero-initialized before use.

        Public Members

        const struct [timeutil\_sync\_config](#c.timeutil_sync_config) \*cfg
        :   Pointer to reference and local rate information.

        struct [timeutil\_sync\_instant](#c.timeutil_sync_instant) base
        :   The base instant in both time scales.

        struct [timeutil\_sync\_instant](#c.timeutil_sync_instant) latest
        :   The most recent instant in both time scales.

            This is captured here to provide data for skew calculation.

        float skew
        :   The scale factor used to correct for clock skew.

            The nominal rate for the local counter is assumed to be inaccurate but stable, i.e. it will generally be some parts-per-million faster or slower than specified.

            A duration in observed local clock ticks must be multiplied by this value to produce a duration in ticks of a clock operating at the nominal local rate.

            A zero value indicates that the skew has not been initialized. If the value is zero when [base](#structtimeutil__sync__state_1aadbd2ecd98197865e3a71daa8967ce99) is initialized the skew will be set to 1. Otherwise the skew is assigned through [timeutil\_sync\_state\_set\_skew()](#group__timeutil__sync__apis_1ga01142931b299e848b0642634a0922be5).

## Concepts Underlying Time Support in Zephyr

Terms from [ISO/TC 154/WG 5 N0038](https://www.loc.gov/standards/datetime/iso-tc154-wg5_n0038_iso_wd_8601-1_2016-02-16.pdf)
(ISO/WD 8601-1) and elsewhere:

- A *time axis* is a representation of time as an ordered sequence of
  instants.
- A *time scale* is a way of representing an instant relative to an origin
  that serves as the epoch.
- A time scale is *monotonic* (increasing) if the representation of successive
  time instants never decreases in value.
- A time scale is *continuous* if the representation has no abrupt changes in
  value, e.g. jumping forward or back when going between successive instants.
- [Civil time](https://en.wikipedia.org/wiki/Civil_time) generally refers
  to time scales that legally defined by civil authorities, like local
  governments, often to align local midnight to solar time.

### Relevant Time Scales

[International Atomic Time](https://en.wikipedia.org/wiki/International_Atomic_Time) (TAI) is a time
scale based on averaging clocks that count in SI seconds. TAI is a monotonic
and continuous time scale.

[Universal Time](https://en.wikipedia.org/wiki/Universal_Time) (UT) is a
time scale based on Earth’s rotation. UT is a discontinuous time scale as it
requires occasional adjustments ([leap seconds](https://en.wikipedia.org/wiki/Leap_second)) to maintain alignment to
changes in Earth’s rotation. Thus the difference between TAI and UT varies
over time. There are several variants of UT, with [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) being the most
common.

UT times are independent of location. UT is the basis for Standard Time
(or “local time”) which is the time at a particular location. Standard
time has a fixed offset from UT at any given instant, primarily
influenced by longitude, but the offset may be adjusted (“daylight
saving time”) to align standard time to the local solar time. In a sense
local time is “more discontinuous” than UT.

[POSIX Time](https://tools.ietf.org/html/rfc8536#section-2) is a time scale
that counts seconds since the “POSIX epoch” at 1970-01-01T00:00:00Z (i.e. the
start of 1970 UTC). [UNIX Time](https://tools.ietf.org/html/rfc8536#section-2) is an extension of POSIX
time using negative values to represent times before the POSIX epoch. Both of
these scales assume that every day has exactly 86400 seconds. In normal use
instants in these scales correspond to times in the UTC scale, so they inherit
the discontinuity.

The continuous analogue is [UNIX Leap Time](https://tools.ietf.org/html/rfc8536#section-2) which is UNIX time plus all
leap-second corrections added after the POSIX epoch (when TAI-UTC was 8 s).

#### Example of Time Scale Differences

A positive leap second was introduced at the end of 2016, increasing the
difference between TAI and UTC from 36 seconds to 37 seconds. There was
no leap second introduced at the end of 1999, when the difference
between TAI and UTC was only 32 seconds. The following table shows
relevant civil and epoch times in several scales:

| UTC Date | UNIX time | TAI Date | TAI-UTC | UNIX Leap Time |
| --- | --- | --- | --- | --- |
| 1970-01-01T00:00:00Z | 0 | 1970-01-01T00:00:08 | +8 | 0 |
| 1999-12-31T23:59:28Z | 946684768 | 2000-01-01T00:00:00 | +32 | 946684792 |
| 1999-12-31T23:59:59Z | 946684799 | 2000-01-01T00:00:31 | +32 | 946684823 |
| 2000-01-01T00:00:00Z | 946684800 | 2000-01-01T00:00:32 | +32 | 946684824 |
| 2016-12-31T23:59:59Z | 1483228799 | 2017-01-01T00:00:35 | +36 | 1483228827 |
| 2016-12-31T23:59:60Z | undefined | 2017-01-01T00:00:36 | +36 | 1483228828 |
| 2017-01-01T00:00:00Z | 1483228800 | 2017-01-01T00:00:37 | +37 | 1483228829 |

#### Functional Requirements

The Zephyr tick counter has no concept of leap seconds or standard time
offsets and is a continuous time scale. However it can be relatively
inaccurate, with drifts as much as three minutes per hour (assuming an RC
timer with 5% tolerance).

There are two stages required to support conversion between Zephyr time and
common human time scales:

- Translation between the continuous but inaccurate Zephyr time scale and an
  accurate external stable time scale;
- Translation between the stable time scale and the (possibly discontinuous)
  civil time scale.

The API around [`timeutil_sync_state_update()`](#c.timeutil_sync_state_update) supports the first step
of converting between continuous time scales.

The second step requires external information including schedules of leap
seconds and local time offset changes. This may be best provided by an
external library, and is not currently part of the time utility APIs.

#### Selecting an External Source and Time Scale

If an application requires civil time accuracy within several seconds then UTC
could be used as the stable time source. However, if the external source
adjusts to a leap second there will be a discontinuity: the elapsed time
between two observations taken at 1 Hz is not equal to the numeric difference
between their timestamps.

For precise activities a continuous scale that is independent of local and
solar adjustments simplifies things considerably. Suitable continuous scales
include:

- GPS time: epoch of 1980-01-06T00:00:00Z, continuous following TAI with an
  offset of TAI-GPS=19 s.
- Bluetooth Mesh time: epoch of 2000-01-01T00:00:00Z, continuous following TAI
  with an offset of -32.
- UNIX Leap Time: epoch of 1970-01-01T00:00:00Z, continuous following TAI with
  an offset of -8.

Because C and Zephyr library functions support conversion between integral and
calendar time representations using the UNIX epoch, UNIX Leap Time is an ideal
choice for the external time scale.

The mechanism used to populate synchronization points is not relevant: it may
involve reading from a local high-precision RTC peripheral, exchanging packets
over a network using a protocol like NTP or PTP, or processing NMEA messages
received a GPS with or without a 1pps signal.
