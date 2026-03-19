---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/smp__dummy_8h.html
original_path: doxygen/html/smp__dummy_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_dummy.h File Reference

Dummy transport for the mcumgr SMP protocol for unit testing.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/mgmt/mgmt.h](mgmt_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/transport/serial.h](serial_8h_source.md)>`

[Go to the source code of this file.](smp__dummy_8h_source.md)

| Functions | |
| --- | --- |
| void | [smp\_dummy\_clear\_state](#ad9b3c7f35e4fa24fe863145a687f53db) (void) |
|  | Clears internal dummy SMP state and resets semaphore. |
| void | [dummy\_mcumgr\_add\_data](#a8bf3d0c12669c2cf5370eb7e148f10c2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_size) |
|  | Adds SMPC data to the internal buffer to be processed. |
| struct [net\_buf](structnet__buf.md) \* | [smp\_dummy\_get\_outgoing](#aa744df8e85bdb93cff2322b215164e9a) (void) |
|  | Processes a single line (fragment) coming from the mcumgr response to be used in tests. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [smp\_dummy\_wait\_for\_data](#a501596f79e8cf48fa1bb07484966fe53) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_time\_s) |
|  | Waits for a period of time for outgoing SMPC data to be ready and returns either when a full message is ready or when the timeout has elapsed. |
| void | [smp\_dummy\_add\_data](#ab5a47cd08e9467c969cbee9c85dcfe8a) (void) |
|  | Calls dummy\_mcumgr\_add\_data with the internal SMPC receive buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [smp\_dummy\_get\_send\_pos](#ab09b0ae8ed526252b4900e77afa57dc5) (void) |
|  | Gets current send buffer position. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [smp\_dummy\_get\_receive\_pos](#a71158b7a935497506a6cc9e2f40a2b1e) (void) |
|  | Gets current receive buffer position. |
| int | [smp\_dummy\_tx\_pkt](#a5440421e4994119fc98ec119706e4dd9) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, int len) |
|  | Converts input data to go out through the internal SMPC buffer. |
| void | [smp\_dummy\_enable](#adde2de8dc7895bda0e5d72a961dfba78) (void) |
|  | Enabled the dummy SMP module (will process sent/received data). |
| void | [smp\_dummy\_disable](#a57d38b86c8b826ef1d49bcae0565b772) (void) |
|  | Disables the dummy SMP module (will not process sent/received data). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [smp\_dummy\_get\_status](#a364817f12c377c6538867c6118d071c6) (void) |
|  | Returns status on if the dummy SMP system is active. |

## Detailed Description

Dummy transport for the mcumgr SMP protocol for unit testing.

## Function Documentation

## [◆ ](#a8bf3d0c12669c2cf5370eb7e148f10c2)dummy\_mcumgr\_add\_data()

| void dummy\_mcumgr\_add\_data | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data\_size* ) |

Adds SMPC data to the internal buffer to be processed.

Parameters
:   | data | Input data buffer |
    | --- | --- |
    | data\_size | Size of data (in bytes) |

## [◆ ](#ab5a47cd08e9467c969cbee9c85dcfe8a)smp\_dummy\_add\_data()

| void smp\_dummy\_add\_data | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Calls dummy\_mcumgr\_add\_data with the internal SMPC receive buffer.

## [◆ ](#ad9b3c7f35e4fa24fe863145a687f53db)smp\_dummy\_clear\_state()

| void smp\_dummy\_clear\_state | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Clears internal dummy SMP state and resets semaphore.

## [◆ ](#a57d38b86c8b826ef1d49bcae0565b772)smp\_dummy\_disable()

| void smp\_dummy\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Disables the dummy SMP module (will not process sent/received data).

## [◆ ](#adde2de8dc7895bda0e5d72a961dfba78)smp\_dummy\_enable()

| void smp\_dummy\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Enabled the dummy SMP module (will process sent/received data).

## [◆ ](#aa744df8e85bdb93cff2322b215164e9a)smp\_dummy\_get\_outgoing()

| struct [net\_buf](structnet__buf.md) \* smp\_dummy\_get\_outgoing | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Processes a single line (fragment) coming from the mcumgr response to be used in tests.

Return values
:   | net | buffer of processed data |
    | --- | --- |

## [◆ ](#a71158b7a935497506a6cc9e2f40a2b1e)smp\_dummy\_get\_receive\_pos()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) smp\_dummy\_get\_receive\_pos | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Gets current receive buffer position.

Return values
:   | Current | receive buffer position (in bytes) |
    | --- | --- |

## [◆ ](#ab09b0ae8ed526252b4900e77afa57dc5)smp\_dummy\_get\_send\_pos()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) smp\_dummy\_get\_send\_pos | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Gets current send buffer position.

Return values
:   | Current | send buffer position (in bytes) |
    | --- | --- |

## [◆ ](#a364817f12c377c6538867c6118d071c6)smp\_dummy\_get\_status()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) smp\_dummy\_get\_status | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Returns status on if the dummy SMP system is active.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if dummy SMP is enabled, false otherwise |
    | --- | --- |

## [◆ ](#a5440421e4994119fc98ec119706e4dd9)smp\_dummy\_tx\_pkt()

| int smp\_dummy\_tx\_pkt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | int | *len* ) |

Converts input data to go out through the internal SMPC buffer.

Parameters
:   | data | Input data buffer |
    | --- | --- |
    | len | Size of data (in bytes) |

Return values
:   | 0 | on success, negative on error. |
    | --- | --- |

## [◆ ](#a501596f79e8cf48fa1bb07484966fe53)smp\_dummy\_wait\_for\_data()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) smp\_dummy\_wait\_for\_data | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *wait\_time\_s* | ) |  |
| --- | --- | --- | --- | --- | --- |

Waits for a period of time for outgoing SMPC data to be ready and returns either when a full message is ready or when the timeout has elapsed.

Parameters
:   | wait\_time\_s | Time to wait for data (in seconds) |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | on message received successfully, false on timeout |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_dummy.h](smp__dummy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
