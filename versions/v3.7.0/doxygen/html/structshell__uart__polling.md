---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__uart__polling.html
original_path: doxygen/html/structshell__uart__polling.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_uart\_polling Struct Reference

`#include <[shell_uart.h](shell__uart_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [shell\_uart\_common](structshell__uart__common.md) | [common](#af53998508fe666d61327cb5340c76354) |
| struct [ring\_buf](structring__buf.md) | [rx\_ringbuf](#ae05061fbe7ea7ea926893c695280698e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_buf](#ad6c0d8d792df20fe2b9f5a1608cd0cfd) [0] |
| struct k\_timer | [rx\_timer](#a4cd8ddcbea91c6ee4994fbe5898537ea) |

## Field Documentation

## [◆ ](#af53998508fe666d61327cb5340c76354)common

| struct [shell\_uart\_common](structshell__uart__common.md) shell\_uart\_polling::common |
| --- |

## [◆ ](#ad6c0d8d792df20fe2b9f5a1608cd0cfd)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_uart\_polling::rx\_buf[0] |
| --- |

## [◆ ](#ae05061fbe7ea7ea926893c695280698e)rx\_ringbuf

| struct [ring\_buf](structring__buf.md) shell\_uart\_polling::rx\_ringbuf |
| --- |

## [◆ ](#a4cd8ddcbea91c6ee4994fbe5898537ea)rx\_timer

| struct k\_timer shell\_uart\_polling::rx\_timer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_uart.h](shell__uart_8h_source.md)

- [shell\_uart\_polling](structshell__uart__polling.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
