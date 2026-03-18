---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/tracing/index.html
original_path: services/tracing/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Tracing

## Overview

The tracing feature provides hooks that permits you to collect data from
your application and allows tools running on a host to visualize the inner-working of
the kernel and various subsystems.

Every system has application-specific events to trace out. Historically,
that has implied:

1. Determining the application-specific payload,
2. Choosing suitable serialization-format,
3. Writing the on-target serialization code,
4. Deciding on and writing the I/O transport mechanics,
5. Writing the PC-side deserializer/parser,
6. Writing custom ad-hoc tools for filtering and presentation.

An application can use one of the existing formats or define a custom format by
overriding the macros declared in [include/zephyr/tracing/tracing.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/tracing/tracing.h).

Different formats, transports and host tools are available and supported in
Zephyr.

In fact, I/O varies greatly from system to system. Therefore, it is
instructive to create a taxonomy for I/O types when we must ensure the
interface between payload/format (Top Layer) and the transport mechanics
(bottom Layer) is generic and efficient enough to model these. See the
*I/O taxonomy* section below.

## Serialization Formats

### Common Trace Format (CTF) Support

Common Trace Format, CTF, is an open format and language to describe trace
formats. This enables tool reuse, of which line-textual (babeltrace) and
graphical (TraceCompass) variants already exist.

