---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/portability/posix/option_groups/index.html
original_path: services/portability/posix/option_groups/index.html
---

# POSIX Option and Option Group Details

## POSIX Option Groups

### POSIX\_BARRIERS

Enable this option group with [`CONFIG_POSIX_BARRIERS`](../../../../kconfig.md#CONFIG_POSIX_BARRIERS "CONFIG_POSIX_BARRIERS").

POSIX\_BARRIERS

| API | Supported |
| --- | --- |
| pthread\_barrier\_destroy() | yes |
| pthread\_barrier\_init() | yes |
| pthread\_barrier\_wait() | yes |
| pthread\_barrierattr\_destroy() | yes |
| pthread\_barrierattr\_init() | yes |

### POSIX\_C\_LANG\_JUMP

The `POSIX_C_LANG_JUMP` Option Group is included in the ISO C standard.

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the
`POSIX_C_LANG_JUMP` Option Group is considered supported.

POSIX\_C\_LANG\_JUMP

| API | Supported |
| --- | --- |
| setjmp() | yes |
| longjmp() | yes |

### POSIX\_C\_LANG\_MATH

The `POSIX_C_LANG_MATH` Option Group is included in the ISO C standard.

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the
`POSIX_C_LANG_MATH` Option Group is considered supported.

Please refer to [Subprofiling Considerations](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html) for details on the `POSIX_C_LANG_MATH` Option
Group.

### POSIX\_C\_LANG\_SUPPORT

The POSIX\_C\_LANG\_SUPPORT option group contains the general ISO C Library.

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the entire
`POSIX_C_LANG_SUPPORT` Option Group is considered supported.

Please refer to [Subprofiling Considerations](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html) for details on the `POSIX_C_LANG_SUPPORT` Option
Group.

For more information on developing Zephyr applications in the C programming language, please refer
to [details](../../../../develop/languages/index.md#language-support).

### POSIX\_C\_LIB\_EXT

Enable this option group with [`CONFIG_POSIX_C_LIB_EXT`](../../../../kconfig.md#CONFIG_POSIX_C_LIB_EXT "CONFIG_POSIX_C_LIB_EXT").

POSIX\_C\_LIB\_EXT

| API | Supported |
| --- | --- |
| fnmatch() | yes |
| getopt() | yes |
| getsubopt() |  |
| optarg | yes |
| opterr | yes |
| optind | yes |
| optopt | yes |
| stpcpy() |  |
| stpncpy() |  |
| strcasecmp() |  |
| strdup() |  |
| strfmon() |  |
| strncasecmp() | yes |
| strndup() |  |
| strnlen() | yes |

### POSIX\_CLOCK\_SELECTION

Enable this option group with [`CONFIG_POSIX_CLOCK_SELECTION`](../../../../kconfig.md#CONFIG_POSIX_CLOCK_SELECTION "CONFIG_POSIX_CLOCK_SELECTION").

POSIX\_CLOCK\_SELECTION

| API | Supported |
| --- | --- |
| pthread\_condattr\_getclock() | yes |
| pthread\_condattr\_setclock() | yes |
| clock\_nanosleep() | yes |

### POSIX\_DEVICE\_IO

Enable this option group with [`CONFIG_POSIX_DEVICE_IO`](../../../../kconfig.md#CONFIG_POSIX_DEVICE_IO "CONFIG_POSIX_DEVICE_IO").

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the
C89 components of the `POSIX_DEVICE_IO` Option Group are considered supported.

POSIX\_DEVICE\_IO

| API | Supported |
| --- | --- |
| FD\_CLR() | yes |
| FD\_ISSET() | yes |
| FD\_SET() | yes |
| FD\_ZERO() | yes |
| clearerr() | yes |
| close() | yes |
| fclose() | yes |
| fdopen() | yes |
| feof() | yes |
| ferror() | yes |
| fflush() | yes |
| fgetc() | yes |
| fgets() | yes |
| fileno() | yes |
| fopen() | yes |
| fprintf() | yes |
| fputc() | yes |
| fputs() | yes |
| fread() | yes |
| freopen() | yes |
| fscanf() | yes |
| fwrite() | yes |
| getc() | yes |
| getchar() | yes |
| gets() | yes |
| open() | yes |
| perror() | yes |
| poll() | yes |
| printf() | yes |
| pread() | yes |
| pselect() | yes |
| putc() | yes |
| putchar() | yes |
| puts() | yes |
| pwrite() | yes |
| read() | yes |
| scanf() | yes |
| select() | yes |
| setbuf() | yes |
| setvbuf() | yes |
| stderr | yes |
| stdin | yes |
| stdout | yes |
| ungetc() | yes |
| vfprintf() | yes |
| vfscanf() | yes |
| vprintf() | yes |
| vscanf() | yes |
| write() | yes |

### POSIX\_FD\_MGMT

Enable this option group with [`CONFIG_POSIX_FD_MGMT`](../../../../kconfig.md#CONFIG_POSIX_FD_MGMT "CONFIG_POSIX_FD_MGMT").

POSIX\_FD\_MGMT

| API | Supported |
| --- | --- |
| dup() |  |
| dup2() |  |
| fcntl() |  |
| fgetpos() |  |
| fseek() |  |
| fseeko() |  |
| fsetpos() |  |
| ftell() |  |
| ftello() |  |
| ftruncate() | yes |
| lseek() |  |
| rewind() |  |

### POSIX\_FILE\_LOCKING

POSIX\_FILE\_LOCKING

| API | Supported |
| --- | --- |
| flockfile() |  |
| ftrylockfile() |  |
| funlockfile() |  |
| getc\_unlocked() |  |
| getchar\_unlocked() |  |
| putc\_unlocked() |  |
| putchar\_unlocked() |  |

### POSIX\_FILE\_SYSTEM

Enable this option group with [`CONFIG_POSIX_FILE_SYSTEM`](../../../../kconfig.md#CONFIG_POSIX_FILE_SYSTEM "CONFIG_POSIX_FILE_SYSTEM").

POSIX\_FILE\_SYSTEM

| API | Supported |
| --- | --- |
| access() |  |
| chdir() |  |
| closedir() | yes |
| creat() |  |
| fchdir() |  |
| fpathconf() |  |
| fstat() | yes |
| fstatvfs() |  |
| getcwd() |  |
| link() |  |
| mkdir() | yes |
| mkstemp() |  |
| opendir() | yes |
| pathconf() |  |
| readdir() | yes |
| remove() | yes |
| rename() | yes |
| rewinddir() |  |
| rmdir() | yes |
| stat() | yes |
| statvfs() |  |
| tmpfile() |  |
| tmpnam() |  |
| truncate() |  |
| unlink() | yes |
| utime() |  |

### POSIX\_MAPPED\_FILES

Enable this option group with [`CONFIG_POSIX_MAPPED_FILES`](../../../../kconfig.md#CONFIG_POSIX_MAPPED_FILES "CONFIG_POSIX_MAPPED_FILES").

POSIX\_MAPPED\_FILES

| API | Supported |
| --- | --- |
| mmap() | yes |
| msync() | yes |
| munmap() | yes |

### POSIX\_MEMORY\_PROTECTION

Enable this option group with [`CONFIG_POSIX_MEMORY_PROTECTION`](../../../../kconfig.md#CONFIG_POSIX_MEMORY_PROTECTION "CONFIG_POSIX_MEMORY_PROTECTION").

POSIX\_MEMORY\_PROTECTION

| API | Supported |
| --- | --- |
| mprotect() | yes [†](../conformance/index.md#posix-undefined-behaviour) |

### POSIX\_MULTI\_PROCESS

Enable this option group with [`CONFIG_POSIX_MULTI_PROCESS`](../../../../kconfig.md#CONFIG_POSIX_MULTI_PROCESS "CONFIG_POSIX_MULTI_PROCESS").

POSIX\_MULTI\_PROCESS

| API | Supported |
| --- | --- |
| \_Exit() | yes |
| \_exit() | yes |
| assert() | yes |
| atexit() | [†](../conformance/index.md#posix-undefined-behaviour) |
| clock() |  |
| execl() | [†](../conformance/index.md#posix-undefined-behaviour) |
| execle() | [†](../conformance/index.md#posix-undefined-behaviour) |
| execlp() | [†](../conformance/index.md#posix-undefined-behaviour) |
| execv() | [†](../conformance/index.md#posix-undefined-behaviour) |
| execve() | [†](../conformance/index.md#posix-undefined-behaviour) |
| execvp() | [†](../conformance/index.md#posix-undefined-behaviour) |
| exit() | yes |
| fork() | [†](../conformance/index.md#posix-undefined-behaviour) |
| getpgrp() | [†](../conformance/index.md#posix-undefined-behaviour) |
| getpgid() | [†](../conformance/index.md#posix-undefined-behaviour) |
| getpid() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| getppid() | [†](../conformance/index.md#posix-undefined-behaviour) |
| getsid() | [†](../conformance/index.md#posix-undefined-behaviour) |
| setsid() | [†](../conformance/index.md#posix-undefined-behaviour) |
| sleep() | yes |
| times() |  |
| wait() | [†](../conformance/index.md#posix-undefined-behaviour) |
| waitid() | [†](../conformance/index.md#posix-undefined-behaviour) |
| waitpid() | [†](../conformance/index.md#posix-undefined-behaviour) |

### POSIX\_NETWORKING

The function `sockatmark()` is not yet supported and is expected to fail setting `errno`
to `ENOSYS` [†](../conformance/index.md#posix-undefined-behaviour).

Enable this option group with [`CONFIG_POSIX_NETWORKING`](../../../../kconfig.md#CONFIG_POSIX_NETWORKING "CONFIG_POSIX_NETWORKING").

POSIX\_NETWORKING

| API | Supported |
| --- | --- |
| accept() | yes |
| bind() | yes |
| connect() | yes |
| endhostent() | yes |
| endnetent() | yes |
| endprotoent() | yes |
| endservent() | yes |
| freeaddrinfo() | yes |
| gai\_strerror() | yes |
| getaddrinfo() | yes |
| gethostent() | yes |
| gethostname() | yes |
| getnameinfo() | yes |
| getnetbyaddr() | yes |
| getnetbyname() | yes |
| getnetent() | yes |
| getpeername() | yes |
| getprotobyname() | yes |
| getprotobynumber() | yes |
| getprotoent() | yes |
| getservbyname() | yes |
| getservbyport() | yes |
| getservent() | yes |
| getsockname() | yes |
| getsockopt() | yes |
| htonl() | yes |
| htons() | yes |
| if\_freenameindex() | yes |
| if\_indextoname() | yes |
| if\_nameindex() | yes |
| if\_nametoindex() | yes |
| inet\_addr() | yes |
| inet\_ntoa() | yes |
| inet\_ntop() | yes |
| inet\_pton() | yes |
| listen() | yes |
| ntohl() | yes |
| ntohs() | yes |
| recv() | yes |
| recvfrom() | yes |
| recvmsg() | yes |
| send() | yes |
| sendmsg() | yes |
| sendto() | yes |
| sethostent() | yes |
| setnetent() | yes |
| setprotoent() | yes |
| setservent() | yes |
| setsockopt() | yes |
| shutdown() | yes |
| socket() | yes |
| sockatmark() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| socketpair() | yes |

### POSIX\_PIPE

POSIX\_PIPE

| API | Supported |
| --- | --- |
| pipe() |  |

### POSIX\_REALTIME\_SIGNALS

Enable this option group with [`CONFIG_POSIX_REALTIME_SIGNALS`](../../../../kconfig.md#CONFIG_POSIX_REALTIME_SIGNALS "CONFIG_POSIX_REALTIME_SIGNALS").

POSIX\_REALTIME\_SIGNALS

| API | Supported |
| --- | --- |
| sigqueue() |  |
| sigtimedwait() |  |
| sigwaitinfo() |  |

### POSIX\_SEMAPHORES

Enable this option group with [`CONFIG_POSIX_SEMAPHORES`](../../../../kconfig.md#CONFIG_POSIX_SEMAPHORES "CONFIG_POSIX_SEMAPHORES").

POSIX\_SEMAPHORES

| API | Supported |
| --- | --- |
| sem\_close() | yes |
| sem\_destroy() | yes |
| sem\_getvalue() | yes |
| sem\_init() | yes |
| sem\_open() | yes |
| sem\_post() | yes |
| sem\_trywait() | yes |
| sem\_unlink() | yes |
| sem\_wait() | yes |

### POSIX\_SIGNAL\_JUMP

POSIX\_SIGNAL\_JUMP

| API | Supported |
| --- | --- |
| siglongjmp() |  |
| sigsetjmp() |  |

### POSIX\_SIGNALS

Enable this option group with [`CONFIG_POSIX_SIGNALS`](../../../../kconfig.md#CONFIG_POSIX_SIGNALS "CONFIG_POSIX_SIGNALS").

Note

As processes are not yet supported in Zephyr, the ISO C functions `abort()`, `signal()`,
and `raise()`, as well as the other POSIX functions listed below, may exhibit undefined
behaviour. The POSIX functions `kill()`, `pause()`, `sigaction()`, `sigpending()`,
`sigsuspend()`, and `sigwait()` are implemented to ensure that conformant applications can
link, but they are expected to fail, setting errno to `ENOSYS`
[†](../conformance/index.md#posix-undefined-behaviour).

POSIX\_SIGNALS

| API | Supported |
| --- | --- |
| abort() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| alarm() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| kill() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| pause() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| raise() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sigaction() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sigaddset() | yes |
| sigdelset() | yes |
| sigemptyset() | yes |
| sigfillset() | yes |
| sigismember() | yes |
| signal() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sigpending() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sigprocmask() | yes |
| sigsuspend() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sigwait() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| strsignal() | yes |

### POSIX\_SINGLE\_PROCESS

The POSIX\_SINGLE\_PROCESS option group contains services for single
process applications.

Enable this option group with [`CONFIG_POSIX_SINGLE_PROCESS`](../../../../kconfig.md#CONFIG_POSIX_SINGLE_PROCESS "CONFIG_POSIX_SINGLE_PROCESS").

POSIX\_SINGLE\_PROCESS

| API | Supported |
| --- | --- |
| confstr() | yes |
| environ | yes |
| errno | yes |
| getenv() | yes |
| setenv() | yes |
| sysconf() | yes |
| uname() | yes |
| unsetenv() | yes |

### POSIX\_SPIN\_LOCKS

Enable this option group with [`CONFIG_POSIX_SPIN_LOCKS`](../../../../kconfig.md#CONFIG_POSIX_SPIN_LOCKS "CONFIG_POSIX_SPIN_LOCKS").

POSIX\_SPIN\_LOCKS

| API | Supported |
| --- | --- |
| pthread\_spin\_destroy() | yes |
| pthread\_spin\_init() | yes |
| pthread\_spin\_lock() | yes |
| pthread\_spin\_trylock() | yes |
| pthread\_spin\_unlock() | yes |

### POSIX\_THREADS\_BASE

The basic assumption in this profile is that the system
consists of a single (implicit) process with multiple threads. Therefore, the
standard requires all basic thread services, except those related to
multiple processes.

Enable this option group with [`CONFIG_POSIX_THREADS`](../../../../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS").

POSIX\_THREADS\_BASE

| API | Supported |
| --- | --- |
| pthread\_atfork() | yes |
| pthread\_attr\_destroy() | yes |
| pthread\_attr\_getdetachstate() | yes |
| pthread\_attr\_getschedparam() | yes |
| pthread\_attr\_init() | yes |
| pthread\_attr\_setdetachstate() | yes |
| pthread\_attr\_setschedparam() | yes |
| pthread\_barrier\_destroy() | yes |
| pthread\_barrier\_init() | yes |
| pthread\_barrier\_wait() | yes |
| pthread\_barrierattr\_destroy() | yes |
| pthread\_barrierattr\_getpshared() | yes |
| pthread\_barrierattr\_init() | yes |
| pthread\_barrierattr\_setpshared() | yes |
| pthread\_cancel() | yes |
| pthread\_cleanup\_pop() | yes |
| pthread\_cleanup\_push() | yes |
| pthread\_cond\_broadcast() | yes |
| pthread\_cond\_destroy() | yes |
| pthread\_cond\_init() | yes |
| pthread\_cond\_signal() | yes |
| pthread\_cond\_timedwait() | yes |
| pthread\_cond\_wait() | yes |
| pthread\_condattr\_destroy() | yes |
| pthread\_condattr\_init() | yes |
| pthread\_create() | yes |
| pthread\_detach() | yes |
| pthread\_equal() | yes |
| pthread\_exit() | yes |
| pthread\_getspecific() | yes |
| pthread\_join() | yes |
| pthread\_key\_create() | yes |
| pthread\_key\_delete() | yes |
| pthread\_kill() |  |
| pthread\_mutex\_destroy() | yes |
| pthread\_mutex\_init() | yes |
| pthread\_mutex\_lock() | yes |
| pthread\_mutex\_trylock() | yes |
| pthread\_mutex\_unlock() | yes |
| pthread\_mutexattr\_destroy() | yes |
| pthread\_mutexattr\_init() | yes |
| pthread\_once() | yes |
| pthread\_self() | yes |
| pthread\_setcancelstate() | yes |
| pthread\_setcanceltype() | yes |
| pthread\_setspecific() | yes |
| pthread\_sigmask() | yes |
| pthread\_testcancel() | yes |

### POSIX\_THREADS\_EXT

Enable this option group with [`CONFIG_POSIX_THREADS_EXT`](../../../../kconfig.md#CONFIG_POSIX_THREADS_EXT "CONFIG_POSIX_THREADS_EXT").

POSIX\_THREADS\_EXT

| API | Supported |
| --- | --- |
| pthread\_attr\_getguardsize() | yes |
| pthread\_attr\_setguardsize() | yes |
| pthread\_mutexattr\_gettype() | yes |
| pthread\_mutexattr\_settype() | yes |

### POSIX\_TIMERS

Enable this option group with [`CONFIG_POSIX_TIMERS`](../../../../kconfig.md#CONFIG_POSIX_TIMERS "CONFIG_POSIX_TIMERS").

POSIX\_TIMERS

| API | Supported |
| --- | --- |
| clock\_getres() | yes |
| clock\_gettime() | yes |
| clock\_settime() | yes |
| nanosleep() | yes |
| timer\_create() | yes |
| timer\_delete() | yes |
| timer\_gettime() | yes |
| timer\_getoverrun() | yes |
| timer\_settime() | yes |

### XSI\_SYSTEM\_LOGGING

Enable this option group with [`CONFIG_XSI_SYSTEM_LOGGING`](../../../../kconfig.md#CONFIG_XSI_SYSTEM_LOGGING "CONFIG_XSI_SYSTEM_LOGGING").

XSI\_SYSTEM\_LOGGING

| API | Supported |
| --- | --- |
| closelog() | yes |
| openlog() | yes |
| setlogmask() | yes |
| syslog() | yes |

### XSI\_THREADS\_EXT

The XSI\_THREADS\_EXT option group is required because it provides
functions to control a thread’s stack. This is considered useful for any
real-time application.

Enable this option group with [`CONFIG_XSI_THREADS_EXT`](../../../../kconfig.md#CONFIG_XSI_THREADS_EXT "CONFIG_XSI_THREADS_EXT").

XSI\_THREADS\_EXT

| API | Supported |
| --- | --- |
| pthread\_attr\_getstack() | yes |
| pthread\_attr\_setstack() | yes |
| pthread\_getconcurrency() | yes |
| pthread\_setconcurrency() | yes |

## POSIX Options

### \_POSIX\_ASYNCHRONOUS\_IO

Functions part of the `_POSIX_ASYNCHRONOUS_IO` Option are not implemented in Zephyr but are
provided so that conformant applications can still link. These functions will fail, setting
`errno` to `ENOSYS`[†](../conformance/index.md#posix-undefined-behaviour).

Enable this option with [`CONFIG_POSIX_ASYNCHRONOUS_IO`](../../../../kconfig.md#CONFIG_POSIX_ASYNCHRONOUS_IO "CONFIG_POSIX_ASYNCHRONOUS_IO").

\_POSIX\_ASYNCHRONOUS\_IO

| API | Supported |
| --- | --- |
| aio\_cancel() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| aio\_error() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| aio\_fsync() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| aio\_read() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| aio\_return() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| aio\_suspend() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| aio\_write() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| lio\_listio() | yes [†](../conformance/index.md#posix-undefined-behaviour) |

### \_POSIX\_CPUTIME

Enable this option with [`CONFIG_POSIX_CPUTIME`](../../../../kconfig.md#CONFIG_POSIX_CPUTIME "CONFIG_POSIX_CPUTIME").

\_POSIX\_CPUTIME

| API | Supported |
| --- | --- |
| CLOCK\_PROCESS\_CPUTIME\_ID | yes |

### \_POSIX\_FSYNC

Enable this option with [`CONFIG_POSIX_FSYNC`](../../../../kconfig.md#CONFIG_POSIX_FSYNC "CONFIG_POSIX_FSYNC").

\_POSIX\_FSYNC

| API | Supported |
| --- | --- |
| fsync() | yes |

### \_POSIX\_IPV6

Internet Protocol Version 6 is supported.

For more information, please refer to [Networking](../../../../connectivity/networking/index.md#networking).

Enable this option with [`CONFIG_POSIX_IPV6`](../../../../kconfig.md#CONFIG_POSIX_IPV6 "CONFIG_POSIX_IPV6").

### \_POSIX\_MEMLOCK

Zephyr’s [Demand Paging API](../../../../kernel/memory_management/demand_paging.md#memory-management-api-demand-paging) does not yet support
pinning or unpinning all virtual memory regions. The functions below are expected to fail and
set `errno` to `ENOSYS` [†](../conformance/index.md#posix-undefined-behaviour).

Enable this option with [`CONFIG_POSIX_MEMLOCK`](../../../../kconfig.md#CONFIG_POSIX_MEMLOCK "CONFIG_POSIX_MEMLOCK").

\_POSIX\_MEMLOCK

| API | Supported |
| --- | --- |
| mlockall() | yes |
| munlockall() | yes |

### \_POSIX\_MEMLOCK\_RANGE

Enable this option with [`CONFIG_POSIX_MEMLOCK_RANGE`](../../../../kconfig.md#CONFIG_POSIX_MEMLOCK_RANGE "CONFIG_POSIX_MEMLOCK_RANGE").

\_POSIX\_MEMLOCK\_RANGE

| API | Supported |
| --- | --- |
| mlock() | yes |
| munlock() | yes |

### \_POSIX\_MESSAGE\_PASSING

Enable this option with [`CONFIG_POSIX_MESSAGE_PASSING`](../../../../kconfig.md#CONFIG_POSIX_MESSAGE_PASSING "CONFIG_POSIX_MESSAGE_PASSING").

\_POSIX\_MESSAGE\_PASSING

| API | Supported |
| --- | --- |
| mq\_close() | yes |
| mq\_getattr() | yes |
| mq\_notify() | yes |
| mq\_open() | yes |
| mq\_receive() | yes |
| mq\_send() | yes |
| mq\_setattr() | yes |
| mq\_unlink() | yes |

### \_POSIX\_MONOTONIC\_CLOCK

Enable this option with [`CONFIG_POSIX_MONOTONIC_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_MONOTONIC_CLOCK "CONFIG_POSIX_MONOTONIC_CLOCK").

\_POSIX\_MONOTONIC\_CLOCK

| API | Supported |
| --- | --- |
| CLOCK\_MONOTONIC | yes |

### \_POSIX\_PRIORITY\_SCHEDULING

As processes are not yet supported in Zephyr, the functions `sched_rr_get_interval()`,
`sched_setparam()`, and `sched_setscheduler()` are expected to fail setting `errno`
to `ENOSYS`[†](../conformance/index.md#posix-undefined-behaviour).

Enable this option with [`CONFIG_POSIX_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_PRIORITY_SCHEDULING "CONFIG_POSIX_PRIORITY_SCHEDULING").

\_POSIX\_PRIORITY\_SCHEDULING

| API | Supported |
| --- | --- |
| sched\_get\_priority\_max() | yes |
| sched\_get\_priority\_min() | yes |
| sched\_getparam() | yes |
| sched\_getscheduler() | yes |
| sched\_rr\_get\_interval() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sched\_setparam() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sched\_setscheduler() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| sched\_yield() | yes |

### \_POSIX\_RAW\_SOCKETS

Raw sockets are supported.

For more information, please refer to [`CONFIG_NET_SOCKETS_PACKET`](../../../../kconfig.md#CONFIG_NET_SOCKETS_PACKET "CONFIG_NET_SOCKETS_PACKET").

Enable this option with [`CONFIG_POSIX_RAW_SOCKETS`](../../../../kconfig.md#CONFIG_POSIX_RAW_SOCKETS "CONFIG_POSIX_RAW_SOCKETS").

### \_POSIX\_READER\_WRITER\_LOCKS

Enable this option with [`CONFIG_POSIX_READER_WRITER_LOCKS`](../../../../kconfig.md#CONFIG_POSIX_READER_WRITER_LOCKS "CONFIG_POSIX_READER_WRITER_LOCKS").

\_POSIX\_READER\_WRITER\_LOCKS

| API | Supported |
| --- | --- |
| pthread\_rwlock\_destroy() | yes |
| pthread\_rwlock\_init() | yes |
| pthread\_rwlock\_rdlock() | yes |
| pthread\_rwlock\_tryrdlock() | yes |
| pthread\_rwlock\_trywrlock() | yes |
| pthread\_rwlock\_unlock() | yes |
| pthread\_rwlock\_wrlock() | yes |
| pthread\_rwlockattr\_destroy() | yes |
| pthread\_rwlockattr\_getpshared() | yes |
| pthread\_rwlockattr\_init() | yes |
| pthread\_rwlockattr\_setpshared() | yes |

### \_POSIX\_SHARED\_MEMORY\_OBJECTS

Enable this option with [`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](../../../../kconfig.md#CONFIG_POSIX_SHARED_MEMORY_OBJECTS "CONFIG_POSIX_SHARED_MEMORY_OBJECTS").

\_POSIX\_SHARED\_MEMORY\_OBJECTS

| API | Supported |
| --- | --- |
| mmap() | yes |
| munmap() | yes |
| shm\_open() | yes |
| shm\_unlink() | yes |

### \_POSIX\_SYNCHRONIZED\_IO

Enable this option with [`CONFIG_POSIX_SYNCHRONIZED_IO`](../../../../kconfig.md#CONFIG_POSIX_SYNCHRONIZED_IO "CONFIG_POSIX_SYNCHRONIZED_IO").

\_POSIX\_SYNCHRONIZED\_IO

| API | Supported |
| --- | --- |
| fdatasync() | yes |
| fsync() | yes |
| msync() | yes |

### \_POSIX\_THREAD\_ATTR\_STACKADDR

Enable this option with [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKADDR "CONFIG_POSIX_THREAD_ATTR_STACKADDR").

\_POSIX\_THREAD\_ATTR\_STACKADDR

| API | Supported |
| --- | --- |
| pthread\_attr\_getstackaddr() | yes |
| pthread\_attr\_setstackaddr() | yes |

### \_POSIX\_THREAD\_ATTR\_STACKSIZE

Enable this option with [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKSIZE "CONFIG_POSIX_THREAD_ATTR_STACKSIZE").

\_POSIX\_THREAD\_ATTR\_STACKSIZE

| API | Supported |
| --- | --- |
| pthread\_attr\_getstacksize() | yes |
| pthread\_attr\_setstacksize() | yes |

### \_POSIX\_THREAD\_CPUTIME

Enable this option with [`CONFIG_POSIX_THREAD_CPUTIME`](../../../../kconfig.md#CONFIG_POSIX_THREAD_CPUTIME "CONFIG_POSIX_THREAD_CPUTIME").

\_POSIX\_THREAD\_CPUTIME

| API | Supported |
| --- | --- |
| CLOCK\_THREAD\_CPUTIME\_ID | yes |
| pthread\_getcpuclockid() | yes |

### \_POSIX\_THREAD\_PRIO\_INHERIT

Enable this option with [`CONFIG_POSIX_THREAD_PRIO_INHERIT`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIO_INHERIT "CONFIG_POSIX_THREAD_PRIO_INHERIT").

\_POSIX\_THREAD\_PRIO\_INHERIT

| API | Supported |
| --- | --- |
| pthread\_mutexattr\_getprotocol() | yes |
| pthread\_mutexattr\_setprotocol() | yes |

### \_POSIX\_THREAD\_PRIO\_PROTECT

Enable this option with [`CONFIG_POSIX_THREAD_PRIO_PROTECT`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIO_PROTECT "CONFIG_POSIX_THREAD_PRIO_PROTECT").

\_POSIX\_THREAD\_PRIO\_PROTECT

| API | Supported |
| --- | --- |
| pthread\_mutex\_getprioceiling() | yes |
| pthread\_mutex\_setprioceiling() | yes |
| pthread\_mutexattr\_getprioceiling() | yes |
| pthread\_mutexattr\_getprotocol() | yes |
| pthread\_mutexattr\_setprioceiling() | yes |
| pthread\_mutexattr\_setprotocol() | yes |

### \_POSIX\_THREAD\_PRIORITY\_SCHEDULING

Enable this option with [`CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING "CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING").

\_POSIX\_THREAD\_PRIORITY\_SCHEDULING

| API | Supported |
| --- | --- |
| pthread\_attr\_getinheritsched() | yes |
| pthread\_attr\_getschedpolicy() | yes |
| pthread\_attr\_getscope() | yes |
| pthread\_attr\_setinheritsched() | yes |
| pthread\_attr\_setschedpolicy() | yes |
| pthread\_attr\_setscope() | yes |
| pthread\_getschedparam() | yes |
| pthread\_setschedparam() | yes |
| pthread\_setschedprio() | yes |

### \_POSIX\_THREAD\_SAFE\_FUNCTIONS

Enable this option with [`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](../../../../kconfig.md#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS "CONFIG_POSIX_THREAD_SAFE_FUNCTIONS").

\_POSIX\_THREAD\_SAFE\_FUNCTIONS

| API | Supported |
| --- | --- |
| asctime\_r() | yes |
| ctime\_r() | yes (UTC timezone only) |
| flockfile() |  |
| ftrylockfile() |  |
| funlockfile() |  |
| getc\_unlocked() |  |
| getchar\_unlocked() |  |
| getgrgid\_r() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| getgrnam\_r() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| getpwnam\_r() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| getpwuid\_r() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| gmtime\_r() | yes |
| localtime\_r() | yes (UTC timezone only) |
| putc\_unlocked() |  |
| putchar\_unlocked() |  |
| rand\_r() | yes |
| readdir\_r() | yes |
| strerror\_r() | yes |
| strtok\_r() | yes |

### \_POSIX\_TIMEOUTS

Enable this option with [`CONFIG_POSIX_TIMEOUTS`](../../../../kconfig.md#CONFIG_POSIX_TIMEOUTS "CONFIG_POSIX_TIMEOUTS").

\_POSIX\_TIMEOUTS

| API | Supported |
| --- | --- |
| mq\_timedreceive() | yes |
| mq\_timedsend() | yes |
| pthread\_mutex\_timedlock() | yes |
| pthread\_rwlock\_timedrdlock() | yes |
| pthread\_rwlock\_timedwrlock() | yes |
| sem\_timedwait() | yes |
| posix\_trace\_timedgetnext\_event() |  |

### \_XOPEN\_STREAMS

With the exception of `ioctl()`, functions in the `_XOPEN_STREAMS` option group are not
implemented in Zephyr but are provided so that conformant applications can still link.
Unimplemented functions in this option group will fail, setting `errno` to `ENOSYS`
[†](../conformance/index.md#posix-undefined-behaviour).

Enable this option with [`CONFIG_XOPEN_STREAMS`](../../../../kconfig.md#CONFIG_XOPEN_STREAMS "CONFIG_XOPEN_STREAMS").

\_XOPEN\_STREAMS

| API | Supported |
| --- | --- |
| fattach() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| fdetach() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| getmsg() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| getpmsg() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| ioctl() | yes |
| isastream() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| putmsg() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
| putpmsg() | yes [†](../conformance/index.md#posix-undefined-behaviour) |
