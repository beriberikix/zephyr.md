---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/languages/c/minimal_libc.html
original_path: develop/languages/c/minimal_libc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Minimal libc

The most basic C library, named “minimal libc”, is part of the Zephyr codebase
and provides the minimal subset of the standard C library required to meet the
needs of Zephyr and its subsystems, primarily in the areas of string
manipulation and display.

It is very low footprint and is suitable for projects that do not rely on less
frequently used portions of the ISO C standard library. It can also be used
with a number of different toolchains.

The minimal libc implementation can be found in `lib/libc/minimal` in the
main Zephyr tree.

## Functions

The minimal libc implements the minimal subset of the ISO/IEC 9899:2011
standard C library functions required to meet the needs of the Zephyr kernel,
as defined by the [Coding Guidelines Rule A.4](../../../contribute/coding_guidelines/index.md#coding-guideline-libc-usage-restrictions-in-zephyr-kernel).

## Formatted Output

The minimal libc does not implement its own formatted output processor;
instead, it maps the C standard formatted output functions such as `printf`
and `sprintf` to the [`cbprintf()`](../../../services/formatted_output.md#c.cbprintf "cbprintf") function, which is Zephyr’s own
C99-compatible formatted output implementation.

For more details, refer to the [Formatted Output](../../../services/formatted_output.md#formatted-output) OS
service documentation.

## Dynamic Memory Management

The minimal libc uses the malloc api family implementation provided by the
[common C library](common_libc.md#c-library-common), which itself is built upon the
[kernel memory heap API](../../../kernel/memory_management/heap.md#heap-v2).

## Error numbers

Error numbers are used throughout Zephyr APIs to signal error conditions as
return values from functions. They are typically returned as the negative value
of the integer literals defined in this section, and are defined in the
`errno.h` header file.

A subset of the error numbers defined in the [POSIX errno.h specification](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/errno.h.html) and
other de-facto standard sources have been added to the minimal libc.

A conscious effort is made in Zephyr to keep the values of the minimal libc
error numbers consistent with the different implementations of the C standard
libraries supported by Zephyr. The minimal libc `errno.h` is checked
against that of the [Newlib](newlib.md#c-library-newlib) to ensure that the error
numbers are kept aligned.

Below is a list of the error number definitions. For the actual numeric values
please refer to [errno.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/include/errno.h).

*group* system\_errno
:   System error numbers Error codes returned by functions.

    Includes a list of those defined by IEEE Std 1003.1-2017.

    Defines

    errno

    EPERM
    :   Not owner.

    ENOENT
    :   No such file or directory.

    ESRCH
    :   No such context.

    EINTR
    :   Interrupted system call.

    EIO
    :   I/O error.

    ENXIO
    :   No such device or address.

    E2BIG
    :   Arg list too long.

    ENOEXEC
    :   Exec format error.

    EBADF
    :   Bad file number.

    ECHILD
    :   No children.

    EAGAIN
    :   No more contexts.

    ENOMEM
    :   Not enough core.

    EACCES
    :   Permission denied.

    EFAULT
    :   Bad address.

    ENOTBLK
    :   Block device required.

    EBUSY
    :   Mount device busy.

    EEXIST
    :   File exists.

    EXDEV
    :   Cross-device link.

    ENODEV
    :   No such device.

    ENOTDIR
    :   Not a directory.

    EISDIR
    :   Is a directory.

    EINVAL
    :   Invalid argument.

    ENFILE
    :   File table overflow.

    EMFILE
    :   Too many open files.

    ENOTTY
    :   Not a typewriter.

    ETXTBSY
    :   Text file busy.

    EFBIG
    :   File too large.

    ENOSPC
    :   No space left on device.

    ESPIPE
    :   Illegal seek.

    EROFS
    :   Read-only file system.

    EMLINK
    :   Too many links.

    EPIPE
    :   Broken pipe.

    EDOM
    :   Argument too large.

    ERANGE
    :   Result too large.

    ENOMSG
    :   Unexpected message type.

    EDEADLK
    :   Resource deadlock avoided.

    ENOLCK
    :   No locks available.

    ENOSTR
    :   STREAMS device required.

    ENODATA
    :   Missing expected message data.

    ETIME
    :   STREAMS timeout occurred.

    ENOSR
    :   Insufficient memory.

    EPROTO
    :   Generic STREAMS error.

    EBADMSG
    :   Invalid STREAMS message.

    ENOSYS
    :   Function not implemented.

    ENOTEMPTY
    :   Directory not empty.

    ENAMETOOLONG
    :   File name too long.

    ELOOP
    :   Too many levels of symbolic links.

    EOPNOTSUPP
    :   Operation not supported on socket.

    EPFNOSUPPORT
    :   Protocol family not supported.

    ECONNRESET
    :   Connection reset by peer.

    ENOBUFS
    :   No buffer space available.

    EAFNOSUPPORT
    :   Addr family not supported.

    EPROTOTYPE
    :   Protocol wrong type for socket.

    ENOTSOCK
    :   Socket operation on non-socket.

    ENOPROTOOPT
    :   Protocol not available.

    ESHUTDOWN
    :   Can’t send after socket shutdown.

    ECONNREFUSED
    :   Connection refused.

    EADDRINUSE
    :   Address already in use.

    ECONNABORTED
    :   Software caused connection abort.

    ENETUNREACH
    :   Network is unreachable.

    ENETDOWN
    :   Network is down.

    ETIMEDOUT
    :   Connection timed out.

    EHOSTDOWN
    :   Host is down.

    EHOSTUNREACH
    :   No route to host.

    EINPROGRESS
    :   Operation now in progress.

    EALREADY
    :   Operation already in progress.

    EDESTADDRREQ
    :   Destination address required.

    EMSGSIZE
    :   Message size.

    EPROTONOSUPPORT
    :   Protocol not supported.

    ESOCKTNOSUPPORT
    :   Socket type not supported.

    EADDRNOTAVAIL
    :   Can’t assign requested address.

    ENETRESET
    :   Network dropped connection on reset.

    EISCONN
    :   Socket is already connected.

    ENOTCONN
    :   Socket is not connected.

    ETOOMANYREFS
    :   Too many references: can’t splice.

    ENOTSUP
    :   Unsupported value.

    EILSEQ
    :   Illegal byte sequence.

    EOVERFLOW
    :   Value overflow.

    ECANCELED
    :   Operation canceled.

    EWOULDBLOCK
    :   Operation would block.