CTF should look familiar to C programmers but adds stronger typing.
See [CTF - A Flexible, High-performance Binary Trace Format](http://diamon.org/ctf/).

CTF allows us to formally describe application specific payload and the
serialization format, which enables common infrastructure for host tools
and parsers and tools for filtering and presentation.

#### A Generic Interface

In CTF, an event is serialized to a packet containing one or more fields.
As seen from *I/O taxonomy* section below, a bottom layer may:

- perform actions at transaction-start (e.g. mutex-lock),
- process each field in some way (e.g. sync-push emit, concat, enqueue to
  thread-bound FIFO),
- perform actions at transaction-stop (e.g. mutex-release, emit of concat
  buffer).

#### CTF Top-Layer Example

The CTF\_EVENT macro will serialize each argument to a field:

```text
/* Example for illustration */
static inline void ctf_top_foo(uint32_t thread_id, ctf_bounded_string_t name)
{
  CTF_EVENT(
    CTF_LITERAL(uint8_t, 42),
    thread_id,
    name,
    "hello, I was emitted from function: ",
    __func__  /* __func__ is standard since C99 */
  );
}
```

How to serialize and emit fields as well as handling alignment, can be done
internally and statically at compile-time in the bottom-layer.

The CTF top layer is enabled using the configuration option
[`CONFIG_TRACING_CTF`](../../kconfig.md#CONFIG_TRACING_CTF "CONFIG_TRACING_CTF") and can be used with the different transport
backends both in synchronous and asynchronous modes.

### SEGGER SystemView Support

Zephyr provides built-in support for [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) that can be enabled in
any application for platforms that have the required hardware support.

The payload and format used with SystemView is custom to the application and
relies on RTT as a transport. Newer versions of SystemView support other
transports, for example UART or using snapshot mode (both still not
supported in Zephyr).

To enable tracing support with [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) add the configuration option
[`CONFIG_SEGGER_SYSTEMVIEW`](../../kconfig.md#CONFIG_SEGGER_SYSTEMVIEW "CONFIG_SEGGER_SYSTEMVIEW") to your project configuration file and set
it to *y*. For example, this can be added to the
[Basic Synchronization](../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample to visualize fast switching between threads.
SystemView can also be used for post-mortem tracing, which can be enabled with
CONFIG\_SEGGER\_SYSVIEW\_POST\_MORTEM\_MODE. In this mode, a debugger can
be attached after the system has crashed using `west attach` after which the
latest data from the internal RAM buffer can be loaded into SystemView:

```text
CONFIG_STDOUT_CONSOLE=y
# enable to use thread names
CONFIG_THREAD_NAME=y
CONFIG_SEGGER_SYSTEMVIEW=y
CONFIG_USE_SEGGER_RTT=y
CONFIG_TRACING=y
# enable for post-mortem tracing
CONFIG_SEGGER_SYSVIEW_POST_MORTEM_MODE=n
```

[![SEGGER SystemView](../../_images/segger_systemview.png)](../../_images/segger_systemview.png)

Recent versions of [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) come with an API translation table for
Zephyr which is incomplete and does not match the current level of support
available in Zephyr. To use the latest Zephyr API description table, copy the
file available in the tree to your local configuration directory to override the
builtin table:

```text
# On Linux and MacOS
cp $ZEPHYR_BASE/subsys/tracing/sysview/SYSVIEW_Zephyr.txt ~/.config/SEGGER/
```

### User-Defined Tracing

This tracing format allows the user to define functions to perform any work desired
when a task is switched in or out, when an interrupt is entered or exited, and when the cpu
is idle.

Examples include:
- simple toggling of GPIO for external scope tracing while minimizing extra cpu load
- generating/outputting trace data in a non-standard or proprietary format that can
not be supported by the other tracing systems

The following functions can be defined by the user:

```c
void sys_trace_thread_create_user(struct k_thread *thread);
void sys_trace_thread_abort_user(struct k_thread *thread);
void sys_trace_thread_suspend_user(struct k_thread *thread);
void sys_trace_thread_resume_user(struct k_thread *thread);
void sys_trace_thread_name_set_user(struct k_thread *thread);
void sys_trace_thread_switched_in_user(struct k_thread *thread);
void sys_trace_thread_switched_out_user(struct k_thread *thread);
void sys_trace_thread_info_user(struct k_thread *thread);
void sys_trace_thread_sched_ready_user(struct k_thread *thread);
void sys_trace_thread_pend_user(struct k_thread *thread);
void sys_trace_thread_priority_set_user(struct k_thread *thread, int prio);
void sys_trace_isr_enter_user(int nested_interrupts);
void sys_trace_isr_exit_user(int nested_interrupts);
void sys_trace_idle_user();
```

Enable this format with the [`CONFIG_TRACING_USER`](../../kconfig.md#CONFIG_TRACING_USER "CONFIG_TRACING_USER") option.

## Transport Backends

The following backends are currently supported:

- UART
- USB
- File (Using the native port with POSIX architecture based targets)
- RTT (With SystemView)
- RAM (buffer to be retrieved by a debugger)

## Using Tracing

The sample [samples/subsys/tracing](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/tracing) demonstrates tracing with
different formats and backends.

To get started, the simplest way is to use the CTF format with the [native\_sim](../../boards/posix/native_sim/doc/index.md#native-sim)
port, build the sample as follows:

Using west:

```shell
west build -b native_sim samples/subsys/tracing -- -DCONF_FILE=prj_native_ctf.conf
```

Using CMake and ninja:

```shell
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=native_sim -DCONF_FILE=prj_native_ctf.conf samples/subsys/tracing

# Now run the build tool on the generated build system:
ninja -Cbuild
```

You can then run the resulting binary with the option `-trace-file` to generate
the tracing data:

```text
mkdir data
cp $ZEPHYR_BASE/subsys/tracing/ctf/tsdl/metadata data/
./build/zephyr/zephyr.exe -trace-file=data/channel0_0
```

The resulting CTF output can be visualized using babeltrace or TraceCompass
by pointing the tool to the `data` directory with the metadata and trace files.

### Using RAM backend

For devices that do not have available I/O for tracing such as USB or UART but have
enough RAM to collect trace data, the ram backend can be enabled with configuration
[`CONFIG_TRACING_BACKEND_RAM`](../../kconfig.md#CONFIG_TRACING_BACKEND_RAM "CONFIG_TRACING_BACKEND_RAM").
Adjust [`CONFIG_RAM_TRACING_BUFFER_SIZE`](../../kconfig.md#CONFIG_RAM_TRACING_BUFFER_SIZE "CONFIG_RAM_TRACING_BUFFER_SIZE") to be able to record enough traces for your needs.
Then thanks to a runtime debugger such as gdb this buffer can be fetched from the target
to an host computer:

```text
(gdb) dump binary memory data/channel0_0 <ram_tracing_start> <ram_tracing_end>
```

The resulting channel0\_0 file have to be placed in a directory with the `metadata`
file like the other backend.

## Visualisation Tools

### TraceCompass

TraceCompass is an open source tool that visualizes CTF events such as thread
scheduling and interrupts, and is helpful to find unintended interactions and
resource conflicts on complex systems.

See also the presentation by Ericsson,
[Advanced Trouble-shooting Of Real-time Systems](https://wiki.eclipse.org/images/0/0e/TechTalkOnlineDemoFeb2017_v1.pdf).

## Future LTTng Inspiration

Currently, the top-layer provided here is quite simple and bare-bones,
and needlessly copied from Zephyr’s Segger SystemView debug module.

For an OS like Zephyr, it would make sense to draw inspiration from
Linux’s LTTng and change the top-layer to serialize to the same format.
Doing this would enable direct reuse of TraceCompass’ canned analyses
for Linux. Alternatively, LTTng-analyses in TraceCompass could be
customized to Zephyr. It is ongoing work to enable TraceCompass
visibility of Zephyr in a target-agnostic and open source way.

### I/O Taxonomy

- Atomic Push/Produce/Write/Enqueue:

  - synchronous:
    :   means data-transmission has completed with the return of the
        call.
  - asynchronous:
    :   means data-transmission is pending or ongoing with the return
        of the call. Usually, interrupts/callbacks/signals or polling
        is used to determine completion.
  - buffered:
    :   means data-transmissions are copied and grouped together to
        form a larger ones. Usually for amortizing overhead (burst
        dequeue) or jitter-mitigation (steady dequeue).

  Examples:
  :   - sync unbuffered
        :   E.g. PIO via GPIOs having steady stream, no extra FIFO memory needed.
            Low jitter but may be less efficient (can’t amortize the overhead of
            writing).
      - sync buffered
        :   E.g. `fwrite()` or enqueuing into FIFO.
            Blockingly burst the FIFO when its buffer-waterlevel exceeds threshold.
            Jitter due to bursts may lead to missed deadlines.
      - async unbuffered
        :   E.g. DMA, or zero-copying in shared memory.
            Be careful of data hazards, race conditions, etc!
      - async buffered
        :   E.g. enqueuing into FIFO.
- Atomic Pull/Consume/Read/Dequeue:

  - synchronous:
    :   means data-reception has completed with the return of the call.
  - asynchronous:
    :   means data-reception is pending or ongoing with the return of
        the call. Usually, interrupts/callbacks/signals or polling is
        used to determine completion.
  - buffered:
    :   means data is copied-in in larger chunks than request-size.
        Usually for amortizing wait-time.

  Examples:
  :   - sync unbuffered
        :   E.g. Blocking read-call, `fread()` or SPI-read, zero-copying in shared
            memory.
      - sync buffered
        :   E.g. Blocking read-call with caching applied.
            Makes sense if read pattern exhibits spatial locality.
      - async unbuffered
        :   E.g. zero-copying in shared memory.
            Be careful of data hazards, race conditions, etc!
      - async buffered
        :   E.g. `aio_read()` or DMA.

Unfortunately, I/O may not be atomic and may, therefore, require locking.
Locking may not be needed if multiple independent channels are available.

> - The system has non-atomic write and one shared channel
>   :   E.g. UART. Locking required.
>
>       `lock(); emit(a); emit(b); emit(c); release();`
> - The system has non-atomic write but many channels
>   :   E.g. Multi-UART. Lock-free if the bottom-layer maps each Zephyr
>       thread+ISR to its own channel, thus alleviating races as each
>       thread is sequentially consistent with itself.
>
>       `emit(a,thread_id); emit(b,thread_id); emit(c,thread_id);`
> - The system has atomic write but one shared channel
>   :   E.g. `native_sim` or board with DMA. May or may not need locking.
>
>       `emit(a ## b ## c); /* Concat to buffer */`
>
>       `lock(); emit(a); emit(b); emit(c); release(); /* No extra mem */`
> - The system has atomic write and many channels
>   :   E.g. native\_sim or board with multi-channel DMA. Lock-free.
>
>       `emit(a ## b ## c, thread_id);`

## Object tracking

The kernel can also maintain lists of objects that can be used to track
their usage. Currently, the following lists can be enabled:

```text
struct k_timer *_track_list_k_timer;
struct k_mem_slab *_track_list_k_mem_slab;
struct k_sem *_track_list_k_sem;
struct k_mutex *_track_list_k_mutex;
struct k_stack *_track_list_k_stack;
struct k_msgq *_track_list_k_msgq;
struct k_mbox *_track_list_k_mbox;
struct k_pipe *_track_list_k_pipe;
struct k_queue *_track_list_k_queue;
struct k_event *_track_list_k_event;
```

Those global variables are the head of each list - they can be traversed
with the help of macro `SYS_PORT_TRACK_NEXT`. For instance, to traverse
all initialized mutexes, one can write:

```text
struct k_mutex *cur = _track_list_k_mutex;
while (cur != NULL) {
  /* Do something */

  cur = SYS_PORT_TRACK_NEXT(cur);
}
```

To enable object tracking, enable [`CONFIG_TRACING_OBJECT_TRACKING`](../../kconfig.md#CONFIG_TRACING_OBJECT_TRACKING "CONFIG_TRACING_OBJECT_TRACKING").
Note that each list can be enabled or disabled via their tracing
configuration. For example, to disable tracking of semaphores, one can
disable [`CONFIG_TRACING_SEMAPHORE`](../../kconfig.md#CONFIG_TRACING_SEMAPHORE "CONFIG_TRACING_SEMAPHORE").

Object tracking is behind tracing configuration as it currently leverages
tracing infrastructure to perform the tracking.

## API

### Common

*group* subsys\_tracing\_apis
:   Tracing APIs.

    Functions

    void sys\_trace\_isr\_enter(void)
    :   Called when entering an ISR.

    void sys\_trace\_isr\_exit(void)
    :   Called when exiting an ISR.

    void sys\_trace\_isr\_exit\_to\_scheduler(void)
    :   Called when exiting an ISR and switching to scheduler.

    void sys\_trace\_idle(void)
    :   Called when the cpu enters the idle state.

### Threads

*group* subsys\_tracing\_apis\_thread
:   Thread Tracing APIs.

    Defines

    sys\_port\_trace\_k\_thread\_foreach\_enter()
    :   Called when entering a k\_thread\_foreach call.

    sys\_port\_trace\_k\_thread\_foreach\_exit()
    :   Called when exiting a k\_thread\_foreach call.

    sys\_port\_trace\_k\_thread\_foreach\_unlocked\_enter()
    :   Called when entering a k\_thread\_foreach\_unlocked.

    sys\_port\_trace\_k\_thread\_foreach\_unlocked\_exit()
    :   Called when exiting a k\_thread\_foreach\_unlocked.

    sys\_port\_trace\_k\_thread\_create(new\_thread)
    :   Trace creating a Thread.

        Parameters:
        :   - **new\_thread** – Thread object

    sys\_port\_trace\_k\_thread\_user\_mode\_enter()
    :   Trace Thread entering user mode.

    sys\_port\_trace\_k\_thread\_join\_enter(thread, timeout)
    :   Called when entering a k\_thread\_join.

        Parameters:
        :   - **thread** – Thread object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_thread\_join\_blocking(thread, timeout)
    :   Called when k\_thread\_join blocks.

        Parameters:
        :   - **thread** – Thread object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_thread\_join\_exit(thread, timeout, ret)
    :   Called when exiting k\_thread\_join.

        Parameters:
        :   - **thread** – Thread object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_thread\_sleep\_enter(timeout)
    :   Called when entering k\_thread\_sleep.

        Parameters:
        :   - **timeout** – Timeout period

    sys\_port\_trace\_k\_thread\_sleep\_exit(timeout, ret)
    :   Called when exiting k\_thread\_sleep.

        Parameters:
        :   - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_thread\_msleep\_enter(ms)
    :   Called when entering k\_thread\_msleep.

        Parameters:
        :   - **ms** – Duration in milliseconds

    sys\_port\_trace\_k\_thread\_msleep\_exit(ms, ret)
    :   Called when exiting k\_thread\_msleep.

        Parameters:
        :   - **ms** – Duration in milliseconds
            - **ret** – Return value

    sys\_port\_trace\_k\_thread\_usleep\_enter(us)
    :   Called when entering k\_thread\_usleep.

        Parameters:
        :   - **us** – Duration in microseconds

    sys\_port\_trace\_k\_thread\_usleep\_exit(us, ret)
    :   Called when exiting k\_thread\_usleep.

        Parameters:
        :   - **us** – Duration in microseconds
            - **ret** – Return value

    sys\_port\_trace\_k\_thread\_busy\_wait\_enter(usec\_to\_wait)
    :   Called when entering k\_thread\_busy\_wait.

        Parameters:
        :   - **usec\_to\_wait** – Duration in microseconds

    sys\_port\_trace\_k\_thread\_busy\_wait\_exit(usec\_to\_wait)
    :   Called when exiting k\_thread\_busy\_wait.

        Parameters:
        :   - **usec\_to\_wait** – Duration in microseconds

    sys\_port\_trace\_k\_thread\_yield()
    :   Called when a thread yields.

    sys\_port\_trace\_k\_thread\_wakeup(thread)
    :   Called when a thread wakes up.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_start(thread)
    :   Called when a thread is started.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_abort(thread)
    :   Called when a thread is being aborted.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_abort\_enter(thread)
    :   Called when a thread enters the k\_thread\_abort routine.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_abort\_exit(thread)
    :   Called when a thread exits the k\_thread\_abort routine.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_priority\_set(thread)
    :   Called when setting priority of a thread.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_suspend\_enter(thread)
    :   Called when a thread enters the k\_thread\_suspend function.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_suspend\_exit(thread)
    :   Called when a thread exits the k\_thread\_suspend function.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_resume\_enter(thread)
    :   Called when a thread enters the resume from suspension function.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_resume\_exit(thread)
    :   Called when a thread exits the resumed from suspension function.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_lock()
    :   Called when the thread scheduler is locked.

    sys\_port\_trace\_k\_thread\_sched\_unlock()
    :   Called when the thread scheduler is unlocked.

    sys\_port\_trace\_k\_thread\_name\_set(thread, ret)
    :   Called when a thread name is set.

        Parameters:
        :   - **thread** – Thread object
            - **ret** – Return value

    sys\_port\_trace\_k\_thread\_switched\_out()
    :   Called before a thread has been selected to run.

    sys\_port\_trace\_k\_thread\_switched\_in()
    :   Called after a thread has been selected to run.

    sys\_port\_trace\_k\_thread\_ready(thread)
    :   Called when a thread is ready to run.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_pend(thread)
    :   Called when a thread is pending.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_info(thread)
    :   Provide information about specific thread.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_wakeup(thread)
    :   Trace implicit thread wakeup invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_abort(thread)
    :   Trace implicit thread abort invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_priority\_set(thread, prio)
    :   Trace implicit thread set priority invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object
            - **prio** – Thread priority

    sys\_port\_trace\_k\_thread\_sched\_ready(thread)
    :   Trace implicit thread ready invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_pend(thread)
    :   Trace implicit thread pend invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_resume(thread)
    :   Trace implicit thread resume invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object

    sys\_port\_trace\_k\_thread\_sched\_suspend(thread)
    :   Trace implicit thread suspend invocation by the scheduler.

        Parameters:
        :   - **thread** – Thread object

### Work Queues

*group* subsys\_tracing\_apis\_work
:   Work Tracing APIs.

    Defines

    sys\_port\_trace\_k\_work\_init(work)
    :   Trace initialisation of a Work structure.

        Parameters:
        :   - **work** – Work structure

    sys\_port\_trace\_k\_work\_submit\_to\_queue\_enter(queue, work)
    :   Trace submit work to work queue call entry.

        Parameters:
        :   - **queue** – Work queue structure
            - **work** – Work structure

    sys\_port\_trace\_k\_work\_submit\_to\_queue\_exit(queue, work, ret)
    :   Trace submit work to work queue call exit.

        Parameters:
        :   - **queue** – Work queue structure
            - **work** – Work structure
            - **ret** – Return value

    sys\_port\_trace\_k\_work\_submit\_enter(work)
    :   Trace submit work to system work queue call entry.

        Parameters:
        :   - **work** – Work structure

    sys\_port\_trace\_k\_work\_submit\_exit(work, ret)
    :   Trace submit work to system work queue call exit.

        Parameters:
        :   - **work** – Work structure
            - **ret** – Return value

    sys\_port\_trace\_k\_work\_flush\_enter(work)
    :   Trace flush work call entry.

        Parameters:
        :   - **work** – Work structure

    sys\_port\_trace\_k\_work\_flush\_blocking(work, timeout)
    :   Trace flush work call blocking.

        Parameters:
        :   - **work** – Work structure
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_work\_flush\_exit(work, ret)
    :   Trace flush work call exit.

        Parameters:
        :   - **work** – Work structure
            - **ret** – Return value

    sys\_port\_trace\_k\_work\_cancel\_enter(work)
    :   Trace cancel work call entry.

        Parameters:
        :   - **work** – Work structure

    sys\_port\_trace\_k\_work\_cancel\_exit(work, ret)
    :   Trace cancel work call exit.

        Parameters:
        :   - **work** – Work structure
            - **ret** – Return value

    sys\_port\_trace\_k\_work\_cancel\_sync\_enter(work, sync)
    :   Trace cancel sync work call entry.

        Parameters:
        :   - **work** – Work structure
            - **sync** – Sync object

    sys\_port\_trace\_k\_work\_cancel\_sync\_blocking(work, sync)
    :   Trace cancel sync work call blocking.

        Parameters:
        :   - **work** – Work structure
            - **sync** – Sync object

    sys\_port\_trace\_k\_work\_cancel\_sync\_exit(work, sync, ret)
    :   Trace cancel sync work call exit.

        Parameters:
        :   - **work** – Work structure
            - **sync** – Sync object
            - **ret** – Return value

### Poll

*group* subsys\_tracing\_apis\_poll
:   Poll Tracing APIs.

    Defines

    sys\_port\_trace\_k\_poll\_api\_event\_init(event)
    :   Trace initialisation of a Poll Event.

        Parameters:
        :   - **event** – Poll Event

    sys\_port\_trace\_k\_poll\_api\_poll\_enter(events)
    :   Trace Polling call start.

        Parameters:
        :   - **events** – Poll Events

    sys\_port\_trace\_k\_poll\_api\_poll\_exit(events, ret)
    :   Trace Polling call outcome.

        Parameters:
        :   - **events** – Poll Events
            - **ret** – Return value

    sys\_port\_trace\_k\_poll\_api\_signal\_init(signal)
    :   Trace initialisation of a Poll Signal.

        Parameters:
        :   - **signal** – Poll Signal

    sys\_port\_trace\_k\_poll\_api\_signal\_reset(signal)
    :   Trace resetting of Poll Signal.

        Parameters:
        :   - **signal** – Poll Signal

    sys\_port\_trace\_k\_poll\_api\_signal\_check(signal)
    :   Trace checking of Poll Signal.

        Parameters:
        :   - **signal** – Poll Signal

    sys\_port\_trace\_k\_poll\_api\_signal\_raise(signal, ret)
    :   Trace raising of Poll Signal.

        Parameters:
        :   - **signal** – Poll Signal
            - **ret** – Return value

### Semaphore

*group* subsys\_tracing\_apis\_sem
:   Semaphore Tracing APIs.

    Defines

    sys\_port\_trace\_k\_sem\_init(sem, ret)
    :   Trace initialisation of a Semaphore.

        Parameters:
        :   - **sem** – Semaphore object
            - **ret** – Return value

    sys\_port\_trace\_k\_sem\_give\_enter(sem)
    :   Trace giving a Semaphore entry.

        Parameters:
        :   - **sem** – Semaphore object

    sys\_port\_trace\_k\_sem\_give\_exit(sem)
    :   Trace giving a Semaphore exit.

        Parameters:
        :   - **sem** – Semaphore object

    sys\_port\_trace\_k\_sem\_take\_enter(sem, timeout)
    :   Trace taking a Semaphore attempt start.

        Parameters:
        :   - **sem** – Semaphore object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_sem\_take\_blocking(sem, timeout)
    :   Trace taking a Semaphore attempt blocking.

        Parameters:
        :   - **sem** – Semaphore object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_sem\_take\_exit(sem, timeout, ret)
    :   Trace taking a Semaphore attempt outcome.

        Parameters:
        :   - **sem** – Semaphore object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_sem\_reset(sem)
    :   Trace resetting a Semaphore.

        Parameters:
        :   - **sem** – Semaphore object

### Mutex

*group* subsys\_tracing\_apis\_mutex
:   Mutex Tracing APIs.

    Defines

    sys\_port\_trace\_k\_mutex\_init(mutex, ret)
    :   Trace initialization of Mutex.

        Parameters:
        :   - **mutex** – Mutex object
            - **ret** – Return value

    sys\_port\_trace\_k\_mutex\_lock\_enter(mutex, timeout)
    :   Trace Mutex lock attempt start.

        Parameters:
        :   - **mutex** – Mutex object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mutex\_lock\_blocking(mutex, timeout)
    :   Trace Mutex lock attempt blocking.

        Parameters:
        :   - **mutex** – Mutex object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mutex\_lock\_exit(mutex, timeout, ret)
    :   Trace Mutex lock attempt outcome.

        Parameters:
        :   - **mutex** – Mutex object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_mutex\_unlock\_enter(mutex)
    :   Trace Mutex unlock entry.

        Parameters:
        :   - **mutex** – Mutex object

    sys\_port\_trace\_k\_mutex\_unlock\_exit(mutex, ret)
    :   Trace Mutex unlock exit.

### Condition Variables

*group* subsys\_tracing\_apis\_condvar
:   Conditional Variable Tracing APIs.

    Defines

    sys\_port\_trace\_k\_condvar\_init(condvar, ret)
    :   Trace initialization of Conditional Variable.

        Parameters:
        :   - **condvar** – Conditional Variable object
            - **ret** – Return value

    sys\_port\_trace\_k\_condvar\_signal\_enter(condvar)
    :   Trace Conditional Variable signaling start.

        Parameters:
        :   - **condvar** – Conditional Variable object

    sys\_port\_trace\_k\_condvar\_signal\_blocking(condvar, timeout)
    :   Trace Conditional Variable signaling blocking.

        Parameters:
        :   - **condvar** – Conditional Variable object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_condvar\_signal\_exit(condvar, ret)
    :   Trace Conditional Variable signaling outcome.

        Parameters:
        :   - **condvar** – Conditional Variable object
            - **ret** – Return value

    sys\_port\_trace\_k\_condvar\_broadcast\_enter(condvar)
    :   Trace Conditional Variable broadcast enter.

        Parameters:
        :   - **condvar** – Conditional Variable object

    sys\_port\_trace\_k\_condvar\_broadcast\_exit(condvar, ret)
    :   Trace Conditional Variable broadcast exit.

        Parameters:
        :   - **condvar** – Conditional Variable object
            - **ret** – Return value

    sys\_port\_trace\_k\_condvar\_wait\_enter(condvar)
    :   Trace Conditional Variable wait enter.

        Parameters:
        :   - **condvar** – Conditional Variable object

    sys\_port\_trace\_k\_condvar\_wait\_exit(condvar, ret)
    :   Trace Conditional Variable wait exit.

        Parameters:
        :   - **condvar** – Conditional Variable object
            - **ret** – Return value

### Queues

*group* subsys\_tracing\_apis\_queue
:   Queue Tracing APIs.

    Defines

    sys\_port\_trace\_k\_queue\_init(queue)
    :   Trace initialization of Queue.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_cancel\_wait(queue)
    :   Trace Queue cancel wait.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_queue\_insert\_enter(queue, alloc)
    :   Trace Queue insert attempt entry.

        Parameters:
        :   - **queue** – Queue object
            - **alloc** – Allocation flag

    sys\_port\_trace\_k\_queue\_queue\_insert\_blocking(queue, alloc, timeout)
    :   Trace Queue insert attempt blocking.

        Parameters:
        :   - **queue** – Queue object
            - **alloc** – Allocation flag
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_queue\_queue\_insert\_exit(queue, alloc, ret)
    :   Trace Queue insert attempt outcome.

        Parameters:
        :   - **queue** – Queue object
            - **alloc** – Allocation flag
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_append\_enter(queue)
    :   Trace Queue append enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_append\_exit(queue)
    :   Trace Queue append exit.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_alloc\_append\_enter(queue)
    :   Trace Queue alloc append enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_alloc\_append\_exit(queue, ret)
    :   Trace Queue alloc append exit.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_prepend\_enter(queue)
    :   Trace Queue prepend enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_prepend\_exit(queue)
    :   Trace Queue prepend exit.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_alloc\_prepend\_enter(queue)
    :   Trace Queue alloc prepend enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_alloc\_prepend\_exit(queue, ret)
    :   Trace Queue alloc prepend exit.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_insert\_enter(queue)
    :   Trace Queue insert attempt entry.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_insert\_blocking(queue, timeout)
    :   Trace Queue insert attempt blocking.

        Parameters:
        :   - **queue** – Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_queue\_insert\_exit(queue)
    :   Trace Queue insert attempt exit.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_append\_list\_enter(queue)
    :   Trace Queue append list enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_append\_list\_exit(queue, ret)
    :   Trace Queue append list exit.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_merge\_slist\_enter(queue)
    :   Trace Queue merge slist enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_merge\_slist\_exit(queue, ret)
    :   Trace Queue merge slist exit.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_get\_enter(queue, timeout)
    :   Trace Queue get attempt enter.

        Parameters:
        :   - **queue** – Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_queue\_get\_blocking(queue, timeout)
    :   Trace Queue get attempt blockings.

        Parameters:
        :   - **queue** – Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_queue\_get\_exit(queue, timeout, ret)
    :   Trace Queue get attempt outcome.

        Parameters:
        :   - **queue** – Queue object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_remove\_enter(queue)
    :   Trace Queue remove enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_remove\_exit(queue, ret)
    :   Trace Queue remove exit.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_unique\_append\_enter(queue)
    :   Trace Queue unique append enter.

        Parameters:
        :   - **queue** – Queue object

    sys\_port\_trace\_k\_queue\_unique\_append\_exit(queue, ret)
    :   Trace Queue unique append exit.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_peek\_head(queue, ret)
    :   Trace Queue peek head.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_queue\_peek\_tail(queue, ret)
    :   Trace Queue peek tail.

        Parameters:
        :   - **queue** – Queue object
            - **ret** – Return value

### FIFO

*group* subsys\_tracing\_apis\_fifo
:   FIFO Tracing APIs.

    Defines

    sys\_port\_trace\_k\_fifo\_init\_enter(fifo)
    :   Trace initialization of FIFO Queue entry.

        Parameters:
        :   - **fifo** – FIFO object

    sys\_port\_trace\_k\_fifo\_init\_exit(fifo)
    :   Trace initialization of FIFO Queue exit.

        Parameters:
        :   - **fifo** – FIFO object

    sys\_port\_trace\_k\_fifo\_cancel\_wait\_enter(fifo)
    :   Trace FIFO Queue cancel wait entry.

        Parameters:
        :   - **fifo** – FIFO object

    sys\_port\_trace\_k\_fifo\_cancel\_wait\_exit(fifo)
    :   Trace FIFO Queue cancel wait exit.

        Parameters:
        :   - **fifo** – FIFO object

    sys\_port\_trace\_k\_fifo\_put\_enter(fifo, data)
    :   Trace FIFO Queue put entry.

        Parameters:
        :   - **fifo** – FIFO object
            - **data** – Data item

    sys\_port\_trace\_k\_fifo\_put\_exit(fifo, data)
    :   Trace FIFO Queue put exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **data** – Data item

    sys\_port\_trace\_k\_fifo\_alloc\_put\_enter(fifo, data)
    :   Trace FIFO Queue alloc put entry.

        Parameters:
        :   - **fifo** – FIFO object
            - **data** – Data item

    sys\_port\_trace\_k\_fifo\_alloc\_put\_exit(fifo, data, ret)
    :   Trace FIFO Queue alloc put exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **data** – Data item
            - **ret** – Return value

    sys\_port\_trace\_k\_fifo\_put\_list\_enter(fifo, head, tail)
    :   Trace FIFO Queue put list entry.

        Parameters:
        :   - **fifo** – FIFO object
            - **head** – First ll-node
            - **tail** – Last ll-node

    sys\_port\_trace\_k\_fifo\_put\_list\_exit(fifo, head, tail)
    :   Trace FIFO Queue put list exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **head** – First ll-node
            - **tail** – Last ll-node

    sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_enter(fifo, list)
    :   Trace FIFO Queue put slist entry.

        Parameters:
        :   - **fifo** – FIFO object
            - **list** – Syslist object

    sys\_port\_trace\_k\_fifo\_alloc\_put\_slist\_exit(fifo, list)
    :   Trace FIFO Queue put slist exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **list** – Syslist object

    sys\_port\_trace\_k\_fifo\_get\_enter(fifo, timeout)
    :   Trace FIFO Queue get entry.

        Parameters:
        :   - **fifo** – FIFO object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_fifo\_get\_exit(fifo, timeout, ret)
    :   Trace FIFO Queue get exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_fifo\_peek\_head\_enter(fifo)
    :   Trace FIFO Queue peek head entry.

        Parameters:
        :   - **fifo** – FIFO object

    sys\_port\_trace\_k\_fifo\_peek\_head\_exit(fifo, ret)
    :   Trace FIFO Queue peek head exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **ret** – Return value

    sys\_port\_trace\_k\_fifo\_peek\_tail\_enter(fifo)
    :   Trace FIFO Queue peek tail entry.

        Parameters:
        :   - **fifo** – FIFO object

    sys\_port\_trace\_k\_fifo\_peek\_tail\_exit(fifo, ret)
    :   Trace FIFO Queue peek tail exit.

        Parameters:
        :   - **fifo** – FIFO object
            - **ret** – Return value

### LIFO

*group* subsys\_tracing\_apis\_lifo
:   LIFO Tracing APIs.

    Defines

    sys\_port\_trace\_k\_lifo\_init\_enter(lifo)
    :   Trace initialization of LIFO Queue entry.

        Parameters:
        :   - **lifo** – LIFO object

    sys\_port\_trace\_k\_lifo\_init\_exit(lifo)
    :   Trace initialization of LIFO Queue exit.

        Parameters:
        :   - **lifo** – LIFO object

    sys\_port\_trace\_k\_lifo\_put\_enter(lifo, data)
    :   Trace LIFO Queue put entry.

        Parameters:
        :   - **lifo** – LIFO object
            - **data** – Data item

    sys\_port\_trace\_k\_lifo\_put\_exit(lifo, data)
    :   Trace LIFO Queue put exit.

        Parameters:
        :   - **lifo** – LIFO object
            - **data** – Data item

    sys\_port\_trace\_k\_lifo\_alloc\_put\_enter(lifo, data)
    :   Trace LIFO Queue alloc put entry.

        Parameters:
        :   - **lifo** – LIFO object
            - **data** – Data item

    sys\_port\_trace\_k\_lifo\_alloc\_put\_exit(lifo, data, ret)
    :   Trace LIFO Queue alloc put exit.

        Parameters:
        :   - **lifo** – LIFO object
            - **data** – Data item
            - **ret** – Return value

    sys\_port\_trace\_k\_lifo\_get\_enter(lifo, timeout)
    :   Trace LIFO Queue get entry.

        Parameters:
        :   - **lifo** – LIFO object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_lifo\_get\_exit(lifo, timeout, ret)
    :   Trace LIFO Queue get exit.

        Parameters:
        :   - **lifo** – LIFO object
            - **timeout** – Timeout period
            - **ret** – Return value

### Stacks

*group* subsys\_tracing\_apis\_stack
:   Stack Tracing APIs.

    Defines

    sys\_port\_trace\_k\_stack\_init(stack)
    :   Trace initialization of Stack.

        Parameters:
        :   - **stack** – Stack object

    sys\_port\_trace\_k\_stack\_alloc\_init\_enter(stack)
    :   Trace Stack alloc init attempt entry.

        Parameters:
        :   - **stack** – Stack object

    sys\_port\_trace\_k\_stack\_alloc\_init\_exit(stack, ret)
    :   Trace Stack alloc init outcome.

        Parameters:
        :   - **stack** – Stack object
            - **ret** – Return value

    sys\_port\_trace\_k\_stack\_cleanup\_enter(stack)
    :   Trace Stack cleanup attempt entry.

        Parameters:
        :   - **stack** – Stack object

    sys\_port\_trace\_k\_stack\_cleanup\_exit(stack, ret)
    :   Trace Stack cleanup outcome.

        Parameters:
        :   - **stack** – Stack object
            - **ret** – Return value

    sys\_port\_trace\_k\_stack\_push\_enter(stack)
    :   Trace Stack push attempt entry.

        Parameters:
        :   - **stack** – Stack object

    sys\_port\_trace\_k\_stack\_push\_exit(stack, ret)
    :   Trace Stack push attempt outcome.

        Parameters:
        :   - **stack** – Stack object
            - **ret** – Return value

    sys\_port\_trace\_k\_stack\_pop\_enter(stack, timeout)
    :   Trace Stack pop attempt entry.

        Parameters:
        :   - **stack** – Stack object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_stack\_pop\_blocking(stack, timeout)
    :   Trace Stack pop attempt blocking.

        Parameters:
        :   - **stack** – Stack object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_stack\_pop\_exit(stack, timeout, ret)
    :   Trace Stack pop attempt outcome.

        Parameters:
        :   - **stack** – Stack object
            - **timeout** – Timeout period
            - **ret** – Return value

### Message Queues

*group* subsys\_tracing\_apis\_msgq
:   Message Queue Tracing APIs.

    Defines

    sys\_port\_trace\_k\_msgq\_init(msgq)
    :   Trace initialization of Message Queue.

        Parameters:
        :   - **msgq** – Message Queue object

    sys\_port\_trace\_k\_msgq\_alloc\_init\_enter(msgq)
    :   Trace Message Queue alloc init attempt entry.

        Parameters:
        :   - **msgq** – Message Queue object

    sys\_port\_trace\_k\_msgq\_alloc\_init\_exit(msgq, ret)
    :   Trace Message Queue alloc init attempt outcome.

        Parameters:
        :   - **msgq** – Message Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_msgq\_cleanup\_enter(msgq)
    :   Trace Message Queue cleanup attempt entry.

        Parameters:
        :   - **msgq** – Message Queue object

    sys\_port\_trace\_k\_msgq\_cleanup\_exit(msgq, ret)
    :   Trace Message Queue cleanup attempt outcome.

        Parameters:
        :   - **msgq** – Message Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_msgq\_put\_enter(msgq, timeout)
    :   Trace Message Queue put attempt entry.

        Parameters:
        :   - **msgq** – Message Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_msgq\_put\_blocking(msgq, timeout)
    :   Trace Message Queue put attempt blocking.

        Parameters:
        :   - **msgq** – Message Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_msgq\_put\_exit(msgq, timeout, ret)
    :   Trace Message Queue put attempt outcome.

        Parameters:
        :   - **msgq** – Message Queue object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_msgq\_get\_enter(msgq, timeout)
    :   Trace Message Queue get attempt entry.

        Parameters:
        :   - **msgq** – Message Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_msgq\_get\_blocking(msgq, timeout)
    :   Trace Message Queue get attempt blockings.

        Parameters:
        :   - **msgq** – Message Queue object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_msgq\_get\_exit(msgq, timeout, ret)
    :   Trace Message Queue get attempt outcome.

        Parameters:
        :   - **msgq** – Message Queue object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_msgq\_peek(msgq, ret)
    :   Trace Message Queue peek.

        Parameters:
        :   - **msgq** – Message Queue object
            - **ret** – Return value

    sys\_port\_trace\_k\_msgq\_purge(msgq)
    :   Trace Message Queue purge.

        Parameters:
        :   - **msgq** – Message Queue object

### Mailbox

*group* subsys\_tracing\_apis\_mbox
:   Mailbox Tracing APIs.

    Defines

    sys\_port\_trace\_k\_mbox\_init(mbox)
    :   Trace initialization of Mailbox.

        Parameters:
        :   - **mbox** – Mailbox object

    sys\_port\_trace\_k\_mbox\_message\_put\_enter(mbox, timeout)
    :   Trace Mailbox message put attempt entry.

        Parameters:
        :   - **mbox** – Mailbox object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mbox\_message\_put\_blocking(mbox, timeout)
    :   Trace Mailbox message put attempt blocking.

        Parameters:
        :   - **mbox** – Mailbox object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mbox\_message\_put\_exit(mbox, timeout, ret)
    :   Trace Mailbox message put attempt outcome.

        Parameters:
        :   - **mbox** – Mailbox object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_mbox\_put\_enter(mbox, timeout)
    :   Trace Mailbox put attempt entry.

        Parameters:
        :   - **mbox** – Mailbox object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mbox\_put\_exit(mbox, timeout, ret)
    :   Trace Mailbox put attempt blocking.

        Parameters:
        :   - **mbox** – Mailbox object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_mbox\_async\_put\_enter(mbox, sem)
    :   Trace Mailbox async put entry.

        Parameters:
        :   - **mbox** – Mailbox object
            - **sem** – Semaphore object

    sys\_port\_trace\_k\_mbox\_async\_put\_exit(mbox, sem)
    :   Trace Mailbox async put exit.

        Parameters:
        :   - **mbox** – Mailbox object
            - **sem** – Semaphore object

    sys\_port\_trace\_k\_mbox\_get\_enter(mbox, timeout)
    :   Trace Mailbox get attempt entry.

        Parameters:
        :   - **mbox** – Mailbox entry
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mbox\_get\_blocking(mbox, timeout)
    :   Trace Mailbox get attempt blocking.

        Parameters:
        :   - **mbox** – Mailbox entry
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mbox\_get\_exit(mbox, timeout, ret)
    :   Trace Mailbox get attempt outcome.

        Parameters:
        :   - **mbox** – Mailbox entry
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_mbox\_data\_get(rx\_msg)
    :   Trace Mailbox data get.

        rx\_msg Receive Message object

### Pipes

*group* subsys\_tracing\_apis\_pipe
:   Pipe Tracing APIs.

    Defines

    sys\_port\_trace\_k\_pipe\_init(pipe)
    :   Trace initialization of Pipe.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_cleanup\_enter(pipe)
    :   Trace Pipe cleanup entry.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_cleanup\_exit(pipe, ret)
    :   Trace Pipe cleanup exit.

        Parameters:
        :   - **pipe** – Pipe object
            - **ret** – Return value

    sys\_port\_trace\_k\_pipe\_alloc\_init\_enter(pipe)
    :   Trace Pipe alloc init entry.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_alloc\_init\_exit(pipe, ret)
    :   Trace Pipe alloc init exit.

        Parameters:
        :   - **pipe** – Pipe object
            - **ret** – Return value

    sys\_port\_trace\_k\_pipe\_flush\_enter(pipe)
    :   Trace Pipe flush entry.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_flush\_exit(pipe)
    :   Trace Pipe flush exit.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_buffer\_flush\_enter(pipe)
    :   Trace Pipe buffer flush entry.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_buffer\_flush\_exit(pipe)
    :   Trace Pipe buffer flush exit.

        Parameters:
        :   - **pipe** – Pipe object

    sys\_port\_trace\_k\_pipe\_put\_enter(pipe, timeout)
    :   Trace Pipe put attempt entry.

        Parameters:
        :   - **pipe** – Pipe object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_pipe\_put\_blocking(pipe, timeout)
    :   Trace Pipe put attempt blocking.

        Parameters:
        :   - **pipe** – Pipe object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_pipe\_put\_exit(pipe, timeout, ret)
    :   Trace Pipe put attempt outcome.

        Parameters:
        :   - **pipe** – Pipe object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_pipe\_get\_enter(pipe, timeout)
    :   Trace Pipe get attempt entry.

        Parameters:
        :   - **pipe** – Pipe object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_pipe\_get\_blocking(pipe, timeout)
    :   Trace Pipe get attempt blocking.

        Parameters:
        :   - **pipe** – Pipe object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_pipe\_get\_exit(pipe, timeout, ret)
    :   Trace Pipe get attempt outcome.

        Parameters:
        :   - **pipe** – Pipe object
            - **timeout** – Timeout period
            - **ret** – Return value

### Heaps

*group* subsys\_tracing\_apis\_heap
:   Heap Tracing APIs.

    Defines

    sys\_port\_trace\_k\_heap\_init(h)
    :   Trace initialization of Heap.

        Parameters:
        :   - **h** – Heap object

    sys\_port\_trace\_k\_heap\_aligned\_alloc\_enter(h, timeout)
    :   Trace Heap aligned alloc attempt entry.

        Parameters:
        :   - **h** – Heap object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_heap\_aligned\_alloc\_blocking(h, timeout)
    :   Trace Heap align alloc attempt blocking.

        Parameters:
        :   - **h** – Heap object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_heap\_aligned\_alloc\_exit(h, timeout, ret)
    :   Trace Heap align alloc attempt outcome.

        Parameters:
        :   - **h** – Heap object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_heap\_alloc\_enter(h, timeout)
    :   Trace Heap alloc enter.

        Parameters:
        :   - **h** – Heap object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_heap\_alloc\_exit(h, timeout, ret)
    :   Trace Heap alloc exit.

        Parameters:
        :   - **h** – Heap object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_heap\_free(h)
    :   Trace Heap free.

        Parameters:
        :   - **h** – Heap object

    sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_enter(heap)
    :   Trace System Heap aligned alloc enter.

        Parameters:
        :   - **heap** – Heap object

    sys\_port\_trace\_k\_heap\_sys\_k\_aligned\_alloc\_exit(heap, ret)
    :   Trace System Heap aligned alloc exit.

        Parameters:
        :   - **heap** – Heap object
            - **ret** – Return value

    sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_enter(heap)
    :   Trace System Heap aligned alloc enter.

        Parameters:
        :   - **heap** – Heap object

    sys\_port\_trace\_k\_heap\_sys\_k\_malloc\_exit(heap, ret)
    :   Trace System Heap aligned alloc exit.

        Parameters:
        :   - **heap** – Heap object
            - **ret** – Return value

    sys\_port\_trace\_k\_heap\_sys\_k\_free\_enter(heap, heap\_ref)
    :   Trace System Heap free entry.

        Parameters:
        :   - **heap** – Heap object
            - **heap\_ref** – Heap reference

    sys\_port\_trace\_k\_heap\_sys\_k\_free\_exit(heap, heap\_ref)
    :   Trace System Heap free exit.

        Parameters:
        :   - **heap** – Heap object
            - **heap\_ref** – Heap reference

    sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_enter(heap)
    :   Trace System heap calloc enter.

        Parameters:
        :   - **heap** –

    sys\_port\_trace\_k\_heap\_sys\_k\_calloc\_exit(heap, ret)
    :   Trace System heap calloc exit.

        Parameters:
        :   - **heap** – Heap object
            - **ret** – Return value

### Memory Slabs

*group* subsys\_tracing\_apis\_mslab
:   Memory Slab Tracing APIs.

    Defines

    sys\_port\_trace\_k\_mem\_slab\_init(slab, rc)
    :   Trace initialization of Memory Slab.

        Parameters:
        :   - **slab** – Memory Slab object
            - **rc** – Return value

    sys\_port\_trace\_k\_mem\_slab\_alloc\_enter(slab, timeout)
    :   Trace Memory Slab alloc attempt entry.

        Parameters:
        :   - **slab** – Memory Slab object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mem\_slab\_alloc\_blocking(slab, timeout)
    :   Trace Memory Slab alloc attempt blocking.

        Parameters:
        :   - **slab** – Memory Slab object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_mem\_slab\_alloc\_exit(slab, timeout, ret)
    :   Trace Memory Slab alloc attempt outcome.

        Parameters:
        :   - **slab** – Memory Slab object
            - **timeout** – Timeout period
            - **ret** – Return value

    sys\_port\_trace\_k\_mem\_slab\_free\_enter(slab)
    :   Trace Memory Slab free entry.

        Parameters:
        :   - **slab** – Memory Slab object

    sys\_port\_trace\_k\_mem\_slab\_free\_exit(slab)
    :   Trace Memory Slab free exit.

        Parameters:
        :   - **slab** – Memory Slab object

### Timers

*group* subsys\_tracing\_apis\_timer
:   Timer Tracing APIs.

    Defines

    sys\_port\_trace\_k\_timer\_init(timer)
    :   Trace initialization of Timer.

        Parameters:
        :   - **timer** – Timer object

    sys\_port\_trace\_k\_timer\_start(timer, duration, period)
    :   Trace Timer start.

        Parameters:
        :   - **timer** – Timer object
            - **duration** – Timer duration
            - **period** – Timer period

    sys\_port\_trace\_k\_timer\_stop(timer)
    :   Trace Timer stop.

        Parameters:
        :   - **timer** – Timer object

    sys\_port\_trace\_k\_timer\_status\_sync\_enter(timer)
    :   Trace Timer status sync entry.

        Parameters:
        :   - **timer** – Timer object

    sys\_port\_trace\_k\_timer\_status\_sync\_blocking(timer, timeout)
    :   Trace Timer Status sync blocking.

        Parameters:
        :   - **timer** – Timer object
            - **timeout** – Timeout period

    sys\_port\_trace\_k\_timer\_status\_sync\_exit(timer, result)
    :   Trace Time Status sync outcome.

        Parameters:
        :   - **timer** – Timer object
            - **result** – Return value

### Object tracking

*group* subsys\_tracing\_object\_tracking
:   Object tracking.

    Object tracking provides lists to kernel objects, so their existence and current status can be tracked.

    The following global variables are the heads of available lists:

    - \_track\_list\_k\_timer
    - \_track\_list\_k\_mem\_slab
    - \_track\_list\_k\_sem
    - \_track\_list\_k\_mutex
    - \_track\_list\_k\_stack
    - \_track\_list\_k\_msgq
    - \_track\_list\_k\_mbox
    - \_track\_list\_k\_pipe
    - \_track\_list\_k\_queue
    - \_track\_list\_k\_event

    Defines

    SYS\_PORT\_TRACK\_NEXT(list)
    :   Gets node’s next element in a object tracking list.

        Parameters:
        :   - **list** – Node to get next element from.

### Syscalls

*group* subsys\_tracing\_apis\_syscall
:   Syscall Tracing APIs.

    Defines

    sys\_port\_trace\_syscall\_enter(id, name, ...)
    :   Trace syscall entry.

        Parameters:
        :   - **id** – Syscall ID (as defined in the generated syscall\_list.h)
            - **name** – Syscall name as a token (ex: k\_thread\_create)
            - **...** – Other parameters passed to the syscall

    sys\_port\_trace\_syscall\_exit(id, name, ...)
    :   Trace syscall exit.

        Parameters:
        :   - **id** – Syscall ID (as defined in the generated syscall\_list.h)
            - **name** – Syscall name as a token (ex: k\_thread\_create)
            - **...** – Other parameters passed to the syscall, if the syscall has a return, the return value is the last parameter in the list
