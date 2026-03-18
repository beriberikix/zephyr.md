---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/other/version.html
original_path: kernel/services/other/version.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Version

Kernel version handling and APIs related to kernel version being used.

## API Reference

uint32\_t sys\_kernel\_version\_get(void)
:   Return the kernel version of the present build.

    The kernel version is a four-byte value, whose format is described in the file “kernel\_version.h”.

    Returns:
    :   kernel version

SYS\_KERNEL\_VER\_MAJOR(ver)

SYS\_KERNEL\_VER\_MINOR(ver)

SYS\_KERNEL\_VER\_PATCHLEVEL(ver)
