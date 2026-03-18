---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/trickle.html
original_path: connectivity/networking/api/trickle.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Trickle Timer Library

## [Overview](#id1)

The Trickle timer library implements
[IETF RFC6206 (Trickle Algorithm)](https://tools.ietf.org/html/rfc6206).

The Trickle algorithm allows nodes in a lossy shared medium (e.g.,
low-power and lossy networks) to exchange information in a highly
robust, energy efficient, simple, and scalable manner.

## [API Reference](#id2)

*group* trickle
:   Trickle algorithm library.

    Typedefs

    typedef void (\*net\_trickle\_cb\_t)(struct [net\_trickle](#c.net_trickle) \*trickle, bool do\_suppress, void \*user\_data)
    :   Trickle timer callback.

        The callback is called after Trickle timeout expires.

        Param Trickle Algorithm Library:
        :   The trickle context to use.

        Param do\_suppress:
        :   Is TX allowed (true) or not (false).

        Param user\_data:
        :   The user data given in [net\_trickle\_start()](#group__trickle_1ga6674fac118a187320d73dc742f0e216f) call.

    Functions

    int net\_trickle\_create(struct [net\_trickle](#c.net_trickle) \*trickle, uint32\_t Imin, uint8\_t Imax, uint8\_t k)
    :   Create a Trickle timer.

        Parameters:
        :   - **Library** (Trickle Algorithm) – Pointer to Trickle struct.
            - **Imin** – Imin configuration parameter in ms.
            - **Imax** – Max number of doublings.
            - **k** – Redundancy constant parameter. See RFC 6206 for details.

        Returns:
        :   Return 0 if ok and <0 if error.

    int net\_trickle\_start(struct [net\_trickle](#c.net_trickle) \*trickle, [net\_trickle\_cb\_t](#c.net_trickle_cb_t) cb, void \*user\_data)
    :   Start a Trickle timer.

        Parameters:
        :   - **Library** (Trickle Algorithm) – Pointer to Trickle struct.
            - **cb** – User callback to call at time T within the current trickle interval
            - **user\_data** – User pointer that is passed to callback.

        Returns:
        :   Return 0 if ok and <0 if error.

    int net\_trickle\_stop(struct [net\_trickle](#c.net_trickle) \*trickle)
    :   Stop a Trickle timer.

        Parameters:
        :   - **Library** (Trickle Algorithm) – Pointer to Trickle struct.

        Returns:
        :   Return 0 if ok and <0 if error.

    void net\_trickle\_consistency(struct [net\_trickle](#c.net_trickle) \*trickle)
    :   To be called by the protocol handler when it hears a consistent network transmission.

        Parameters:
        :   - **Library** (Trickle Algorithm) – Pointer to Trickle struct.

    void net\_trickle\_inconsistency(struct [net\_trickle](#c.net_trickle) \*trickle)
    :   To be called by the protocol handler when it hears an inconsistent network transmission.

        Parameters:
        :   - **Library** (Trickle Algorithm) – Pointer to Trickle struct.

    static inline bool net\_trickle\_is\_running(struct [net\_trickle](#c.net_trickle) \*trickle)
    :   Check if the Trickle timer is running or not.

        Parameters:
        :   - **Library** (Trickle Algorithm) – Pointer to Trickle struct.

        Returns:
        :   Return True if timer is running and False if not.

    struct net\_trickle
    :   *#include <trickle.h>*

        The variable names are taken directly from RFC 6206 when applicable.

        Note that the struct members should not be accessed directly but only via the Trickle API.

        Public Members

        uint32\_t Imin
        :   Min interval size in ms.

        uint8\_t Imax
        :   Max number of doublings.

        uint8\_t k
        :   Redundancy constant.

        uint32\_t I
        :   Current interval size.

        uint32\_t Istart
        :   Start of the interval in ms.

        uint8\_t c
        :   Consistency counter.

        uint32\_t Imax\_abs
        :   Max interval size in ms (not doublings).

        [net\_trickle\_cb\_t](#c.net_trickle_cb_t) cb
        :   Callback to be called when timer expires.
