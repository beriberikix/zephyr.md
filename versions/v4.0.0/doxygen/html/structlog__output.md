---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__output.html
original_path: doxygen/html/structlog__output.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log output API](group__log__output.md)

Log\_output instance structure.
[More...](#details)

`#include <[log_output.h](log__output_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d) | [func](#aea6a7a7dee29f474d55b726ca3787f95) |
| struct [log\_output\_control\_block](structlog__output__control__block.md) \* | [control\_block](#a5228e6c2111cb28a8a69e4d99443dd55) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#af43d26be4e52647c2b281362a01d1a10) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#af88be3afe8b2fc2f7acb703a93992030) |

## Detailed Description

Log\_output instance structure.

## Field Documentation

## [◆ ](#af43d26be4e52647c2b281362a01d1a10)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* log\_output::buf |
| --- |

## [◆ ](#a5228e6c2111cb28a8a69e4d99443dd55)control\_block

| struct [log\_output\_control\_block](structlog__output__control__block.md)\* log\_output::control\_block |
| --- |

## [◆ ](#aea6a7a7dee29f474d55b726ca3787f95)func

| [log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d) log\_output::func |
| --- |

## [◆ ](#af88be3afe8b2fc2f7acb703a93992030)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) log\_output::size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_output.h](log__output_8h_source.md)

- [log\_output](structlog__output.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
