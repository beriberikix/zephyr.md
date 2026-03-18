---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/thread.html
original_path: connectivity/networking/api/thread.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Thread protocol

## [Overview](#id1)

Thread is a low-power mesh networking technology, designed specifically for home
automation applications. It is an IPv6-based standard, which uses 6LoWPAN
technology over IEEE 802.15.4 protocol. IP connectivity lets you easily connect
a Thread mesh network to the internet with a Thread Border Router.

The Thread specification provides a high level of network security. Mesh networks
built with Thread are secure - only authenticated devices can join the network
and all communications within the mesh are encrypted. More information about
Thread protocol can be found at
[Thread Group website](https://www.threadgroup.org).

Zephyr integrates an open source Thread protocol implementation called OpenThread,
documented on the [OpenThread website](https://openthread.io/).

## [Internet connectivity](#id2)

A Thread Border Router is required to connect mesh network to the internet.
An open source implementation of Thread Border Router is provided by the OpenThread
community. See
[OpenThread Border Router guide](https://openthread.io/guides/border-router)
for instructions on how to set up a Border Router.

## [Sample usage](#id3)

You can try using OpenThread with the Zephyr Echo server and Echo client samples,
which provide out-of-the-box configuration for OpenThread. To enable OpenThread
support in these samples, build them with `overlay-ot.conf` overlay config file.
See [Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") and [Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")
samples for details.

## [Thread related APIs](#id4)

### [OpenThread Driver API](#id5)

OpenThread L2 uses Zephyr’s protocol agnostic IEEE 802.15.4 driver API
internally. This API is of interest to **driver developers** that want to
support OpenThread.

The driver API is part of the [IEEE 802.15.4 Driver API](ieee802154.md#ieee802154-driver-api) subsystem and
documented there.

### [OpenThread L2 Adaptation Layer API](#id6)

Zephyr’s OpenThread L2 platform adaptation layer glues the external OpenThread
stack together with Zephyr’s IEEE 802.15.4 protocol agnostic driver API. This
API is of interest to OpenThread L2 **subsystem contributors** only.

Related code samples

[OpenThread co-processor](../../../samples/net/openthread/coprocessor/README.md#coprocessor "Build a Thread border-router using OpenThread's co-processor designs.")
:   Build a Thread border-router using OpenThread's co-processor designs.

*group* OpenThread L2 abstraction layer
:   OpenThread Layer 2 abstraction layer.

    Functions

    int openthread\_state\_changed\_cb\_register(struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](#c.openthread_state_changed_cb) \*cb)
    :   Registers callbacks which will be called when certain configuration or state changes occur within OpenThread.

        Parameters:
        :   - **ot\_context** – the OpenThread context to register the callback with.
            - **cb** – callback struct to register.

    int openthread\_state\_changed\_cb\_unregister(struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](#c.openthread_state_changed_cb) \*cb)
    :   Unregisters OpenThread configuration or state changed callbacks.

        Parameters:
        :   - **ot\_context** – the OpenThread context to unregister the callback from.
            - **cb** – callback struct to unregister.

    k\_tid\_t openthread\_thread\_id\_get(void)
    :   Get OpenThread thread identification.

    struct openthread\_context \*openthread\_get\_default\_context(void)
    :   Get pointer to default OpenThread context.

        Return values:
        :   - **!NULL** – On success.
            - **NULL** – On failure.

    struct otInstance \*openthread\_get\_default\_instance(void)
    :   Get pointer to default OpenThread instance.

        Return values:
        :   - **!NULL** – On success.
            - **NULL** – On failure.

    int openthread\_start(struct openthread\_context \*ot\_context)
    :   Starts the OpenThread network.

        Depends on active settings: it uses stored network configuration, start joining procedure or uses default network configuration. Additionally when the device is MTD, it sets the SED mode to properly attach the network.

        Parameters:
        :   - **ot\_context**

    void openthread\_api\_mutex\_lock(struct openthread\_context \*ot\_context)
    :   Lock internal mutex before accessing OT API.

        OpenThread API is not thread-safe, therefore before accessing any API function, it’s needed to lock the internal mutex, to prevent the OpenThread thread from preempting the API call.

        Parameters:
        :   - **ot\_context** – Context to lock.

    int openthread\_api\_mutex\_try\_lock(struct openthread\_context \*ot\_context)
    :   Try to lock internal mutex before accessing OT API.

        This function behaves like [openthread\_api\_mutex\_lock()](#group__openthread_1ga1f702bb5768795bce5561efe457b1028) provided that the internal mutex is unlocked. Otherwise, it exists immediately and returns a negative value.

        Parameters:
        :   - **ot\_context** – Context to lock.

        Return values:
        :   - **0** – On success.
            - **<0** – On failure.

    void openthread\_api\_mutex\_unlock(struct openthread\_context \*ot\_context)
    :   Unlock internal mutex after accessing OT API.

        Parameters:
        :   - **ot\_context** – Context to unlock.

    struct openthread\_state\_changed\_cb
    :   *#include <openthread.h>*

        OpenThread state change callback.

        OpenThread state change callback structure

        Used to register a callback in the callback list. As many callbacks as needed can be added as long as each of them are unique pointers of struct [openthread\_state\_changed\_cb](#structopenthread__state__changed__cb). Beware such structure should not be allocated on stack.

        Public Members

        void (\*state\_changed\_cb)(otChangedFlags flags, struct openthread\_context \*ot\_context, void \*user\_data)
        :   Callback for notifying configuration or state changes.

            Param flags:
            :   as per OpenThread otStateChangedCallback() aFlags parameter. See [https://openthread.io/reference/group/api-instance#otstatechangedcallback](https://openthread.io/reference/group/api-instance#otstatechangedcallback)

            Param ot\_context:
            :   the OpenThread context the callback is registered with.

            Param user\_data:
            :   Data to pass to the callback.

        void \*user\_data
        :   User data if required.

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Internally used field for list handling.

            - user must not directly modify
