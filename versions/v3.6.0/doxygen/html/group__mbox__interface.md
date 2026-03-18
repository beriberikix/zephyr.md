---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mbox__interface.html
original_path: doxygen/html/group__mbox__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MBOX Interface

[Device Driver APIs](group__io__interfaces.md)

MBOX Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mbox\_msg](structmbox__msg.md) |
|  | Message struct (to hold data and its size). [More...](structmbox__msg.md#details) |
| struct | [mbox\_channel](structmbox__channel.md) |
|  | Provides a type to hold an MBOX channel. [More...](structmbox__channel.md#details) |
| struct | [mbox\_driver\_api](structmbox__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [MBOX\_DT\_CHANNEL\_GET](#ga9e02e3a523a63ff564ce2bb42c03aa1f)(node\_id, name) |
|  | Structure initializer for [mbox\_channel](structmbox__channel.md "Provides a type to hold an MBOX channel.") from devicetree. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mbox\_callback\_t](#ga3f1273aa6518b36f6c7f95e57292b7b8)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, void \*user\_data, struct [mbox\_msg](structmbox__msg.md) \*data) |
|  | Callback API for incoming MBOX messages. |
| typedef int(\* | [mbox\_send\_t](#gaaecf1d595053c6ea282abb0bbe637beb)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Callback API to send MBOX messages. |
| typedef int(\* | [mbox\_mtu\_get\_t](#gadce4d6561407c2d8d7bc54a0b7350297)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get maximum data size. |
| typedef int(\* | [mbox\_register\_callback\_t](#gac8959349175e67d0e02f98252a52647b)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [mbox\_callback\_t](#ga3f1273aa6518b36f6c7f95e57292b7b8) cb, void \*user\_data) |
|  | Callback API upon registration. |
| typedef int(\* | [mbox\_set\_enabled\_t](#ga64dad0e5a73903e3a55d619838f53176)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Callback API upon enablement of interrupts. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [mbox\_max\_channels\_get\_t](#ga822c7691cdd429f18f2e5e922102ef1c)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get maximum number of channels. |

| Functions | |
| --- | --- |
| static void | [mbox\_init\_channel](#ga70253c432c8064a2760731f1d237f2b7) (struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ch\_id) |
|  | Initialize a channel struct. |
| int | [mbox\_send](#ga18828e5c28201ad838ed9ba7c0afabfe) (const struct [mbox\_channel](structmbox__channel.md) \*channel, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Try to send a message over the MBOX device. |
| static int | [mbox\_register\_callback](#gad48e48c984e70348336a896bb2835c77) (const struct [mbox\_channel](structmbox__channel.md) \*channel, [mbox\_callback\_t](#ga3f1273aa6518b36f6c7f95e57292b7b8) cb, void \*user\_data) |
|  | Register a callback function on a channel for incoming messages. |
| int | [mbox\_mtu\_get](#ga82d9def1b5c31c574d2114abcce2eb1f) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of bytes possible in an outbound message. |
| int | [mbox\_set\_enabled](#ga563c6c0e2199b0608b2cd0606c46fc81) (const struct [mbox\_channel](structmbox__channel.md) \*channel, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable (disable) interrupts and callbacks for inbound channels. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mbox\_max\_channels\_get](#gaf2f8adbd5e4f7f5972b2d34cfce68bdb) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of channels. |

## Detailed Description

MBOX Interface.

CPU #1 |

+----------+ | +----------+

| +---TX9----+ +--------+--RX8---+ |

| dev A | | | | | CPU #2 |

| <---RX8--+ | | +------+--TX9---> |

+----------+ | | | | | +----------+

+--+-v---v-+--+ |

| | |

| MBOX dev | |

| | |

+--+-^---^--+-+ |

+----------+ | | | | | +----------+

| <---RX2--+ | | +-----+--TX3---> |

| dev B | | | | | CPU #3 |

| +---TX3----+ +--------+--RX2---+ |

+----------+ | +----------+

|

An MBOX device is a peripheral capable of passing signals (and data depending on the peripheral) between CPUs and clusters in the system. Each MBOX instance is providing one or more channels, each one targeting one other CPU cluster (multiple channels can target the same cluster).

For example in the plot the device 'dev A' is using the TX channel 9 to signal (or send data to) the CPU #2 and it's expecting data or signals on the RX channel 8. Thus it can send the message through the channel 9, and it can register a callback on the channel 8 of the MBOX device.

This API supports two modes: signalling mode and data transfer mode.

In signalling mode:

- [mbox\_mtu\_get()](#ga82d9def1b5c31c574d2114abcce2eb1f) must return 0
- [mbox\_send()](#ga18828e5c28201ad838ed9ba7c0afabfe) must have (msg == NULL)
- the callback must be called with (data == NULL)

In data transfer mode:

- [mbox\_mtu\_get()](#ga82d9def1b5c31c574d2114abcce2eb1f) must return a (value != 0)
- [mbox\_send()](#ga18828e5c28201ad838ed9ba7c0afabfe) must have (msg != NULL)
- the callback must be called with (data != NULL)
- The msg content must be the same between sender and receiver

## Macro Definition Documentation

## [◆ ](#ga9e02e3a523a63ff564ce2bb42c03aa1f)MBOX\_DT\_CHANNEL\_GET

| #define MBOX\_DT\_CHANNEL\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

**Value:**

{ \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_MBOX\_CTLR\_BY\_NAME](group__devicetree-mbox.md#gabb96e9b997d99ed54d167d592d623ff7)(node\_id, name)), \

.id = [DT\_MBOX\_CHANNEL\_BY\_NAME](group__devicetree-mbox.md#ga4ea23945e3aacae6a8daacb4c24c88e4)(node\_id, name), \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_MBOX\_CHANNEL\_BY\_NAME](group__devicetree-mbox.md#ga4ea23945e3aacae6a8daacb4c24c88e4)

#define DT\_MBOX\_CHANNEL\_BY\_NAME(node\_id, name)

Get a MBOX channel value by name.

**Definition** mbox.h:89

[DT\_MBOX\_CTLR\_BY\_NAME](group__devicetree-mbox.md#gabb96e9b997d99ed54d167d592d623ff7)

#define DT\_MBOX\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the MBOX controller from a mboxes property by name.

**Definition** mbox.h:52

Structure initializer for [mbox\_channel](structmbox__channel.md "Provides a type to hold an MBOX channel.") from devicetree.

This helper macro expands to a static initializer for a `[mbox_channel](structmbox__channel.md "Provides a type to hold an MBOX channel.")` by reading the relevant device controller and channel number from the devicetree.

Example devicetree fragment:

```
mbox1: mbox-controller@... { ... };

n: node {
        mboxes = <&mbox1 8>,
                 <&mbox1 9>;
        mbox-names = "tx", "rx";
};
```

Example usage:

```
const struct mbox_channel channel = MBOX_DT_CHANNEL_GET(DT_NODELABEL(n), tx);
```

Parameters
:   | node\_id | Devicetree node identifier for the MBOX device |
    | --- | --- |
    | name | lowercase-and-underscores name of the mboxes element |

## Typedef Documentation

## [◆ ](#ga3f1273aa6518b36f6c7f95e57292b7b8)mbox\_callback\_t

| typedef void(\* mbox\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, void \*user\_data, struct [mbox\_msg](structmbox__msg.md) \*data) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Callback API for incoming MBOX messages.

These callbacks execute in interrupt context. Therefore, use only interrupt-safe APIS. Registration of callbacks is done via *[mbox\_register\_callback()](#gad48e48c984e70348336a896bb2835c77)*

The data parameter must be NULL in signalling mode.

Parameters
:   | dev | Driver instance |
    | --- | --- |
    | channel | Channel ID |
    | user\_data | Pointer to some private data provided at registration time |
    | data | Message struct |

## [◆ ](#ga822c7691cdd429f18f2e5e922102ef1c)mbox\_max\_channels\_get\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* mbox\_max\_channels\_get\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Callback API to get maximum number of channels.

See *[mbox\_max\_channels\_get()](#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)* for argument definitions.

## [◆ ](#gadce4d6561407c2d8d7bc54a0b7350297)mbox\_mtu\_get\_t

| typedef int(\* mbox\_mtu\_get\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Callback API to get maximum data size.

See *[mbox\_mtu\_get()](#ga82d9def1b5c31c574d2114abcce2eb1f)* for argument definitions.

## [◆ ](#gac8959349175e67d0e02f98252a52647b)mbox\_register\_callback\_t

| typedef int(\* mbox\_register\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [mbox\_callback\_t](#ga3f1273aa6518b36f6c7f95e57292b7b8) cb, void \*user\_data) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Callback API upon registration.

See *[mbox\_register\_callback()](#gad48e48c984e70348336a896bb2835c77)* for function description

Parameters
:   | dev | Driver instance |
    | --- | --- |
    | channel | Channel ID |
    | cb | Callback function to execute on incoming message interrupts. |
    | user\_data | Application-specific data pointer which will be passed to the callback function when executed. |

Returns
:   See return values for *[mbox\_register\_callback()](#gad48e48c984e70348336a896bb2835c77)*

## [◆ ](#gaaecf1d595053c6ea282abb0bbe637beb)mbox\_send\_t

| typedef int(\* mbox\_send\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Callback API to send MBOX messages.

See *[mbox\_send()](#ga18828e5c28201ad838ed9ba7c0afabfe)* for function description

Parameters
:   | dev | Driver instance |
    | --- | --- |
    | channel | Channel ID |
    | msg | Message struct |

Returns
:   See return values for *[mbox\_send()](#ga18828e5c28201ad838ed9ba7c0afabfe)*

## [◆ ](#ga64dad0e5a73903e3a55d619838f53176)mbox\_set\_enabled\_t

| typedef int(\* mbox\_set\_enabled\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Callback API upon enablement of interrupts.

See *[mbox\_set\_enabled()](#ga563c6c0e2199b0608b2cd0606c46fc81)* for function description

Parameters
:   | dev | Driver instance |
    | --- | --- |
    | channel | Channel ID |
    | enable | Set to 0 to disable and to nonzero to enable. |

Returns
:   See return values for *[mbox\_set\_enabled()](#ga563c6c0e2199b0608b2cd0606c46fc81)*

## Function Documentation

## [◆ ](#ga70253c432c8064a2760731f1d237f2b7)mbox\_init\_channel()

| | void mbox\_init\_channel | ( | struct [mbox\_channel](structmbox__channel.md) \* | *channel*, | | --- | --- | --- | --- | |  |  | const struct [device](structdevice.md) \* | *dev*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ch\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Initialize a channel struct.

Initialize an `[mbox_channel](structmbox__channel.md "Provides a type to hold an MBOX channel.")` passed by the user with a provided MBOX device and channel ID. This function is needed when the information about the device and the channel ID is not in the DT. In the DT case [MBOX\_DT\_CHANNEL\_GET()](#ga9e02e3a523a63ff564ce2bb42c03aa1f) must be used instead.

Parameters
:   | channel | Pointer to the channel struct |
    | --- | --- |
    | dev | Driver instance |
    | ch\_id | Channel ID |

## [◆ ](#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)mbox\_max\_channels\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mbox\_max\_channels\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Return the maximum number of channels.

Return the maximum number of channels supported by the hardware.

Parameters
:   | dev | Driver instance pointer. |
    | --- | --- |

Returns
:   Maximum possible number of supported channels on success, negative value on error.

## [◆ ](#ga82d9def1b5c31c574d2114abcce2eb1f)mbox\_mtu\_get()

| int mbox\_mtu\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Return the maximum number of bytes possible in an outbound message.

Returns the actual number of bytes that it is possible to send through an outgoing channel.

This number can be 0 when the driver only supports signalling or when on the receiving side the content and size of the message must be retrieved in an indirect way (i.e. probing some other peripheral, reading memory regions, etc...).

If this function returns 0, the msg parameter in *[mbox\_send()](#ga18828e5c28201ad838ed9ba7c0afabfe)* is expected to be NULL.

Parameters
:   | dev | Driver instance pointer. |
    | --- | --- |

Returns
:   Maximum possible size of a message in bytes, 0 for signalling, negative value on error.

## [◆ ](#gad48e48c984e70348336a896bb2835c77)mbox\_register\_callback()

| | int mbox\_register\_callback | ( | const struct [mbox\_channel](structmbox__channel.md) \* | *channel*, | | --- | --- | --- | --- | |  |  | [mbox\_callback\_t](#ga3f1273aa6518b36f6c7f95e57292b7b8) | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Register a callback function on a channel for incoming messages.

This function doesn't assume anything concerning the status of the interrupts. Use *[mbox\_set\_enabled()](#ga563c6c0e2199b0608b2cd0606c46fc81)* to enable or to disable the interrupts if needed.

Parameters
:   | channel | Channel instance pointer. |
    | --- | --- |
    | cb | Callback function to execute on incoming message interrupts. |
    | user\_data | Application-specific data pointer which will be passed to the callback function when executed. |

Return values
:   | 0 | On success, negative value on error. |
    | --- | --- |

## [◆ ](#ga18828e5c28201ad838ed9ba7c0afabfe)mbox\_send()

| int mbox\_send | ( | const struct [mbox\_channel](structmbox__channel.md) \* | *channel*, |
| --- | --- | --- | --- |
|  |  | const struct [mbox\_msg](structmbox__msg.md) \* | *msg* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Try to send a message over the MBOX device.

Send a message over an `[mbox_channel](structmbox__channel.md "Provides a type to hold an MBOX channel.")`. The msg parameter must be NULL when the driver is used for signalling.

If the msg parameter is not NULL, this data is expected to be delivered on the receiving side using the data parameter of the receiving callback.

Parameters
:   | channel | Channel instance pointer |
    | --- | --- |
    | msg | Pointer to the message struct |

Return values
:   | -EBUSY | If the remote hasn't yet read the last data sent. |
    | --- | --- |
    | -EMSGSIZE | If the supplied data size is unsupported by the driver. |
    | -EINVAL | If there was a bad parameter, such as: too-large channel descriptor or the device isn't an outbound MBOX channel. |
    | 0 | On success, negative value on error. |

## [◆ ](#ga563c6c0e2199b0608b2cd0606c46fc81)mbox\_set\_enabled()

| int mbox\_set\_enabled | ( | const struct [mbox\_channel](structmbox__channel.md) \* | *channel*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Enable (disable) interrupts and callbacks for inbound channels.

Enable interrupt for the channel when the parameter 'enable' is set to true. Disable it otherwise.

Immediately after calling this function with 'enable' set to true, the channel is considered enabled and ready to receive signal and messages (even already pending), so the user must take care of installing a proper callback (if needed) using *[mbox\_register\_callback()](#gad48e48c984e70348336a896bb2835c77)* on the channel before enabling it. For this reason it is recommended that all the channels are disabled at probe time.

Enabling a channel for which there is no installed callback is considered undefined behavior (in general the driver must take care of gracefully handling spurious interrupts with no installed callback).

Parameters
:   | channel | Channel instance pointer. |
    | --- | --- |
    | enable | Set to 0 to disable and to nonzero to enable. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If it isn't an inbound channel. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
