---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/portability/posix/option_groups/index.html
original_path: services/portability/posix/option_groups/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Subprofiling Option Groups

## POSIX\_THREADS\_BASE

The basic assumption in this profile is that the system
consists of a single (implicit) process with multiple threads. Therefore, the
standard requires all basic thread services, except those related to
multiple processes.

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

## POSIX\_THREADS\_EXT

This table lists service support status in Zephyr:

POSIX\_THREADS\_EXT

| API | Supported |
| --- | --- |
| pthread\_attr\_getguardsize() | yes |
| pthread\_attr\_setguardsize() | yes |
| pthread\_mutexattr\_gettype() | yes |
| pthread\_mutexattr\_settype() | yes |

## XSI\_THREADS\_EXT

The XSI\_THREADS\_EXT option group is required because it provides
functions to control a thread’s stack. This is considered useful for any
real-time application.

This table lists service support status in Zephyr:

XSI\_THREADS\_EXT

| API | Supported |
| --- | --- |
| pthread\_attr\_getstack() | yes |
| pthread\_attr\_setstack() | yes |
| pthread\_getconcurrency() | yes |
| pthread\_setconcurrency() | yes |

## POSIX\_C\_LANG\_JUMP

The `POSIX_C_LANG_JUMP` Option Group is included in the ISO C standard.

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the
`POSIX_C_LANG_JUMP` Option Group is considered supported.

POSIX\_C\_LANG\_JUMP

| API | Supported |
| --- | --- |
| setjmp() | yes |
| longjmp() | yes |

## POSIX\_C\_LANG\_MATH

The `POSIX_C_LANG_MATH` Option Group is included in the ISO C standard.

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the
`POSIX_C_LANG_MATH` Option Group is considered supported.

Please refer to [Subprofiling Considerations](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html) for details on the `POSIX_C_LANG_MATH` Option
Group.

## POSIX\_C\_LANG\_SUPPORT

The POSIX\_C\_LANG\_SUPPORT option group contains the general ISO C Library.

Note

When using Newlib, Picolibc, or other C libraries conforming to the ISO C Standard, the entire
`POSIX_C_LANG_SUPPORT` Option Group is considered supported.

Please refer to [Subprofiling Considerations](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html) for details on the `POSIX_C_LANG_SUPPORT` Option
Group.

