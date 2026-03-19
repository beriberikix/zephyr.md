---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/settings_8h.html
original_path: doxygen/html/settings_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](settings_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [settings\_handler](structsettings__handler.md) |
|  | Config handlers for subtree implement a set of handler functions. [More...](structsettings__handler.md#details) |
| struct | [settings\_handler\_static](structsettings__handler__static.md) |
|  | Config handlers without the node element, used for static handlers. [More...](structsettings__handler__static.md#details) |
| struct | [settings\_store](structsettings__store.md) |
|  | Backend handler node for storage handling. [More...](structsettings__store.md#details) |
| struct | [settings\_load\_arg](structsettings__load__arg.md) |
|  | Arguments for data loading. [More...](structsettings__load__arg.md#details) |
| struct | [settings\_store\_itf](structsettings__store__itf.md) |
|  | Backend handler functions. [More...](structsettings__store__itf.md#details) |

| Macros | |
| --- | --- |
| #define | [SETTINGS\_MAX\_DIR\_DEPTH](group__settings.md#ga2afa32b032e88a188c5263156d9e73e1)   8 /\* max depth of settings tree \*/ |
| #define | [SETTINGS\_MAX\_NAME\_LEN](group__settings.md#gad96357290d7289dd1d7917abd575c4f7)   (8 \* [SETTINGS\_MAX\_DIR\_DEPTH](group__settings.md#ga2afa32b032e88a188c5263156d9e73e1)) |
| #define | [SETTINGS\_MAX\_VAL\_LEN](group__settings.md#gaa9705c71c2d7cfdf3beab49d6b510769)   256 |
| #define | [SETTINGS\_NAME\_SEPARATOR](group__settings.md#gab66e3bb2f0f5f5e3a20c6702df6a0694)   '/' |
| #define | [SETTINGS\_NAME\_END](group__settings.md#ga41fb7b74ecb502093d4aa5cd6adb4093)   '=' |
| #define | [SETTINGS\_EXTRA\_LEN](group__settings.md#ga9f10069ed74c368aef366d659d3a917d)   (([SETTINGS\_MAX\_DIR\_DEPTH](group__settings.md#ga2afa32b032e88a188c5263156d9e73e1) - 1) + 2) |
| #define | [SETTINGS\_STATIC\_HANDLER\_DEFINE\_WITH\_CPRIO](group__settings.md#ga2ab4b85d30c5f6c19e505fdd8cc8f437)(\_hname, \_tree, \_get, \_set, \_commit, \_export, \_cprio) |
|  | Define a static handler for settings items. |
| #define | [SETTINGS\_STATIC\_HANDLER\_DEFINE](group__settings.md#ga2098bcfc32c6daa13292d937712e476e)(\_hname, \_tree, \_get, \_set, \_commit, \_export) |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04)) (void \*cb\_arg, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Function used to read the data from the settings storage in h\_set handler implementations. |
| typedef int(\* | [settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535)) (const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg, void \*param) |
|  | Callback function used for direct loading. |

| Functions | |
| --- | --- |
| int | [settings\_subsys\_init](group__settings.md#gaf81fad8575840f73a739d16d79613f8e) (void) |
|  | Initialization of settings and backend. |
| int | [settings\_register\_with\_cprio](group__settings.md#gadf612631e30119ff688f83f16ad5aa89) (struct [settings\_handler](structsettings__handler.md) \*cf, int cprio) |
|  | Register a handler for settings items stored in RAM with commit priority. |
| int | [settings\_register](group__settings.md#gab2043a6d799202e177cc3dfa0cbfa531) (struct [settings\_handler](structsettings__handler.md) \*cf) |
|  | Register a handler for settings items stored in RAM with commit priority set to default. |
| int | [settings\_load](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648) (void) |
|  | Load serialized items from registered persistence sources. |
| int | [settings\_load\_subtree](group__settings.md#gab80e8a21c80243359b652386f7ce2424) (const char \*subtree) |
|  | Load limited set of serialized items from registered persistence sources. |
| int | [settings\_load\_subtree\_direct](group__settings.md#ga1dfe42f40a7d63bbdb81aed864d0ff12) (const char \*subtree, [settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535) cb, void \*param) |
|  | Load limited set of serialized items using given callback. |
| int | [settings\_save](group__settings.md#ga789410aa059398d6c8a7851ea6945b55) (void) |
|  | Save currently running serialized items. |
| int | [settings\_save\_subtree](group__settings.md#ga988b9cb22e256c87ac99d8007ff54a13) (const char \*subtree) |
|  | Save limited set of currently running serialized items. |
| int | [settings\_save\_one](group__settings.md#gaf22356f0dd01d4cf43a6297fafa86e30) (const char \*name, const void \*value, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len) |
|  | Write a single serialized value to persisted storage (if it has changed value). |
| int | [settings\_delete](group__settings.md#ga070b6ad31bca0bee71ec1f1a4d67618d) (const char \*name) |
|  | Delete a single serialized in persisted storage. |
| int | [settings\_commit](group__settings.md#ga623c60b89dda3145f9334343748d5954) (void) |
|  | Call commit for all settings handler. |
| int | [settings\_commit\_subtree](group__settings.md#ga11523bc43121d78e0ac8ee1443559e42) (const char \*subtree) |
|  | Call commit for settings handler that belong to subtree. |
| void | [settings\_src\_register](group__settings__backend.md#gad16bb70588cf69873f8872d7bf90e1c6) (struct [settings\_store](structsettings__store.md) \*cs) |
|  | Register a backend handler acting as source. |
| void | [settings\_dst\_register](group__settings__backend.md#ga37bcada0be44b023cd3759e519e69d01) (struct [settings\_store](structsettings__store.md) \*cs) |
|  | Register a backend handler acting as destination. |
| struct [settings\_handler\_static](structsettings__handler__static.md) \* | [settings\_parse\_and\_lookup](group__settings__backend.md#gab03a10ed0b65809369b4b6f220aa3df6) (const char \*name, const char \*\*next) |
|  | Parses a key to an array of elements and locate corresponding module handler. |
| int | [settings\_call\_set\_handler](group__settings__backend.md#gaf94e311eba2b109cdbddd2767e502e77) (const char \*name, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*read\_cb\_arg, const struct [settings\_load\_arg](structsettings__load__arg.md) \*load\_arg) |
|  | Calls settings handler. |
| int | [settings\_name\_steq](group__settings__name__proc.md#ga6d9d36d54a1bfd59bf7729621653edd9) (const char \*name, const char \*key, const char \*\*next) |
|  | Compares the start of name with a key. |
| int | [settings\_name\_next](group__settings__name__proc.md#gacf259320845ae83c46df634f93c6d3e5) (const char \*name, const char \*\*next) |
|  | determine the number of characters before the first separator |
| int | [settings\_runtime\_set](group__settings__rt.md#gae1b95c47c49774d53b4745af810e881e) (const char \*name, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set a value with a specific key to a module handler. |
| int | [settings\_runtime\_get](group__settings__rt.md#ga99a4714ba8c184afc659c43ec2020844) (const char \*name, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get a value corresponding to a key from a module handler. |
| int | [settings\_runtime\_commit](group__settings__rt.md#gafa96974170dced7a131bfd5f022483f8) (const char \*name) |
|  | Apply settings in a module handler. |
| int | [settings\_storage\_get](#a282c5c2c25ae5a375c51150a87869f14) (void \*\*storage) |
|  | Get the storage instance used by zephyr. |

## Function Documentation

## [◆ ](#a282c5c2c25ae5a375c51150a87869f14)settings\_storage\_get()

| int settings\_storage\_get | ( | void \*\* | *storage* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the storage instance used by zephyr.

The type of storage object instance depends on the settings backend used. It might pointer to: struct [nvs\_fs](structnvs__fs.md "Non-volatile Storage File system structure."), struct [fcb](structfcb.md "FCB instance structure.") or string witch file name depends on settings backend type used.

Return values
:   | Pointer | to which reference to the storage object can be stored. |
    | --- | --- |
    | 0 | on success, negative error code on failure. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [settings](dir_d86a196c339fcb483c3ba090e397efd2.md)
- [settings.h](settings_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
