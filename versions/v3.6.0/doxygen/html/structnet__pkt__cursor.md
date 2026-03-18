---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__pkt__cursor.html
original_path: doxygen/html/structnet__pkt__cursor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_pkt\_cursor Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Packet Library](group__net__pkt.md)

`#include <[net_pkt.h](net__pkt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [buf](#af81267720cf13d06b90ddaa87fb7ad67) |
|  | Current [net\_buf](structnet__buf.md "Network buffer representation.") pointer by the cursor. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [pos](#a0901a4cc727e55b94e2dcb60f3c54caf) |
|  | Current position in the data buffer of the [net\_buf](structnet__buf.md "Network buffer representation."). |

## Field Documentation

## [◆ ](#af81267720cf13d06b90ddaa87fb7ad67)buf

| struct [net\_buf](structnet__buf.md)\* net\_pkt\_cursor::buf |
| --- |

Current [net\_buf](structnet__buf.md "Network buffer representation.") pointer by the cursor.

## [◆ ](#a0901a4cc727e55b94e2dcb60f3c54caf)pos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* net\_pkt\_cursor::pos |
| --- |

Current position in the data buffer of the [net\_buf](structnet__buf.md "Network buffer representation.").

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_pkt.h](net__pkt_8h_source.md)

- [net\_pkt\_cursor](structnet__pkt__cursor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
