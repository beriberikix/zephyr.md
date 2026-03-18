---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/x86__acpi__osal_8h_source.html
original_path: doxygen/html/x86__acpi__osal_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

x86\_acpi\_osal.h

[Go to the documentation of this file.](x86__acpi__osal_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#include <[zephyr/arch/x86/efi.h](efi_8h.md)>

7#include <[zephyr/arch/x86/legacy\_bios.h](legacy__bios_8h.md)>

8

9#ifndef ZEPHYR\_ARCH\_X86\_INCLUDE\_X86\_ACPI\_H\_

[ 10](x86__acpi__osal_8h.md#ae9d75b39c455425398c1df34aa1d8f9f)#define ZEPHYR\_ARCH\_X86\_INCLUDE\_X86\_ACPI\_H\_

11

12#if defined(CONFIG\_X86\_EFI)

13static inline void \*[acpi\_rsdp\_get](x86__acpi__osal_8h.md#ac9239bf0202814bbe5c23ccd9be589af)(void)

14{

15 void \*rsdp = [efi\_get\_acpi\_rsdp](efi_8h.md#a858813d36a2fb7ce319394fb5c87c612)();

16

17 if (!rsdp) {

18 rsdp = [bios\_acpi\_rsdp\_get](legacy__bios_8h.md#abd0e1084c1d664b8f05ddea1d956151a)();

19 }

20

21 return rsdp;

22}

23#else

[ 24](x86__acpi__osal_8h.md#ac9239bf0202814bbe5c23ccd9be589af)static inline void \*[acpi\_rsdp\_get](x86__acpi__osal_8h.md#ac9239bf0202814bbe5c23ccd9be589af)(void)

25{

26 return [bios\_acpi\_rsdp\_get](legacy__bios_8h.md#abd0e1084c1d664b8f05ddea1d956151a)();

27}

28#endif /\* CONFIG\_X86\_EFI \*/

29

[ 30](x86__acpi__osal_8h.md#a53a33848ad089415c688bd52fa1b2da2)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [acpi\_timer\_get](x86__acpi__osal_8h.md#a53a33848ad089415c688bd52fa1b2da2)(void)

31{

32 return z\_tsc\_read();

33}

34#endif /\* ZEPHYR\_ARCH\_X86\_INCLUDE\_X86\_ACPI\_H\_ \*/

[efi.h](efi_8h.md)

[efi\_get\_acpi\_rsdp](efi_8h.md#a858813d36a2fb7ce319394fb5c87c612)

#define efi\_get\_acpi\_rsdp(...)

**Definition** efi.h:38

[legacy\_bios.h](legacy__bios_8h.md)

[bios\_acpi\_rsdp\_get](legacy__bios_8h.md#abd0e1084c1d664b8f05ddea1d956151a)

void \* bios\_acpi\_rsdp\_get(void)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[acpi\_timer\_get](x86__acpi__osal_8h.md#a53a33848ad089415c688bd52fa1b2da2)

static uint64\_t acpi\_timer\_get(void)

**Definition** x86\_acpi\_osal.h:30

[acpi\_rsdp\_get](x86__acpi__osal_8h.md#ac9239bf0202814bbe5c23ccd9be589af)

static void \* acpi\_rsdp\_get(void)

**Definition** x86\_acpi\_osal.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [x86\_acpi\_osal.h](x86__acpi__osal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
