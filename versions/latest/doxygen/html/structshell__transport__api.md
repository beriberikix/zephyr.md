---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structshell__transport__api.html
original_path: doxygen/html/structshell__transport__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_transport\_api Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

Unified shell transport interface.
[More...](#details)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#a59afba962312a077343b440448d67135) )(const struct [shell\_transport](structshell__transport.md) \*transport, const void \*config, [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) evt\_handler, void \*context) |
|  | Function for initializing the shell transport interface. |
| int(\* | [uninit](#a94cc7843174a4aba668389a4b46928d3) )(const struct [shell\_transport](structshell__transport.md) \*transport) |
|  | Function for uninitializing the shell transport interface. |
| int(\* | [enable](#a95535c7195088e68230ecb306f105713) )(const struct [shell\_transport](structshell__transport.md) \*transport, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) blocking\_tx) |
|  | Function for enabling transport in given TX mode. |
| int(\* | [write](#a6bbf2905abcbf6ca564ecf3f07d95712) )(const struct [shell\_transport](structshell__transport.md) \*transport, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*cnt) |
|  | Function for writing data to the transport interface. |
| int(\* | [read](#aae0e8ad92065dbff10691c28045d0c8f) )(const struct [shell\_transport](structshell__transport.md) \*transport, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*cnt) |
|  | Function for reading data from the transport interface. |
| void(\* | [update](#a3b447d16d7c30f994c582d67bde57ba8) )(const struct [shell\_transport](structshell__transport.md) \*transport) |
|  | Function called in shell thread loop. |

## Detailed Description

Unified shell transport interface.

## Field Documentation

## [◆ ](#a95535c7195088e68230ecb306f105713)enable

| int(\* shell\_transport\_api::enable) (const struct [shell\_transport](structshell__transport.md) \*transport, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) blocking\_tx) |
| --- |

Function for enabling transport in given TX mode.

Function can be used to reconfigure TX to work in blocking mode.

Parameters
:   | transport | Pointer to the transfer instance. |
    | --- | --- |
    | blocking\_tx | If true, the transport TX is enabled in blocking mode. |

Returns
:   NRF\_SUCCESS on successful enabling, error otherwise (also if not supported).

## [◆ ](#a59afba962312a077343b440448d67135)init

| int(\* shell\_transport\_api::init) (const struct [shell\_transport](structshell__transport.md) \*transport, const void \*config, [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) evt\_handler, void \*context) |
| --- |

Function for initializing the shell transport interface.

Parameters
:   | [in] | transport | Pointer to the transfer instance. |
    | --- | --- | --- |
    | [in] | config | Pointer to instance configuration. |
    | [in] | evt\_handler | Event handler. |
    | [in] | context | Pointer to the context passed to event handler. |

Returns
:   Standard error code.

## [◆ ](#aae0e8ad92065dbff10691c28045d0c8f)read

| int(\* shell\_transport\_api::read) (const struct [shell\_transport](structshell__transport.md) \*transport, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*cnt) |
| --- |

Function for reading data from the transport interface.

Parameters
:   | [in] | transport | Pointer to the transfer instance. |
    | --- | --- | --- |
    | [in] | data | Pointer to the destination buffer. |
    | [in] | length | Destination buffer length. |
    | [out] | cnt | Pointer to the received bytes counter. |

Returns
:   Standard error code.

## [◆ ](#a94cc7843174a4aba668389a4b46928d3)uninit

| int(\* shell\_transport\_api::uninit) (const struct [shell\_transport](structshell__transport.md) \*transport) |
| --- |

Function for uninitializing the shell transport interface.

Parameters
:   | [in] | transport | Pointer to the transfer instance. |
    | --- | --- | --- |

Returns
:   Standard error code.

## [◆ ](#a3b447d16d7c30f994c582d67bde57ba8)update

| void(\* shell\_transport\_api::update) (const struct [shell\_transport](structshell__transport.md) \*transport) |
| --- |

Function called in shell thread loop.

Can be used for backend operations that require longer execution time

Parameters
:   | [in] | transport | Pointer to the transfer instance. |
    | --- | --- | --- |

## [◆ ](#a6bbf2905abcbf6ca564ecf3f07d95712)write

| int(\* shell\_transport\_api::write) (const struct [shell\_transport](structshell__transport.md) \*transport, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*cnt) |
| --- |

Function for writing data to the transport interface.

Parameters
:   | [in] | transport | Pointer to the transfer instance. |
    | --- | --- | --- |
    | [in] | data | Pointer to the source buffer. |
    | [in] | length | Source buffer length. |
    | [out] | cnt | Pointer to the sent bytes counter. |

Returns
:   Standard error code.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_transport\_api](structshell__transport__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
