---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__log__backend_8h.html
original_path: doxygen/html/shell__log__backend_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_log\_backend.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/logging/log_backend.h](log__backend_8h_source.md)>`  
`#include <[zephyr/logging/log_output.h](log__output_8h_source.md)>`  
`#include <[zephyr/sys/mpsc_pbuf.h](mpsc__pbuf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`

[Go to the source code of this file.](shell__log__backend_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_log\_backend\_control\_block](structshell__log__backend__control__block.md) |
|  | Shell log backend control block (RW data). [More...](structshell__log__backend__control__block.md#details) |
| struct | [shell\_log\_backend](structshell__log__backend.md) |
|  | Shell log backend instance structure (RO data). [More...](structshell__log__backend.md#details) |
| struct | [shell\_log\_backend\_msg](structshell__log__backend__msg.md) |
|  | Shell log backend message structure. [More...](structshell__log__backend__msg.md#details) |

| Enumerations | |
| --- | --- |
| enum | [shell\_log\_backend\_state](#a4d98f9c89ac476fe4ef2299921dd0c7d) { [SHELL\_LOG\_BACKEND\_UNINIT](#a4d98f9c89ac476fe4ef2299921dd0c7da1dd95c355c7e47f53dee0804e8209b1d) , [SHELL\_LOG\_BACKEND\_ENABLED](#a4d98f9c89ac476fe4ef2299921dd0c7daf49ef7ffee9d397007533897ba0cf935) , [SHELL\_LOG\_BACKEND\_DISABLED](#a4d98f9c89ac476fe4ef2299921dd0c7dae0888042a003fdb68effd8a63358cc57) , [SHELL\_LOG\_BACKEND\_PANIC](#a4d98f9c89ac476fe4ef2299921dd0c7da82ae0d6b6bd04ff39b2485b2a078362f) } |
|  | Shell log backend states. [More...](#a4d98f9c89ac476fe4ef2299921dd0c7d) |

| Variables | |
| --- | --- |
| const struct [log\_backend\_api](structlog__backend__api.md) | [log\_backend\_shell\_api](#addf27615ed72440ecb63aa1d84962c82) |

## Enumeration Type Documentation

## [◆ ](#a4d98f9c89ac476fe4ef2299921dd0c7d)shell\_log\_backend\_state

| enum [shell\_log\_backend\_state](#a4d98f9c89ac476fe4ef2299921dd0c7d) |
| --- |

Shell log backend states.

| Enumerator | |
| --- | --- |
| SHELL\_LOG\_BACKEND\_UNINIT |  |
| SHELL\_LOG\_BACKEND\_ENABLED |  |
| SHELL\_LOG\_BACKEND\_DISABLED |  |
| SHELL\_LOG\_BACKEND\_PANIC |  |

## Variable Documentation

## [◆ ](#addf27615ed72440ecb63aa1d84962c82)log\_backend\_shell\_api

| | const struct [log\_backend\_api](structlog__backend__api.md) log\_backend\_shell\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_log\_backend.h](shell__log__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
