---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fnmatch_8h.html
original_path: doxygen/html/fnmatch_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fnmatch.h File Reference

[Go to the source code of this file.](fnmatch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [FNM\_NOMATCH](#af2661230e0cfc9970d6cdbe01571e753)   1 /\* Match failed. \*/ |
| #define | [FNM\_NOSYS](#abf296e95251824c90803dd3aa374190d)   2 /\* Function not implemented. \*/ |
| #define | [FNM\_NORES](#a944d56e32e8885bb5f89d654b383abf8)   3 /\* Out of resources \*/ |
| #define | [FNM\_NOESCAPE](#a0c050a8a7551c2ca86560396de3d20d0)   0x01 /\* Disable backslash escaping. \*/ |
| #define | [FNM\_PATHNAME](#aed9e649990b20ba86e1aa7cacdc1bafe)   0x02 /\* Slash must be matched by slash. \*/ |
| #define | [FNM\_PERIOD](#aab98fecc02c06d6379bfcf416d6d297e)   0x04 /\* Period must be matched by period. \*/ |
| #define | [FNM\_CASEFOLD](#ad41e3158a654dd4dfdab19d97745698a)   0x08 /\* Pattern is matched case-insensitive \*/ |
| #define | [FNM\_LEADING\_DIR](#a94f8f78b6d024e35c971dd3ec057140c)   0x10 /\* Ignore /<tail> after Imatch. \*/ |

| Functions | |
| --- | --- |
| int | [fnmatch](#ae8c5fe22c6e8e83faa4a413e9f07f6a0) (const char \*, const char \*, int) |

## Macro Definition Documentation

## [◆ ](#ad41e3158a654dd4dfdab19d97745698a)FNM\_CASEFOLD

| #define FNM\_CASEFOLD   0x08 /\* Pattern is matched case-insensitive \*/ |
| --- |

## [◆ ](#a94f8f78b6d024e35c971dd3ec057140c)FNM\_LEADING\_DIR

| #define FNM\_LEADING\_DIR   0x10 /\* Ignore /<tail> after Imatch. \*/ |
| --- |

## [◆ ](#a0c050a8a7551c2ca86560396de3d20d0)FNM\_NOESCAPE

| #define FNM\_NOESCAPE   0x01 /\* Disable backslash escaping. \*/ |
| --- |

## [◆ ](#af2661230e0cfc9970d6cdbe01571e753)FNM\_NOMATCH

| #define FNM\_NOMATCH   1 /\* Match failed. \*/ |
| --- |

## [◆ ](#a944d56e32e8885bb5f89d654b383abf8)FNM\_NORES

| #define FNM\_NORES   3 /\* Out of resources \*/ |
| --- |

## [◆ ](#abf296e95251824c90803dd3aa374190d)FNM\_NOSYS

| #define FNM\_NOSYS   2 /\* Function not implemented. \*/ |
| --- |

## [◆ ](#aed9e649990b20ba86e1aa7cacdc1bafe)FNM\_PATHNAME

| #define FNM\_PATHNAME   0x02 /\* Slash must be matched by slash. \*/ |
| --- |

## [◆ ](#aab98fecc02c06d6379bfcf416d6d297e)FNM\_PERIOD

| #define FNM\_PERIOD   0x04 /\* Period must be matched by period. \*/ |
| --- |

## Function Documentation

## [◆ ](#ae8c5fe22c6e8e83faa4a413e9f07f6a0)fnmatch()

| int fnmatch | ( | const char \* | , |
| --- | --- | --- | --- |
|  |  | const char \* | , |
|  |  | int | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [fnmatch.h](fnmatch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
