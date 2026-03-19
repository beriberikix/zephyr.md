---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mbox__interface.html
original_path: doxygen/html/group__mbox__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| struct | [mbox\_dt\_spec](structmbox__dt__spec.md) |
|  | MBOX specification from DT. [More...](structmbox__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [MBOX\_DT\_SPEC\_GET](#gadd0a5b06ab4b208460cf49952a2b4b43)(node\_id, name) |
|  | Structure initializer for struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") from devicetree. |
| #define | [MBOX\_DT\_SPEC\_INST\_GET](#gafb05876cbac7967d93d9ffccbd4761a5)(inst, name) |
|  | Instance version of MBOX\_DT\_CHANNEL\_GET(). |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) |
|  | Type for MBOX channel identifiers. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mbox\_is\_ready\_dt](#gab1bea02e9f49442b7454706fb434f5f2) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec) |
|  | Validate if MBOX device instance from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") is ready. |
| int | [mbox\_send](#gaf4d02fb3a3ed788ba28a58783209d359) (const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Try to send a message over the MBOX device. |
| static int | [mbox\_send\_dt](#ga8f737ce94afac19dd8924526d48c68ba) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec, const struct [mbox\_msg](structmbox__msg.md) \*msg) |
|  | Try to send a message over the MBOX device from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| static int | [mbox\_register\_callback](#gac1cc65cc54b9c7e6cf2639152a4d6a7a) (const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, mbox\_callback\_t cb, void \*user\_data) |
|  | Register a callback function on a channel for incoming messages. |
| static int | [mbox\_register\_callback\_dt](#ga9cda3048389f4f57d425eac8257048a7) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec, mbox\_callback\_t cb, void \*user\_data) |
|  | Register a callback function on a channel for incoming messages from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| int | [mbox\_mtu\_get](#ga82d9def1b5c31c574d2114abcce2eb1f) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of bytes possible in an outbound message. |
| static int | [mbox\_mtu\_get\_dt](#ga9565933b282fe8e5fd057fbb238e00b9) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec) |
|  | Return the maximum number of bytes possible in an outbound message from struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| int | [mbox\_set\_enabled](#ga9eea4b9501751919125cd6124f9e9868) (const struct [device](structdevice.md) \*dev, [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) channel\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Enable (disable) interrupts and callbacks for inbound channels. |
| static int | [mbox\_set\_enabled\_dt](#ga50282848e03481fe8b6f5caa900892d3) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Enable (disable) interrupts and callbacks for inbound channels from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mbox\_max\_channels\_get](#gaf2f8adbd5e4f7f5972b2d34cfce68bdb) (const struct [device](structdevice.md) \*dev) |
|  | Return the maximum number of channels. |
| static int | [mbox\_max\_channels\_get\_dt](#gad9321777457f958e9291ded26e4ed5c6) (const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \*spec) |
|  | Return the maximum number of channels from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT."). |

## Detailed Description

MBOX Interface.

Since
:   1.0

Version
:   0.1.0

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
- [mbox\_send()](#gaf4d02fb3a3ed788ba28a58783209d359) must have (msg == NULL)
- the callback must be called with (data == NULL)

In data transfer mode:

- [mbox\_mtu\_get()](#ga82d9def1b5c31c574d2114abcce2eb1f) must return a (value != 0)
- [mbox\_send()](#gaf4d02fb3a3ed788ba28a58783209d359) must have (msg != NULL)
- the callback must be called with (data != NULL)
- The msg content must be the same between sender and receiver

## Macro Definition Documentation

## [◆ ](#gadd0a5b06ab4b208460cf49952a2b4b43)MBOX\_DT\_SPEC\_GET

| #define MBOX\_DT\_SPEC\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

**Value:**

{ \

.dev = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_MBOX\_CTLR\_BY\_NAME](group__devicetree-mbox.md#gabb96e9b997d99ed54d167d592d623ff7)(node\_id, name)), \

.channel\_id = [DT\_MBOX\_CHANNEL\_BY\_NAME](group__devicetree-mbox.md#ga4ea23945e3aacae6a8daacb4c24c88e4)(node\_id, name), \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:255

[DT\_MBOX\_CHANNEL\_BY\_NAME](group__devicetree-mbox.md#ga4ea23945e3aacae6a8daacb4c24c88e4)

#define DT\_MBOX\_CHANNEL\_BY\_NAME(node\_id, name)

Get a MBOX channel value by name.

**Definition** mbox.h:89

[DT\_MBOX\_CTLR\_BY\_NAME](group__devicetree-mbox.md#gabb96e9b997d99ed54d167d592d623ff7)

#define DT\_MBOX\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the MBOX controller from a mboxes property by name.

**Definition** mbox.h:52

Structure initializer for struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") from devicetree.

This helper macro expands to a static initializer for a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") by reading the relevant device controller and channel number from the devicetree.

Example devicetree fragment:

n: node {

mboxes = <&mbox1 8>,

<&mbox1 9>;

mbox-names = "tx", "rx";

};

Example usage:

const struct [mbox\_dt\_spec](structmbox__dt__spec.md) spec = [MBOX\_DT\_SPEC\_GET](#gadd0a5b06ab4b208460cf49952a2b4b43)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), tx);

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[MBOX\_DT\_SPEC\_GET](#gadd0a5b06ab4b208460cf49952a2b4b43)

#define MBOX\_DT\_SPEC\_GET(node\_id, name)

Structure initializer for struct mbox\_dt\_spec from devicetree.

**Definition** mbox.h:122

[mbox\_dt\_spec](structmbox__dt__spec.md)

MBOX specification from DT.

**Definition** mbox.h:87

Parameters
:   | node\_id | Devicetree node identifier for the MBOX device |
    | --- | --- |
    | name | lowercase-and-underscores name of the mboxes element |

Returns
:   static initializer for a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.")

## [◆ ](#gafb05876cbac7967d93d9ffccbd4761a5)MBOX\_DT\_SPEC\_INST\_GET

| #define MBOX\_DT\_SPEC\_INST\_GET | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

**Value:**

[MBOX\_DT\_SPEC\_GET](#gadd0a5b06ab4b208460cf49952a2b4b43)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

Instance version of MBOX\_DT\_CHANNEL\_GET().

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of the mboxes element |

Returns
:   static initializer for a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.")

## Typedef Documentation

## [◆ ](#gaf16ce0f9d2138b63165f6e9862c9df37)mbox\_channel\_id\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) |
| --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Type for MBOX channel identifiers.

## Function Documentation

## [◆ ](#gab1bea02e9f49442b7454706fb434f5f2)mbox\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mbox\_is\_ready\_dt | ( | const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Validate if MBOX device instance from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.") is ready.

Parameters
:   | spec | MBOX specification from devicetree |
    | --- | --- |

Returns
:   See return values for [mbox\_send()](#gaf4d02fb3a3ed788ba28a58783209d359)

## [◆ ](#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)mbox\_max\_channels\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mbox\_max\_channels\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Return the maximum number of channels.

Return the maximum number of channels supported by the hardware.

Parameters
:   | dev | MBOX device instance. |
    | --- | --- |

Returns
:   >0 Maximum possible number of supported channels on success
:   -errno Negative errno on error.

## [◆ ](#gad9321777457f958e9291ded26e4ed5c6)mbox\_max\_channels\_get\_dt()

| | int mbox\_max\_channels\_get\_dt | ( | const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Return the maximum number of channels from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.").

Parameters
:   | spec | MBOX specification from devicetree |
    | --- | --- |

Returns
:   See return values for [mbox\_max\_channels\_get()](#gaf2f8adbd5e4f7f5972b2d34cfce68bdb)

## [◆ ](#ga82d9def1b5c31c574d2114abcce2eb1f)mbox\_mtu\_get()

| int mbox\_mtu\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Return the maximum number of bytes possible in an outbound message.

Returns the actual number of bytes that it is possible to send through an outgoing channel.

This number can be 0 when the driver only supports signalling or when on the receiving side the content and size of the message must be retrieved in an indirect way (i.e. probing some other peripheral, reading memory regions, etc...).

If this function returns 0, the msg parameter in [mbox\_send()](#gaf4d02fb3a3ed788ba28a58783209d359) is expected to be NULL.

Parameters
:   | dev | MBOX device instance. |
    | --- | --- |

Return values
:   | >0 | Maximum possible size of a message in bytes |
    | --- | --- |
    | 0 | Indicates signalling |
    | -errno | Negative errno on error. |

## [◆ ](#ga9565933b282fe8e5fd057fbb238e00b9)mbox\_mtu\_get\_dt()

| | int mbox\_mtu\_get\_dt | ( | const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Return the maximum number of bytes possible in an outbound message from struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.").

Parameters
:   | spec | MBOX specification from devicetree |
    | --- | --- |

Returns
:   See return values for [mbox\_register\_callback()](#gac1cc65cc54b9c7e6cf2639152a4d6a7a)

## [◆ ](#gac1cc65cc54b9c7e6cf2639152a4d6a7a)mbox\_register\_callback()

| | int mbox\_register\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) | *channel\_id*, | |  |  | mbox\_callback\_t | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Register a callback function on a channel for incoming messages.

This function doesn't assume anything concerning the status of the interrupts. Use [mbox\_set\_enabled()](#ga9eea4b9501751919125cd6124f9e9868) to enable or to disable the interrupts if needed.

Parameters
:   | dev | MBOX device instance |
    | --- | --- |
    | channel\_id | MBOX channel identifier |
    | cb | Callback function to execute on incoming message interrupts. |
    | user\_data | Application-specific data pointer which will be passed to the callback function when executed. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -errno | Negative errno on error. |

## [◆ ](#ga9cda3048389f4f57d425eac8257048a7)mbox\_register\_callback\_dt()

| | int mbox\_register\_callback\_dt | ( | const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | mbox\_callback\_t | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Register a callback function on a channel for incoming messages from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.").

Parameters
:   | spec | MBOX specification from devicetree |
    | --- | --- |
    | cb | Callback function to execute on incoming message interrupts. |
    | user\_data | Application-specific data pointer which will be passed to the callback function when executed. |

Returns
:   See return values for [mbox\_register\_callback()](#gac1cc65cc54b9c7e6cf2639152a4d6a7a)

## [◆ ](#gaf4d02fb3a3ed788ba28a58783209d359)mbox\_send()

| int mbox\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) | *channel\_id*, |
|  |  | const struct [mbox\_msg](structmbox__msg.md) \* | *msg* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Try to send a message over the MBOX device.

Send a message over an struct mbox\_channel. The msg parameter must be NULL when the driver is used for signalling.

If the msg parameter is not NULL, this data is expected to be delivered on the receiving side using the data parameter of the receiving callback.

Parameters
:   | dev | MBOX device instance |
    | --- | --- |
    | channel\_id | MBOX channel identifier |
    | msg | Message |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EBUSY | If the remote hasn't yet read the last data sent. |
    | -EMSGSIZE | If the supplied data size is unsupported by the driver. |
    | -EINVAL | If there was a bad parameter, such as: too-large channel descriptor or the device isn't an outbound MBOX channel. |

## [◆ ](#ga8f737ce94afac19dd8924526d48c68ba)mbox\_send\_dt()

| | int mbox\_send\_dt | ( | const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | const struct [mbox\_msg](structmbox__msg.md) \* | *msg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Try to send a message over the MBOX device from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.").

Parameters
:   | spec | MBOX specification from devicetree |
    | --- | --- |
    | msg | Message |

Returns
:   See return values for [mbox\_send()](#gaf4d02fb3a3ed788ba28a58783209d359)

## [◆ ](#ga9eea4b9501751919125cd6124f9e9868)mbox\_set\_enabled()

| int mbox\_set\_enabled | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [mbox\_channel\_id\_t](#gaf16ce0f9d2138b63165f6e9862c9df37) | *channel\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enabled* ) |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Enable (disable) interrupts and callbacks for inbound channels.

Enable interrupt for the channel when the parameter 'enable' is set to true. Disable it otherwise.

Immediately after calling this function with 'enable' set to true, the channel is considered enabled and ready to receive signal and messages (even already pending), so the user must take care of installing a proper callback (if needed) using [mbox\_register\_callback()](#gac1cc65cc54b9c7e6cf2639152a4d6a7a) on the channel before enabling it. For this reason it is recommended that all the channels are disabled at probe time.

Enabling a channel for which there is no installed callback is considered undefined behavior (in general the driver must take care of gracefully handling spurious interrupts with no installed callback).

Parameters
:   | dev | MBOX device instance |
    | --- | --- |
    | channel\_id | MBOX channel identifier |
    | enabled | Enable (true) or disable (false) the channel. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If it isn't an inbound channel. |
    | -EALREADY | If channel is already `enabled`. |

## [◆ ](#ga50282848e03481fe8b6f5caa900892d3)mbox\_set\_enabled\_dt()

| | int mbox\_set\_enabled\_dt | ( | const struct [mbox\_dt\_spec](structmbox__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enabled* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mbox.h](drivers_2mbox_8h.md)>`

Enable (disable) interrupts and callbacks for inbound channels from a struct [mbox\_dt\_spec](structmbox__dt__spec.md "MBOX specification from DT.").

Parameters
:   | spec | MBOX specification from devicetree |
    | --- | --- |
    | enabled | Enable (true) or disable (false) the channel. |

Returns
:   See return values for [mbox\_set\_enabled()](#ga9eea4b9501751919125cd6124f9e9868)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
