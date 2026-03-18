---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__fff__extensions.html
original_path: doxygen/html/group__fff__extensions.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FFF extensions

[Testing](group__testing.md)

This module provides extensions to FFF for simplifying the configuration and usage of fakes.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [RETURN\_HANDLED\_CONTEXT](#ga4a4e81f6291e0bfbe7f60e0a03c2e9b1)(FUNCNAME, CONTEXTTYPE, RESULTFIELD, CONTEXTPTRNAME, HANDLERBODY) |
|  | Wrap custom fake body to extract defined context struct. |

## Detailed Description

This module provides extensions to FFF for simplifying the configuration and usage of fakes.

## Macro Definition Documentation

## [◆ ](#ga4a4e81f6291e0bfbe7f60e0a03c2e9b1)RETURN\_HANDLED\_CONTEXT

| #define RETURN\_HANDLED\_CONTEXT | ( |  | *FUNCNAME*, |
| --- | --- | --- | --- |
|  |  |  | *CONTEXTTYPE*, |
|  |  |  | *RESULTFIELD*, |
|  |  |  | *CONTEXTPTRNAME*, |
|  |  |  | *HANDLERBODY* ) |

`#include <[fff_extensions.h](fff__extensions_8h.md)>`

**Value:**

if (FUNCNAME##\_fake.return\_val\_seq\_len) { \

CONTEXTTYPE \* const contexts = \

CONTAINER\_OF(FUNCNAME##\_fake.return\_val\_seq, \

CONTEXTTYPE, RESULTFIELD); \

size\_t const seq\_idx = (FUNCNAME##\_fake.return\_val\_seq\_idx < \

FUNCNAME##\_fake.return\_val\_seq\_len) ? \

FUNCNAME##\_fake.return\_val\_seq\_idx++ :\

FUNCNAME##\_fake.return\_val\_seq\_idx - 1;\

CONTEXTTYPE \* const CONTEXTPTRNAME = &contexts[seq\_idx]; \

HANDLERBODY; \

} \

return FUNCNAME##\_fake.return\_val

Wrap custom fake body to extract defined context struct.

Add extension macro for simplified creation of fake functions needing call-specific context data.

This macro enables a fake to be implemented as follows and requires no familiarity with the inner workings of FFF.

struct FUNCNAME##\_custom\_fake\_context

{

struct instance \* const instance;

int result;

};

int FUNCNAME##\_custom\_fake(

const struct instance \*\*instance\_out)

{

[RETURN\_HANDLED\_CONTEXT](#ga4a4e81f6291e0bfbe7f60e0a03c2e9b1)(

FUNCNAME,

struct FUNCNAME##\_custom\_fake\_context,

result,

context,

{

if (context != NULL)

{

if (context->result == 0)

{

if (instance\_out != NULL)

{

\*instance\_out = context->instance;

}

}

return context->result;

}

return FUNCNAME##\_fake.return\_val;

}

);

}

[RETURN\_HANDLED\_CONTEXT](#ga4a4e81f6291e0bfbe7f60e0a03c2e9b1)

#define RETURN\_HANDLED\_CONTEXT(FUNCNAME, CONTEXTTYPE, RESULTFIELD, CONTEXTPTRNAME, HANDLERBODY)

Wrap custom fake body to extract defined context struct.

**Definition** fff\_extensions.h:79

Parameters
:   | FUNCNAME | Name of function being faked |
    | --- | --- |
    | CONTEXTTYPE | type of custom defined fake context struct |
    | RESULTFIELD | name of field holding the return type & value |
    | CONTEXTPTRNAME | expected name of pointer to custom defined fake context struct |
    | HANDLERBODY | in-line custom fake handling logic |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
