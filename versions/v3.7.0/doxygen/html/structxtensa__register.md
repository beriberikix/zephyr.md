---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structxtensa__register.html
original_path: doxygen/html/structxtensa__register.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xtensa\_register Struct Reference

Register description for GDB stub.
[More...](#details)

`#include <[gdbstub.h](arch_2xtensa_2gdbstub_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [val](#a58afab24c5b54d15dcd36ebcdf0e750d) |
|  | Register value. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [idx](#a7c2a71ffd07ce4b17c9d8bab43536670) |
|  | GDB register index (for p/P packets). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [byte\_size](#a4b0b68c1c0b8401cb7f7fdc8ef653844) |
|  | Size of register. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [regno](#a9c85b2544da4849db91f5a70e75630f2) |
|  | Xtensa register number. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [gpkt\_offset](#aa0a1af384d561e5a33819d64b475bdbb) |
|  | Offset of this register in GDB G-packet. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [stack\_offset](#ae2daef15a43d111728d559cb68adee37) |
|  | Offset of saved register in stack frame. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [seqno](#a8ec99f010bc979cb4f7736fda9786c7b) |
|  | Sequence number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [is\_read\_only](#aaf92daddc205651cba3aa07d08afbf16):1 |
|  | Set to 1 if register should not be written to during debugging. |

## Detailed Description

Register description for GDB stub.

Values are based on gdb/gdb/xtensa-config.c in the Xtensa overlay, where registers are defined using XTREG() macro: XTREG(index,ofs,bsz,sz,al,tnum,flg,cp,ty,gr,name,fet,sto,mas,ct,x,y)

Translation: idx : index regno : tnum 0x00xx : General Registers (A0 - A15, PC) 0x01xx : Address Registers (AR0 - AR31/AR63) 0x02xx : Special Registers (access via RSR/WSR) 0x03xx : User Registers (access via RUR/WUR) byte\_size : sz gpkt\_offset : ofs

## Field Documentation

## [◆ ](#a4b0b68c1c0b8401cb7f7fdc8ef653844)byte\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xtensa\_register::byte\_size |
| --- |

Size of register.

## [◆ ](#aa0a1af384d561e5a33819d64b475bdbb)gpkt\_offset

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) xtensa\_register::gpkt\_offset |
| --- |

Offset of this register in GDB G-packet.

-1 if register is not in G-packet.

## [◆ ](#a7c2a71ffd07ce4b17c9d8bab43536670)idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xtensa\_register::idx |
| --- |

GDB register index (for p/P packets).

## [◆ ](#aaf92daddc205651cba3aa07d08afbf16)is\_read\_only

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xtensa\_register::is\_read\_only |
| --- |

Set to 1 if register should not be written to during debugging.

## [◆ ](#a9c85b2544da4849db91f5a70e75630f2)regno

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) xtensa\_register::regno |
| --- |

Xtensa register number.

## [◆ ](#a8ec99f010bc979cb4f7736fda9786c7b)seqno

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xtensa\_register::seqno |
| --- |

Sequence number.

## [◆ ](#ae2daef15a43d111728d559cb68adee37)stack\_offset

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) xtensa\_register::stack\_offset |
| --- |

Offset of saved register in stack frame.

0 if not saved in stack frame.

## [◆ ](#a58afab24c5b54d15dcd36ebcdf0e750d)val

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) xtensa\_register::val |
| --- |

Register value.

---

The documentation for this struct was generated from the following file:

- zephyr/arch/xtensa/[gdbstub.h](arch_2xtensa_2gdbstub_8h_source.md)

- [xtensa\_register](structxtensa__register.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
