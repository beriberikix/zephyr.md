---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgptp__clk__src__time__invoke__params.html
original_path: doxygen/html/structgptp__clk__src__time__invoke__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp\_clk\_src\_time\_invoke\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [gPTP support](group__gptp.md)

ClockSourceTime.invoke function parameters.
[More...](#details)

`#include <[gptp.h](gptp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| double | [last\_gm\_freq\_change](#aaf1ca90ce4e1b216c2edbb9fa72b044a) |
|  | Frequency change on the last Time Base Indicator Change. |
| struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) | [src\_time](#a990360a4fdc5bdc8f6626e9dfdc05563) |
|  | The time this function is invoked. |
| struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) | [last\_gm\_phase\_change](#ab2328d1a7458ccc8e7fe771e50b463eb) |
|  | Phase change on the last Time Base Indicator Change. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [time\_base\_indicator](#ada4c313104488059a520d4a2ffff33b4) |
|  | Time Base - changed only if Phase or Frequency changes. |

## Detailed Description

ClockSourceTime.invoke function parameters.

Parameters passed by ClockSourceTime.invoke function.

## Field Documentation

## [◆ ](#aaf1ca90ce4e1b216c2edbb9fa72b044a)last\_gm\_freq\_change

| double gptp\_clk\_src\_time\_invoke\_params::last\_gm\_freq\_change |
| --- |

Frequency change on the last Time Base Indicator Change.

## [◆ ](#ab2328d1a7458ccc8e7fe771e50b463eb)last\_gm\_phase\_change

| struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) gptp\_clk\_src\_time\_invoke\_params::last\_gm\_phase\_change |
| --- |

Phase change on the last Time Base Indicator Change.

## [◆ ](#a990360a4fdc5bdc8f6626e9dfdc05563)src\_time

| struct [net\_ptp\_extended\_time](structnet__ptp__extended__time.md) gptp\_clk\_src\_time\_invoke\_params::src\_time |
| --- |

The time this function is invoked.

## [◆ ](#ada4c313104488059a520d4a2ffff33b4)time\_base\_indicator

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gptp\_clk\_src\_time\_invoke\_params::time\_base\_indicator |
| --- |

Time Base - changed only if Phase or Frequency changes.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[gptp.h](gptp_8h_source.md)

- [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
