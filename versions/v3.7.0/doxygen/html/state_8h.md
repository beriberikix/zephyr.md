---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/state_8h.html
original_path: doxygen/html/state_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

state.h File Reference

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](state_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pm\_state\_info](structpm__state__info.md) |
|  | Information about a power management state. [More...](structpm__state__info.md#details) |
| struct | [pm\_state\_constraint](structpm__state__constraint.md) |
|  | Power state information needed to lock a power state. [More...](structpm__state__constraint.md#details) |

| Macros | |
| --- | --- |
| #define | [PM\_STATE\_INFO\_DT\_INIT](group__subsys__pm__states.md#ga1e77683479b589093f06cca9b1d142b9)(node\_id) |
|  | Initializer for struct [pm\_state\_info](structpm__state__info.md "Information about a power management state.") given a DT node identifier with zephyr,power-state compatible. |
| #define | [PM\_STATE\_DT\_INIT](group__subsys__pm__states.md#gadd0dca42aef0a021fed9ca2d588ce393)(node\_id) |
|  | Initializer for enum [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5 "Power management state.") given a DT node identifier with zephyr,power-state compatible. |
| #define | [DT\_NUM\_CPU\_POWER\_STATES](group__subsys__pm__states.md#ga70e4a8cbc3b0e9427f4bf67ee31b3edd)(node\_id) |
|  | Obtain number of CPU power states supported and enabled by the given CPU node identifier. |
| #define | [PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU](group__subsys__pm__states.md#ga2846f402e20570fc61118b8545cdbe12)(node\_id) |
|  | Initialize an array of struct [pm\_state\_info](structpm__state__info.md "Information about a power management state.") with information from all the states present and enabled in the given CPU node identifier. |
| #define | [PM\_STATE\_LIST\_FROM\_DT\_CPU](group__subsys__pm__states.md#ga8248587108fcb76adefb50a360bc5db7)(node\_id) |
|  | Initialize an array of struct [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5 "Power management state.") with information from all the states present and enabled in the given CPU node identifier. |

| Enumerations | |
| --- | --- |
| enum | [pm\_state](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) {     [PM\_STATE\_ACTIVE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743) , [PM\_STATE\_RUNTIME\_IDLE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19) , [PM\_STATE\_SUSPEND\_TO\_IDLE](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0) , [PM\_STATE\_STANDBY](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429) ,     [PM\_STATE\_SUSPEND\_TO\_RAM](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00) , [PM\_STATE\_SUSPEND\_TO\_DISK](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695) , [PM\_STATE\_SOFT\_OFF](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01) , [PM\_STATE\_COUNT](group__subsys__pm__states.md#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737)   } |
|  | Power management state. [More...](group__subsys__pm__states.md#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pm\_state\_cpu\_get\_all](group__subsys__pm__states.md#ga682f75eb5324455ce95a5c7d4c2d6242) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*\*states) |
|  | Obtain information about all supported states by a CPU. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [state.h](state_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
