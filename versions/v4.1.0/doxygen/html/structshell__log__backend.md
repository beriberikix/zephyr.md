---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structshell__log__backend.html
original_path: doxygen/html/structshell__log__backend.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_log\_backend Struct Reference

Shell log backend instance structure (RO data).
[More...](#details)

`#include <[shell_log_backend.h](shell__log__backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [log\_backend](structlog__backend.md) \* | [backend](#a653ca6a48ab4d6166ad9e2e25afbbca9) |
| const struct [log\_output](structlog__output.md) \* | [log\_output](#ad535b0244a1936cce72c10e14c3ca605) |
| struct [shell\_log\_backend\_control\_block](structshell__log__backend__control__block.md) \* | [control\_block](#af6439c070382d4376d347328ed942695) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timeout](#a24632f6459b4587de33646d809088b53) |
| const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \* | [mpsc\_buffer\_config](#aa04574a9aa9a1268850555f8c9756402) |
| struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | [mpsc\_buffer](#a4382a87da96780513c1717fa760630b0) |

## Detailed Description

Shell log backend instance structure (RO data).

## Field Documentation

## [◆ ](#a653ca6a48ab4d6166ad9e2e25afbbca9)backend

| const struct [log\_backend](structlog__backend.md)\* shell\_log\_backend::backend |
| --- |

## [◆ ](#af6439c070382d4376d347328ed942695)control\_block

| struct [shell\_log\_backend\_control\_block](structshell__log__backend__control__block.md)\* shell\_log\_backend::control\_block |
| --- |

## [◆ ](#ad535b0244a1936cce72c10e14c3ca605)log\_output

| const struct [log\_output](structlog__output.md)\* shell\_log\_backend::log\_output |
| --- |

## [◆ ](#a4382a87da96780513c1717fa760630b0)mpsc\_buffer

| struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)\* shell\_log\_backend::mpsc\_buffer |
| --- |

## [◆ ](#aa04574a9aa9a1268850555f8c9756402)mpsc\_buffer\_config

| const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)\* shell\_log\_backend::mpsc\_buffer\_config |
| --- |

## [◆ ](#a24632f6459b4587de33646d809088b53)timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_log\_backend::timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_log\_backend.h](shell__log__backend_8h_source.md)

- [shell\_log\_backend](structshell__log__backend.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
