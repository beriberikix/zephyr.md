---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2dma_8h.html
original_path: doxygen/html/drivers_2dma_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma.h File Reference

Public APIs for the DMA drivers.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/dma.h>`

[Go to the source code of this file.](drivers_2dma_8h_source.md)

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
| #define | [DMA\_STATUS\_COMPLETE](group__dma__interface.md#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)   0 |
|  | The DMA callback event has occurred at the completion of a transfer list. |
| #define | [DMA\_STATUS\_BLOCK](group__dma__interface.md#gab74c89289c8429071522cb89ac066eea)   1 |
|  | The DMA callback has occurred at the completion of a single transfer block in a transfer list. |
| #define | [DMA\_MAGIC](group__dma__interface.md#gae28ba5114dc2e9ecb89ccf9b623e938f)   0x47494749 |
|  | Magic code to identify context content. |
| #define | [DMA\_BUF\_ADDR\_ALIGNMENT](group__dma__interface.md#ga542e1a0fa0d851a51e4c8abf9a820e0c)(node) |
|  | Get the device tree property describing the buffer address alignment. |
| #define | [DMA\_BUF\_SIZE\_ALIGNMENT](group__dma__interface.md#ga76dfdfecc732319908f381883c630a2b)(node) |
|  | Get the device tree property describing the buffer size alignment. |
| #define | [DMA\_COPY\_ALIGNMENT](group__dma__interface.md#ga083e8b0a863b0833c55158053d286f15)(node) |
|  | Get the device tree property describing the minimal chunk of data possible to be copied. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [dma\_callback\_t](group__dma__interface.md#ga94745b4472ee1addd4f82db4e59e9fb5)) (const struct [device](structdevice.md) \*dev, void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, int status) |
|  | Callback function for DMA transfer completion. |

| Enumerations | |
| --- | --- |
| enum | [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) {     [MEMORY\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5) = 0x0 , [MEMORY\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a) , [PERIPHERAL\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165) , [PERIPHERAL\_TO\_PERIPHERAL](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449) ,     [HOST\_TO\_MEMORY](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c) , [MEMORY\_TO\_HOST](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60) , [DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a) , [DMA\_CHANNEL\_DIRECTION\_PRIV\_START](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037) = DMA\_CHANNEL\_DIRECTION\_COMMON\_COUNT ,     [DMA\_CHANNEL\_DIRECTION\_MAX](group__dma__interface.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02) = 0x7   } |
|  | DMA channel direction. [More...](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) |
| enum | [dma\_addr\_adj](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c) { [DMA\_ADDR\_ADJ\_INCREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e) , [DMA\_ADDR\_ADJ\_DECREMENT](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717) , [DMA\_ADDR\_ADJ\_NO\_CHANGE](group__dma__interface.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f) } |
|  | DMA address adjustment. [More...](group__dma__interface.md#gafe0877ef4bd7790a4bcd46052088231c) |
| enum | [dma\_channel\_filter](group__dma__interface.md#gade594552920aabbfd2106059a338498b) { [DMA\_CHANNEL\_NORMAL](group__dma__interface.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f) , [DMA\_CHANNEL\_PERIODIC](group__dma__interface.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c) } |
|  | DMA channel attributes. [More...](group__dma__interface.md#gade594552920aabbfd2106059a338498b) |
| enum | [dma\_attribute\_type](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b) { [DMA\_ATTR\_BUFFER\_ADDRESS\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f) , [DMA\_ATTR\_BUFFER\_SIZE\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873) , [DMA\_ATTR\_COPY\_ALIGNMENT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b) , [DMA\_ATTR\_MAX\_BLOCK\_COUNT](group__dma__interface.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18) } |
|  | DMA attributes. [More...](group__dma__interface.md#ga08c366c8d47672eeeb37b258af20101b) |

| Functions | |
| --- | --- |
| static int | [dma\_config](group__dma__interface.md#ga6df1a6b89f271a0eae01c17b748bd2df) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, struct dma\_config \*config) |
|  | Configure individual channel for DMA transfer. |
| static int | [dma\_reload](group__dma__interface.md#ga55bd5d550349c11c63ef47c2ed861f36) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Reload buffer(s) for a DMA channel. |
| int | [dma\_start](group__dma__interface.md#gac2ddafd17680f59e4e8fe5f6e2eaba48) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Enables DMA channel and starts the transfer, the channel must be configured beforehand. |
| int | [dma\_stop](group__dma__interface.md#ga305cc72d0804028b77aa82dd07c926ad) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Stops the DMA transfer and disables the channel. |
| int | [dma\_suspend](group__dma__interface.md#ga6779850f6082259f5bef29b1282effdb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Suspend a DMA channel transfer. |
| int | [dma\_resume](group__dma__interface.md#ga89a3d056803d7f2dd1c8b6e535ef4f1d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | Resume a DMA channel transfer. |
| int | [dma\_request\_channel](group__dma__interface.md#ga91cc55f781744069f1f9f29249bdee8d) (const struct [device](structdevice.md) \*dev, void \*filter\_param) |
|  | request DMA channel. |
| void | [dma\_release\_channel](group__dma__interface.md#gab02df5277d79a04a65132365e7b5d3de) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel) |
|  | release DMA channel. |
| int | [dma\_chan\_filter](group__dma__interface.md#ga729d8f1163458d447d0a4b20cb9e4659) (const struct [device](structdevice.md) \*dev, int channel, void \*filter\_param) |
|  | DMA channel filter. |
| static int | [dma\_get\_status](group__dma__interface.md#ga2cae500f1f9ed42ad338a40ec8655544) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, struct [dma\_status](structdma__status.md) \*[stat](structstat.md)) |
|  | get current runtime status of DMA transfer |
| static int | [dma\_get\_attribute](group__dma__interface.md#ga641f3fa492bfb17cf9f0a0361d429257) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value) |
|  | get attribute of a dma controller |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dma\_width\_index](group__dma__interface.md#gadd1724a843bba4ccc1c65c9fb9d3d921) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Look-up generic width index to be used in registers. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dma\_burst\_index](group__dma__interface.md#gaac27f2ee664671884087ee3d2a2863ce) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) burst) |
|  | Look-up generic burst index to be used in registers. |

## Detailed Description

Public APIs for the DMA drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma.h](drivers_2dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
