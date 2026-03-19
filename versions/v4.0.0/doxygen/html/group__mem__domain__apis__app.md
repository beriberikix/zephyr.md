---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mem__domain__apis__app.html
original_path: doxygen/html/group__mem__domain__apis__app.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Application memory domain APIs

[Kernel APIs](group__kernel__apis.md) » [Memory domain APIs](group__mem__domain__apis.md)

Application memory domain APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [K\_APP\_DMEM\_SECTION](#ga81962bb530118ffa13fccdf99f973787)(id) |
|  | Name of the data section for a particular partition. |
| #define | [K\_APP\_BMEM\_SECTION](#ga24cb6342261cc6abc76a7809a4170e64)(id) |
|  | Name of the bss section for a particular partition. |
| #define | [K\_APP\_DMEM](#gace571a7f6ee313a732976cc863b5d0e6)(id) |
|  | Place data in a partition's data section. |
| #define | [K\_APP\_BMEM](#ga8fd691f9c9007ec80432c19f7ce84881)(id) |
|  | Place data in a partition's bss section. |
| #define | [K\_APPMEM\_PARTITION\_DEFINE](#gaba1614a7fa1a2ce2fc7cfd6ecfc02796)(name) |
|  | Define an application memory partition with linker support. |

## Detailed Description

Application memory domain APIs.

## Macro Definition Documentation

## [◆ ](#ga8fd691f9c9007ec80432c19f7ce84881)K\_APP\_BMEM

| #define K\_APP\_BMEM | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[app_memdomain.h](app__memdomain_8h.md)>`

**Value:**

Z\_GENERIC\_SECTION([K\_APP\_BMEM\_SECTION](#ga24cb6342261cc6abc76a7809a4170e64)(id))

[K\_APP\_BMEM\_SECTION](#ga24cb6342261cc6abc76a7809a4170e64)

#define K\_APP\_BMEM\_SECTION(id)

Name of the bss section for a particular partition.

**Definition** app\_memdomain.h:40

Place data in a partition's bss section.

Globals tagged with this will end up in the bss section for the specified memory partition. This data will be zeroed at boot.

Parameters
:   | id | Name of the memory partition to associate this data |
    | --- | --- |

## [◆ ](#ga24cb6342261cc6abc76a7809a4170e64)K\_APP\_BMEM\_SECTION

| #define K\_APP\_BMEM\_SECTION | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[app_memdomain.h](app__memdomain_8h.md)>`

**Value:**

data\_smem\_##id##\_bss

Name of the bss section for a particular partition.

Useful for defining memory pools, or any other macro that takes a section name as a parameter.

Parameters
:   | id | Partition name |
    | --- | --- |

## [◆ ](#gace571a7f6ee313a732976cc863b5d0e6)K\_APP\_DMEM

| #define K\_APP\_DMEM | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[app_memdomain.h](app__memdomain_8h.md)>`

**Value:**

Z\_GENERIC\_SECTION([K\_APP\_DMEM\_SECTION](#ga81962bb530118ffa13fccdf99f973787)(id))

[K\_APP\_DMEM\_SECTION](#ga81962bb530118ffa13fccdf99f973787)

#define K\_APP\_DMEM\_SECTION(id)

Name of the data section for a particular partition.

**Definition** app\_memdomain.h:30

Place data in a partition's data section.

Globals tagged with this will end up in the data section for the specified memory partition. This data should be initialized to some desired value.

Parameters
:   | id | Name of the memory partition to associate this data |
    | --- | --- |

## [◆ ](#ga81962bb530118ffa13fccdf99f973787)K\_APP\_DMEM\_SECTION

| #define K\_APP\_DMEM\_SECTION | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[app_memdomain.h](app__memdomain_8h.md)>`

**Value:**

data\_smem\_##id##\_data

Name of the data section for a particular partition.

Useful for defining memory pools, or any other macro that takes a section name as a parameter.

Parameters
:   | id | Partition name |
    | --- | --- |

## [◆ ](#gaba1614a7fa1a2ce2fc7cfd6ecfc02796)K\_APPMEM\_PARTITION\_DEFINE

| #define K\_APPMEM\_PARTITION\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[app_memdomain.h](app__memdomain_8h.md)>`

**Value:**

extern char Z\_APP\_START(name)[]; \

extern char Z\_APP\_SIZE(name)[]; \

struct [k\_mem\_partition](structk__mem__partition.md) name = { \

.start = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) &Z\_APP\_START(name)[0], \

.size = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) &Z\_APP\_SIZE(name)[0], \

.attr = [K\_MEM\_PARTITION\_P\_RW\_U\_RW](arm__mpu__v7m_8h.md#a9b7cc3c51f518517031d76807470aa10) \

}; \

extern char Z\_APP\_BSS\_START(name)[]; \

extern char Z\_APP\_BSS\_SIZE(name)[]; \

Z\_GENERIC\_SECTION(.app\_regions.name) \

const struct z\_app\_region name##\_region = { \

.bss\_start = &Z\_APP\_BSS\_START(name)[0], \

.bss\_size = ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) &Z\_APP\_BSS\_SIZE(name)[0] \

}; \

Z\_APPMEM\_PLACEHOLDER(name)

[K\_MEM\_PARTITION\_P\_RW\_U\_RW](arm__mpu__v7m_8h.md#a9b7cc3c51f518517031d76807470aa10)

#define K\_MEM\_PARTITION\_P\_RW\_U\_RW

**Definition** arm\_mpu\_v7m.h:190

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

Define an application memory partition with linker support.

Defines a k\_mem\_paritition with the provided name. This name may be used with the K\_APP\_DMEM and K\_APP\_BMEM macros to place globals automatically in this partition.

NOTE: placeholder char variable is defined here to prevent build errors if a partition is defined but nothing ever placed in it.

Parameters
:   | name | Name of the [k\_mem\_partition](structk__mem__partition.md "Memory Partition.") to declare |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
