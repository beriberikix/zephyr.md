---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnanoEsf.html
original_path: doxygen/html/structnanoEsf.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nanoEsf Struct Reference

Exception Stack Frame.
[More...](#details)

`#include <[arch.h](x86_2ia32_2arch_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ss](#a4ae87af42cd376c493dccd3fd257e823) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [gs](#a6f38a14fc76ee0ef99ef9ce5b7eb10fe) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [fs](#a8e2788e018d8ceb3b83cd889d86723d9) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [es](#a61d97934f9586b15ef9082ff57317362) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ds](#a6d5b8f4e7c220b804de0951294aaab95) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [esp](#ab872f78692b5e2145fc891880558238d) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ebp](#a4a4c4ec64e8f01e8a6e3e14bde63aa8c) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ebx](#afe46163b57c39529c3dce5284b0a7eb8) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [esi](#aff8554d808df765988252674e89d7bef) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [edi](#a483a384f835722c4c99a70e3c690e37a) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [edx](#a92a995abd01f4a5fd1a4f04a4e6400a4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [eax](#a1e72ac245fae9d8454ea572780fe6845) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ecx](#a4741e6bc706a7489fe2b45c34f7bdbb6) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [errorCode](#ae3b485a947962361d91ee59786d46b93) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [eip](#af1f3d43a394af43c49caf59a8bd384ab) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [cs](#a8ed38e432a8ef09ee219d062802bcb78) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [eflags](#acfb5ead961181e179f31f92393517420) |

## Detailed Description

Exception Stack Frame.

A pointer to an "exception stack frame" (ESF) is passed as an argument to exception handlers registered via nanoCpuExcConnect(). As the system always operates at ring 0, only the EIP, CS and EFLAGS registers are pushed onto the stack when an exception occurs.

The exception stack frame includes the volatile registers (EAX, ECX, and EDX) as well as the 5 non-volatile registers (EDI, ESI, EBX, EBP and ESP). Those registers are pushed onto the stack by \_ExcEnt().

## Field Documentation

## [◆ ](#a8ed38e432a8ef09ee219d062802bcb78)cs

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::cs |
| --- |

## [◆ ](#a6d5b8f4e7c220b804de0951294aaab95)ds

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::ds |
| --- |

## [◆ ](#a1e72ac245fae9d8454ea572780fe6845)eax

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::eax |
| --- |

## [◆ ](#a4a4c4ec64e8f01e8a6e3e14bde63aa8c)ebp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::ebp |
| --- |

## [◆ ](#afe46163b57c39529c3dce5284b0a7eb8)ebx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::ebx |
| --- |

## [◆ ](#a4741e6bc706a7489fe2b45c34f7bdbb6)ecx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::ecx |
| --- |

## [◆ ](#a483a384f835722c4c99a70e3c690e37a)edi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::edi |
| --- |

## [◆ ](#a92a995abd01f4a5fd1a4f04a4e6400a4)edx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::edx |
| --- |

## [◆ ](#acfb5ead961181e179f31f92393517420)eflags

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::eflags |
| --- |

## [◆ ](#af1f3d43a394af43c49caf59a8bd384ab)eip

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::eip |
| --- |

## [◆ ](#ae3b485a947962361d91ee59786d46b93)errorCode

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::errorCode |
| --- |

## [◆ ](#a61d97934f9586b15ef9082ff57317362)es

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::es |
| --- |

## [◆ ](#aff8554d808df765988252674e89d7bef)esi

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::esi |
| --- |

## [◆ ](#ab872f78692b5e2145fc891880558238d)esp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::esp |
| --- |

## [◆ ](#a8e2788e018d8ceb3b83cd889d86723d9)fs

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::fs |
| --- |

## [◆ ](#a6f38a14fc76ee0ef99ef9ce5b7eb10fe)gs

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::gs |
| --- |

## [◆ ](#a4ae87af42cd376c493dccd3fd257e823)ss

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nanoEsf::ss |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/ia32/[arch.h](x86_2ia32_2arch_8h_source.md)

- [nanoEsf](structnanoEsf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