For more information on developing Zephyr applications in the C programming language, please refer
to [details](../../../../develop/languages/index.md#language-support).

## POSIX\_SINGLE\_PROCESS

The POSIX\_SINGLE\_PROCESS option group contains services for single
process applications.

POSIX\_SINGLE\_PROCESS

| API | Supported |
| --- | --- |
| confstr() |  |
| environ |  |
| errno | yes |
| getenv() |  |
| setenv() |  |
| sysconf() | yes |
| uname() | yes |
| unsetenv() |  |

## POSIX\_SIGNALS

Signal services are a basic mechanism within POSIX-based systems and are
required for error and event handling.

POSIX\_SIGNALS

| API | Supported |
| --- | --- |
| abort() | yes |
| alarm() |  |
| kill() |  |
| pause() |  |
| raise() |  |
| sigaction() |  |
| sigaddset() | yes |
| sigdelset() | yes |
| sigemptyset() | yes |
| sigfillset() | yes |
| sigismember() | yes |
| signal() |  |
| sigpending() |  |
| sigprocmask() | yes |
| sigsuspend() |  |
| sigwait() |  |
| strsignal() | yes |

## POSIX\_DEVICE\_IO

POSIX\_DEVICE\_IO

| API | Supported |
| --- | --- |
| FD\_CLR() | yes |
| FD\_ISSET() | yes |
| FD\_SET() | yes |
| FD\_ZERO() | yes |
| clearerr() | yes |
| close() | yes |
| fclose() |  |
| fdopen() |  |
| feof() |  |
| ferror() |  |
| fflush() |  |
| fgetc() |  |
| fgets() |  |
| fileno() |  |
| fopen() |  |
| fprintf() | yes |
| fputc() | yes |
| fputs() | yes |
| fread() |  |
| freopen() |  |
| fscanf() |  |
| fwrite() | yes |
| getc() |  |
| getchar() |  |
| gets() |  |
| open() | yes |
| perror() | yes |
| poll() | yes |
| printf() | yes |
| pread() |  |
| pselect() |  |
| putc() | yes |
| putchar() | yes |
| puts() | yes |
| pwrite() |  |
| read() | yes |
| scanf() |  |
| select() | yes |
| setbuf() |  |
| setvbuf() |  |
| stderr |  |
| stdin |  |
| stdout |  |
| ungetc() |  |
| vfprintf() | yes |
| vfscanf() |  |
| vprintf() | yes |
| vscanf() |  |
| write() | yes |

## POSIX\_BARRIERS

POSIX\_BARRIERS

| API | Supported |
| --- | --- |
| pthread\_barrier\_destroy() | yes |
| pthread\_barrier\_init() | yes |
| pthread\_barrier\_wait() | yes |
| pthread\_barrierattr\_destroy() | yes |
| pthread\_barrierattr\_init() | yes |

## POSIX\_CLOCK\_SELECTION

POSIX\_CLOCK\_SELECTION

| API | Supported |
| --- | --- |
| pthread\_condattr\_getclock() | yes |
| pthread\_condattr\_setclock() | yes |
| clock\_nanosleep() | yes |

## POSIX\_SEMAPHORES

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

## POSIX\_SPIN\_LOCKS

POSIX\_SPIN\_LOCKS

| API | Supported |
| --- | --- |
| pthread\_spin\_destroy() | yes |
| pthread\_spin\_init() | yes |
| pthread\_spin\_lock() | yes |
| pthread\_spin\_trylock() | yes |
| pthread\_spin\_unlock() | yes |

## POSIX\_TIMERS

POSIX\_TIMERS

| API | Supported |
| --- | --- |
| clock\_getres() |  |
| clock\_gettime() | yes |
| clock\_settime() | yes |
| nanosleep() | yes |
| timer\_create() | yes |
| timer\_delete() | yes |
| timer\_gettime() | yes |
| timer\_getoverrun() | yes |
| timer\_settime() | yes |

## Additional POSIX Options

### \_POSIX\_MESSAGE\_PASSING

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

### \_POSIX\_PRIORITY\_SCHEDULING

\_POSIX\_PRIORITY\_SCHEDULING

| API | Supported |
| --- | --- |
| sched\_get\_priority\_max() | yes |
| sched\_get\_priority\_min() | yes |
| sched\_getparam() | yes |
| sched\_getscheduler() | yes |
| sched\_rr\_get\_interval() | yes |
| sched\_setparam() | yes |
| sched\_setscheduler() | yes |
| sched\_yield() | yes |

### \_POSIX\_READER\_WRITER\_LOCKS

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
| pthread\_rwlockattr\_getpshared() |  |
| pthread\_rwlockattr\_init() | yes |
| pthread\_rwlockattr\_setpshared() |  |

### \_POSIX\_THREAD\_ATTR\_STACKADDR

\_POSIX\_THREAD\_ATTR\_STACKADDR

| API | Supported |
| --- | --- |
| pthread\_attr\_getstackaddr() | yes |
| pthread\_attr\_setstackaddr() | yes |

### \_POSIX\_THREAD\_ATTR\_STACKSIZE

\_POSIX\_THREAD\_ATTR\_STACKSIZE

| API | Supported |
| --- | --- |
| pthread\_attr\_getstacksize() | yes |
| pthread\_attr\_setstacksize() | yes |

### \_POSIX\_THREAD\_PRIORITY\_SCHEDULING

\_POSIX\_THREAD\_PRIORITY\_SCHEDULING

| API | Supported |
| --- | --- |
| pthread\_attr\_getinheritsched() |  |
| pthread\_attr\_getschedpolicy() | yes |
| pthread\_attr\_getscope() |  |
| pthread\_attr\_setinheritsched() |  |
| pthread\_attr\_setschedpolicy() | yes |
| pthread\_attr\_setscope() |  |
| pthread\_getschedparam() | yes |
| pthread\_setschedparam() | yes |
| pthread\_setschedprio() | yes |

### \_POSIX\_THREAD\_SAFE\_FUNCTIONS

\_POSIX\_THREAD\_SAFE\_FUNCTIONS

| API | Supported |
| --- | --- |
| asctime\_r() |  |
| ctime\_r() |  |
| flockfile() |  |
| ftrylockfile() |  |
| funlockfile() |  |
| getc\_unlocked() | yes |
| getchar\_unlocked() | yes |
| getgrgid\_r() |  |
| getgrnam\_r() |  |
| getpwnam\_r() |  |
| getpwuid\_r() |  |
| gmtime\_r() | yes |
| localtime\_r() |  |
| putc\_unlocked() | yes |
| putchar\_unlocked() | yes |
| rand\_r() | yes |
| readdir\_r() |  |
| strerror\_r() | yes |
| strtok\_r() | yes |

### \_POSIX\_TIMEOUTS

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

\_XOPEN\_STREAMS

| API | Supported |
| --- | --- |
| fattach() |  |
| fdetach() |  |
| getmsg() |  |
| getpmsg() |  |
| ioctl() | yes |
| isastream() |  |
| putmsg() |  |
| putpmsg() |  |
