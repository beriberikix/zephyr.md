---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/logging/index.html
original_path: services/logging/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Logging

The logging API provides a common interface to process messages issued by
developers. Messages are passed through a frontend and are then
processed by active backends.
Custom frontend and backends can be used if needed.

Summary of the logging features:

- Deferred logging reduces the time needed to log a message by shifting time
  consuming operations to a known context instead of processing and sending
  the log message when called.
- Multiple backends supported (up to 9 backends).
- Custom frontend support. It can work together with backends.
- Compile time filtering on module level.
- Run time filtering independent for each backend.
- Additional run time filtering on module instance level.
- Timestamping with user provided function. Timestamp can have 32 or 64 bits.
- Dedicated API for dumping data.
- Dedicated API for handling transient strings.
- Panic support - in panic mode logging switches to blocking, synchronous
  processing.
- Printk support - printk message can be redirected to the logging.
- Design ready for multi-domain/multi-processor system.
- Support for logging floating point variables and long long arguments.
- Built-in copying of transient strings used as arguments.
- Support for multi-domain logging.

Logging API is highly configurable at compile time as well as at run time. Using
Kconfig options (see [Global Kconfig Options](#logging-kconfig)) logs can be gradually removed from
compilation to reduce image size and execution time when logs are not needed.
During compilation logs can be filtered out on module basis and severity level.

Logs can also be compiled in but filtered on run time using dedicate API. Run
time filtering is independent for each backend and each source of log messages.
Source of log messages can be a module or specific instance of the module.

There are four severity levels available in the system: error, warning, info
and debug. For each severity level the logging API ([include/zephyr/logging/log.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log.h))
has set of dedicated macros. Logger API also has macros for logging data.

For each level the following set of macros are available:

- `LOG_X` for standard printf-like messages, e.g. [`LOG_ERR`](#c.LOG_ERR).
- `LOG_HEXDUMP_X` for dumping data, e.g. [`LOG_HEXDUMP_WRN`](#c.LOG_HEXDUMP_WRN).
- `LOG_INST_X` for standard printf-like message associated with the
  particular instance, e.g. [`LOG_INST_INF`](#c.LOG_INST_INF).
- `LOG_INST_HEXDUMP_X` for dumping data associated with the particular
  instance, e.g. [`LOG_INST_HEXDUMP_DBG`](#c.LOG_INST_HEXDUMP_DBG)

The warning level also exposes the following additional macro:

- [`LOG_WRN_ONCE`](#c.LOG_WRN_ONCE) for warnings where only the first occurrence is of interest.

There are two configuration categories: configurations per module and global
configuration. When logging is enabled globally, it works for modules. However,
modules can disable logging locally. Every module can specify its own logging
level. The module must define the `LOG_LEVEL` macro before using the
API. Unless a global override is set, the module logging level will be honored.
The global override can only increase the logging level. It cannot be used to
lower module logging levels that were previously set higher. It is also possible
to globally limit logs by providing maximal severity level present in the
system, where maximal means lowest severity (e.g. if maximal level in the system
is set to info, it means that errors, warnings and info levels are present but
debug messages are excluded).

Each module which is using the logging must specify its unique name and
register itself to the logging. If module consists of more than one file,
registration is performed in one file but each file must define a module name.

Logger’s default frontend is designed to be thread safe and minimizes time needed
to log the message. Time consuming operations like string formatting or access to the
transport are not performed by default when logging API is called. When logging
API is called a message is created and added to the list. Dedicated,
configurable buffer for pool of log messages is used. There are 2 types of messages:
standard and hexdump. Each message contain source ID (module or instance ID and
domain ID which might be used for multiprocessor systems), timestamp and
severity level. Standard message contains pointer to the string and arguments.
Hexdump message contains copied data and string.

## [Global Kconfig Options](#id17)

These options can be found in the following path [subsys/logging/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig).

[`CONFIG_LOG`](../../kconfig.md#CONFIG_LOG "CONFIG_LOG"): Global switch, turns on/off the logging.

Mode of operations:

[`CONFIG_LOG_MODE_DEFERRED`](../../kconfig.md#CONFIG_LOG_MODE_DEFERRED "CONFIG_LOG_MODE_DEFERRED"): Deferred mode.

[`CONFIG_LOG_MODE_IMMEDIATE`](../../kconfig.md#CONFIG_LOG_MODE_IMMEDIATE "CONFIG_LOG_MODE_IMMEDIATE"): Immediate (synchronous) mode.

[`CONFIG_LOG_MODE_MINIMAL`](../../kconfig.md#CONFIG_LOG_MODE_MINIMAL "CONFIG_LOG_MODE_MINIMAL"): Minimal footprint mode.

Filtering options:

[`CONFIG_LOG_RUNTIME_FILTERING`](../../kconfig.md#CONFIG_LOG_RUNTIME_FILTERING "CONFIG_LOG_RUNTIME_FILTERING"): Enables runtime reconfiguration of the
filtering.

[`CONFIG_LOG_DEFAULT_LEVEL`](../../kconfig.md#CONFIG_LOG_DEFAULT_LEVEL "CONFIG_LOG_DEFAULT_LEVEL"): Default level, sets the logging level
used by modules that are not setting their own logging level.

[`CONFIG_LOG_OVERRIDE_LEVEL`](../../kconfig.md#CONFIG_LOG_OVERRIDE_LEVEL "CONFIG_LOG_OVERRIDE_LEVEL"): It overrides module logging level when
it is not set or set lower than the override value.

[`CONFIG_LOG_MAX_LEVEL`](../../kconfig.md#CONFIG_LOG_MAX_LEVEL "CONFIG_LOG_MAX_LEVEL"): Maximal (lowest severity) level which is
compiled in.

Processing options:

[`CONFIG_LOG_MODE_OVERFLOW`](../../kconfig.md#CONFIG_LOG_MODE_OVERFLOW "CONFIG_LOG_MODE_OVERFLOW"): When new message cannot be allocated,
oldest one are discarded.

[`CONFIG_LOG_BLOCK_IN_THREAD`](../../kconfig.md#CONFIG_LOG_BLOCK_IN_THREAD "CONFIG_LOG_BLOCK_IN_THREAD"): If enabled and new log message cannot
be allocated thread context will block for up to
[`CONFIG_LOG_BLOCK_IN_THREAD_TIMEOUT_MS`](../../kconfig.md#CONFIG_LOG_BLOCK_IN_THREAD_TIMEOUT_MS "CONFIG_LOG_BLOCK_IN_THREAD_TIMEOUT_MS") or until log message is
allocated.

[`CONFIG_LOG_PRINTK`](../../kconfig.md#CONFIG_LOG_PRINTK "CONFIG_LOG_PRINTK"): Redirect printk calls to the logging.

[`CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`](../../kconfig.md#CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD "CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD"): When the number of buffered log
messages reaches the threshold, the dedicated thread (see [`log_thread_set()`](#c.log_thread_set))
is woken up. If [`CONFIG_LOG_PROCESS_THREAD`](../../kconfig.md#CONFIG_LOG_PROCESS_THREAD "CONFIG_LOG_PROCESS_THREAD") is enabled then this
threshold is used by the internal thread.

[`CONFIG_LOG_PROCESS_THREAD`](../../kconfig.md#CONFIG_LOG_PROCESS_THREAD "CONFIG_LOG_PROCESS_THREAD"): When enabled, logging thread is created
which handles log processing.

[`CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS`](../../kconfig.md#CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS "CONFIG_LOG_PROCESS_THREAD_STARTUP_DELAY_MS"): Delay in milliseconds
after which logging thread is started.

[`CONFIG_LOG_BUFFER_SIZE`](../../kconfig.md#CONFIG_LOG_BUFFER_SIZE "CONFIG_LOG_BUFFER_SIZE"): Number of bytes dedicated for the circular
packet buffer.

[`CONFIG_LOG_FRONTEND`](../../kconfig.md#CONFIG_LOG_FRONTEND "CONFIG_LOG_FRONTEND"): Direct logs to a custom frontend.

[`CONFIG_LOG_FRONTEND_ONLY`](../../kconfig.md#CONFIG_LOG_FRONTEND_ONLY "CONFIG_LOG_FRONTEND_ONLY"): No backends are used when messages goes to frontend.

[`CONFIG_LOG_FRONTEND_OPT_API`](../../kconfig.md#CONFIG_LOG_FRONTEND_OPT_API "CONFIG_LOG_FRONTEND_OPT_API"): Optional API optimized for the most common
simple messages.

[`CONFIG_LOG_CUSTOM_HEADER`](../../kconfig.md#CONFIG_LOG_CUSTOM_HEADER "CONFIG_LOG_CUSTOM_HEADER"): Injects an application provided header into log.h

[`CONFIG_LOG_TIMESTAMP_64BIT`](../../kconfig.md#CONFIG_LOG_TIMESTAMP_64BIT "CONFIG_LOG_TIMESTAMP_64BIT"): 64 bit timestamp.

[`CONFIG_LOG_SIMPLE_MSG_OPTIMIZE`](../../kconfig.md#CONFIG_LOG_SIMPLE_MSG_OPTIMIZE "CONFIG_LOG_SIMPLE_MSG_OPTIMIZE"): Optimizes simple log messages for size
and performance. Option available only for 32 bit architectures.

Formatting options:

[`CONFIG_LOG_FUNC_NAME_PREFIX_ERR`](../../kconfig.md#CONFIG_LOG_FUNC_NAME_PREFIX_ERR "CONFIG_LOG_FUNC_NAME_PREFIX_ERR"): Prepend standard ERROR log messages
with function name. Hexdump messages are not prepended.

[`CONFIG_LOG_FUNC_NAME_PREFIX_WRN`](../../kconfig.md#CONFIG_LOG_FUNC_NAME_PREFIX_WRN "CONFIG_LOG_FUNC_NAME_PREFIX_WRN"): Prepend standard WARNING log messages
with function name. Hexdump messages are not prepended.

[`CONFIG_LOG_FUNC_NAME_PREFIX_INF`](../../kconfig.md#CONFIG_LOG_FUNC_NAME_PREFIX_INF "CONFIG_LOG_FUNC_NAME_PREFIX_INF"): Prepend standard INFO log messages
with function name. Hexdump messages are not prepended.

[`CONFIG_LOG_FUNC_NAME_PREFIX_DBG`](../../kconfig.md#CONFIG_LOG_FUNC_NAME_PREFIX_DBG "CONFIG_LOG_FUNC_NAME_PREFIX_DBG"): Prepend standard DEBUG log messages
with function name. Hexdump messages are not prepended.

[`CONFIG_LOG_BACKEND_SHOW_COLOR`](../../kconfig.md#CONFIG_LOG_BACKEND_SHOW_COLOR "CONFIG_LOG_BACKEND_SHOW_COLOR"): Enables coloring of errors (red)
and warnings (yellow).

[`CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP`](../../kconfig.md#CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP "CONFIG_LOG_BACKEND_FORMAT_TIMESTAMP"): If enabled timestamp is
formatted to *hh:mm:ss:mmm,uuu*. Otherwise is printed in raw format.

Backend options:

[`CONFIG_LOG_BACKEND_UART`](../../kconfig.md#CONFIG_LOG_BACKEND_UART "CONFIG_LOG_BACKEND_UART"): Enabled built-in UART backend.

## [Usage](#id18)

### [Logging in a module](#id19)

In order to use logging in the module, a unique name of a module must be
specified and module must be registered using [`LOG_MODULE_REGISTER`](#c.LOG_MODULE_REGISTER).
Optionally, a compile time log level for the module can be specified as the
second parameter. Default log level ([`CONFIG_LOG_DEFAULT_LEVEL`](../../kconfig.md#CONFIG_LOG_DEFAULT_LEVEL "CONFIG_LOG_DEFAULT_LEVEL")) is used
if custom log level is not provided.

```c
#include <zephyr/logging/log.h>
LOG_MODULE_REGISTER(foo, CONFIG_FOO_LOG_LEVEL);
```

If the module consists of multiple files, then `LOG_MODULE_REGISTER()` should
appear in exactly one of them. Each other file should use
[`LOG_MODULE_DECLARE`](#c.LOG_MODULE_DECLARE) to declare its membership in the module.
Optionally, a compile time log level for the module can be specified as
the second parameter. Default log level ([`CONFIG_LOG_DEFAULT_LEVEL`](../../kconfig.md#CONFIG_LOG_DEFAULT_LEVEL "CONFIG_LOG_DEFAULT_LEVEL"))
is used if custom log level is not provided.

```c
#include <zephyr/logging/log.h>
/* In all files comprising the module but one */
LOG_MODULE_DECLARE(foo, CONFIG_FOO_LOG_LEVEL);
```

In order to use logging API in a function implemented in a header file
[`LOG_MODULE_DECLARE`](#c.LOG_MODULE_DECLARE) macro must be used in the function body
before logging API is called. Optionally, a compile time log level for the module
can be specified as the second parameter. Default log level
([`CONFIG_LOG_DEFAULT_LEVEL`](../../kconfig.md#CONFIG_LOG_DEFAULT_LEVEL "CONFIG_LOG_DEFAULT_LEVEL")) is used if custom log level is not
provided.

```c
#include <zephyr/logging/log.h>

static inline void foo(void)
{
     LOG_MODULE_DECLARE(foo, CONFIG_FOO_LOG_LEVEL);

     LOG_INF("foo");
}
```

Dedicated Kconfig template ([subsys/logging/Kconfig.template.log\_config](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config))
can be used to create local log level configuration.

Example below presents usage of the template. As a result CONFIG\_FOO\_LOG\_LEVEL
will be generated:

```text
module = FOO
module-str = foo
source "subsys/logging/Kconfig.template.log_config"
```

### [Logging in a module instance](#id20)

In case of modules which are multi-instance and instances are widely used
across the system enabling logs will lead to flooding. The logger provides the tools
which can be used to provide filtering on instance level rather than module
level. In that case logging can be enabled for particular instance.

In order to use instance level filtering following steps must be performed:

- a pointer to specific logging structure is declared in instance structure.
  `LOG_INSTANCE_PTR_DECLARE` is used for that.

```c
#include <zephyr/logging/log_instance.h>

struct foo_object {
     LOG_INSTANCE_PTR_DECLARE(log);
     uint32_t id;
}
```

- module must provide macro for instantiation. In that macro, logging instance
  is registered and log instance pointer is initialized in the object structure.

```c
#define FOO_OBJECT_DEFINE(_name)                             \
     LOG_INSTANCE_REGISTER(foo, _name, CONFIG_FOO_LOG_LEVEL) \
     struct foo_object _name = {                             \
             LOG_INSTANCE_PTR_INIT(log, foo, _name)          \
     }
```

Note that when logging is disabled logging instance and pointer to that instance
are not created.

In order to use the instance logging API in a source file, a compile-time log
level must be set using [`LOG_LEVEL_SET`](#c.LOG_LEVEL_SET).

```c
LOG_LEVEL_SET(CONFIG_FOO_LOG_LEVEL);

void foo_init(foo_object *f)
{
     LOG_INST_INF(f->log, "Initialized.");
}
```

In order to use the instance logging API in a header file, a compile-time log
level must be set using [`LOG_LEVEL_SET`](#c.LOG_LEVEL_SET).

```c
static inline void foo_init(foo_object *f)
{
     LOG_LEVEL_SET(CONFIG_FOO_LOG_LEVEL);

     LOG_INST_INF(f->log, "Initialized.");
}
```

### [Controlling the logging](#id21)

By default, logging processing in deferred mode is handled internally by the
dedicated task which starts automatically. However, it might not be available
if multithreading is disabled. It can also be disabled by unsetting
[`CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`](../../kconfig.md#CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD "CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD"). In that case, logging can
be controlled using the API defined in [include/zephyr/logging/log\_ctrl.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_ctrl.h).
Logging must be initialized before it can be used. Optionally, the user can provide
a function which returns the timestamp value. If not provided, `k_cycle_get`
or [`k_cycle_get_32`](../../kernel/services/timing/clocks.md#c.k_cycle_get_32 "k_cycle_get_32") is used for timestamping.
The [`log_process()`](#c.log_process) function is used to trigger processing of one log
message (if pending), and returns true if there are more messages pending.
However, it is recommended to use macro wrappers ([`LOG_INIT`](#c.LOG_INIT) and
[`LOG_PROCESS`](#c.LOG_PROCESS)) which handle the case where logging is disabled.

The following snippet shows how logging can be processed in simple forever loop.

```c
#include <zephyr/logging/log_ctrl.h>

int main(void)
{
     LOG_INIT();
     /* If multithreading is enabled provide thread id to the logging. */
     log_thread_set(k_current_get());

     while (1) {
             if (LOG_PROCESS() == false) {
                     /* sleep */
             }
     }
}
```

If logs are processed from a thread (user or internal) then it is possible to enable
a feature which will wake up processing thread when certain amount of log messages are
buffered (see [`CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD`](../../kconfig.md#CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD "CONFIG_LOG_PROCESS_TRIGGER_THRESHOLD")).

## [Logging panic](#id22)

In case of error condition system usually can no longer rely on scheduler or
interrupts. In that situation deferred log message processing is not an option.
Logger controlling API provides a function for entering into panic mode
([`log_panic()`](#c.log_panic)) which should be called in such situation.

When [`log_panic()`](#c.log_panic) is called, \_panic\_ notification is sent to all active
backends. Once all backends are notified, all buffered messages are flushed. Since
that moment all logs are processed in a blocking way.

## [Printk](#id23)

Typically, logging and `printk()` use the same output, which they compete
for. This can lead to issues if the output does not support preemption but it may
also result in corrupted output because logging data is interleaved with printk
data. However, it is possible to redirect printk messages to the
logging subsystem by enabling [`CONFIG_LOG_PRINTK`](../../kconfig.md#CONFIG_LOG_PRINTK "CONFIG_LOG_PRINTK"). In that case,
printk entries are treated as log messages with level 0 (they cannot be disabled).
When enabled, logging manages the output so there is no interleaving. However,
in deferred mode the printk behaviour is changed since the output is delayed
until the logging thread processes the data. [`CONFIG_LOG_PRINTK`](../../kconfig.md#CONFIG_LOG_PRINTK "CONFIG_LOG_PRINTK")
is enabled by default.

## [Architecture](#id24)

Logging consists of 3 main parts:

- Frontend
- Core
- Backends

Log message is generated by a source of logging which can be a module or
instance of a module.

### [Default Frontend](#id25)

Default frontend is engaged when the logging API is called in a source of logging (e.g.
[`LOG_INF`](#c.LOG_INF)) and is responsible for filtering a message (compile and run
time), allocating a buffer for the message, creating the message and committing that
message. Since the logging API can be called in an interrupt, the frontend is optimized
to log the message as fast as possible.

#### Log message

A log message contains a message descriptor (source, domain and level), timestamp,
formatted string details (see [Cbprintf Packaging](../formatted_output.md#cbprintf-packaging)) and optional data.
Log messages are stored in a continuous block of memory.
Memory is allocated from a circular packet buffer ([Multi Producer Single Consumer Packet Buffer](../../kernel/data_structures/mpsc_pbuf.md#mpsc-pbuf)), which has
a few consequences:

> - Each message is a self-contained, continuous block of memory thus it is suited
>   for copying the message (e.g. for offline processing).
> - Messages must be sequentially freed. Backend processing is synchronous. Backend
>   can make a copy for deferred processing.

A log message has following format:

| Message Header | 2 bits: MPSC packet buffer header |
| --- | --- |
| 1 bit: Trace/Log message flag |
| 3 bits: Domain ID |
| 3 bits: Level |
| 10 bits: Cbprintf Package Length |
| 12 bits: Data length |
| 1 bit: Reserved |
| pointer: Pointer to the source descriptor [[1]](#l0) |
| 32 or 64 bits: Timestamp [[1]](#l0) |
| Optional padding [[2]](#l1) |
| Cbprintf  package  (optional) | Header |
| Arguments |
| Appended strings |
| Hexdump data (optional) | |
| Alignment padding (optional) | |

Footnotes

[1]
([1](#id2),[2](#id3))

Depending on the platform and the timestamp size fields may be swapped.

[[2](#id4)]

It may be required for cbprintf package alignment

#### Log message allocation

It may happen that the frontend cannot allocate a message. This happens if the
system is generating more log messages than it can process in certain time
frame. There are two strategies to handle that case:

- No overflow - the new log is dropped if space for a message cannot be allocated.
- Overflow - the oldest pending messages are freed, until the new message can be
  allocated. Enabled by [`CONFIG_LOG_MODE_OVERFLOW`](../../kconfig.md#CONFIG_LOG_MODE_OVERFLOW "CONFIG_LOG_MODE_OVERFLOW"). Note that it degrades
  performance thus it is recommended to adjust buffer size and amount of enabled
  logs to limit dropping.

#### Run-time filtering

If run-time filtering is enabled, then for each source of logging a filter
structure in RAM is declared. Such filter is using 32 bits divided into ten 3
bit slots. Except *slot 0*, each slot stores current filter for one backend in
the system. *Slot 0* (bits 0-2) is used to aggregate maximal filter setting for
given source of logging. Aggregate slot determines if log message is created
for given entry since it indicates if there is at least one backend expecting
that log entry. Backend slots are examined when message is processed by the core
to determine if message is accepted by the given backend. Contrary to compile
time filtering, binary footprint is increased because logs are compiled in.

In the example below backend 1 is set to receive errors (*slot 1*) and backend
2 up to info level (*slot 2*). Slots 3-9 are not used. Aggregated filter
(*slot 0*) is set to info level and up to this level message from that
particular source will be buffered.

| slot 0 | slot 1 | slot 2 | slot 3 | … | slot 9 |
| --- | --- | --- | --- | --- | --- |
| INF | ERR | INF | OFF | … | OFF |

### [Custom Frontend](#id26)

Custom frontend is enabled using [`CONFIG_LOG_FRONTEND`](../../kconfig.md#CONFIG_LOG_FRONTEND "CONFIG_LOG_FRONTEND"). Logs are directed
to functions declared in [include/zephyr/logging/log\_frontend.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_frontend.h).
If option [`CONFIG_LOG_FRONTEND_ONLY`](../../kconfig.md#CONFIG_LOG_FRONTEND_ONLY "CONFIG_LOG_FRONTEND_ONLY") is enabled then log message is not
created and no backend is handled. Otherwise, custom frontend can coexist with
backends.

In some cases, logs need to be redirected at the macro level. For these cases,
[`CONFIG_LOG_CUSTOM_HEADER`](../../kconfig.md#CONFIG_LOG_CUSTOM_HEADER "CONFIG_LOG_CUSTOM_HEADER") can be used to inject an application provided
header named zephyr\_custom\_log.h at the end of [include/zephyr/logging/log.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log.h).

### [Logging strings](#id27)

String arguments are handled by [Cbprintf Packaging](../formatted_output.md#cbprintf-packaging). See
[Limitations and recommendations](../formatted_output.md#cbprintf-packaging-limitations) for limitations and recommendations.

### [Multi-domain support](#id28)

More complex systems can consist of multiple domains where each domain is an
independent binary. Examples of domains are a core in a multicore SoC or one
of the binaries (Secure or Nonsecure) on an ARM TrustZone core.

Tracing and debugging on a multi-domain system is more complex and requires an efficient logging
system. Two approaches can be used to structure this logging system:

- Log inside each domain independently.
  This option is not always possible as it requires that each domain has an available backend
  (for example, UART). This approach can also be troublesome to use and not scalable,
  as logs are presented on independent outputs.
- Use a multi-domain logging system where log messages from each domain end up in one root domain,
  where they are processed exactly as in a single domain case.
  In this approach, log messages are passed between domains using a connection between domains
  created from the backend on one side and linked to the other.

  The Log link is an interface introduced in this multi-domain approach. The Log link is
  responsible for receiving any log message from another domain, creating a copy, and
  putting that local log message copy (including remote data) into the message queue.
  This specific log link implementation matches the complementary backend implementation
  to allow log messages exchange and logger control like configuring filtering, getting log
  source names, and so on.

There are three types of domains in a multi-domain system:

- The *end domain* has the logging core implementation and a cross-domain
  backend. It can also have other backends in parallel.
- The *relay domain* has one or more links to other domains but does not
  have backends that output logs to the user. It has a cross-domain backend either to
  another relay or to the root domain.
- The *root domain* has one or multiple links and a backend that outputs logs
  to the user.

See the following image for an example of a multi-domain setup:

![../../_images/multidomain.png](../../_images/multidomain.png)

Multi-domain example

In this architecture, a link can handle multiple domains.
For example, let’s consider an SoC with two ARM Cortex-M33 cores with TrustZone: cores A and B (see
the example illustrated above). There are four domains in the system, as
each core has both a Secure and a Nonsecure domain. If *core A nonsecure* (A\_NS) is the
root domain, it has two links: one to *core A secure* (A\_NS-A\_S) and one to
*core B nonsecure* (A\_NS-B\_NS). *B\_NS* domain has one link, to *core B secure*
*B\_NS-B\_S*), and a backend to *A\_NS*.

Since in all instances there is a standard logging subsystem, it is always possible
to have multiple backends and simultaneously output messages to them. An example of this is shown
in the illustration above as a dotted UART backend on the *B\_NS* domain.

#### Domain ID

The source of each log message can be identified by the following fields in the header:
`source_id` and `domain_id`.

The value assigned to the `domain_id` is relative. Whenever a domain creates a log message,
it sets its `domain_id` to `0`.
When a message crosses the domain, `domain_id` changes as it is increased by the link offset.
The link offset is assigned during the initialization, where the logger core is iterating
over all the registered links and assigned offsets.

The first link has the offset set to 1.
The following offset equals the previous link offset plus the number of domains in the previous
link.

The following example is shown below, where
the assigned `domain_ids` are shown for each domain:

![../../_images/domain_ids.png](../../_images/domain_ids.png)

Domain IDs assigning example

Let’s consider a log message created on the *B\_S* domain:

1. Initially, it has its `domain_id` set to `0`.
2. When the *B\_NS-B\_S* link receives the message, it increases the `domain_id`
   to `1` by adding the *B\_NS-B\_S* offset.
3. The message is passed to *A\_NS*.
4. When the *A\_NS-B\_NS* link receives the message, it adds the offset (`2`) to the `domain_id`.
   The message ends up with the `domain_id` set to `3`, which uniquely identifies the message
   originator.

#### Cross-domain log message

In most cases, the address space of each domain is unique, and one domain
cannot access directly the data in another domain. For this reason, the backend can
partially process the message before it is passed to another domain. Partial
processing can include converting a string package to a *fully self-contained*
version (copying read-only strings to the package body).

Each domain can have a different timestamp source in terms of frequency and
offset. Logging does not perform any timestamp conversion.

#### Runtime filtering

In the single-domain case, each log source has a dedicated variable with runtime
filtering for each backend in the system. In the multi-domain case, the originator of
the log message is not aware of the number of backends in the root domain.

As such, to filter logs in multiple domains, each source requires a runtime
filtering setting in each domain on the way to the root domain. As the number of
sources in other domains is not known during the compilation, the runtime filtering
of remote sources must use dynamically allocated memory (one word per
source). When a backend in the root domain changes the filtering of the module from a
remote domain, the local filter is updated. After the update, the aggregated
filter (the maximum from all the local backends) is checked and, if changed, the remote domain is
informed about this change. With this approach, the runtime filtering works identically
in both multi-domain and single-domain scenarios.

#### Message ordering

Logging does not provide any mechanism for synchronizing timestamps across multiple
domains:

- If domains have different timestamp sources, messages will be
  processed in the order of arrival to the buffer in the root domain.
- If domains have the same timestamp source or if there is an out-of-bound mechanism that
  recalculates timestamps, there are 2 options:

  - Messages are processed as they arrive in the buffer in the root domain.
    Messages are unordered but they can be sorted by the host as the timestamp
    indicates the time of the message generation.
  - Links have dedicated buffers. During processing, the head of each buffer is checked
    and the oldest message is processed first.

    With this approach, it is possible to maintain the order of the messages at the cost
    of a suboptimal memory utilization (since the buffer is not shared) and increased processing
    latency (see [`CONFIG_LOG_PROCESSING_LATENCY_US`](../../kconfig.md#CONFIG_LOG_PROCESSING_LATENCY_US "CONFIG_LOG_PROCESSING_LATENCY_US")).

### [Logging backends](#id29)

Logging backends are registered using [`LOG_BACKEND_DEFINE`](#c.LOG_BACKEND_DEFINE). The macro
creates an instance in the dedicated memory section. Backends can be dynamically
enabled ([`log_backend_enable()`](#c.log_backend_enable)) and disabled. When
[Run-time filtering](#logging-runtime-filtering) is enabled, [`log_filter_set()`](#c.log_filter_set) can be used
to dynamically change filtering of a module logs for given backend. Module is
identified by source ID and domain ID. Source ID can be retrieved if source name
is known by iterating through all registered sources.

Logging supports up to 9 concurrent backends. Log message is passed to the
each backend in processing phase. Additionally, backend is notified when logging
enter panic mode with [`log_backend_panic()`](#c.log_backend_panic). On that call backend should
switch to synchronous, interrupt-less operation or shut down itself if that is
not supported. Occasionally, logging may inform backend about number of dropped
messages with [`log_backend_dropped()`](#c.log_backend_dropped). Message processing API is version
specific.

[`log_backend_msg_process()`](#c.log_backend_msg_process) is used for processing message. It is common for
standard and hexdump messages because log message hold string with arguments
and data. It is also common for deferred and immediate logging.

#### Message formatting

Logging provides set of function that can be used by the backend to format a
message. Helper functions are available in [include/zephyr/logging/log\_output.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_output.h).

Example message formatted using [`log_output_msg_process()`](#c.log_output_msg_process).

```shell
[00:00:00.000,274] <info> sample_instance.inst1: logging message
```

### [Dictionary-based Logging](#id30)

Dictionary-based logging, instead of human readable texts, outputs the log
messages in binary format. This binary format encodes arguments to formatted
strings in their native storage formats which can be more compact than their
text equivalents. For statically defined strings (including the format
strings and any string arguments), references to the ELF file are encoded
instead of the whole strings. A dictionary created at build time contains
the mappings between these references and the actual strings. This allows
the offline parser to obtain the strings from the dictionary to parse
the log messages. This binary format allows a more compact representation
of log messages in certain scenarios. However, this requires the use of
an offline parser and is not as intuitive to use as text-based log messages.

Note that `long double` is not supported by Python’s `struct` module.
Therefore, log messages with `long double` will not display the correct
values.

#### Configuration

Here are kconfig options related to dictionary-based logging:

- [`CONFIG_LOG_DICTIONARY_SUPPORT`](../../kconfig.md#CONFIG_LOG_DICTIONARY_SUPPORT "CONFIG_LOG_DICTIONARY_SUPPORT") enables dictionary-based logging
  support. This should be selected by the backends which require it.
- The UART backend can be used for dictionary-based logging. These are
  additional config for the UART backend:

  - [`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX`](../../kconfig.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX "CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX") tells
    the UART backend to output hexadecimal characters for dictionary based
    logging. This is useful when the log data needs to be captured manually
    via terminals and consoles.
  - [`CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_BIN`](../../kconfig.md#CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_BIN "CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_BIN") tells
    the UART backend to output binary data.

#### Usage

When dictionary-based logging is enabled via enabling related logging backends,
a JSON database file, named `log_dictionary.json`, will be created
in the build directory. This database file contains information for the parser
to correctly parse the log data. Note that this database file only works
with the same build, and cannot be used for any other builds.

To use the log parser:

```shell
./scripts/logging/dictionary/log_parser.py <build dir>/log_dictionary.json <log data file>
```

The parser takes two required arguments, where the first one is the full path
to the JSON database file, and the second part is the file containing log data.
Add an optional argument `--hex` to the end if the log data file contains
hexadecimal characters
(e.g. when `CONFIG_LOG_BACKEND_UART_OUTPUT_DICTIONARY_HEX=y`). This tells
the parser to convert the hexadecimal characters to binary before parsing.

Please refer to the [Dictionary-based logging](../../samples/subsys/logging/dictionary/README.md#logging-dictionary "Output binary log data using the dictionary-based logging API.") sample to learn more on how to use
the log parser.

## [Recommendations](#id31)

The are following recommendations:

- Enable [`CONFIG_LOG_SPEED`](../../kconfig.md#CONFIG_LOG_SPEED "CONFIG_LOG_SPEED") to slightly speed up deferred logging at the
  cost of slight increase in memory footprint.
- Compiler with C11 `_Generic` keyword support is recommended. Logging
  performance is significantly degraded without it. See [Cbprintf Packaging](../formatted_output.md#cbprintf-packaging).
- It is recommended to cast pointer to `const char *` when it is used with `%s`
  format specifier and it points to a constant string.
- It is recommended to cast pointer to `char *` when it is used with `%s`
  format specifier and it points to a transient string.
- It is recommended to cast character pointer to non character pointer
  (e.g., `void *`) when it is used with `%p` format specifier.

```c
LOG_WRN("%s", str);
LOG_WRN("%p", (void *)str);
```

## [Benchmark](#id32)

Benchmark numbers from [tests/subsys/logging/log\_benchmark](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/logging/log_benchmark) performed
on `qemu_x86`. It is a rough comparison to give a general overview.

| Feature |  |
| --- | --- |
| Kernel logging | 7us [[3]](#f0)/11us |
| User logging | 13us |
| kernel logging with overwrite | 10us [[3]](#f0)/15us |
| Logging transient string | 42us |
| Logging transient string from user | 50us |
| Memory utilization [[4]](#f1) | 518 |
| Memory footprint (test) [[5]](#f2) | 2k |
| Memory footprint (application) [[6]](#f3) | 3.5k |
| Message footprint [[7]](#f4) | 47 [[3]](#f0)/32 bytes |

Benchmark details

[3]
([1](#id7),[2](#id8),[3](#id13))

[`CONFIG_LOG_SPEED`](../../kconfig.md#CONFIG_LOG_SPEED "CONFIG_LOG_SPEED") enabled.

[[4](#id9)]

Number of log messages with various number of arguments that fits in 2048
bytes dedicated for logging.

[[5](#id10)]

Logging subsystem memory footprint in [tests/subsys/logging/log\_benchmark](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/logging/log_benchmark)
where filtering and formatting features are not used.

[[6](#id11)]

Logging subsystem memory footprint in [samples/subsys/logging/logger](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/logging/logger).

[[7](#id12)]

Average size of a log message (excluding string) with 2 arguments on `Cortex M3`

## [Stack usage](#id33)

When logging is enabled it impacts stack usage of the context that uses logging API. If stack
is optimized it may lead to stack overflow. Stack usage depends on mode and optimization. It
also significantly varies between platforms. In general, when [`CONFIG_LOG_MODE_DEFERRED`](../../kconfig.md#CONFIG_LOG_MODE_DEFERRED "CONFIG_LOG_MODE_DEFERRED")
is used stack usage is smaller since logging is limited to creating and storing log message.
When [`CONFIG_LOG_MODE_IMMEDIATE`](../../kconfig.md#CONFIG_LOG_MODE_IMMEDIATE "CONFIG_LOG_MODE_IMMEDIATE") is used then log message is processed by the backend
which includes string formatting. In case of that mode, stack usage will depend on which backends
are used.

[tests/subsys/logging/log\_stack](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/logging/log_stack) test is used to characterize stack usage depending
on mode, optimization and platform used. Test is using only the default backend.

Some of the platforms characterization for log message with two `integer` arguments listed below:

| Platform | Deferred | Deferred (no optimization) | Immediate | Immediate (no optimization) |
| --- | --- | --- | --- | --- |
| ARM Cortex-M3 | 40 | 152 | 412 | 783 |
| x86 | 12 | 224 | 388 | 796 |
| riscv32 | 24 | 208 | 456 | 844 |
| xtensa | 72 | 336 | 504 | 944 |
| x86\_64 | 32 | 528 | 1088 | 1440 |

## [API Reference](#id34)

### [Logger API](#id35)

Related code samples

[BLE logging backend](../../samples/subsys/logging/ble_backend/README.md#logging-ble-backend "Send log messages over BLE using the BLE logging backend.")
:   Send log messages over BLE using the BLE logging backend.

[Dictionary-based logging](../../samples/subsys/logging/dictionary/README.md#logging-dictionary "Output binary log data using the dictionary-based logging API.")
:   Output binary log data using the dictionary-based logging API.

[Logging](../../samples/subsys/logging/logger/README.md#logging "Output log messages to the console using the logging subsystem.")
:   Output log messages to the console using the logging subsystem.

*group* Logging API
:   Logger API.

    Defines

    LOG\_ERR(...)
    :   Writes an ERROR level message to the log.

        It’s meant to report severe errors, such as those from which it’s not possible to recover.

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_WRN(...)
    :   Writes a WARNING level message to the log.

        It’s meant to register messages related to unusual situations that are not necessarily errors.

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_INF(...)
    :   Writes an INFO level message to the log.

        It’s meant to write generic user oriented messages.

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_DBG(...)
    :   Writes a DEBUG level message to the log.

        It’s meant to write developer oriented information.

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_WRN\_ONCE(...)
    :   Writes a WARNING level message to the log on the first execution only.

        It’s meant for situations that warrant investigation but could clutter the logs if output on every execution.

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_PRINTK(...)
    :   Unconditionally print raw log message.

        The result is same as if printk was used but it goes through logging infrastructure thus utilizes logging mode, e.g. deferred mode.

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_RAW(...)
    :   Unconditionally print raw log message.

        Provided string is printed as is without appending any characters (e.g., color or newline).

        Parameters:
        :   - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_INST\_ERR(\_log\_inst, ...)
    :   Writes an ERROR level message associated with the instance to the log.

        Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It’s meant to report severe errors, such as those from which it’s not possible to recover.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_INST\_WRN(\_log\_inst, ...)
    :   Writes a WARNING level message associated with the instance to the log.

        Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It’s meant to register messages related to unusual situations that are not necessarily errors.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_INST\_INF(\_log\_inst, ...)
    :   Writes an INFO level message associated with the instance to the log.

        Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It’s meant to write generic user oriented messages.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_INST\_DBG(\_log\_inst, ...)
    :   Writes a DEBUG level message associated with the instance to the log.

        Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It’s meant to write developer oriented information.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **...** – A string optionally containing printk valid conversion specifier, followed by as many values as specifiers.

    LOG\_HEXDUMP\_ERR(\_data, \_length, \_str)
    :   Writes an ERROR level hexdump message to the log.

        It’s meant to report severe errors, such as those from which it’s not possible to recover.

        Parameters:
        :   - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_HEXDUMP\_WRN(\_data, \_length, \_str)
    :   Writes a WARNING level message to the log.

        It’s meant to register messages related to unusual situations that are not necessarily errors.

        Parameters:
        :   - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_HEXDUMP\_INF(\_data, \_length, \_str)
    :   Writes an INFO level message to the log.

        It’s meant to write generic user oriented messages.

        Parameters:
        :   - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_HEXDUMP\_DBG(\_data, \_length, \_str)
    :   Writes a DEBUG level message to the log.

        It’s meant to write developer oriented information.

        Parameters:
        :   - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_INST\_HEXDUMP\_ERR(\_log\_inst, \_data, \_length, \_str)
    :   Writes an ERROR hexdump message associated with the instance to the log.

        Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It’s meant to report severe errors, such as those from which it’s not possible to recover.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_INST\_HEXDUMP\_WRN(\_log\_inst, \_data, \_length, \_str)
    :   Writes a WARNING level hexdump message associated with the instance to the log.

        It’s meant to register messages related to unusual situations that are not necessarily errors.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_INST\_HEXDUMP\_INF(\_log\_inst, \_data, \_length, \_str)
    :   Writes an INFO level hexdump message associated with the instance to the log.

        It’s meant to write generic user oriented messages.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_INST\_HEXDUMP\_DBG(\_log\_inst, \_data, \_length, \_str)
    :   Writes a DEBUG level hexdump message associated with the instance to the log.

        It’s meant to write developer oriented information.

        Parameters:
        :   - **\_log\_inst** – Pointer to the log structure associated with the instance.
            - **\_data** – Pointer to the data to be logged.
            - **\_length** – Length of data (in bytes).
            - **\_str** – Persistent, raw string.

    LOG\_MODULE\_REGISTER(...)
    :   Create module-specific state and register the module with Logger.

        This macro normally must be used after including <zephyr/logging/log.h> to complete the initialization of the module.

        Module registration can be skipped in two cases:

        - The module consists of more than one file, and another file invokes this macro. ([LOG\_MODULE\_DECLARE()](#group__log__api_1ga8193b0e10e5ee64b86848bb52be31869) should be used instead in all of the module’s other files.)
        - Instance logging is used and there is no need to create module entry. In that case [LOG\_LEVEL\_SET()](#group__log__api_1gac396852328a77360a0c27dbf7b52356e) should be used to set log level used within the file.

        Macro accepts one or two parameters:

        - module name
        - optional log level. If not provided then default log level is used in the file.

        Example usage:

        - [LOG\_MODULE\_REGISTER(foo, CONFIG\_FOO\_LOG\_LEVEL)](#group__log__api_1ga2404243df68fb6e51129d1c7ecc5ca45)
        - [LOG\_MODULE\_REGISTER(foo)](#group__log__api_1ga2404243df68fb6e51129d1c7ecc5ca45)

        See also

        [LOG\_MODULE\_DECLARE](#group__log__api_1ga8193b0e10e5ee64b86848bb52be31869)

        Note

        The module’s state is defined, and the module is registered, only if LOG\_LEVEL for the current source file is non-zero or it is not defined and CONFIG\_LOG\_DEFAULT\_LEVEL is non-zero. In other cases, this macro has no effect.

    LOG\_MODULE\_DECLARE(...)
    :   Macro for declaring a log module (not registering it).

        Modules which are split up over multiple files must have exactly one file use [LOG\_MODULE\_REGISTER()](#group__log__api_1ga2404243df68fb6e51129d1c7ecc5ca45) to create module-specific state and register the module with the logger core.

        The other files in the module should use this macro instead to declare that same state. (Otherwise, [LOG\_INF()](#group__log__api_1ga9c338f3170acf38a8532d1181d26704e) etc. will not be able to refer to module-specific state variables.)

        Macro accepts one or two parameters:

        - module name
        - optional log level. If not provided then default log level is used in the file.

        Example usage:

        - [LOG\_MODULE\_DECLARE(foo, CONFIG\_FOO\_LOG\_LEVEL)](#group__log__api_1ga8193b0e10e5ee64b86848bb52be31869)
        - [LOG\_MODULE\_DECLARE(foo)](#group__log__api_1ga8193b0e10e5ee64b86848bb52be31869)

        See also

        [LOG\_MODULE\_REGISTER](#group__log__api_1ga2404243df68fb6e51129d1c7ecc5ca45)

        Note

        The module’s state is declared only if LOG\_LEVEL for the current source file is non-zero or it is not defined and CONFIG\_LOG\_DEFAULT\_LEVEL is non-zero. In other cases, this macro has no effect.

    LOG\_LEVEL\_SET(level)
    :   Macro for setting log level in the file or function where instance logging API is used.

        Parameters:
        :   - **level** – Level used in file or in function.

### [Logger control](#id36)

Related code samples

[Logging](../../samples/subsys/logging/logger/README.md#logging "Output log messages to the console using the logging subsystem.")
:   Output log messages to the console using the logging subsystem.

[Remote syslog](../../samples/net/syslog_net/README.md#syslog-net "Enable a remote syslog service that sends syslog messages to a remote server")
:   Enable a remote syslog service that sends syslog messages to a remote server

*group* Logger control API
:   Logger control API.

    **Since**
    :   1.13

    Defines

    LOG\_CORE\_INIT()

    LOG\_INIT()

    LOG\_PANIC()

    LOG\_PROCESS()

    Typedefs

    typedef log\_timestamp\_t (\*log\_timestamp\_get\_t)(void)

    Functions

    void log\_core\_init(void)
    :   Function system initialization of the logger.

        Function is called during start up to allow logging before user can explicitly initialize the logger.

    void log\_init(void)
    :   Function for user initialization of the logger.

    void log\_thread\_trigger(void)
    :   Trigger the log processing thread to process logs immediately.

        Note

        Function has no effect when CONFIG\_LOG\_MODE\_IMMEDIATE is set.

    void log\_thread\_set(k\_tid\_t process\_tid)
    :   Function for providing thread which is processing logs.

        See CONFIG\_LOG\_PROCESS\_TRIGGER\_THRESHOLD.

        Note

        Function has asserts and has no effect when CONFIG\_LOG\_PROCESS\_THREAD is set.

        Parameters:
        :   - **process\_tid** – Process thread id. Used to wake up the thread.

    int log\_set\_timestamp\_func([log\_timestamp\_get\_t](#c.log_timestamp_get_t) timestamp\_getter, uint32\_t freq)
    :   Function for providing timestamp function.

        Parameters:
        :   - **timestamp\_getter** – Timestamp function.
            - **freq** – Timestamping frequency.

        Returns:
        :   0 on success or error.

    void log\_panic(void)
    :   Switch the logger subsystem to the panic mode.

        Returns immediately if the logger is already in the panic mode.

        On panic the logger subsystem informs all backends about panic mode. Backends must switch to blocking mode or halt. All pending logs are flushed after switching to panic mode. In panic mode, all log messages must be processed in the context of the call.

    bool log\_process(void)
    :   Process one pending log message.

        Return values:
        :   - **true** – There are more messages pending to be processed.
            - **false** – No messages pending.

    uint32\_t log\_buffered\_cnt(void)
    :   Return number of buffered log messages.

        Returns:
        :   Number of currently buffered log messages.

    uint32\_t log\_src\_cnt\_get(uint32\_t domain\_id)
    :   Get number of independent logger sources (modules and instances).

        Parameters:
        :   - **domain\_id** – Domain ID.

        Returns:
        :   Number of sources.

    const char \*log\_source\_name\_get(uint32\_t domain\_id, uint32\_t source\_id)
    :   Get name of the source (module or instance).

        Parameters:
        :   - **domain\_id** – Domain ID.
            - **source\_id** – Source ID.

        Returns:
        :   Source name or NULL if invalid arguments.

    static inline uint8\_t log\_domains\_count(void)
    :   Return number of domains present in the system.

        There will be at least one local domain.

        Returns:
        :   Number of domains.

    const char \*log\_domain\_name\_get(uint32\_t domain\_id)
    :   Get name of the domain.

        Parameters:
        :   - **domain\_id** – Domain ID.

        Returns:
        :   Domain name.

    int log\_source\_id\_get(const char \*name)
    :   Function for finding source ID based on source name.

        Parameters:
        :   - **name** – Source name

        Returns:
        :   Source ID or negative number when source ID is not found.

    uint32\_t log\_filter\_get(struct [log\_backend](#c.log_backend) const \*const backend, uint32\_t domain\_id, int16\_t source\_id, bool runtime)
    :   Get source filter for the provided backend.

        Parameters:
        :   - **backend** – Backend instance.
            - **domain\_id** – ID of the domain.
            - **source\_id** – Source (module or instance) ID.
            - **runtime** – True for runtime filter or false for compiled in.

        Returns:
        :   Severity level.

    uint32\_t log\_filter\_set(struct [log\_backend](#c.log_backend) const \*const backend, uint32\_t domain\_id, int16\_t source\_id, uint32\_t level)
    :   Set filter on given source for the provided backend.

        Parameters:
        :   - **backend** – Backend instance. NULL for all backends (and frontend).
            - **domain\_id** – ID of the domain.
            - **source\_id** – Source (module or instance) ID.
            - **level** – Severity level.

        Returns:
        :   Actual level set which may be limited by compiled level. If filter was set for all backends then maximal level that was set is returned.

    uint32\_t log\_frontend\_filter\_get(int16\_t source\_id, bool runtime)
    :   Get source filter for the frontend.

        Parameters:
        :   - **source\_id** – Source (module or instance) ID.
            - **runtime** – True for runtime filter or false for compiled in.

        Returns:
        :   Severity level.

    uint32\_t log\_frontend\_filter\_set(int16\_t source\_id, uint32\_t level)
    :   Set filter on given source for the frontend.

        Parameters:
        :   - **source\_id** – Source (module or instance) ID.
            - **level** – Severity level.

        Returns:
        :   Actual level set which may be limited by compiled level.

    void log\_backend\_enable(struct [log\_backend](#c.log_backend) const \*const backend, void \*ctx, uint32\_t level)
    :   Enable backend with initial maximum filtering level.

        Parameters:
        :   - **backend** – Backend instance.
            - **ctx** – User context.
            - **level** – Severity level.

    void log\_backend\_disable(struct [log\_backend](#c.log_backend) const \*const backend)
    :   Disable backend.

        Parameters:
        :   - **backend** – Backend instance.

    const struct [log\_backend](#c.log_backend) \*log\_backend\_get\_by\_name(const char \*backend\_name)
    :   Get backend by name.

        Parameters:
        :   - **backend\_name** – **[in]** Name of the backend as defined by the LOG\_BACKEND\_DEFINE.

        Return values:
        :   **Pointer** – to the backend instance if found, NULL if backend is not found.

    const struct [log\_backend](#c.log_backend) \*log\_format\_set\_all\_active\_backends(size\_t log\_type)
    :   Sets logging format for all active backends.

        Parameters:
        :   - **log\_type** – Log format.

        Return values:
        :   **Pointer** – to the last backend that failed, NULL for success.

    static inline bool log\_data\_pending(void)
    :   Check if there is pending data to be processed by the logging subsystem.

        Function can be used to determine if all logs have been flushed. Function returns false when deferred mode is not enabled.

        Return values:
        :   - **true** – There is pending data.
            - **false** – No pending data to process.

    int log\_set\_tag(const char \*tag)
    :   Configure tag used to prefix each message.

        Parameters:
        :   - **tag** – Tag.

        Return values:
        :   - **0** – on successful operation.
            - **-ENOTSUP** – if feature is disabled.
            - **-ENOMEM** – if string is longer than the buffer capacity. Tag will be trimmed.

    int log\_mem\_get\_usage(uint32\_t \*buf\_size, uint32\_t \*usage)
    :   Get current memory usage.

        Parameters:
        :   - **buf\_size** – **[out]** Capacity of the buffer used for storing log messages.
            - **usage** – **[out]** Number of bytes currently containing pending log messages.

        Return values:
        :   - **-EINVAL** – if logging mode does not use the buffer.
            - **0** – successfully collected usage data.

    int log\_mem\_get\_max\_usage(uint32\_t \*max)
    :   Get maximum memory usage.

        Requires CONFIG\_LOG\_MEM\_UTILIZATION option.

        Parameters:
        :   - **max** – **[out]** Maximum number of bytes used for pending log messages.

        Return values:
        :   - **-EINVAL** – if logging mode does not use the buffer.
            - **-ENOTSUP** – if instrumentation is not enabled. not been enabled.
            - **0** – successfully collected usage data.

### [Log message](#id37)

*group* Log message API
:   Log message API.

    Defines

    LOG\_MSG\_GENERIC\_HDR

    LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK(...)

    LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_0(fmt)

    LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_1(fmt, arg)

    LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_2(fmt, arg0, arg1)

    LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK(...)
    :   brief Determine if string arguments types allow to use simplified message creation mode.

        Parameters:
        :   - **...** – String with arguments.

    LOG\_MSG\_SIMPLE\_CHECK(...)
    :   Check if message can be handled using simplified method.

        Following conditions must be met:

        - 32 bit platform
        - Number of arguments from 0 to 2
        - Type of an argument must be a numeric value that fits in 32 bit word.

        Parameters:
        :   - **...** – String with arguments.

        Return values:
        :   - **1** – if message qualifies.
            - **0** – if message does not qualify.

    LOG\_MSG\_SIMPLE\_FUNC(\_source, \_level, ...)
    :   Call specific function to create a log message.

        Macro picks matching function (based on number of arguments) and calls it. String arguments are casted to uint32\_t.

        Parameters:
        :   - **\_source** – Source.
            - **\_level** – Severity level.
            - **...** – String with arguments.

    Functions

    static inline uint32\_t log\_msg\_get\_total\_wlen(const struct [log\_msg\_desc](#c.log_msg_desc) desc)
    :   Get total length (in 32 bit words) of a log message.

        Parameters:
        :   - **desc** – Log message descriptor.

        Returns:
        :   Length.

    static inline uint32\_t log\_msg\_generic\_get\_wlen(const union mpsc\_pbuf\_generic \*item)
    :   Get length of the log item.

        Parameters:
        :   - **item** – Item.

        Returns:
        :   Length in 32 bit words.

    static inline uint8\_t log\_msg\_get\_domain(struct [log\_msg](#c.log_msg) \*msg)
    :   Get log message domain ID.

        Parameters:
        :   - **msg** – Log message.

        Returns:
        :   Domain ID

    static inline uint8\_t log\_msg\_get\_level(struct [log\_msg](#c.log_msg) \*msg)
    :   Get log message level.

        Parameters:
        :   - **msg** – Log message.

        Returns:
        :   Log level.

    static inline const void \*log\_msg\_get\_source(struct [log\_msg](#c.log_msg) \*msg)
    :   Get message source data.

        Parameters:
        :   - **msg** – Log message.

        Returns:
        :   Pointer to the source data.

    int16\_t log\_msg\_get\_source\_id(struct [log\_msg](#c.log_msg) \*msg)
    :   Get log message source ID.

        Parameters:
        :   - **msg** – Log message.

        Returns:
        :   Source ID, or -1 if not available.

    static inline log\_timestamp\_t log\_msg\_get\_timestamp(struct [log\_msg](#c.log_msg) \*msg)
    :   Get timestamp.

        Parameters:
        :   - **msg** – Log message.

        Returns:
        :   Timestamp.

    static inline void \*log\_msg\_get\_tid(struct [log\_msg](#c.log_msg) \*msg)
    :   Get Thread ID.

        Parameters:
        :   - **msg** – Log message.

        Returns:
        :   Thread ID.

    static inline uint8\_t \*log\_msg\_get\_data(struct [log\_msg](#c.log_msg) \*msg, size\_t \*len)
    :   Get data buffer.

        Parameters:
        :   - **msg** – log message.
            - **len** – location where data length is written.

        Returns:
        :   pointer to the data buffer.

    static inline uint8\_t \*log\_msg\_get\_package(struct [log\_msg](#c.log_msg) \*msg, size\_t \*len)
    :   Get string package.

        Parameters:
        :   - **msg** – log message.
            - **len** – location where string package length is written.

        Returns:
        :   pointer to the package.

    struct log\_msg\_desc
    :   *#include <log\_msg.h>*

    union log\_msg\_source
    :   *#include <log\_msg.h>*

        Public Members

        const struct log\_source\_const\_data \*fixed

        struct log\_source\_dynamic\_data \*dynamic

        void \*raw

    struct log\_msg\_hdr
    :   *#include <log\_msg.h>*

    struct log\_msg
    :   *#include <log\_msg.h>*

    struct log\_msg\_generic\_hdr
    :   *#include <log\_msg.h>*

    union log\_msg\_generic
    :   *#include <log\_msg.h>*

        Public Members

        union mpsc\_pbuf\_generic buf

        struct [log\_msg\_generic\_hdr](#c.log_msg_generic_hdr) generic

        struct [log\_msg](#c.log_msg) log

### [Logger backend interface](#id38)

Related code samples

[BLE logging backend](../../samples/subsys/logging/ble_backend/README.md#logging-ble-backend "Send log messages over BLE using the BLE logging backend.")
:   Send log messages over BLE using the BLE logging backend.

[Remote syslog](../../samples/net/syslog_net/README.md#syslog-net "Enable a remote syslog service that sends syslog messages to a remote server")
:   Enable a remote syslog service that sends syslog messages to a remote server

*group* Logger backend interface
:   Logger backend interface.

    Defines

    LOG\_BACKEND\_DEFINE(\_name, \_api, \_autostart, ...)
    :   Macro for creating a logger backend instance.

        Parameters:
        :   - **\_name** – Name of the backend instance.
            - **\_api** – Logger backend API.
            - **\_autostart** – If true backend is initialized and activated together with the logger subsystem.
            - **...** – Optional context.

    Enums

    enum log\_backend\_evt
    :   Backend events.

        *Values:*

        enumerator LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE
        :   Event when process thread finishes processing.

            This event is emitted when the process thread finishes processing pending log messages.

            Note

            This is not emitted when there are no pending log messages being processed.

            Note

            Deferred mode only.

        enumerator LOG\_BACKEND\_EVT\_MAX
        :   Maximum number of backend events.

    Functions

    static inline void log\_backend\_init(const struct [log\_backend](#c.log_backend) \*const backend)
    :   Initialize or initiate the logging backend.

        If backend initialization takes longer time it could block logging thread if backend is autostarted. That is because all backends are initialized in the context of the logging thread. In that case, backend shall provide function for polling for readiness ([log\_backend\_is\_ready](#group__log__backend_1gaf57e7a27a1337815338410db93603e0b)).

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.

    static inline int log\_backend\_is\_ready(const struct [log\_backend](#c.log_backend) \*const backend)
    :   Poll for backend readiness.

        If backend is ready immediately after initialization then backend may not provide this function.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.

        Return values:
        :   - **0** – if backend is ready.
            - **-EBUSY** – if backend is not yet ready.

    static inline void log\_backend\_msg\_process(const struct [log\_backend](#c.log_backend) \*const backend, union [log\_msg\_generic](#c.log_msg_generic) \*msg)
    :   Process message.

        Function is used in deferred and immediate mode. On return, message content is processed by the backend and memory can be freed.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.
            - **msg** – **[in]** Pointer to message with log entry.

    static inline void log\_backend\_dropped(const struct [log\_backend](#c.log_backend) \*const backend, uint32\_t cnt)
    :   Notify backend about dropped log messages.

        Function is optional.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.
            - **cnt** – **[in]** Number of dropped logs since last notification.

    static inline void log\_backend\_panic(const struct [log\_backend](#c.log_backend) \*const backend)
    :   Reconfigure backend to panic mode.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.

    static inline void log\_backend\_id\_set(const struct [log\_backend](#c.log_backend) \*const backend, uint8\_t id)
    :   Set backend id.

        Note

        It is used internally by the logger.

        Parameters:
        :   - **backend** – Pointer to the backend instance.
            - **id** – ID.

    static inline uint8\_t log\_backend\_id\_get(const struct [log\_backend](#c.log_backend) \*const backend)
    :   Get backend id.

        Note

        It is used internally by the logger.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.

        Returns:
        :   Id.

    static inline const struct [log\_backend](#c.log_backend) \*log\_backend\_get(uint32\_t idx)
    :   Get backend.

        Parameters:
        :   - **idx** – **[in]** Pointer to the backend instance.

        Returns:
        :   Pointer to the backend instance.

    static inline int log\_backend\_count\_get(void)
    :   Get number of backends.

        Returns:
        :   Number of backends.

    static inline void log\_backend\_activate(const struct [log\_backend](#c.log_backend) \*const backend, void \*ctx)
    :   Activate backend.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.
            - **ctx** – **[in]** User context.

    static inline void log\_backend\_deactivate(const struct [log\_backend](#c.log_backend) \*const backend)
    :   Deactivate backend.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.

    static inline bool log\_backend\_is\_active(const struct [log\_backend](#c.log_backend) \*const backend)
    :   Check state of the backend.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend instance.

        Returns:
        :   True if backend is active, false otherwise.

    static inline int log\_backend\_format\_set(const struct [log\_backend](#c.log_backend) \*backend, uint32\_t log\_type)
    :   Set logging format.

        Parameters:
        :   - **backend** – Pointer to the backend instance.
            - **log\_type** – Log format.

        Return values:
        :   - **-ENOTSUP** – If the backend does not support changing format types.
            - **-EINVAL** – If the input is invalid.
            - **0** – for success.

    static inline void log\_backend\_notify(const struct [log\_backend](#c.log_backend) \*const backend, enum [log\_backend\_evt](#c.log_backend_evt) event, union [log\_backend\_evt\_arg](#c.log_backend_evt_arg) \*arg)
    :   Notify a backend of an event.

        Parameters:
        :   - **backend** – Pointer to the backend instance.
            - **event** – Event to be notified.
            - **arg** – Pointer to the argument(s).

    union log\_backend\_evt\_arg
    :   *#include <log\_backend.h>*

        Argument(s) for backend events.

        Public Members

        void \*raw
        :   Unspecified argument(s).

    struct log\_backend\_api
    :   *#include <log\_backend.h>*

        Logger backend API.

    struct log\_backend\_control\_block
    :   *#include <log\_backend.h>*

        Logger backend control block.

    struct log\_backend
    :   *#include <log\_backend.h>*

        Logger backend structure.

### [Logger output formatting](#id39)

*group* Log output API
:   Log output API.

    Unnamed Group

    void log\_custom\_output\_msg\_process(const struct [log\_output](#c.log_custom_output_msg_process) \*log\_output, struct [log\_msg](#c.log_msg) \*msg, uint32\_t flags)
    :   Custom logging output formatting.

        Process log messages from an external output function set with log\_custom\_output\_msg\_set

        Function is using provided context with the buffer and output function to process formatted string and output the data.

        Parameters:
        :   - **log\_output** – Pointer to the log output instance.
            - **msg** – Log message.
            - **flags** – Optional flags.

    Defines

    LOG\_OUTPUT\_TEXT
    :   Supported backend logging format types for use with log\_format\_set() API to switch log format at runtime.

    LOG\_OUTPUT\_SYST

    LOG\_OUTPUT\_DICT

    LOG\_OUTPUT\_CUSTOM

    LOG\_OUTPUT\_DEFINE(\_name, \_func, \_buf, \_size)
    :   Create [log\_output](#structlog__output) instance.

        Parameters:
        :   - **\_name** – Instance name.
            - **\_func** – Function for processing output data.
            - **\_buf** – Pointer to the output buffer.
            - **\_size** – Size of the output buffer.

    Typedefs

    typedef int (\*log\_output\_func\_t)(uint8\_t \*buf, size\_t size, void \*ctx)
    :   Prototype of the function processing output data.

        Note

        If the log output function cannot process all of the data, it is its responsibility to mark them as dropped or discarded by returning the corresponding number of bytes dropped or discarded to the caller.

        Param buf:
        :   The buffer data.

        Param size:
        :   The buffer size.

        Param ctx:
        :   User context.

        Return:
        :   Number of bytes processed, dropped or discarded.

    typedef void (\*log\_format\_func\_t)(const struct [log\_output](#c.log_output) \*output, struct [log\_msg](#c.log_msg) \*msg, uint32\_t flags)
    :   Typedef of the function pointer table “format\_table”.

        Param output:
        :   Pointer to [log\_output](#structlog__output) struct.

        Param msg:
        :   Pointer to [log\_msg](#structlog__msg) struct.

        Param flags:
        :   Flags used for text formatting options.

        Return:
        :   Function pointer based on Kconfigs defined for backends.

    Functions

    [log\_format\_func\_t](#c.log_format_func_t) log\_format\_func\_t\_get(uint32\_t log\_type)
    :   Declaration of the get routine for function pointer table format\_table.

    void log\_output\_msg\_process(const struct [log\_output](#c.log_output_msg_process) \*log\_output, struct [log\_msg](#c.log_msg) \*msg, uint32\_t flags)
    :   Process log messages v2 to readable strings.

        Function is using provided context with the buffer and output function to process formatted string and output the data.

        Parameters:
        :   - **log\_output** – Pointer to the log output instance.
            - **msg** – Log message.
            - **flags** – Optional flags. See Log output formatting flags..

    void log\_output\_process(const struct [log\_output](#c.log_output_process) \*log\_output, log\_timestamp\_t timestamp, const char \*domain, const char \*source, k\_tid\_t tid, uint8\_t level, const uint8\_t \*package, const uint8\_t \*data, size\_t data\_len, uint32\_t flags)
    :   Process input data to a readable string.

        Parameters:
        :   - **log\_output** – Pointer to the log output instance.
            - **timestamp** – Timestamp.
            - **domain** – Domain name string. Can be NULL.
            - **source** – Source name string. Can be NULL.
            - **tid** – Thread ID.
            - **level** – Criticality level.
            - **package** – Cbprintf package with a logging message string.
            - **data** – Data passed to hexdump API. Can be NULL.
            - **data\_len** – Data length.
            - **flags** – Formatting flags. See Log output formatting flags..

    void log\_output\_msg\_syst\_process(const struct [log\_output](#c.log_output_msg_syst_process) \*log\_output, struct [log\_msg](#c.log_msg) \*msg, uint32\_t flags)
    :   Process log messages v2 to SYS-T format.

        Function is using provided context with the buffer and output function to process formatted string and output the data in sys-t log output format.

        Parameters:
        :   - **log\_output** – Pointer to the log output instance.
            - **msg** – Log message.
            - **flags** – Optional flags. See Log output formatting flags..

    void log\_output\_dropped\_process(const struct [log\_output](#c.log_output) \*output, uint32\_t cnt)
    :   Process dropped messages indication.

        Function prints error message indicating lost log messages.

        Parameters:
        :   - **output** – Pointer to the log output instance.
            - **cnt** – Number of dropped messages.

    void log\_output\_flush(const struct [log\_output](#c.log_output) \*output)
    :   Flush output buffer.

        Parameters:
        :   - **output** – Pointer to the log output instance.

    static inline void log\_output\_ctx\_set(const struct [log\_output](#c.log_output) \*output, void \*ctx)
    :   Function for setting user context passed to the output function.

        Parameters:
        :   - **output** – Pointer to the log output instance.
            - **ctx** – User context.

    static inline void log\_output\_hostname\_set(const struct [log\_output](#c.log_output) \*output, const char \*hostname)
    :   Function for setting hostname of this device.

        Parameters:
        :   - **output** – Pointer to the log output instance.
            - **hostname** – Hostname of this device

    void log\_output\_timestamp\_freq\_set(uint32\_t freq)
    :   Set timestamp frequency.

        Parameters:
        :   - **freq** – Frequency in Hz.

    uint64\_t log\_output\_timestamp\_to\_us(log\_timestamp\_t timestamp)
    :   Convert timestamp of the message to us.

        Parameters:
        :   - **timestamp** – Message timestamp

        Returns:
        :   Timestamp value in us.

    struct log\_output\_control\_block
    :   *#include <log\_output.h>*

    struct log\_output
    :   *#include <log\_output.h>*

        Log\_output instance structure.
