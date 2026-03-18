---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__settings.html
original_path: doxygen/html/group__settings.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Settings

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md)

| Topics | |
| --- | --- |
|  | [Settings backend interface](group__settings__backend.md) |
|  | settings |
|  | [Settings name processing](group__settings__name__proc.md) |
|  | API for const name processing. |
|  | [Settings subsystem runtime](group__settings__rt.md) |
|  | API for runtime settings. |

| Data Structures | |
| --- | --- |
| struct | [settings\_handler](structsettings__handler.md) |
|  | Config handlers for subtree implement a set of handler functions. [More...](structsettings__handler.md#details) |
| struct | [settings\_handler\_static](structsettings__handler__static.md) |
|  | Config handlers without the node element, used for static handlers. [More...](structsettings__handler__static.md#details) |

| Macros | |
| --- | --- |
| #define | [SETTINGS\_MAX\_DIR\_DEPTH](#ga2afa32b032e88a188c5263156d9e73e1)   8 /\* max depth of settings tree \*/ |
| #define | [SETTINGS\_MAX\_NAME\_LEN](#gad96357290d7289dd1d7917abd575c4f7)   (8 \* [SETTINGS\_MAX\_DIR\_DEPTH](#ga2afa32b032e88a188c5263156d9e73e1)) |
| #define | [SETTINGS\_MAX\_VAL\_LEN](#gaa9705c71c2d7cfdf3beab49d6b510769)   256 |
| #define | [SETTINGS\_NAME\_SEPARATOR](#gab66e3bb2f0f5f5e3a20c6702df6a0694)   '/' |
| #define | [SETTINGS\_NAME\_END](#ga41fb7b74ecb502093d4aa5cd6adb4093)   '=' |
| #define | [SETTINGS\_EXTRA\_LEN](#ga9f10069ed74c368aef366d659d3a917d)   (([SETTINGS\_MAX\_DIR\_DEPTH](#ga2afa32b032e88a188c5263156d9e73e1) - 1) + 2) |
| #define | [SETTINGS\_STATIC\_HANDLER\_DEFINE](#ga2098bcfc32c6daa13292d937712e476e)(\_hname, \_tree, \_get, \_set, \_commit, \_export) |
|  | Define a static handler for settings items. |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [settings\_read\_cb](#ga51cdac276c1fb8cd27fc3eec42749a04)) (void \*cb\_arg, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Function used to read the data from the settings storage in h\_set handler implementations. |
| typedef int(\* | [settings\_load\_direct\_cb](#ga767bf6c2709b1c58afcf4d1c5ef0d535)) (const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg, void \*param) |
|  | Callback function used for direct loading. |

| Functions | |
| --- | --- |
| int | [settings\_subsys\_init](#gaf81fad8575840f73a739d16d79613f8e) (void) |
|  | Initialization of settings and backend. |
| int | [settings\_register](#gab2043a6d799202e177cc3dfa0cbfa531) (struct [settings\_handler](structsettings__handler.md) \*cf) |
|  | Register a handler for settings items stored in RAM. |
| int | [settings\_load](#ga89c6d618df81f197cc5c1a2018b00648) (void) |
|  | Load serialized items from registered persistence sources. |
| int | [settings\_load\_subtree](#gab80e8a21c80243359b652386f7ce2424) (const char \*subtree) |
|  | Load limited set of serialized items from registered persistence sources. |
| int | [settings\_load\_subtree\_direct](#ga1dfe42f40a7d63bbdb81aed864d0ff12) (const char \*subtree, [settings\_load\_direct\_cb](#ga767bf6c2709b1c58afcf4d1c5ef0d535) cb, void \*param) |
|  | Load limited set of serialized items using given callback. |
| int | [settings\_save](#ga789410aa059398d6c8a7851ea6945b55) (void) |
|  | Save currently running serialized items. |
| int | [settings\_save\_subtree](#ga988b9cb22e256c87ac99d8007ff54a13) (const char \*subtree) |
|  | Save limited set of currently running serialized items. |
| int | [settings\_save\_one](#gaf22356f0dd01d4cf43a6297fafa86e30) (const char \*name, const void \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len) |
|  | Write a single serialized value to persisted storage (if it has changed value). |
| int | [settings\_delete](#ga070b6ad31bca0bee71ec1f1a4d67618d) (const char \*name) |
|  | Delete a single serialized in persisted storage. |
| int | [settings\_commit](#ga623c60b89dda3145f9334343748d5954) (void) |
|  | Call commit for all settings handler. |
| int | [settings\_commit\_subtree](#ga11523bc43121d78e0ac8ee1443559e42) (const char \*subtree) |
|  | Call commit for settings handler that belong to subtree. |

## Detailed Description

Since
:   1.12

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga9f10069ed74c368aef366d659d3a917d)SETTINGS\_EXTRA\_LEN

| #define SETTINGS\_EXTRA\_LEN   (([SETTINGS\_MAX\_DIR\_DEPTH](#ga2afa32b032e88a188c5263156d9e73e1) - 1) + 2) |
| --- |

`#include <[settings.h](settings_8h.md)>`

## [◆ ](#ga2afa32b032e88a188c5263156d9e73e1)SETTINGS\_MAX\_DIR\_DEPTH

| #define SETTINGS\_MAX\_DIR\_DEPTH   8 /\* max depth of settings tree \*/ |
| --- |

`#include <[settings.h](settings_8h.md)>`

## [◆ ](#gad96357290d7289dd1d7917abd575c4f7)SETTINGS\_MAX\_NAME\_LEN

| #define SETTINGS\_MAX\_NAME\_LEN   (8 \* [SETTINGS\_MAX\_DIR\_DEPTH](#ga2afa32b032e88a188c5263156d9e73e1)) |
| --- |

`#include <[settings.h](settings_8h.md)>`

## [◆ ](#gaa9705c71c2d7cfdf3beab49d6b510769)SETTINGS\_MAX\_VAL\_LEN

| #define SETTINGS\_MAX\_VAL\_LEN   256 |
| --- |

`#include <[settings.h](settings_8h.md)>`

## [◆ ](#ga41fb7b74ecb502093d4aa5cd6adb4093)SETTINGS\_NAME\_END

| #define SETTINGS\_NAME\_END   '=' |
| --- |

`#include <[settings.h](settings_8h.md)>`

## [◆ ](#gab66e3bb2f0f5f5e3a20c6702df6a0694)SETTINGS\_NAME\_SEPARATOR

| #define SETTINGS\_NAME\_SEPARATOR   '/' |
| --- |

`#include <[settings.h](settings_8h.md)>`

## [◆ ](#ga2098bcfc32c6daa13292d937712e476e)SETTINGS\_STATIC\_HANDLER\_DEFINE

| #define SETTINGS\_STATIC\_HANDLER\_DEFINE | ( |  | *\_hname*, |
| --- | --- | --- | --- |
|  |  |  | *\_tree*, |
|  |  |  | *\_get*, |
|  |  |  | *\_set*, |
|  |  |  | *\_commit*, |
|  |  |  | *\_export* ) |

`#include <[settings.h](settings_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([settings\_handler\_static](structsettings__handler__static.md), \

settings\_handler\_ ## \_hname) = { \

.name = \_tree, \

.h\_get = \_get, \

.h\_set = \_set, \

.h\_commit = \_commit, \

.h\_export = \_export, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[settings\_handler\_static](structsettings__handler__static.md)

Config handlers without the node element, used for static handlers.

**Definition** settings.h:134

Define a static handler for settings items.

Parameters
:   | \_hname | handler name |
    | --- | --- |
    | \_tree | subtree name |
    | \_get | get routine (can be NULL) |
    | \_set | set routine (can be NULL) |
    | \_commit | commit routine (can be NULL) |
    | \_export | export routine (can be NULL) |

This creates a variable *hname prepended by [settings\_handler](structsettings__handler.md "Config handlers for subtree implement a set of handler functions.")*.

## Typedef Documentation

## [◆ ](#ga767bf6c2709b1c58afcf4d1c5ef0d535)settings\_load\_direct\_cb

| typedef int(\* settings\_load\_direct\_cb) (const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg, void \*param) |
| --- |

`#include <[settings.h](settings_8h.md)>`

Callback function used for direct loading.

Used by [settings\_load\_subtree\_direct](#ga1dfe42f40a7d63bbdb81aed864d0ff12) function.

Parameters
:   | [in] | key | the name with skipped part that was used as name in handler registration |
    | --- | --- | --- |
    | [in] | len | the size of the data found in the backend. |
    | [in] | read\_cb | function provided to read the data from the backend. |
    | [in,out] | cb\_arg | arguments for the read function provided by the backend. |
    | [in,out] | param | parameter given to the [settings\_load\_subtree\_direct](#ga1dfe42f40a7d63bbdb81aed864d0ff12) function. |

Returns
:   When nonzero value is returned, further subtree searching is stopped.

## [◆ ](#ga51cdac276c1fb8cd27fc3eec42749a04)settings\_read\_cb

| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* settings\_read\_cb) (void \*cb\_arg, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[settings.h](settings_8h.md)>`

Function used to read the data from the settings storage in h\_set handler implementations.

Parameters
:   | [in] | cb\_arg | arguments for the read function. Appropriate cb\_arg is transferred to h\_set handler implementation by the backend. |
    | --- | --- | --- |
    | [out] | data | the destination buffer |
    | [in] | len | length of read |

Returns
:   positive: Number of bytes read, 0: key-value pair is deleted. On error returns -ERRNO code.

## Function Documentation

## [◆ ](#ga623c60b89dda3145f9334343748d5954)settings\_commit()

| int settings\_commit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Call commit for all settings handler.

This should apply all settings which has been set, but not applied yet.

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga11523bc43121d78e0ac8ee1443559e42)settings\_commit\_subtree()

| int settings\_commit\_subtree | ( | const char \* | *subtree* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Call commit for settings handler that belong to subtree.

This should apply all settings which has been set, but not applied yet.

Parameters
:   | [in] | subtree | name of the subtree to be committed. |
    | --- | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga070b6ad31bca0bee71ec1f1a4d67618d)settings\_delete()

| int settings\_delete | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Delete a single serialized in persisted storage.

Deleting an existing key-value pair in the settings mean to set its value to NULL.

Parameters
:   | name | Name/key of the settings item. |
    | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga89c6d618df81f197cc5c1a2018b00648)settings\_load()

| int settings\_load | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Load serialized items from registered persistence sources.

Handlers for serialized item subtrees registered earlier will be called for encountered values.

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gab80e8a21c80243359b652386f7ce2424)settings\_load\_subtree()

| int settings\_load\_subtree | ( | const char \* | *subtree* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Load limited set of serialized items from registered persistence sources.

Handlers for serialized item subtrees registered earlier will be called for encountered values that belong to the subtree.

Parameters
:   | [in] | subtree | name of the subtree to be loaded. |
    | --- | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga1dfe42f40a7d63bbdb81aed864d0ff12)settings\_load\_subtree\_direct()

| int settings\_load\_subtree\_direct | ( | const char \* | *subtree*, |
| --- | --- | --- | --- |
|  |  | [settings\_load\_direct\_cb](#ga767bf6c2709b1c58afcf4d1c5ef0d535) | *cb*, |
|  |  | void \* | *param* ) |

`#include <[settings.h](settings_8h.md)>`

Load limited set of serialized items using given callback.

This function bypasses the normal data workflow in settings module. All the settings values that are found are passed to the given callback.

Note
:   This function does not call commit function. It works as a blocking function, so it is up to the user to call any kind of commit function when this operation ends.

Parameters
:   | [in] | subtree | subtree name of the subtree to be loaded. |
    | --- | --- | --- |
    | [in] | cb | pointer to the callback function. |
    | [in,out] | param | parameter to be passed when callback function is called. |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gab2043a6d799202e177cc3dfa0cbfa531)settings\_register()

| int settings\_register | ( | struct [settings\_handler](structsettings__handler.md) \* | *cf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Register a handler for settings items stored in RAM.

Parameters
:   | cf | Structure containing registration info. |
    | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga789410aa059398d6c8a7851ea6945b55)settings\_save()

| int settings\_save | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Save currently running serialized items.

All serialized items which are different from currently persisted values will be saved.

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gaf22356f0dd01d4cf43a6297fafa86e30)settings\_save\_one()

| int settings\_save\_one | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const void \* | *value*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *val\_len* ) |

`#include <[settings.h](settings_8h.md)>`

Write a single serialized value to persisted storage (if it has changed value).

Parameters
:   | name | Name/key of the settings item. |
    | --- | --- |
    | value | Pointer to the value of the settings item. This value will be transferred to the [settings\_handler::h\_export](structsettings__handler.md#a30207125407f57a0f117ecaee5a2054a "settings_handler::h_export") handler implementation. |
    | val\_len | Length of the value. |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga988b9cb22e256c87ac99d8007ff54a13)settings\_save\_subtree()

| int settings\_save\_subtree | ( | const char \* | *subtree* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Save limited set of currently running serialized items.

All serialized items that belong to subtree and which are different from currently persisted values will be saved.

Parameters
:   | [in] | subtree | name of the subtree to be loaded. |
    | --- | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#gaf81fad8575840f73a739d16d79613f8e)settings\_subsys\_init()

| int settings\_subsys\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Initialization of settings and backend.

Can be called at application startup. In case the backend is a FS Remember to call it after the FS was mounted. For FCB backend it can be called without such a restriction.

Returns
:   0 on success, non-zero on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
