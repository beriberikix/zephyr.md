---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmipi__dbi__driver__api.html
original_path: doxygen/html/structmipi__dbi__driver__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dbi\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MIPI-DBI driver APIs](group__mipi__dbi__interface.md)

MIPI-DBI host driver API.
[More...](#details)

`#include <[mipi_dbi.h](drivers_2mipi__dbi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [command\_write](#ab9d25998b352b21c3af790ec863a8afd) )(const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int(\* | [command\_read](#a5e8c4b3084d81c2de655cf3dbb7b8532) )(const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_cmds, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int(\* | [write\_display](#ac1ddd47d5c394089bac92d74fc959279) )(const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf, struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt) |
| int(\* | [reset](#a3e4def02d3756bb587eacf2c87a5aa71) )(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) delay) |
| int(\* | [release](#a555a20b383debcf451331a8f770b1585) )(const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config) |
| int(\* | [configure\_te](#ae5d60b75a2cb0cc89956ff31726887a5) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edge, [k\_timeout\_t](structk__timeout__t.md) delay) |

## Detailed Description

MIPI-DBI host driver API.

## Field Documentation

## [◆ ](#a5e8c4b3084d81c2de655cf3dbb7b8532)command\_read

| int(\* mipi\_dbi\_driver\_api::command\_read) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_cmds, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

## [◆ ](#ab9d25998b352b21c3af790ec863a8afd)command\_write

| int(\* mipi\_dbi\_driver\_api::command\_write) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

## [◆ ](#ae5d60b75a2cb0cc89956ff31726887a5)configure\_te

| int(\* mipi\_dbi\_driver\_api::configure\_te) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) edge, [k\_timeout\_t](structk__timeout__t.md) delay) |
| --- |

## [◆ ](#a555a20b383debcf451331a8f770b1585)release

| int(\* mipi\_dbi\_driver\_api::release) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config) |
| --- |

## [◆ ](#a3e4def02d3756bb587eacf2c87a5aa71)reset

| int(\* mipi\_dbi\_driver\_api::reset) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) delay) |
| --- |

## [◆ ](#ac1ddd47d5c394089bac92d74fc959279)write\_display

| int(\* mipi\_dbi\_driver\_api::write\_display) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf, struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mipi\_dbi.h](drivers_2mipi__dbi_8h_source.md)

- [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
