---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__dma__interface.html
original_path: doxygen/html/group__dma__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DMA Interface

[Device Driver APIs](group__io__interfaces.md)

DMA Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [dma\_block\_config](structdma__block__config.md) |
|  | DMA block configuration structure. [More...](structdma__block__config.md#details) |
| struct | [dma\_config](structdma__config.md) |
|  | DMA configuration structure. [More...](structdma__config.md#details) |
| struct | [dma\_status](structdma__status.md) |
|  | DMA runtime status structure. [More...](structdma__status.md#details) |
| struct | [dma\_context](structdma__context.md) |
|  | DMA context structure Note: the [dma\_context](structdma__context.md "DMA context structure Note: the dma_context shall be the first member of DMA client driver Data,...") shall be the first member of DMA client driver Data, got by dev->data. [More...](structdma__context.md#details) |

| Macros | |
| --- | --- |
| #define | [DMA\_STATUS\_COMPLETE](#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)   0 |
|  | The DMA callback event has occurred at the completion of a transfer list. |
| #define | [DMA\_STATUS\_BLOCK](#gab74c89289c8429071522cb89ac066eea)   1 |
|  | The DMA callback has occurred at the completion of a single transfer block in a transfer list. |
| #define | [DMA\_MAGIC](#gae28ba5114dc2e9ecb89ccf9b623e938f)   0x47494749 |
|  | Magic code to identify context content. |
| #define | [DMA\_BUF\_ADDR\_ALIGNMENT](#ga542e1a0fa0d851a51e4c8abf9a820e0c)(node) |
|  | Get the device tree property describing the buffer address alignment. |
| #define | [DMA\_BUF\_SIZE\_ALIGNMENT](#ga76dfdfecc732319908f381883c630a2b)(node) |
|  | Get the device tree property describing the buffer size alignment. |
| #define | [DMA\_COPY\_ALIGNMENT](#ga083e8b0a863b0833c55158053d286f15)(node) |
|  | Get the device tree property describing the minimal chunk of data possible to be copied. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [dma\_callback\_t](#ga94745b4472ee1addd4f82db4e59e9fb5)) (const struct [device](structdevice.md) \*dev, void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, int status) |
|  | Callback function for DMA transfer completion. |

| Enumerations | |
| --- | --- |
| enum | [dma\_channel\_direction](#gae442d8ba73be7e53b68165647b0ea402) {     [MEMORY\_TO\_MEMORY](#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5) = 0x0 , [MEMORY\_TO\_PERIPHERAL](#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a) , [PERIPHERAL\_TO\_MEMORY](#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165) , [PERIPHERAL\_TO\_PERIPHERAL](#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449) ,     [HOST\_TO\_MEMORY](#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c) , [MEMORY\_TO\_HOST](#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60) , [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a) , [DMA\_CHANNEL\_DIRECTION\_PRIV\_START](#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037) = DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT ,     [DMA\_CHANNEL\_DIRECTION\_MAX](#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02) = 0x7   } |
|  | DMA channel direction. [More...](#gae442d8ba73be7e53b68165647b0ea402) |
| enum | [dma\_addr\_adj](#gafe0877ef4bd7790a4bcd46052088231c) { [DMA\_ADDR\_ADJ\_INCREMENT](#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e) , [DMA\_ADDR\_ADJ\_DECREMENT](#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717) , [DMA\_ADDR\_ADJ\_NO\_CHANGE](#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f) } |
|  | DMA address adjustment. [More...](#gafe0877ef4bd7790a4bcd46052088231c) |
| enum | [dma\_channel\_filter](#gade594552920aabbfd2106059a338498b) { [DMA\_CHANNEL\_NORMAL](#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f) , [DMA\_CHANNEL\_PERIODIC](#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c) } |
|  | DMA channel attributes. [More...](#gade594552920aabbfd2106059a338498b) |
| enum | [dma\_attribute\_type](#ga08c366c8d47672eeeb37b258af20101b) { [DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT](#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f) , [DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT](#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873) , [DMA\_ATTR\_COPY\_ALIGNMENT](#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b) , [DMA\_ATTR\_MAX\_BLOCK\_COUNT](#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18) } |
|  | DMA attributes. [More...](#ga08c366c8d47672eeeb37b258af20101b) |

| Functions | |
| --- | --- |
| static int | [dma\_config](#ga6df1a6b89f271a0eae01c17b748bd2df) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, struct dma\_config \*config) |
|  | Configure individual channel for DMA transfer. |
| static int | [dma\_reload](#ga55bd5d550349c11c63ef47c2ed861f36) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Reload buffer(s) for a DMA channel. |
| int | [dma\_start](#gac2ddafd17680f59e4e8fe5f6e2eaba48) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Enables DMA channel and starts the transfer, the channel must be configured beforehand. |
| int | [dma\_stop](#ga305cc72d0804028b77aa82dd07c926ad) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Stops the DMA transfer and disables the channel. |
| int | [dma\_suspend](#ga6779850f6082259f5bef29b1282effdb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Suspend a DMA channel transfer. |
| int | [dma\_resume](#ga89a3d056803d7f2dd1c8b6e535ef4f1d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Resume a DMA channel transfer. |
| int | [dma\_request\_channel](#ga91cc55f781744069f1f9f29249bdee8d) (const struct [device](structdevice.md) \*dev, void \*filter\_param) |
|  | request DMA channel. |
| void | [dma\_release\_channel](#gab02df5277d79a04a65132365e7b5d3de) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | release DMA channel. |
| int | [dma\_chan\_filter](#ga729d8f1163458d447d0a4b20cb9e4659) (const struct [device](structdevice.md) \*dev, int channel, void \*filter\_param) |
|  | DMA channel filter. |
| static int | [dma\_get\_status](#ga2cae500f1f9ed42ad338a40ec8655544) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, struct [dma\_status](structdma__status.md) \*[stat](structstat.md)) |
|  | get current runtime status of DMA transfer |
| static int | [dma\_get\_attribute](#ga641f3fa492bfb17cf9f0a0361d429257) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | get attribute of a dma controller |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dma\_width\_index](#gadd1724a843bba4ccc1c65c9fb9d3d921) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Look-up generic width index to be used in registers. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dma\_burst\_index](#gaac27f2ee664671884087ee3d2a2863ce) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) burst) |
|  | Look-up generic burst index to be used in registers. |

## Detailed Description

DMA Interface.

Since
:   1.5

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga542e1a0fa0d851a51e4c8abf9a820e0c)DMA\_BUF\_ADDR\_ALIGNMENT

| #define DMA\_BUF\_ADDR\_ALIGNMENT | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, dma\_buf\_addr\_alignment)

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

Get the device tree property describing the buffer address alignment.

Useful when statically defining or allocating buffers for DMA usage where memory alignment often matters.

Parameters
:   | node | Node identifier, e.g. [DT\_NODELABEL(dma\_0)](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79 "Get a node identifier for a node label.") |
    | --- | --- |

Returns
:   alignment Memory byte alignment required for DMA buffers

## [◆ ](#ga76dfdfecc732319908f381883c630a2b)DMA\_BUF\_SIZE\_ALIGNMENT

| #define DMA\_BUF\_SIZE\_ALIGNMENT | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, dma\_buf\_size\_alignment)

Get the device tree property describing the buffer size alignment.

Useful when statically defining or allocating buffers for DMA usage where memory alignment often matters.

Parameters
:   | node | Node identifier, e.g. [DT\_NODELABEL(dma\_0)](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79 "Get a node identifier for a node label.") |
    | --- | --- |

Returns
:   alignment Memory byte alignment required for DMA buffers

## [◆ ](#ga083e8b0a863b0833c55158053d286f15)DMA\_COPY\_ALIGNMENT

| #define DMA\_COPY\_ALIGNMENT | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node, dma\_copy\_alignment)

Get the device tree property describing the minimal chunk of data possible to be copied.

Parameters
:   | node | Node identifier, e.g. [DT\_NODELABEL(dma\_0)](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79 "Get a node identifier for a node label.") |
    | --- | --- |

Returns
:   minimal Minimal chunk of data possible to be copied

## [◆ ](#gae28ba5114dc2e9ecb89ccf9b623e938f)DMA\_MAGIC

| #define DMA\_MAGIC   0x47494749 |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Magic code to identify context content.

## [◆ ](#gab74c89289c8429071522cb89ac066eea)DMA\_STATUS\_BLOCK

| #define DMA\_STATUS\_BLOCK   1 |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

The DMA callback has occurred at the completion of a single transfer block in a transfer list.

## [◆ ](#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)DMA\_STATUS\_COMPLETE

| #define DMA\_STATUS\_COMPLETE   0 |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

The DMA callback event has occurred at the completion of a transfer list.

## Typedef Documentation

## [◆ ](#ga94745b4472ee1addd4f82db4e59e9fb5)dma\_callback\_t

| typedef void(\* dma\_callback\_t) (const struct [device](structdevice.md) \*dev, void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, int status) |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Callback function for DMA transfer completion.

If enabled, callback function will be invoked at transfer or block completion, or when an error happens. In circular mode, `status` indicates that the DMA device has reached either the end of the buffer (DMA\_STATUS\_COMPLETE) or a water mark (DMA\_STATUS\_BLOCK).

Parameters
:   | dev | Pointer to the DMA device calling the callback. |
    | --- | --- |
    | user\_data | A pointer to some user data or NULL |
    | channel | The channel number |
    | status | Status of the transfer  - DMA\_STATUS\_COMPLETE buffer fully consumed - DMA\_STATUS\_BLOCK buffer consumption reached a configured block or water mark - A negative errno otherwise |

## Enumeration Type Documentation

## [◆ ](#gafe0877ef4bd7790a4bcd46052088231c)dma\_addr\_adj

| enum [dma\_addr\_adj](#gafe0877ef4bd7790a4bcd46052088231c) |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

DMA address adjustment.

Valid values for *source\_addr\_adj* and *dest\_addr\_adj*

| Enumerator | |
| --- | --- |
| DMA\_ADDR\_ADJ\_INCREMENT | Increment the address. |
| DMA\_ADDR\_ADJ\_DECREMENT | Decrement the address. |
| DMA\_ADDR\_ADJ\_NO\_CHANGE | No change the address. |

## [◆ ](#ga08c366c8d47672eeeb37b258af20101b)dma\_attribute\_type

| enum [dma\_attribute\_type](#ga08c366c8d47672eeeb37b258af20101b) |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

DMA attributes.

| Enumerator | |
| --- | --- |
| DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT |  |
| DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT |  |
| DMA\_ATTR\_COPY\_ALIGNMENT |  |
| DMA\_ATTR\_MAX\_BLOCK\_COUNT |  |

## [◆ ](#gae442d8ba73be7e53b68165647b0ea402)dma\_channel\_direction

| enum [dma\_channel\_direction](#gae442d8ba73be7e53b68165647b0ea402) |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

DMA channel direction.

| Enumerator | |
| --- | --- |
| MEMORY\_TO\_MEMORY | Memory to memory. |
| MEMORY\_TO\_PERIPHERAL | Memory to peripheral. |
| PERIPHERAL\_TO\_MEMORY | Peripheral to memory. |
| PERIPHERAL\_TO\_PERIPHERAL | Peripheral to peripheral. |
| HOST\_TO\_MEMORY | Host to memory. |
| MEMORY\_TO\_HOST | Memory to host. |
| DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT | Number of all common channel directions. |
| DMA\_CHANNEL\_DIRECTION\_PRIV\_START | This and higher values are dma controller or soc specific.  Refer to the specified dma driver header file. |
| DMA\_CHANNEL\_DIRECTION\_MAX | Maximum allowed value (3 bit field!). |

## [◆ ](#gade594552920aabbfd2106059a338498b)dma\_channel\_filter

| enum [dma\_channel\_filter](#gade594552920aabbfd2106059a338498b) |
| --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

DMA channel attributes.

| Enumerator | |
| --- | --- |
| DMA\_CHANNEL\_NORMAL |  |
| DMA\_CHANNEL\_PERIODIC |  |

## Function Documentation

## [◆ ](#gaac27f2ee664671884087ee3d2a2863ce)dma\_burst\_index()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_burst\_index | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *burst* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Look-up generic burst index to be used in registers.

Warning
:   This look-up works for most controllers, but *may* not work for yours. Ensure your controller expects the most common register bit values before using this convenience function. If your controller does not support these values, you will have to write your own look-up inside the controller driver.

Parameters
:   | burst | number of bytes to be sent in a single burst |
    | --- | --- |

Return values
:   | common | DMA index to be placed into registers. |
    | --- | --- |

## [◆ ](#ga729d8f1163458d447d0a4b20cb9e4659)dma\_chan\_filter()

| int dma\_chan\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *channel*, |
|  |  | void \* | *filter\_param* ) |

`#include <[dma.h](drivers_2dma_8h.md)>`

DMA channel filter.

filter channel by attribute

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | channel number |
    | filter\_param | filter attribute |

Return values
:   | Negative | errno code if not support |
    | --- | --- |

## [◆ ](#ga6df1a6b89f271a0eae01c17b748bd2df)dma\_config()

| | int dma\_config | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | struct dma\_config \* | *config* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Configure individual channel for DMA transfer.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel to configure |
    | config | Data structure containing the intended configuration for the selected channel |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga641f3fa492bfb17cf9f0a0361d429257)dma\_get\_attribute()

| | int dma\_get\_attribute | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *type*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *value* ) | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

get attribute of a dma controller

This function allows to get a device specific static or runtime attribute like required address and size alignment of a buffer. Implementations must check the validity of the type passed in and return -EINVAL if it is invalid or -ENOSYS if not supported.

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | type | Numeric identification of the attribute |
    | value | A non-NULL pointer to the variable where the read value is to be placed |

Return values
:   | non-negative | if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga2cae500f1f9ed42ad338a40ec8655544)dma\_get\_status()

| | int dma\_get\_status | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | struct [dma\_status](structdma__status.md) \* | *stat* ) | | inlinestaticisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

get current runtime status of DMA transfer

Implementations must check the validity of the channel ID passed in and return -EINVAL if it is invalid or -ENOSYS if not supported.

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel where the transfer was being processed |
    | [stat](structstat.md) | a non-NULL [dma\_status](structdma__status.md "DMA runtime status structure.") object for storing DMA status |

Return values
:   | non-negative | if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#gab02df5277d79a04a65132365e7b5d3de)dma\_release\_channel()

| void dma\_release\_channel | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) |

`#include <[dma.h](drivers_2dma_8h.md)>`

release DMA channel.

release DMA channel resources

Note
:   It is safe to use this function in contexts where blocking is not allowed, e.g. ISR, provided the implementation of the release function does not block.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | channel number |

## [◆ ](#ga55bd5d550349c11c63ef47c2ed861f36)dma\_reload()

| | int dma\_reload | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *src*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dst*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Reload buffer(s) for a DMA channel.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel to configure selected channel |
    | src | source address for the DMA transfer |
    | dst | destination address for the DMA transfer |
    | size | size of DMA transfer |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga91cc55f781744069f1f9f29249bdee8d)dma\_request\_channel()

| int dma\_request\_channel | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | void \* | *filter\_param* ) |

`#include <[dma.h](drivers_2dma_8h.md)>`

request DMA channel.

request DMA channel resources return -EINVAL if there is no valid channel available.

Note
:   It is safe to use this function in contexts where blocking is not allowed, e.g. ISR, provided the implementation of the filter function does not block.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | filter\_param | filter function parameter |

Return values
:   | dma | channel if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga89a3d056803d7f2dd1c8b6e535ef4f1d)dma\_resume()

| | int dma\_resume | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Resume a DMA channel transfer.

Implementations must check the validity of the channel state and ID passed in and return -EINVAL if either are invalid.

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel to resume |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If not implemented |
    | -EINVAL | If invalid channel id or state. |
    | -errno | Other negative errno code failure. |

## [◆ ](#gac2ddafd17680f59e4e8fe5f6e2eaba48)dma\_start()

| | int dma\_start | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Enables DMA channel and starts the transfer, the channel must be configured beforehand.

Implementations must check the validity of the channel ID passed in and return -EINVAL if it is invalid.

Start is allowed on channels that have already been started and must report success.

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel where the transfer will be processed |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga305cc72d0804028b77aa82dd07c926ad)dma\_stop()

| | int dma\_stop | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Stops the DMA transfer and disables the channel.

Implementations must check the validity of the channel ID passed in and return -EINVAL if it is invalid.

Stop is allowed on channels that have already been stopped and must report success.

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel where the transfer was being processed |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga6779850f6082259f5bef29b1282effdb)dma\_suspend()

| | int dma\_suspend | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel* ) | | isr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Suspend a DMA channel transfer.

Implementations must check the validity of the channel state and ID passed in and return -EINVAL if either are invalid.

Function properties (list may not be complete)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Numeric identification of the channel to suspend |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If not implemented. |
    | -EINVAL | If invalid channel id or state. |
    | -errno | Other negative errno code failure. |

## [◆ ](#gadd1724a843bba4ccc1c65c9fb9d3d921)dma\_width\_index()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_width\_index | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dma.h](drivers_2dma_8h.md)>`

Look-up generic width index to be used in registers.

Warning
:   This look-up works for most controllers, but *may* not work for yours. Ensure your controller expects the most common register bit values before using this convenience function. If your controller does not support these values, you will have to write your own look-up inside the controller driver.

Parameters
:   | size | width of bus (in bytes) |
    | --- | --- |

Return values
:   | common | DMA index to be placed into registers. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
