---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/notify.html
original_path: services/notify.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Asynchronous Notifications

Zephyr APIs often include [async](../develop/api/terminology.md#api-term-async) functions where an
operation is initiated and the application needs to be informed when it
completes, and whether it succeeded. Using [`k_poll()`](../kernel/services/polling.md#c.k_poll "k_poll") is
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

- [`sys_notify`](#c.sys_notify) is not a kernel object;
- copying the notification content from userspace will break use of
  [`CONTAINER_OF`](../kernel/util/index.md#c.CONTAINER_OF "CONTAINER_OF") in the implementing function;
- neither the spin-wait nor callback notification methods can be
  accepted from userspace callers.

Where a notification is required for an asynchronous operation invoked
from a user mode thread the subsystem or driver should provide a syscall
API that uses [`k_poll_signal`](../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") for notification.

## API Reference

*group* sys\_notify\_apis
:   Typedefs

    typedef void (\*sys\_notify\_generic\_callback)()
    :   Generic signature used to notify of result completion by callback.

        Functions with this role may be invoked from any context including pre-kernel, ISR, or cooperative or pre-emptible threads. Compatible functions must be isr-ok and not sleep.

        Parameters that should generally be passed to such functions include:

        - a pointer to a specific client request structure, i.e. the one that contains the [sys\_notify](#structsys__notify) structure.
        - the result of the operation, either as passed to [sys\_notify\_finalize()](#group__sys__notify__apis_1ga424b1c94c1010bdc4170cf06c7f2ec72) or extracted afterwards using [sys\_notify\_fetch\_result()](#group__sys__notify__apis_1ga823397b1917e10593d606daf3ec06a65). Expected values are service-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed.

    Functions

    static inline uint32\_t sys\_notify\_get\_method(const struct [sys\_notify](#c.sys_notify) \*notify)

    int sys\_notify\_validate(struct [sys\_notify](#c.sys_notify) \*notify)
    :   Validate and initialize the notify structure.

        This should be invoked at the start of any service-specific configuration validation. It ensures that the basic asynchronous notification configuration is consistent, and clears the result.

        Note that this function does not validate extension bits (zeroed by async notify API init functions like [sys\_notify\_init\_callback()](#group__sys__notify__apis_1gaa9f31f78c03f48a3c649bbac15cc3a6c)). It may fail to recognize that an uninitialized structure has been passed because only method bits of flags are tested against method settings. To reduce the chance of accepting an uninitialized operation service validation of structures that contain an [sys\_notify](#structsys__notify) instance should confirm that the extension bits are set or cleared as expected.

        Return values:
        :   - **0** – on successful validation and reinitialization
            - **-EINVAL** – if the configuration is not valid.

    [sys\_notify\_generic\_callback](#c.sys_notify_generic_callback) sys\_notify\_finalize(struct [sys\_notify](#c.sys_notify) \*notify, int res)
    :   Record and signal the operation completion.

        Parameters:
        :   - **notify** – pointer to the notification state structure.
            - **res** – the result of the operation. Expected values are service-specific, but the value shall be non-negative if the operation succeeded, and negative if the operation failed.

        Returns:
        :   If the notification is to be done by callback this returns the generic version of the function to be invoked. The caller must immediately invoke that function with whatever arguments are expected by the callback. If notification is by spin-wait or signal, the notification has been completed by the point this function returns, and a null pointer is returned.

    static inline int sys\_notify\_fetch\_result(const struct [sys\_notify](#c.sys_notify) \*notify, int \*result)
    :   Check for and read the result of an asynchronous operation.

        Parameters:
        :   - **notify** – pointer to the object used to specify asynchronous function behavior and store completion information.
            - **result** – pointer to storage for the result of the operation. The result is stored only if the operation has completed.

        Return values:
        :   - **0** – if the operation has completed.
            - **-EAGAIN** – if the operation has not completed.

    static inline void sys\_notify\_init\_spinwait(struct [sys\_notify](#c.sys_notify) \*notify)
    :   Initialize a notify object for spin-wait notification.

        Clients that use this initialization receive no asynchronous notification, and instead must periodically check for completion using [sys\_notify\_fetch\_result()](#group__sys__notify__apis_1ga823397b1917e10593d606daf3ec06a65).

        On completion of the operation the client object must be reinitialized before it can be re-used.

        Parameters:
        :   - **notify** – pointer to the notification configuration object.

    static inline void sys\_notify\_init\_signal(struct [sys\_notify](#c.sys_notify) \*notify, struct [k\_poll\_signal](../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sigp)
    :   Initialize a notify object for (k\_poll) signal notification.

        Clients that use this initialization will be notified of the completion of operations through the provided signal.

        On completion of the operation the client object must be reinitialized before it can be re-used.

        Note

        This capability is available only when  [`CONFIG_POLL`](../kconfig.md#CONFIG_POLL "CONFIG_POLL") is selected.

        Parameters:
        :   - **notify** – pointer to the notification configuration object.
            - **sigp** – pointer to the signal to use for notification. The value must not be null. The signal must be reset before the client object is passed to the on-off service API.

    static inline void sys\_notify\_init\_callback(struct [sys\_notify](#c.sys_notify) \*notify, [sys\_notify\_generic\_callback](#c.sys_notify_generic_callback) handler)
    :   Initialize a notify object for callback notification.

        Clients that use this initialization will be notified of the completion of operations through the provided callback. Note that callbacks may be invoked from various contexts depending on the specific service; see [sys\_notify\_generic\_callback](#group__sys__notify__apis_1ga2a9ffe35a5ad44fb7c5b00bb5c5c0499).

        On completion of the operation the client object must be reinitialized before it can be re-used.

        Parameters:
        :   - **notify** – pointer to the notification configuration object.
            - **handler** – a function pointer to use for notification.

    static inline bool sys\_notify\_uses\_callback(const struct [sys\_notify](#c.sys_notify) \*notify)
    :   Detect whether a particular notification uses a callback.

        The generic handler does not capture the signature expected by the callback, and the translation to a service-specific callback must be provided by the service. This check allows abstracted services to reject callback notification requests when the service doesn’t provide a translation function.

        Returns:
        :   true if and only if a callback is to be used for notification.

    struct sys\_notify
    :   *#include <notify.h>*

        State associated with notification for an asynchronous operation.

        Objects of this type are allocated by a client, which must use an initialization function (e.g. [sys\_notify\_init\_signal()](#group__sys__notify__apis_1ga30f9eff4b20b7d637a3a1df5f4cb38f8)) to configure them. Generally the structure is a member of a service-specific client structure, such as [onoff\_client](resource_management/index.md#structonoff__client).

        Control of the containing object transfers to the service provider when a pointer to the object is passed to a service function that is documented to take control of the object, such as onoff\_service\_request(). While the service provider controls the object the client must not change any object fields. Control reverts to the client:

        - if the call to the service API returns an error;
        - when operation completion is posted. This may occur before the call to the service API returns.

        Operation completion is technically posted when the flags field is updated so that [sys\_notify\_fetch\_result()](#group__sys__notify__apis_1ga823397b1917e10593d606daf3ec06a65) returns success. This will happen before the signal is posted or callback is invoked. Note that although the manager will no longer reference the [sys\_notify](#structsys__notify) object past this point, the containing object may have state that will be referenced within the callback. Where callbacks are used control of the containing object does not revert to the client until the callback has been invoked. (Re-use within the callback is explicitly permitted.)

        After control has reverted to the client the notify object must be reinitialized for the next operation.

        The content of this structure is not public API to clients: all configuration and inspection should be done with functions like [sys\_notify\_init\_callback()](#group__sys__notify__apis_1gaa9f31f78c03f48a3c649bbac15cc3a6c) and [sys\_notify\_fetch\_result()](#group__sys__notify__apis_1ga823397b1917e10593d606daf3ec06a65). However, services that use this structure may access certain fields directly.

        union method
        :   *#include <notify.h>*

            Public Members

            struct [k\_poll\_signal](../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*signal

            [sys\_notify\_generic\_callback](#c.sys_notify_generic_callback) callback
