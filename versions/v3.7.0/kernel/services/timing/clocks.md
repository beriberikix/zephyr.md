---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/services/timing/clocks.html
original_path: kernel/services/timing/clocks.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Kernel Timing

Zephyr provides a robust and scalable timing framework to enable
reporting and tracking of timed events from hardware timing sources of
arbitrary precision.

## Time Units

Kernel time is tracked in several units which are used for different
purposes.

Real time values, typically specified in milliseconds or microseconds,
are the default presentation of time to application code. They have
the advantages of being universally portable and pervasively
understood, though they may not match the precision of the underlying
hardware perfectly.

The kernel presents a “cycle” count via the [`k_cycle_get_32()`](#c.k_cycle_get_32)
and [`k_cycle_get_64()`](#c.k_cycle_get_64) APIs. The intent is that this counter
represents the fastest cycle counter that the operating system is able
to present to the user (for example, a CPU cycle counter) and that the
read operation is very fast. The expectation is that very sensitive
application code might use this in a polling manner to achieve maximal
precision. The frequency of this counter is required to be steady
over time, and is available from
`sys_clock_hw_cycles_per_sec()` (which on almost all
platforms is a runtime constant that evaluates to
CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC).

For asynchronous timekeeping, the kernel defines a “ticks” concept. A
“tick” is the internal count in which the kernel does all its internal
uptime and timeout bookkeeping. Interrupts are expected to be
delivered on tick boundaries to the extent practical, and no
fractional ticks are tracked. The choice of tick rate is configurable
via [`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC"). Defaults on most
hardware platforms (ones that support setting arbitrary interrupt
timeouts) are expected to be in the range of 10 kHz, with software
emulation platforms and legacy drivers using a more traditional 100 Hz
value.

### Conversion

Zephyr provides an extensively enumerated conversion library with
rounding control for all time units. Any unit of “ms” (milliseconds),
“us” (microseconds), “tick”, or “cyc” can be converted to any other.
Control of rounding is provided, and each conversion is available in
“floor” (round down to nearest output unit), “ceil” (round up) and
“near” (round to nearest). Finally the output precision can be
specified as either 32 or 64 bits.

For example: `k_ms_to_ticks_ceil32()` will convert a
millisecond input value to the next higher number of ticks, returning
a result truncated to 32 bits of precision; and
`k_cyc_to_us_floor64()` will convert a measured cycle count
to an elapsed number of microseconds in a full 64 bits of precision.
See the reference documentation for the full enumeration of conversion
routines.

On most platforms, where the various counter rates are integral
multiples of each other and where the output fits within a single
word, these conversions expand to a 2-4 operation sequence, requiring
full precision only where actually required and requested.

## Uptime

The kernel tracks a system uptime count on behalf of the application.
This is available at all times via [`k_uptime_get()`](#c.k_uptime_get), which
provides an uptime value in milliseconds since system boot. This is
expected to be the utility used by most portable application code.

The internal tracking, however, is as a 64 bit integer count of ticks.
Apps with precise timing requirements (that are willing to do their
own conversions to portable real time units) may access this with
[`k_uptime_ticks()`](#c.k_uptime_ticks).

## Timeouts

The Zephyr kernel provides many APIs with a “timeout” parameter.
Conceptually, this indicates the time at which an event will occur.
For example:

- Kernel blocking operations like [`k_sem_take()`](../synchronization/semaphores.md#c.k_sem_take "k_sem_take") or
  [`k_queue_get()`](../data_passing/queues.md#c.k_queue_get "k_queue_get") may provide a timeout after which the
  routine will return with an error code if no data is available.
- Kernel `k_timer` objects must specify delays for
  their duration and period.
- The kernel [`k_work_delayable`](../threads/workqueue.md#c.k_work_delayable "k_work_delayable") API provides a timeout parameter
  indicating when a work queue item will be added to the system queue.

All these values are specified using a [`k_timeout_t`](#c.k_timeout_t) value. This is
an opaque struct type that must be initialized using one of a family
of kernel timeout macros. The most common, [`K_MSEC`](#c.K_MSEC), defines
a time in milliseconds after the current time.

What is meant by “current time” for relative timeouts depends on the context:

- When scheduling a relative timeout from within a timeout callback (e.g. from
  within the expiry function passed to [`k_timer_init()`](timers.md#c.k_timer_init "k_timer_init") or the work handler
  passed to [`k_work_init_delayable()`](../threads/workqueue.md#c.k_work_init_delayable "k_work_init_delayable")), “current time” is the exact time at
  which the currently firing timeout was originally scheduled even if the “real
  time” will already have advanced. This is to ensure that timers scheduled from
  within another timer’s callback will always be calculated with a precise offset
  to the firing timer. It is thereby possible to fire at regular intervals without
  introducing systematic clock drift over time.
- When scheduling a timeout from application context, “current time” means the
  value returned by [`k_uptime_ticks()`](#c.k_uptime_ticks) at the time at which the kernel
  receives the timeout value.

Other options for timeout initialization follow the unit conventions
described above: [`K_NSEC()`](#c.K_NSEC), [`K_USEC`](#c.K_USEC), [`K_TICKS`](#c.K_TICKS) and
[`K_CYC()`](#c.K_CYC) specify timeout values that will expire after specified
numbers of nanoseconds, microseconds, ticks and cycles, respectively.

Precision of [`k_timeout_t`](#c.k_timeout_t) values is configurable, with the default
being 32 bits. Large uptime counts in non-tick units will experience
complicated rollover semantics, so it is expected that
timing-sensitive applications with long uptimes will be configured to
use a 64 bit timeout type.

Finally, it is possible to specify timeouts as absolute times since
system boot. A timeout initialized with `K_TIMEOUT_ABS_MS`
indicates a timeout that will expire after the system uptime reaches
the specified value. There are likewise nanosecond, microsecond,
cycles and ticks variants of this API.

## Timing Internals

### Timeout Queue

All Zephyr [`k_timeout_t`](#c.k_timeout_t) events specified using the API above are
managed in a single, global queue of events. Each event is stored in
a double-linked list, with an attendant delta count in ticks from the
previous event. The action to take on an event is specified as a
callback function pointer provided by the subsystem requesting the
event, along with a `_timeout` tracking struct that is
expected to be embedded within subsystem-defined data structures (for
example: a `wait_q` struct, or a `k_tid_t` thread struct).

Note that all variant units passed via a [`k_timeout_t`](#c.k_timeout_t) are converted
to ticks once on insertion into the list. There no
multiple-conversion steps internal to the kernel, so precision is
guaranteed at the tick level no matter how many events exist or how
long a timeout might be.

Note that the list structure means that the CPU work involved in
managing large numbers of timeouts is quadratic in the number of
active timeouts. The API design of the timeout queue was intended to
permit a more scalable backend data structure, but no such
implementation exists currently.

### Timer Drivers

Kernel timing at the tick level is driven by a timer driver with a
comparatively simple API.

- The driver is expected to be able to “announce” new ticks to the
  kernel via the [`sys_clock_announce()`](#c.sys_clock_announce) call, which passes an integer
  number of ticks that have elapsed since the last announce call (or
  system boot). These calls can occur at any time, but the driver is
  expected to attempt to ensure (to the extent practical given
  interrupt latency interactions) that they occur near tick boundaries
  (i.e. not “halfway through” a tick), and most importantly that they
  be correct over time and subject to minimal skew vs. other counters
  and real world time.
- The driver is expected to provide a [`sys_clock_set_timeout()`](#c.sys_clock_set_timeout) call
  to the kernel which indicates how many ticks may elapse before the
  kernel must receive an announce call to trigger registered timeouts.
  It is legal to announce new ticks before that moment (though they
  must be correct) but delay after that will cause events to be
  missed. Note that the timeout value passed here is in a delta from
  current time, but that does not absolve the driver of the
  requirement to provide ticks at a steady rate over time. Naive
  implementations of this function are subject to bugs where the
  fractional tick gets “reset” incorrectly and causes clock skew.
- The driver is expected to provide a [`sys_clock_elapsed()`](#c.sys_clock_elapsed) call which
  provides a current indication of how many ticks have elapsed (as
  compared to a real world clock) since the last call to
  [`sys_clock_announce()`](#c.sys_clock_announce), which the kernel needs to test newly
  arriving timeouts for expiration.

Note that a natural implementation of this API results in a “tickless”
kernel, which receives and processes timer interrupts only for
registered events, relying on programmable hardware counters to
provide irregular interrupts. But a traditional, “ticked” or “dumb”
counter driver can be trivially implemented also:

- The driver can receive interrupts at a regular rate corresponding to
  the OS tick rate, calling [`sys_clock_announce()`](#c.sys_clock_announce) with an argument of one
  each time.
- The driver can ignore calls to [`sys_clock_set_timeout()`](#c.sys_clock_set_timeout), as every
  tick will be announced regardless of timeout status.
- The driver can return zero for every call to [`sys_clock_elapsed()`](#c.sys_clock_elapsed)
  as no more than one tick can be detected as having elapsed (because
  otherwise an interrupt would have been received).

### SMP Details

In general, the timer API described above does not change when run in
a multiprocessor context. The kernel will internally synchronize all
access appropriately, and ensure that all critical sections are small
and minimal. But some notes are important to detail:

- Zephyr is agnostic about which CPU services timer interrupts. It is
  not illegal (though probably undesirable in some circumstances) to
  have every timer interrupt handled on a single processor. Existing
  SMP architectures implement symmetric timer drivers.
- The [`sys_clock_announce()`](#c.sys_clock_announce) call is expected to be globally
  synchronized at the driver level. The kernel does not do any
  per-CPU tracking, and expects that if two timer interrupts fire near
  simultaneously, that only one will provide the current tick count to
  the timing subsystem. The other may legally provide a tick count of
  zero if no ticks have elapsed. It should not “skip” the announce
  call because of timeslicing requirements (see below).
- Some SMP hardware uses a single, global timer device, others use a
  per-CPU counter. The complexity here (for example: ensuring counter
  synchronization between CPUs) is expected to be managed by the
  driver, not the kernel.
- The next timeout value passed back to the driver via
  [`sys_clock_set_timeout()`](#c.sys_clock_set_timeout) is done identically for every CPU.
  So by default, every CPU will see simultaneous timer interrupts for
  every event, even though by definition only one of them should see a
  non-zero ticks argument to [`sys_clock_announce()`](#c.sys_clock_announce). This is probably
  a correct default for timing sensitive applications (because it
  minimizes the chance that an errant ISR or interrupt lock will delay
  a timeout), but may be a performance problem in some cases. The
  current design expects that any such optimization is the
  responsibility of the timer driver.

### Time Slicing

An auxiliary job of the timing subsystem is to provide tick counters
to the scheduler that allow implementation of time slicing of threads.
A thread time-slice cannot be a timeout value, as it does not reflect
a global expiration but instead a per-CPU value that needs to be
tracked independently on each CPU in an SMP context.

Because there may be no other hardware available to drive timeslicing,
Zephyr multiplexes the existing timer driver. This means that the
value passed to [`sys_clock_set_timeout()`](#c.sys_clock_set_timeout) may be clamped to a
smaller value than the current next timeout when a time sliced thread
is currently scheduled.

### Subsystems that keep millisecond APIs

In general, code like this will port just like applications code will.
Millisecond values from the user may be treated any way the subsystem
likes, and then converted into kernel timeouts using
[`K_MSEC()`](#c.K_MSEC) at the point where they are presented to the
kernel.

Obviously this comes at the cost of not being able to use new
features, like the higher precision timeout constructors or absolute
timeouts. But for many subsystems with simple needs, this may be
acceptable.

One complexity is [`K_FOREVER`](#c.K_FOREVER). Subsystems that might have
been able to accept this value to their millisecond API in the past no
longer can, because it is no longer an integral type. Such code
will need to use a different, integer-valued token to represent
“forever”. [`K_NO_WAIT`](#c.K_NO_WAIT) has the same typesafety concern too,
of course, but as it is (and has always been) simply a numerical zero,
it has a natural porting path.

### Subsystems using `k_timeout_t`

Ideally, code that takes a “timeout” parameter specifying a time to
wait should be using the kernel native abstraction where possible.
But [`k_timeout_t`](#c.k_timeout_t) is opaque, and needs to be converted before
it can be inspected by an application.

Some conversions are simple. Code that needs to test for
[`K_FOREVER`](#c.K_FOREVER) can simply use the [`K_TIMEOUT_EQ()`](#c.K_TIMEOUT_EQ)
macro to test the opaque struct for equality and take special action.

The more complicated case is when the subsystem needs to take a
timeout and loop, waiting for it to finish while doing some processing
that may require multiple blocking operations on underlying kernel
code. For example, consider this design:

```c
void my_wait_for_event(struct my_subsys *obj, int32_t timeout_in_ms)
{
    while (true) {
        uint32_t start = k_uptime_get_32();

        if (is_event_complete(obj)) {
            return;
        }

        /* Wait for notification of state change */
        k_sem_take(obj->sem, timeout_in_ms);

        /* Subtract elapsed time */
        timeout_in_ms -= (k_uptime_get_32() - start);
    }
}
```

This code requires that the timeout value be inspected, which is no
longer possible. For situations like this, the new API provides the
internal [`sys_timepoint_calc()`](#c.sys_timepoint_calc) and [`sys_timepoint_timeout()`](#c.sys_timepoint_timeout) routines
that converts an arbitrary timeout to and from a timepoint value based on
an uptime tick at which it will expire. So such a loop might look like:

```c
void my_wait_for_event(struct my_subsys *obj, k_timeout_t timeout)
{
    /* Compute the end time from the timeout */
    k_timepoint_t end = sys_timepoint_calc(timeout);

    do {
        if (is_event_complete(obj)) {
            return;
        }

        /* Update timeout with remaining time */
        timeout = sys_timepoint_timeout(end);

        /* Wait for notification of state change */
        k_sem_take(obj->sem, timeout);
    } while (!K_TIMEOUT_EQ(timeout, K_NO_WAIT));
}
```

Note that [`sys_timepoint_calc()`](#c.sys_timepoint_calc) accepts special values [`K_FOREVER`](#c.K_FOREVER)
and [`K_NO_WAIT`](#c.K_NO_WAIT), and works identically for absolute timeouts as well
as conventional ones. Conversely, [`sys_timepoint_timeout()`](#c.sys_timepoint_timeout) may return
[`K_FOREVER`](#c.K_FOREVER) or [`K_NO_WAIT`](#c.K_NO_WAIT) if those were used to create
the timepoint, the later also being returned if the timepoint is now in the
past. For simple cases, [`sys_timepoint_expired()`](#c.sys_timepoint_expired) can be used as well.

But some care is still required for subsystems that use those. Note that
delta timeouts need to be interpreted relative to a “current time”,
and obviously that time is the time of the call to
[`sys_timepoint_calc()`](#c.sys_timepoint_calc). But the user expects that the time is
the time they passed the timeout to you. Care must be taken to call
this function just once, as synchronously as possible to the timeout
creation in user code. It should not be used on a “stored” timeout
value, and should never be called iteratively in a loop.

#### API Reference

*group* System Clock APIs
:   System Clock APIs.

    Defines

    K\_NO\_WAIT
    :   Generate null timeout delay.

        This macro generates a timeout delay that instructs a kernel API not to wait if the requested operation cannot be performed immediately.

        Returns:
        :   Timeout delay value.

    K\_NSEC(t)
    :   Generate timeout delay from nanoseconds.

        This macro generates a timeout delay that instructs a kernel API to wait up to *t* nanoseconds to perform the requested operation. Note that timer precision is limited to the tick rate, not the requested value.

        Parameters:
        :   - **t** – Duration in nanoseconds.

        Returns:
        :   Timeout delay value.

    K\_USEC(t)
    :   Generate timeout delay from microseconds.

        This macro generates a timeout delay that instructs a kernel API to wait up to *t* microseconds to perform the requested operation. Note that timer precision is limited to the tick rate, not the requested value.

        Parameters:
        :   - **t** – Duration in microseconds.

        Returns:
        :   Timeout delay value.

    K\_CYC(t)
    :   Generate timeout delay from cycles.

        This macro generates a timeout delay that instructs a kernel API to wait up to *t* cycles to perform the requested operation.

        Parameters:
        :   - **t** – Duration in cycles.

        Returns:
        :   Timeout delay value.

    K\_TICKS(t)
    :   Generate timeout delay from system ticks.

        This macro generates a timeout delay that instructs a kernel API to wait up to *t* ticks to perform the requested operation.

        Parameters:
        :   - **t** – Duration in system ticks.

        Returns:
        :   Timeout delay value.

    K\_MSEC(ms)
    :   Generate timeout delay from milliseconds.

        This macro generates a timeout delay that instructs a kernel API to wait up to *ms* milliseconds to perform the requested operation.

        Parameters:
        :   - **ms** – Duration in milliseconds.

        Returns:
        :   Timeout delay value.

    K\_SECONDS(s)
    :   Generate timeout delay from seconds.

        This macro generates a timeout delay that instructs a kernel API to wait up to *s* seconds to perform the requested operation.

        Parameters:
        :   - **s** – Duration in seconds.

        Returns:
        :   Timeout delay value.

    K\_MINUTES(m)
    :   Generate timeout delay from minutes.

        This macro generates a timeout delay that instructs a kernel API to wait up to *m* minutes to perform the requested operation.

        Parameters:
        :   - **m** – Duration in minutes.

        Returns:
        :   Timeout delay value.

    K\_HOURS(h)
    :   Generate timeout delay from hours.

        This macro generates a timeout delay that instructs a kernel API to wait up to *h* hours to perform the requested operation.

        Parameters:
        :   - **h** – Duration in hours.

        Returns:
        :   Timeout delay value.

    K\_FOREVER
    :   Generate infinite timeout delay.

        This macro generates a timeout delay that instructs a kernel API to wait as long as necessary to perform the requested operation.

        Returns:
        :   Timeout delay value.

    K\_TICKS\_FOREVER

    K\_TIMEOUT\_EQ(a, b)
    :   Compare timeouts for equality.

        The [k\_timeout\_t](#structk__timeout__t) object is an opaque struct that should not be inspected by application code. This macro exists so that users can test timeout objects for equality with known constants (e.g. K\_NO\_WAIT and K\_FOREVER) when implementing their own APIs in terms of Zephyr timeout constants.

        Returns:
        :   True if the timeout objects are identical

    NSEC\_PER\_USEC
    :   number of nanoseconds per micorsecond

    NSEC\_PER\_MSEC
    :   number of nanoseconds per millisecond

    USEC\_PER\_MSEC
    :   number of microseconds per millisecond

    MSEC\_PER\_SEC
    :   number of milliseconds per second

    SEC\_PER\_MIN
    :   number of seconds per minute

    MIN\_PER\_HOUR
    :   number of minutes per hour

    HOUR\_PER\_DAY
    :   number of hours per day

    USEC\_PER\_SEC
    :   number of microseconds per second

    NSEC\_PER\_SEC
    :   number of nanoseconds per second

    SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG(X, NCYCLES)
    :   SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG converts CPU clock cycles to nanoseconds and calculates the average cycle time.

    Typedefs

    typedef uint32\_t k\_ticks\_t
    :   Tick precision used in timeout APIs.

        This type defines the word size of the timeout values used in [k\_timeout\_t](#structk__timeout__t) objects, and thus defines an upper bound on maximum timeout length (or equivalently minimum tick duration). Note that this does not affect the size of the system uptime counter, which is always a 64 bit count of ticks.

    Functions

    void sys\_clock\_set\_timeout(int32\_t ticks, bool idle)
    :   Set system clock timeout.

        Informs the system clock driver that the next needed call to [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) will not be until the specified number of ticks from the current time have elapsed. Note that spurious calls to [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5)

        are allowed (i.e. it’s legal to announce every tick and implement this function as a noop), the requirement is that one tick announcement should occur within one tick BEFORE the specified expiration (that is, passing ticks==1 means “announce

        the next tick”, this convention was chosen to match legacy usage). Similarly a ticks value of zero (or even negative) is legal and treated identically: it simply indicates the kernel would like the next tick announcement as soon as possible.

        Note that ticks can also be passed the special value K\_TICKS\_FOREVER, indicating that no future timer interrupts are expected or required and that the system is permitted to enter an indefinite sleep even if this could cause rollover of the internal counter (i.e. the system uptime counter is allowed to be wrong

        Note also that it is conventional for the kernel to pass INT\_MAX for ticks if it wants to preserve the uptime tick count but doesn’t have a specific event to await. The intent here is that the driver will schedule any needed timeout as far into the future as possible. For the specific case of INT\_MAX, the next call to [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) may occur at any point in the future, not just at INT\_MAX ticks. But the correspondence between the announced ticks and real-world time must be correct.

        A final note about SMP: note that the call to [sys\_clock\_set\_timeout()](#group__clock__apis_1ga747c1f4a99a3bc48e7ec65d7bc5e4767) is made on any CPU, and reflects the next timeout desired globally. The resulting calls(s) to [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) must be properly serialized by the driver such that a given tick is announced exactly once across the system. The kernel does not (cannot, really) attempt to serialize things by “assigning” timeouts to specific CPUs.

        Parameters:
        :   - **ticks** – Timeout in tick units
            - **idle** – Hint to the driver that the system is about to enter the idle state immediately after setting the timeout

    void sys\_clock\_idle\_exit(void)
    :   Timer idle exit notification.

        This notifies the timer driver that the system is exiting the idle and allows it to do whatever bookkeeping is needed to restore timer operation and compute elapsed ticks.

        Note

        Legacy timer drivers also use this opportunity to call back into [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) to notify the kernel of expired ticks. This is allowed for compatibility, but not recommended. The kernel will figure that out on its own.

    void sys\_clock\_announce(int32\_t ticks)
    :   Announce time progress to the kernel.

        Informs the kernel that the specified number of ticks have elapsed since the last call to [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) (or system startup for the first call). The timer driver is expected to delivery these announcements as close as practical (subject to hardware and latency limitations) to tick boundaries.

        Parameters:
        :   - **ticks** – Elapsed time, in ticks

    uint32\_t sys\_clock\_elapsed(void)
    :   Ticks elapsed since last [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) call.

        Queries the clock driver for the current time elapsed since the last call to [sys\_clock\_announce()](#group__clock__apis_1gaa7d3b1bdb8d15c907aaafea3b96ac2b5) was made. The kernel will call this with appropriate locking, the driver needs only provide an instantaneous answer.

    void sys\_clock\_disable(void)
    :   Disable system timer.

        Note

        Not all system timer drivers has the capability of being disabled. The config  [`CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT`](../../../kconfig.md#CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT "CONFIG_SYSTEM_TIMER_HAS_DISABLE_SUPPORT") can be used to check if the system timer has the capability of being disabled.

    uint32\_t sys\_clock\_cycle\_get\_32(void)
    :   Hardware cycle counter.

        Timer drivers are generally responsible for the system cycle counter as well as the tick announcements. This function is generally called out of the architecture layer (

        See also

        arch\_k\_cycle\_get\_32()) to implement the cycle counter, though the user-facing API is owned by the architecture, not the driver. The rate must match CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC.

        Note

        If the counter clock is large enough for this to wrap its full range within a few seconds (i.e. CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC is greater than 50Mhz) then it is recommended to also implement [sys\_clock\_cycle\_get\_64()](#group__clock__apis_1ga25328a181bd0229ef5110c15e8452fc1).

        Returns:
        :   The current cycle time. This should count up monotonically through the full 32 bit space, wrapping at 0xffffffff. Hardware with fewer bits of precision in the timer is expected to synthesize a 32 bit count.

    uint64\_t sys\_clock\_cycle\_get\_64(void)
    :   64 bit hardware cycle counter

        As for [sys\_clock\_cycle\_get\_32()](#group__clock__apis_1ga42dcd1878309a82246dbfa26510f868a), but with a 64 bit return value. Not all hardware has 64 bit counters. This function need be implemented only if CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER is set.

        Note

        If the counter clock is large enough for [sys\_clock\_cycle\_get\_32()](#group__clock__apis_1ga42dcd1878309a82246dbfa26510f868a) to wrap its full range within a few seconds (i.e. CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC is greater than 50Mhz) then it is recommended to implement this API.

        Returns:
        :   The current cycle time. This should count up monotonically through the full 64 bit space, wrapping at 2^64-1. Hardware with fewer bits of precision in the timer is generally not expected to implement this API.

    int64\_t k\_uptime\_ticks(void)
    :   Get system uptime, in system ticks.

        This routine returns the elapsed time since the system booted, in ticks (c.f.  [`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") ), which is the fundamental unit of resolution of kernel timekeeping.

        Returns:
        :   Current uptime in ticks.

    static inline int64\_t k\_uptime\_get(void)
    :   Get system uptime.

        This routine returns the elapsed time since the system booted, in milliseconds.

        Note

        While this function returns time in milliseconds, it does not mean it has millisecond resolution. The actual resolution depends on  [`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") config option.

        Returns:
        :   Current uptime in milliseconds.

    static inline uint32\_t k\_uptime\_get\_32(void)
    :   Get system uptime (32-bit version).

        This routine returns the lower 32 bits of the system uptime in milliseconds.

        Because correct conversion requires full precision of the system clock there is no benefit to using this over [k\_uptime\_get()](#group__clock__apis_1gae3e992cd3257c23d5b26d765fcbb2b69) unless you know the application will never run long enough for the system clock to approach 2^32 ticks. Calls to this function may involve interrupt blocking and 64-bit math.

        Note

        While this function returns time in milliseconds, it does not mean it has millisecond resolution. The actual resolution depends on  [`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") config option

        Returns:
        :   The low 32 bits of the current uptime, in milliseconds.

    static inline uint32\_t k\_uptime\_seconds(void)
    :   Get system uptime in seconds.

        This routine returns the elapsed time since the system booted, in seconds.

        Returns:
        :   Current uptime in seconds.

    static inline int64\_t k\_uptime\_delta(int64\_t \*reftime)
    :   Get elapsed time.

        This routine computes the elapsed time between the current system uptime and an earlier reference time, in milliseconds.

        Parameters:
        :   - **reftime** – Pointer to a reference time, which is updated to the current uptime upon return.

        Returns:
        :   Elapsed time.

    static inline uint32\_t k\_cycle\_get\_32(void)
    :   Read the hardware clock.

        This routine returns the current time, as measured by the system’s hardware clock.

        Returns:
        :   Current hardware clock up-counter (in cycles).

    static inline uint64\_t k\_cycle\_get\_64(void)
    :   Read the 64-bit hardware clock.

        This routine returns the current time in 64-bits, as measured by the system’s hardware clock, if available.

        See also

        CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER

        Returns:
        :   Current hardware clock up-counter (in cycles).

    uint32\_t sys\_clock\_tick\_get\_32(void)
    :   Return the lower part of the current system tick count.

        Returns:
        :   the current system tick count

    int64\_t sys\_clock\_tick\_get(void)
    :   Return the current system tick count.

        Returns:
        :   the current system tick count

    [k\_timepoint\_t](#c.k_timepoint_t) sys\_timepoint\_calc([k\_timeout\_t](#c.k_timeout_t) timeout)
    :   Calculate a timepoint value.

        Returns a timepoint corresponding to the expiration (relative to an unlocked “now”!) of a timeout object. When used correctly, this should be called once, synchronously with the user passing a new timeout value. It should not be used iteratively to adjust a timeout (see `[sys_timepoint_timeout()](#group__clock__apis_1ga6f6d06ef8c13e2fa54c63831fc00ecaa)` for that purpose).

        See also

        [sys\_timepoint\_timeout()](#group__clock__apis_1ga6f6d06ef8c13e2fa54c63831fc00ecaa)

        See also

        [sys\_timepoint\_expired()](#group__clock__apis_1ga87d0d7a0f7bcdcc8c4909962eac12985)

        Parameters:
        :   - **timeout** – Timeout value relative to current time (may also be `[K_FOREVER](#group__clock__apis_1ga0bb4b83f0222193b21a8910311bab0ca)` or `[K_NO_WAIT](#group__clock__apis_1ga3d9541cfe2e8395af66d186efa77362f)`).

        Return values:
        :   **Timepoint** – value corresponding to given timeout

    [k\_timeout\_t](#c.k_timeout_t) sys\_timepoint\_timeout([k\_timepoint\_t](#c.k_timepoint_t) timepoint)
    :   Remaining time to given timepoint.

        Returns the timeout interval between current time and provided timepoint. If the timepoint is now in the past or if it was created with `[K_NO_WAIT](#group__clock__apis_1ga3d9541cfe2e8395af66d186efa77362f)` then `[K_NO_WAIT](#group__clock__apis_1ga3d9541cfe2e8395af66d186efa77362f)` is returned. If it was created with `[K_FOREVER](#group__clock__apis_1ga0bb4b83f0222193b21a8910311bab0ca)` then `[K_FOREVER](#group__clock__apis_1ga0bb4b83f0222193b21a8910311bab0ca)` is returned.

        See also

        [sys\_timepoint\_calc()](#group__clock__apis_1ga509cf4599c1f162c97540743e8c21d33)

        Parameters:
        :   - **timepoint** – Timepoint for which a timeout value is wanted.

        Return values:
        :   **Corresponding** – timeout value.

    static inline uint64\_t sys\_clock\_timeout\_end\_calc([k\_timeout\_t](#c.k_timeout_t) timeout)
    :   Provided for backward compatibility.

        This is deprecated. Consider `[sys_timepoint_calc()](#group__clock__apis_1ga509cf4599c1f162c97540743e8c21d33)` instead.

        See also

        [sys\_timepoint\_calc()](#group__clock__apis_1ga509cf4599c1f162c97540743e8c21d33)

    static inline int sys\_timepoint\_cmp([k\_timepoint\_t](#c.k_timepoint_t) a, [k\_timepoint\_t](#c.k_timepoint_t) b)
    :   Compare two timepoint values.

        This function is used to compare two timepoint values.

        Parameters:
        :   - **a** – Timepoint to compare
            - **b** – Timepoint to compare against.

        Returns:
        :   zero if both timepoints are the same. Negative value if timepoint *a* is before timepoint *b*, positive otherwise.

    static inline bool sys\_timepoint\_expired([k\_timepoint\_t](#c.k_timepoint_t) timepoint)
    :   Indicates if timepoint is expired.

        See also

        [sys\_timepoint\_calc()](#group__clock__apis_1ga509cf4599c1f162c97540743e8c21d33)

        Parameters:
        :   - **timepoint** – Timepoint to evaluate

        Return values:
        :   **true** – if the timepoint is in the past, false otherwise

    struct k\_timeout\_t
    :   *#include <sys\_clock.h>*

        Kernel timeout type.

        Timeout arguments presented to kernel APIs are stored in this opaque type, which is capable of representing times in various formats and units. It should be constructed from application data using one of the macros defined for this purpose (e.g. `[K_MSEC()](#group__clock__apis_1ga302af954e87b10a9b731f1ad07775e9f)`, `K_TIMEOUT_ABS_TICKS()`, etc…), or be one of the two constants K\_NO\_WAIT or K\_FOREVER. Applications should not inspect the internal data once constructed. Timeout values may be compared for equality with the `[K_TIMEOUT_EQ()](#group__clock__apis_1ga9abf00b34e16ab7ad0883603b6778b1b)` macro.

    struct k\_timepoint\_t
    :   *#include <sys\_clock.h>*

        Kernel timepoint type.

        Absolute timepoints are stored in this opaque type. It is best not to inspect its content directly.

        See also

        [sys\_timepoint\_calc()](#group__clock__apis_1ga509cf4599c1f162c97540743e8c21d33)

        See also

        [sys\_timepoint\_timeout()](#group__clock__apis_1ga6f6d06ef8c13e2fa54c63831fc00ecaa)

        See also

        [sys\_timepoint\_expired()](#group__clock__apis_1ga87d0d7a0f7bcdcc8c4909962eac12985)
