---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdmic__cfg.html
original_path: doxygen/html/structdmic__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dmic\_cfg Struct Reference

[Audio](group__audio__interface.md) » [Digital Microphone Interface](group__audio__dmic__interface.md)

Input configuration structure for the DMIC configuration API.
[More...](#details)

`#include <[dmic.h](dmic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [pdm\_io\_cfg](structpdm__io__cfg.md) | [io](#abac7595e0a03cf976d8359a86259f54b) |
| struct [pcm\_stream\_cfg](structpcm__stream__cfg.md) \* | [streams](#a90f08070236a8e2c07c30edc54c687a5) |
|  | Array of [pcm\_stream\_cfg](structpcm__stream__cfg.md "Configuration of the PCM streams to be output by the PDM hardware.") for application to provide configuration for each stream. |
| struct [pdm\_chan\_cfg](structpdm__chan__cfg.md) | [channel](#aaef2d2b475ce65d18c48d60cd1d393c4) |

## Detailed Description

Input configuration structure for the DMIC configuration API.

## Field Documentation

## [◆ ](#aaef2d2b475ce65d18c48d60cd1d393c4)channel

| struct [pdm\_chan\_cfg](structpdm__chan__cfg.md) dmic\_cfg::channel |
| --- |

## [◆ ](#abac7595e0a03cf976d8359a86259f54b)io

| struct [pdm\_io\_cfg](structpdm__io__cfg.md) dmic\_cfg::io |
| --- |

## [◆ ](#a90f08070236a8e2c07c30edc54c687a5)streams

| struct [pcm\_stream\_cfg](structpcm__stream__cfg.md)\* dmic\_cfg::streams |
| --- |

Array of [pcm\_stream\_cfg](structpcm__stream__cfg.md "Configuration of the PCM streams to be output by the PDM hardware.") for application to provide configuration for each stream.

---

The documentation for this struct was generated from the following file:

- zephyr/audio/[dmic.h](dmic_8h_source.md)

- [dmic\_cfg](structdmic__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
