---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mcumgr__handler__api.html
original_path: doxygen/html/group__mcumgr__handler__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr handler API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr handler registration API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [MCUMGR\_HANDLER\_DEFINE](#ga59833a6c16520816e4488210308b7c7b)(name, \_init) |
|  | Define a MCUmgr handler to register. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mcumgr\_handler\_init\_t](#gaceb63293a54178de29ce0cdf6a03083a)) (void) |
|  | Type definition for a MCUmgr handler initialisation function. |

## Detailed Description

MCUmgr handler registration API.

## Macro Definition Documentation

## [◆ ](#ga59833a6c16520816e4488210308b7c7b)MCUMGR\_HANDLER\_DEFINE

| #define MCUMGR\_HANDLER\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *\_init* ) |

`#include <[handlers.h](handlers_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(mcumgr\_handler, name) = { \

.init = \_init, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Define a MCUmgr handler to register.

This adds a new entry to the iterable section linker list of MCUmgr handers.

Parameters
:   | name | Name of the MCUmgr handler to registger. |
    | --- | --- |
    | \_init | Init function to be called ([mcumgr\_handler\_init\_t](#gaceb63293a54178de29ce0cdf6a03083a)). |

## Typedef Documentation

## [◆ ](#gaceb63293a54178de29ce0cdf6a03083a)mcumgr\_handler\_init\_t

| typedef void(\* mcumgr\_handler\_init\_t) (void) |
| --- |

`#include <[handlers.h](handlers_8h.md)>`

Type definition for a MCUmgr handler initialisation function.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
