---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/device_8h.html
original_path: doxygen/html/device_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/init.h](init_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`  
`#include <[zephyr/sys/device_mmio.h](device__mmio_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <syscalls/device.h>`

[Go to the source code of this file.](device_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [device\_state](structdevice__state.md) |
|  | Runtime device dynamic structure (in RAM) per driver instance. [More...](structdevice__state.md#details) |
| struct | [device](structdevice.md) |
|  | Runtime device structure (in ROM) per driver instance. [More...](structdevice.md#details) |

| Macros | |
| --- | --- |
| #define | [DEVICE\_HANDLE\_NULL](group__device__model.md#ga4dd918c3a59b8afa185a4851165d2ca0)   0 |
|  | Flag value used to identify an unknown device. |
| #define | [DEVICE\_NAME\_GET](group__device__model.md#ga430eb7530aeb3cff5708b55f9b571eb9)(dev\_id) |
|  | Expands to the name of a global device object. |
| #define | [DEVICE\_DEFINE](group__device__model.md#gac12521f4d900e8947aac45c1b228366d)(dev\_id, name, init\_fn, pm, data, config, level, prio, api) |
|  | Create a device object and set it up for boot time initialization. |
| #define | [DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id) |
|  | Return a string name for a devicetree node. |
| #define | [DEVICE\_DT\_DEFINE](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Create a device object from a devicetree node identifier and set it up for boot time initialization. |
| #define | [DEVICE\_DT\_INST\_DEFINE](group__device__model.md#gada5ba4aca9e0662ccebb2232c7256419)(inst, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization."), but uses an instance of a DT\_DRV\_COMPAT compatible instead of a node identifier. |
| #define | [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node\_id) |
|  | The name of the global device object for `node_id`. |
| #define | [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)(node\_id) |
|  | Get a [device](structdevice.md "device") reference from a devicetree node identifier. |
| #define | [DEVICE\_DT\_INST\_GET](group__device__model.md#ga9165e550ae175ce305eafe33390af78b)(inst) |
|  | Get a [device](structdevice.md "device") reference for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [DEVICE\_DT\_GET\_ANY](group__device__model.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)(compat) |
|  | Get a [device](structdevice.md "device") reference from a devicetree compatible. |
| #define | [DEVICE\_DT\_GET\_ONE](group__device__model.md#ga39c760429534ef9ae77f3d996987cd2b)(compat) |
|  | Get a [device](structdevice.md "device") reference from a devicetree compatible. |
| #define | [DEVICE\_DT\_GET\_OR\_NULL](group__device__model.md#ga6ce1dbfda6847ca6c3858712e9b41989)(node\_id) |
|  | Utility macro to obtain an optional reference to a device. |
| #define | [DEVICE\_GET](group__device__model.md#gaf9403e7eb573a30d2dfaed357f4ef3f4)(dev\_id) |
|  | Obtain a pointer to a device object by name. |
| #define | [DEVICE\_DECLARE](group__device__model.md#ga4e763eae14dcd41d599c485410ac2983)(dev\_id) |
|  | Declare a static device object. |
| #define | [DEVICE\_INIT\_DT\_GET](group__device__model.md#gad829bbf36723e8cb6c3df8f996a908be)(node\_id) |
|  | Get a [init\_entry](structinit__entry.md "init_entry") reference from a devicetree node. |
| #define | [DEVICE\_INIT\_GET](group__device__model.md#ga7b7d3030fea734304c61665e75191cc0)(dev\_id) |
|  | Get a [init\_entry](structinit__entry.md "init_entry") reference from a device identifier. |

| Typedefs | |
| --- | --- |
| typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) |
|  | Type used to represent a "handle" for a device. |
| typedef int(\* | [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb)) (const struct [device](structdevice.md) \*dev, void \*context) |
|  | Prototype for functions used when iterating over a set of devices. |

| Functions | |
| --- | --- |
| static [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) | [device\_handle\_get](group__device__model.md#ga456366a9ca0a8e97484c97c279745203) (const struct [device](structdevice.md) \*dev) |
|  | Get the handle for a given device. |
| static const struct [device](structdevice.md) \* | [device\_from\_handle](group__device__model.md#ga73680daef9f8d7dc2541d83d09737f4a) ([device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) dev\_handle) |
|  | Get the device corresponding to a handle. |
| static const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [device\_required\_handles\_get](group__device__model.md#ga2157bbfc2deecfae6514f58221663618) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the device handles for devicetree dependencies of this device. |
| static const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [device\_injected\_handles\_get](group__device__model.md#gae89b0d818c45fdf258c0a421bc103ddc) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the device handles for injected dependencies of this device. |
| static const [device\_handle\_t](group__device__model.md#ga21415b8e9967ecd2c3d3d3b1724f93c3) \* | [device\_supported\_handles\_get](group__device__model.md#ga3c9ae15d3224c792b915b107b2d5d00f) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Get the set of handles that this device supports. |
| int | [device\_required\_foreach](group__device__model.md#ga6e3b6dbb15ca28d6c94ee07702663245) (const struct [device](structdevice.md) \*dev, [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb, void \*context) |
|  | Visit every device that `dev` directly requires. |
| int | [device\_supported\_foreach](group__device__model.md#gaf5fce5e93fd6d5e13aa8b20251b82b2a) (const struct [device](structdevice.md) \*dev, [device\_visitor\_callback\_t](group__device__model.md#ga9a1118e5c76c44c998f7258a7de0bfbb) visitor\_cb, void \*context) |
|  | Visit every device that `dev` directly supports. |
| const struct [device](structdevice.md) \* | [device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835) (const char \*name) |
|  | Get a [device](structdevice.md "device") reference from its [device::name](structdevice.md#a1e74e8d3b0b1a981c67e1d0284ccac3d "device::name") field. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [device\_is\_ready](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb) (const struct [device](structdevice.md) \*dev) |
|  | Verify that a device is ready for use. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [device.h](device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
