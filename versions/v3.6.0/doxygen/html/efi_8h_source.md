---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/efi_8h_source.html
original_path: doxygen/html/efi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

efi.h

[Go to the documentation of this file.](efi_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_ARCH\_X86\_INCLUDE\_EFI\_H\_

8#define ZEPHYR\_ARCH\_X86\_INCLUDE\_EFI\_H\_

9

10/\* Boot type value (see prep\_c.c) \*/

[ 11](efi_8h.md#ae7b99236126041cdfd9ad84d93a4e4aa)#define EFI\_BOOT\_TYPE 2

12

13#ifndef \_ASMLANGUAGE

14

[ 15](structefi__boot__arg.md)struct [efi\_boot\_arg](structefi__boot__arg.md) {

[ 16](structefi__boot__arg.md#a00fa2c3d95fa237f5874b7696a69de78) void \*[efi\_systab](structefi__boot__arg.md#a00fa2c3d95fa237f5874b7696a69de78); /\* EFI system table \*/

[ 17](structefi__boot__arg.md#a6164dd7a842052aaa6228dc8ee5b0c43) unsigned long long [efi\_cr3](structefi__boot__arg.md#a6164dd7a842052aaa6228dc8ee5b0c43); /\* EFI page table \*/

[ 18](structefi__boot__arg.md#acbad7866b3242df65d04b95078735829) void \*[acpi\_rsdp](structefi__boot__arg.md#acbad7866b3242df65d04b95078735829);

19};

20

21#if defined(CONFIG\_X86\_EFI)

22

27void [efi\_init](efi_8h.md#a0f53035058d559e128d6c528ec8450d2)(struct [efi\_boot\_arg](structefi__boot__arg.md) \*efi\_arg);

28

33void \*[efi\_get\_acpi\_rsdp](efi_8h.md#a858813d36a2fb7ce319394fb5c87c612)(void);

34

35#else /\* CONFIG\_X86\_EFI \*/

36

[ 37](efi_8h.md#a0f53035058d559e128d6c528ec8450d2)#define efi\_init(...)

[ 38](efi_8h.md#a858813d36a2fb7ce319394fb5c87c612)#define efi\_get\_acpi\_rsdp(...) NULL

39

40#endif /\* CONFIG\_X86\_EFI \*/

41

42#endif /\* \_ASMLANGUAGE \*/

43

44#endif /\* ZEPHYR\_ARCH\_X86\_INCLUDE\_EFI\_H\_ \*/

[efi\_init](efi_8h.md#a0f53035058d559e128d6c528ec8450d2)

#define efi\_init(...)

**Definition** efi.h:37

[efi\_get\_acpi\_rsdp](efi_8h.md#a858813d36a2fb7ce319394fb5c87c612)

#define efi\_get\_acpi\_rsdp(...)

**Definition** efi.h:38

[efi\_boot\_arg](structefi__boot__arg.md)

**Definition** efi.h:15

[efi\_boot\_arg::efi\_systab](structefi__boot__arg.md#a00fa2c3d95fa237f5874b7696a69de78)

void \* efi\_systab

**Definition** efi.h:16

[efi\_boot\_arg::efi\_cr3](structefi__boot__arg.md#a6164dd7a842052aaa6228dc8ee5b0c43)

unsigned long long efi\_cr3

**Definition** efi.h:17

[efi\_boot\_arg::acpi\_rsdp](structefi__boot__arg.md#acbad7866b3242df65d04b95078735829)

void \* acpi\_rsdp

**Definition** efi.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [efi.h](efi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
