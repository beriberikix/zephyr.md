---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/notify.html
original_path: services/notify.html
---

# Asynchronous Notifications

Zephyr APIs often include [async](../develop/api/terminology.md#api-term-async) functions where an
operation is initiated and the application needs to be informed when it
completes, and whether it succeeded. Using [`k_poll()`](../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) is
often a good method, but some application architectures may be more
suited to a callback notification, and operations like enabling clocks
and power rails may need to be invoked before kernel functions are
available so a busy-wait for completion may be needed.

This API is intended to be embedded within specific subsystems such as
[On-Off Manager](resource_management/index.md#resource-mgmt-onoff) and other APIs that support async
transactions. The subsystem wrappers are responsible for extracting
operation-specific data from requests that include a notification
element, and for invoking callbacks with the parameters required by the
API.

A limitation is that this API is not suitable for [System Calls](../kernel/usermode/syscalls.md#syscalls)
because:

- [`sys_notify`](../doxygen/html/structsys__notify.md) is not a kernel object;
- copying the notification content from userspace will break use of
  [`CONTAINER_OF`](../doxygen/html/group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f) in the implementing function;
- neither the spin-wait nor callback notification methods can be
  accepted from userspace callers.

Where a notification is required for an asynchronous operation invoked
from a user mode thread the subsystem or driver should provide a syscall
API that uses [`k_poll_signal`](../doxygen/html/structk__poll__signal.md) for notification.

## API Reference

[Asynchronous Notification APIs](../doxygen/html/group__sys__notify__apis.md)
