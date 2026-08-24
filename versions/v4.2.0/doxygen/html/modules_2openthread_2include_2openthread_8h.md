---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/modules_2openthread_2include_2openthread_8h.html
original_path: doxygen/html/modules_2openthread_2include_2openthread_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <openthread/instance.h>`  
`#include <openthread/message.h>`

[Go to the source code of this file.](modules_2openthread_2include_2openthread_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) |
|  | OpenThread state change callback. [More...](structopenthread__state__changed__callback.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [openthread\_receive\_cb](#a8f95392e11afa85e9bd80569c1793e76)) (struct otMessage \*message, void \*context) |
|  | The common callback type for receiving IPv4 (translated by NAT64) and IPv6 datagrams. |

| Functions | |
| --- | --- |
| int | [openthread\_state\_changed\_callback\_register](#a4178b72288585869e2c941acdc21db57) (struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) \*cb) |
|  | Register callbacks that will be called when a certain configuration or state changes occur within OpenThread. |
| int | [openthread\_state\_changed\_callback\_unregister](#ae4ad25613f8eada1a0a29426a2f4a518) (struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) \*cb) |
|  | Unregister OpenThread configuration or state changed callbacks. |
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [openthread\_thread\_id\_get](#a9499c4c69a0094f0b7ef803ac05fb19a) (void) |
|  | Get OpenThread thread identification. |
| struct otInstance \* | [openthread\_get\_default\_instance](#a517a538fa32afac8ca8968ada2cea89d) (void) |
|  | Get pointer to default OpenThread instance. |
| int | [openthread\_init](#a4d213cad99e6eeb747bd0057248251e5) (void) |
|  | Initialize the OpenThread module. |
| int | [openthread\_run](#a558165d2e49e9335649c94ac0be53392) (void) |
|  | Run the OpenThread network. |
| int | [openthread\_stop](#af52cc96d5d4be673f16eb4856de6cc58) (void) |
|  | Disable the OpenThread network. |
| void | [openthread\_set\_receive\_cb](#a14ea88a5f4e4a9e014f2381cd853e8de) ([openthread\_receive\_cb](#a8f95392e11afa85e9bd80569c1793e76) cb, void \*context) |
|  | Set the additional callback for receiving packets. |
| void | [openthread\_mutex\_lock](#ae3945bc3549118dc5420f9859588282d) (void) |
|  | Lock internal mutex before accessing OpenThread API. |
| int | [openthread\_mutex\_try\_lock](#ab5669622dfd83d3a5175fa47325dade3) (void) |
|  | Try to lock internal mutex before accessing OpenThread API. |
| void | [openthread\_mutex\_unlock](#a420c3321272141f63ea86166b84ec845) (void) |
|  | Unlock internal mutex after accessing OpenThread API. |

## Typedef Documentation

## [◆ ](#a8f95392e11afa85e9bd80569c1793e76)openthread\_receive\_cb

| typedef void(\* openthread\_receive\_cb) (struct otMessage \*message, void \*context) |
| --- |

The common callback type for receiving IPv4 (translated by NAT64) and IPv6 datagrams.

This callback is called when a datagram is received.

Parameters
:   | message | The message to receive. |
    | --- | --- |
    | context | The context to pass to the callback. |

## Function Documentation

## [◆ ](#a517a538fa32afac8ca8968ada2cea89d)openthread\_get\_default\_instance()

| struct otInstance \* openthread\_get\_default\_instance | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get pointer to default OpenThread instance.

Return values
:   | !NULL | On success. |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | On failure. |

## [◆ ](#a4d213cad99e6eeb747bd0057248251e5)openthread\_init()

| int openthread\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize the OpenThread module.

This function:

- Initializes the OpenThread module.
- Creates an OpenThread single instance.
- Starts the shell.
- Enables the UART and NCP HDLC for coprocessor purposes.
- Initializes the NAT64 translator.
- Creates a work queue for the OpenThread module.

Note
:   This function is automatically called by Zephyr's networking layer. If you want to initialize the OpenThread independently, call this function in your application init code.

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EIO | On failure. |

## [◆ ](#ae3945bc3549118dc5420f9859588282d)openthread\_mutex\_lock()

| void openthread\_mutex\_lock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Lock internal mutex before accessing OpenThread API.

OpenThread API is not thread-safe. Therefore, before accessing any API function, you need to lock the internal mutex, to prevent the OpenThread thread from pre-empting the API call.

## [◆ ](#ab5669622dfd83d3a5175fa47325dade3)openthread\_mutex\_try\_lock()

| int openthread\_mutex\_try\_lock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Try to lock internal mutex before accessing OpenThread API.

This function behaves like [openthread\_mutex\_lock()](#ae3945bc3549118dc5420f9859588282d), provided that the internal mutex is unlocked. Otherwise, it returns a negative value without waiting.

## [◆ ](#a420c3321272141f63ea86166b84ec845)openthread\_mutex\_unlock()

| void openthread\_mutex\_unlock | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Unlock internal mutex after accessing OpenThread API.

## [◆ ](#a558165d2e49e9335649c94ac0be53392)openthread\_run()

| int openthread\_run | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Run the OpenThread network.

Prepares the OpenThread network and enables it. Depends on active settings: it uses the stored network configuration, starts the joining procedure or uses the default network configuration. Additionally, when the device is MTD, it sets the SED mode to properly attach the network.

## [◆ ](#a14ea88a5f4e4a9e014f2381cd853e8de)openthread\_set\_receive\_cb()

| void openthread\_set\_receive\_cb | ( | [openthread\_receive\_cb](#a8f95392e11afa85e9bd80569c1793e76) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *context* ) |

Set the additional callback for receiving packets.

This callback is called once a packet is received and can be used to inject packets into the Zephyr networking stack. Setting this callback is optional.

Parameters
:   | cb | Callback to set. |
    | --- | --- |
    | context | Context to pass to the callback. |

## [◆ ](#a4178b72288585869e2c941acdc21db57)openthread\_state\_changed\_callback\_register()

| int openthread\_state\_changed\_callback\_register | ( | struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Register callbacks that will be called when a certain configuration or state changes occur within OpenThread.

Parameters
:   | cb | Callback struct to register. |
    | --- | --- |

## [◆ ](#ae4ad25613f8eada1a0a29426a2f4a518)openthread\_state\_changed\_callback\_unregister()

| int openthread\_state\_changed\_callback\_unregister | ( | struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Unregister OpenThread configuration or state changed callbacks.

Parameters
:   | cb | Callback struct to unregister. |
    | --- | --- |

## [◆ ](#af52cc96d5d4be673f16eb4856de6cc58)openthread\_stop()

| int openthread\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable the OpenThread network.

## [◆ ](#a9499c4c69a0094f0b7ef803ac05fb19a)openthread\_thread\_id\_get()

| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) openthread\_thread\_id\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get OpenThread thread identification.

- [modules](dir_e05d7e2b1ecd646af5bb94391405f3b5.md)
- [openthread](dir_31612689e320779a8afe131e155c6b49.md)
- [include](dir_8ac3cad2d91a5e145958cbd7c9ff59cb.md)
- [openthread.h](modules_2openthread_2include_2openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
