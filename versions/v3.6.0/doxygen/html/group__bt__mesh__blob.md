---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__blob.html
original_path: doxygen/html/group__bt__mesh__blob.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Mesh BLOB model API

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) |
|  | BLOB transfer data block. [More...](structbt__mesh__blob__block.md#details) |
| struct | [bt\_mesh\_blob\_chunk](structbt__mesh__blob__chunk.md) |
|  | BLOB data chunk. [More...](structbt__mesh__blob__chunk.md#details) |
| struct | [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) |
|  | BLOB transfer. [More...](structbt__mesh__blob__xfer.md#details) |
| struct | [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) |
|  | BLOB stream. [More...](structbt__mesh__blob__io.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](#ga4e1ea17e8a8ffd42f62d64286ddc576e)   0 |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_blob\_xfer\_mode](#gae0cb28c0e50d02f6e003062457053618) { [BT\_MESH\_BLOB\_XFER\_MODE\_NONE](#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6) , [BT\_MESH\_BLOB\_XFER\_MODE\_PUSH](#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b) , [BT\_MESH\_BLOB\_XFER\_MODE\_PULL](#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd) , [BT\_MESH\_BLOB\_XFER\_MODE\_ALL](#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089) } |
|  | BLOB transfer mode. [More...](#gae0cb28c0e50d02f6e003062457053618) |
| enum | [bt\_mesh\_blob\_xfer\_phase](#ga26ed2c64bae03758a8a53b28052d0f81) {     [BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE](#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600) , [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START](#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9) , [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK](#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1) , [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK](#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581) ,     [BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE](#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd) , [BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED](#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)   } |
|  | Transfer phase. [More...](#ga26ed2c64bae03758a8a53b28052d0f81) |
| enum | [bt\_mesh\_blob\_status](#ga7b5e2895a6577103a8a680a94ee7776d) {     [BT\_MESH\_BLOB\_SUCCESS](#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d) , [BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM](#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e) , [BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE](#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a) , [BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE](#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009) ,     [BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE](#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa) , [BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM](#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0) , [BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID](#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b) , [BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE](#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f) ,     [BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE](#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768) , [BT\_MESH\_BLOB\_ERR\_INTERNAL](#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb) , [BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE](#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)   } |
|  | BLOB model status codes. [More...](#ga7b5e2895a6577103a8a680a94ee7776d) |
| enum | [bt\_mesh\_blob\_io\_mode](#ga2618fb7365f180a73a7eecd11cf2f962) { [BT\_MESH\_BLOB\_READ](#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a) , [BT\_MESH\_BLOB\_WRITE](#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab) } |
|  | BLOB stream interaction mode. [More...](#ga2618fb7365f180a73a7eecd11cf2f962) |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga4e1ea17e8a8ffd42f62d64286ddc576e)CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX

| #define CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX   0 |
| --- |

`#include <[blob.h](blob_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga2618fb7365f180a73a7eecd11cf2f962)bt\_mesh\_blob\_io\_mode

| enum [bt\_mesh\_blob\_io\_mode](#ga2618fb7365f180a73a7eecd11cf2f962) |
| --- |

`#include <[blob.h](blob_8h.md)>`

BLOB stream interaction mode.

| Enumerator | |
| --- | --- |
| BT\_MESH\_BLOB\_READ | Read data from the stream. |
| BT\_MESH\_BLOB\_WRITE | Write data to the stream. |

## [◆ ](#ga7b5e2895a6577103a8a680a94ee7776d)bt\_mesh\_blob\_status

| enum [bt\_mesh\_blob\_status](#ga7b5e2895a6577103a8a680a94ee7776d) |
| --- |

`#include <[blob.h](blob_8h.md)>`

BLOB model status codes.

| Enumerator | |
| --- | --- |
| BT\_MESH\_BLOB\_SUCCESS | The message was processed successfully. |
| BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM | The Block Number field value is not within the range of blocks being transferred. |
| BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE | The block size is smaller than the size indicated by the Min Block Size Log state or is larger than the size indicated by the Max Block Size Log state. |
| BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE | The chunk size exceeds the size indicated by the Max Chunk Size state, or the number of chunks exceeds the number specified by the Max Total Chunks state. |
| BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE | The operation cannot be performed while the server is in the current phase. |
| BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM | A parameter value in the message cannot be accepted. |
| BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID | The message contains a BLOB ID value that is not expected. |
| BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE | There is not enough space available in memory to receive the BLOB. |
| BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE | The transfer mode is not supported by the BLOB Transfer Server model. |
| BT\_MESH\_BLOB\_ERR\_INTERNAL | An internal error occurred on the node. |
| BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE | The requested information cannot be provided while the server is in the current phase. |

## [◆ ](#gae0cb28c0e50d02f6e003062457053618)bt\_mesh\_blob\_xfer\_mode

| enum [bt\_mesh\_blob\_xfer\_mode](#gae0cb28c0e50d02f6e003062457053618) |
| --- |

`#include <[blob.h](blob_8h.md)>`

BLOB transfer mode.

| Enumerator | |
| --- | --- |
| BT\_MESH\_BLOB\_XFER\_MODE\_NONE | No valid transfer mode. |
| BT\_MESH\_BLOB\_XFER\_MODE\_PUSH | Push mode (Push BLOB Transfer Mode). |
| BT\_MESH\_BLOB\_XFER\_MODE\_PULL | Pull mode (Pull BLOB Transfer Mode). |
| BT\_MESH\_BLOB\_XFER\_MODE\_ALL | Both modes are valid. |

## [◆ ](#ga26ed2c64bae03758a8a53b28052d0f81)bt\_mesh\_blob\_xfer\_phase

| enum [bt\_mesh\_blob\_xfer\_phase](#ga26ed2c64bae03758a8a53b28052d0f81) |
| --- |

`#include <[blob.h](blob_8h.md)>`

Transfer phase.

| Enumerator | |
| --- | --- |
| BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE | The BLOB Transfer Server is awaiting configuration. |
| BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START | The BLOB Transfer Server is ready to receive a BLOB transfer. |
| BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK | The BLOB Transfer Server is waiting for the next block of data. |
| BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK | The BLOB Transfer Server is waiting for the next chunk of data. |
| BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE | The BLOB was transferred successfully. |
| BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED | The BLOB transfer is paused. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
