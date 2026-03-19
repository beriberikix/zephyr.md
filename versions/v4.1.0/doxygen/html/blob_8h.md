---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/blob_8h.html
original_path: doxygen/html/blob_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](blob_8h_source.md)

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
| #define | [CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e)   0 |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) { [BT\_MESH\_BLOB\_XFER\_MODE\_NONE](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6) , [BT\_MESH\_BLOB\_XFER\_MODE\_PUSH](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b) , [BT\_MESH\_BLOB\_XFER\_MODE\_PULL](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd) , [BT\_MESH\_BLOB\_XFER\_MODE\_ALL](group__bt__mesh__blob.md#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089) } |
|  | BLOB transfer mode. [More...](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) |
| enum | [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) {     [BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600) , [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9) , [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_BLOCK](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1) , [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_CHUNK](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581) ,     [BT\_MESH\_BLOB\_XFER\_PHASE\_COMPLETE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd) , [BT\_MESH\_BLOB\_XFER\_PHASE\_SUSPENDED](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)   } |
|  | Transfer phase. [More...](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) |
| enum | [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) {     [BT\_MESH\_BLOB\_SUCCESS](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d) , [BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_NUM](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e) , [BT\_MESH\_BLOB\_ERR\_INVALID\_BLOCK\_SIZE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a) , [BT\_MESH\_BLOB\_ERR\_INVALID\_CHUNK\_SIZE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009) ,     [BT\_MESH\_BLOB\_ERR\_WRONG\_PHASE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa) , [BT\_MESH\_BLOB\_ERR\_INVALID\_PARAM](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0) , [BT\_MESH\_BLOB\_ERR\_WRONG\_BLOB\_ID](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b) , [BT\_MESH\_BLOB\_ERR\_BLOB\_TOO\_LARGE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f) ,     [BT\_MESH\_BLOB\_ERR\_UNSUPPORTED\_MODE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768) , [BT\_MESH\_BLOB\_ERR\_INTERNAL](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb) , [BT\_MESH\_BLOB\_ERR\_INFO\_UNAVAILABLE](group__bt__mesh__blob.md#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)   } |
|  | BLOB model status codes. [More...](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) |
| enum | [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) { [BT\_MESH\_BLOB\_READ](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a) , [BT\_MESH\_BLOB\_WRITE](group__bt__mesh__blob.md#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab) } |
|  | BLOB stream interaction mode. [More...](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob.h](blob_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
