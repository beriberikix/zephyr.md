---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__zbus__apis.html
original_path: doxygen/html/group__zbus__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Zbus APIs

[Operating System Services](group__os__services.md)

Zbus API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [zbus\_channel\_data](structzbus__channel__data.md) |
|  | Type used to represent a channel mutable data. [More...](structzbus__channel__data.md#details) |
| struct | [zbus\_channel](structzbus__channel.md) |
|  | Type used to represent a channel. [More...](structzbus__channel.md#details) |
| struct | [zbus\_observer\_data](structzbus__observer__data.md) |
| struct | [zbus\_observer](structzbus__observer.md) |
|  | Type used to represent an observer. [More...](structzbus__observer.md#details) |

| Macros | |
| --- | --- |
| #define | [ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK](#ga7f763caca474e6c910793d2c714f80b4)(\_chan, \_obs, \_masked, \_prio) |
|  | Add a static channel observation. |
| #define | [ZBUS\_CHAN\_ADD\_OBS](#gaf63215f3f53741edf52b4d0d7b2b97df)(\_chan, \_obs, \_prio) |
|  | Add a static channel observation. |
| #define | [ZBUS\_OBS\_DECLARE](#ga49f169c6d50a3bad57e1b319362d2924)(...) |
|  | This macro list the observers to be used in a file. |
| #define | [ZBUS\_CHAN\_DECLARE](#ga0662b2db8077a8075c07a3afd0161d0f)(...) |
|  | This macro list the channels to be used in a file. |
| #define | [ZBUS\_OBSERVERS\_EMPTY](#ga763dad07a1ae9bb38f9c240e1920caef) |
|  | This macro indicates the channel has no observers. |
| #define | [ZBUS\_OBSERVERS](#gafed25f045c3b8d438daf4ebd5e517692)(...) |
|  | This macro indicates the channel has listed observers. |
| #define | [ZBUS\_CHAN\_DEFINE](#ga29a3a39e5c78a34b2d8491615d1f0687)(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) |
|  | Zbus channel definition. |
| #define | [ZBUS\_MSG\_INIT](#ga4bf8c445814c1fcee9b9819a36bc9bd6)(\_val, ...) |
|  | Initialize a message. |
| #define | [ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](#gaf56f71babe2bb27258f025332b80c58f)(\_name, \_queue\_size, \_enable) |
|  | Define and initialize a subscriber. |
| #define | [ZBUS\_SUBSCRIBER\_DEFINE](#gac17a735cccecfc90f26127e48cf6279a)(\_name, \_queue\_size) |
|  | Define and initialize a subscriber. |
| #define | [ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE](#gace4ac9da0e1bab7ba72797783ded948f)(\_name, \_cb, \_enable) |
|  | Define and initialize a listener. |
| #define | [ZBUS\_LISTENER\_DEFINE](#gabfc7be8298e76fe2f7ae628be30b8390)(\_name, \_cb) |
|  | Define and initialize a listener. |
| #define | [ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](#ga6089c1ae0dad91306f79d48a63b31785)(\_name, \_enable) |
|  | Define and initialize a message subscriber. |
| #define | [ZBUS\_MSG\_SUBSCRIBER\_DEFINE](#ga07a0c2c428c9e4891e86a63a420b2268)(\_name) |
|  | Define and initialize an enabled message subscriber. |

| Enumerations | |
| --- | --- |
| enum | [zbus\_observer\_type](#ga88941281d7bdd24f3cfbb53e57711d8f) { [ZBUS\_OBSERVER\_LISTENER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) , [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) , [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) } |
|  | Type used to represent an observer type. [More...](#ga88941281d7bdd24f3cfbb53e57711d8f) |

| Functions | |
| --- | --- |
| int | [zbus\_chan\_pub](#gadfcaba65b397c1d8c31836ef3cf61244) (const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Publish to a channel. |
| int | [zbus\_chan\_read](#ga8209721e0a295c84d112ba1a7171100e) (const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read a channel. |
| int | [zbus\_chan\_claim](#ga00bfb7db54594029f4d288bcf5b56b3a) (const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Claim a channel. |
| int | [zbus\_chan\_finish](#ga74747affb345e68ce1d564c349409e59) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Finish a channel claim. |
| int | [zbus\_chan\_notify](#ga6ec2f463801499e23a011fa4e68aa3e7) (const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Force a channel notification. |
| static const char \* | [zbus\_chan\_name](#ga05a220636fc6bb58b97805e558b76d73) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the channel's name. |
| static void \* | [zbus\_chan\_msg](#gaaf8b34113b7b993438bd42db64812572) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the reference for a channel message directly. |
| static const void \* | [zbus\_chan\_const\_msg](#gafee07c355df9ac86b85e601196b56a10) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get a constant reference for a channel message directly. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [zbus\_chan\_msg\_size](#ga8895a18b282ca2fe7528b4e5cf48e025) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the channel's message size. |
| static void \* | [zbus\_chan\_user\_data](#gac0b0ed0356fca5a8b65a3332931a369a) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the channel's user data. |
| static void | [zbus\_chan\_set\_msg\_sub\_pool](#ga3f90d50f20e7779ef257676ac10da357) (const struct [zbus\_channel](structzbus__channel.md) \*chan, struct [net\_buf\_pool](structnet__buf__pool.md) \*pool) |
|  | Set the channel's msg subscriber [net\_buf](structnet__buf.md "Network buffer representation.") pool. |
| static void | [zbus\_chan\_pub\_stats\_update](#gaef067fb1e8b834993662af84b916483a) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Update the publishing statistics for a channel. |
| static [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [zbus\_chan\_pub\_stats\_last\_time](#gac5dff9990d709d736b30f36d68c0297b) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the time a channel was last published to. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [zbus\_chan\_pub\_stats\_count](#ga5648bf527de4aff89648a34bf8a7539a) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the number of times a channel has been published to. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [zbus\_chan\_pub\_stats\_avg\_period](#ga09503e2b9c01f79136f9eb600ddb3f31) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the average period between publishes to a channel. |
| int | [zbus\_chan\_add\_obs](#gaddd8ce480bc29ead4442e529915cfbf6) (const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Add an observer to a channel. |
| int | [zbus\_chan\_rm\_obs](#gaee11d7472a3f87156b8ef1dcfbe897c4) (const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Remove an observer from a channel. |
| int | [zbus\_obs\_set\_enable](#ga96767314e040e42609867a36684a6349) (const struct [zbus\_observer](structzbus__observer.md) \*obs, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Change the observer state. |
| static int | [zbus\_obs\_is\_enabled](#ga315fd4e0b6a3c01a23307dd890e69894) (const struct [zbus\_observer](structzbus__observer.md) \*obs, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*enable) |
|  | Get the observer state. |
| int | [zbus\_obs\_set\_chan\_notification\_mask](#ga9513264f912f54b60c4341642f578e5a) (const struct [zbus\_observer](structzbus__observer.md) \*obs, const struct [zbus\_channel](structzbus__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) masked) |
|  | Mask notifications from a channel to an observer. |
| int | [zbus\_obs\_is\_chan\_notification\_masked](#ga41ae9799a52c2a7954500b0a3c78d19f) (const struct [zbus\_observer](structzbus__observer.md) \*obs, const struct [zbus\_channel](structzbus__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*masked) |
|  | Get the notifications masking state from a channel to an observer. |
| static const char \* | [zbus\_obs\_name](#ga5bb33ec5b914e6cbc87fa70bf763ad15) (const struct [zbus\_observer](structzbus__observer.md) \*obs) |
|  | Get the observer's name. |
| int | [zbus\_obs\_attach\_to\_thread](#gabecf160e4d468d0275ad79e22fd0fb5b) (const struct [zbus\_observer](structzbus__observer.md) \*obs) |
|  | Set the observer thread priority by attaching it to a thread. |
| int | [zbus\_obs\_detach\_from\_thread](#ga493c125c31e44d5a222f0e9c6d01249e) (const struct [zbus\_observer](structzbus__observer.md) \*obs) |
|  | Clear the observer thread priority by detaching it from a thread. |
| int | [zbus\_sub\_wait](#ga84a65e276a01ef97eeb5c81b880da72b) (const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for a channel notification. |
| int | [zbus\_sub\_wait\_msg](#gaeffce45446509e488192a4e6442453fb) (const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for a channel message. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_channels](#ga6dffd25f4eb368e773c2bd55f34a0e10) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan)) |
|  | Iterate over channels. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_channels\_with\_user\_data](#gab8df108b0238757ff631ec1e120fa2c3) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), void \*user\_data) |
|  | Iterate over channels with user data. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_observers](#ga2fa50316993afc5807e9d707d664be14) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs)) |
|  | Iterate over observers. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_observers\_with\_user\_data](#ga2f4e39c500fed0a6bcfedb5dec3f797a) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), void \*user\_data) |
|  | Iterate over observers with user data. |

## Detailed Description

Zbus API.

## Macro Definition Documentation

## [◆ ](#gaf63215f3f53741edf52b4d0d7b2b97df)ZBUS\_CHAN\_ADD\_OBS

| #define ZBUS\_CHAN\_ADD\_OBS | ( |  | *\_chan*, |
| --- | --- | --- | --- |
|  |  |  | *\_obs*, |
|  |  |  | *\_prio* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK](#ga7f763caca474e6c910793d2c714f80b4)(\_chan, \_obs, false, \_prio)

[ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK](#ga7f763caca474e6c910793d2c714f80b4)

#define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK(\_chan, \_obs, \_masked, \_prio)

Add a static channel observation.

**Definition** zbus.h:281

Add a static channel observation.

This macro initializes a channel observation by receiving the channel and the observer.

Parameters
:   | \_chan | Channel instance. |
    | --- | --- |
    | \_obs | Observer instance. |
    | \_prio | Observer notification sequence priority. |

## [◆ ](#ga7f763caca474e6c910793d2c714f80b4)ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK

| #define ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK | ( |  | *\_chan*, |
| --- | --- | --- | --- |
|  |  |  | *\_obs*, |
|  |  |  | *\_masked*, |
|  |  |  | *\_prio* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(zbus\_channel\_observation, \

\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs))) = { \

.chan = &\_chan, \

.obs = &\_obs, \

}; \

STRUCT\_SECTION\_ITERABLE(zbus\_channel\_observation\_mask, \

\_CONCAT(\_CONCAT(\_CONCAT(\_chan, zz), \_CONCAT(\_prio, \_obs)), \

\_mask)) = {.enabled = \_masked}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Add a static channel observation.

This macro initializes a channel observation by receiving the channel and the observer.

Parameters
:   | \_chan | Channel instance. |
    | --- | --- |
    | \_obs | Observer instance. |
    | \_masked | Observation state. |
    | \_prio | Observer notification sequence priority. |

## [◆ ](#ga0662b2db8077a8075c07a3afd0161d0f)ZBUS\_CHAN\_DECLARE

| #define ZBUS\_CHAN\_DECLARE | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)(\_ZBUS\_CHAN\_EXTERN, (;), \_\_VA\_ARGS\_\_)

[FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)

#define FOR\_EACH(F, sep,...)

Call a macro F on each provided argument with a given separator between each call.

**Definition** util\_macro.h:481

This macro list the channels to be used in a file.

Internally, it declares the channels with the extern statement. Note it is only necessary when the channels are declared outside the file.

## [◆ ](#ga29a3a39e5c78a34b2d8491615d1f0687)ZBUS\_CHAN\_DEFINE

| #define ZBUS\_CHAN\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_type*, |
|  |  |  | *\_validator*, |
|  |  |  | *\_user\_data*, |
|  |  |  | *\_observers*, |
|  |  |  | *\_init\_val* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

static \_type \_CONCAT(\_zbus\_message\_, \_name) = \_init\_val; \

static struct [zbus\_channel\_data](structzbus__channel__data.md) \_CONCAT(\_zbus\_chan\_data\_, \_name) = { \

.observers\_start\_idx = -1, \

.observers\_end\_idx = -1, \

.sem = Z\_SEM\_INITIALIZER(\_CONCAT(\_zbus\_chan\_data\_, \_name).sem, 1, 1), \

IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

.highest\_observer\_priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

)) \

IF\_ENABLED(CONFIG\_ZBUS\_RUNTIME\_OBSERVERS, ( \

.observers = [SYS\_SLIST\_STATIC\_INIT](group__single-linked-list__apis.md#ga7f4710125f45643b7acdaa58dbfff225)( \

&\_CONCAT(\_zbus\_chan\_data\_, \_name).observers), \

)) \

}; \

static [K\_MUTEX\_DEFINE](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)(\_CONCAT(\_zbus\_mutex\_, \_name)); \

\_ZBUS\_CPP\_EXTERN const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([zbus\_channel](structzbus__channel.md), \_name) = { \

ZBUS\_CHANNEL\_NAME\_INIT(\_name) /\* Maybe removed \*/ \

.message = &\_CONCAT(\_zbus\_message\_, \_name), \

.message\_size = sizeof(\_type), \

.user\_data = \_user\_data, \

.validator = \_validator, \

.data = &\_CONCAT(\_zbus\_chan\_data\_, \_name), \

IF\_ENABLED(ZBUS\_MSG\_SUBSCRIBER\_NET\_BUF\_POOL\_ISOLATION, ( \

.msg\_subscriber\_pool = &\_zbus\_msg\_subscribers\_pool, \

)) \

}; \

/\* Extern declaration of observers \*/ \

ZBUS\_OBS\_DECLARE(\_observers); \

/\* Create all channel observations from observers list \*/ \

FOR\_EACH\_FIXED\_ARG\_NONEMPTY\_TERM(\_ZBUS\_CHAN\_OBSERVATION, (;), \_name, \_observers)

[K\_MUTEX\_DEFINE](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)

#define K\_MUTEX\_DEFINE(name)

Statically define and initialize a mutex.

**Definition** kernel.h:3037

[SYS\_SLIST\_STATIC\_INIT](group__single-linked-list__apis.md#ga7f4710125f45643b7acdaa58dbfff225)

#define SYS\_SLIST\_STATIC\_INIT(ptr\_to\_list)

Statically initialize a single-linked list.

**Definition** slist.h:209

[zbus\_channel\_data](structzbus__channel__data.md)

Type used to represent a channel mutable data.

**Definition** zbus.h:30

[zbus\_channel](structzbus__channel.md)

Type used to represent a channel.

**Definition** zbus.h:80

Zbus channel definition.

This macro defines a channel.

Parameters
:   | \_name | The channel's name. |
    | --- | --- |
    | \_type | The Message type. It must be a struct or union. |
    | \_validator | The validator function. |
    | \_user\_data | A pointer to the user data. |

See also
:   struct [zbus\_channel](structzbus__channel.md "Type used to represent a channel.")

Parameters
:   | \_observers | The observers list. The sequence indicates the priority of the observer. The first the highest priority. |
    | --- | --- |
    | \_init\_val | The message initialization. |

## [◆ ](#gabfc7be8298e76fe2f7ae628be30b8390)ZBUS\_LISTENER\_DEFINE

| #define ZBUS\_LISTENER\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_cb* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE](#gace4ac9da0e1bab7ba72797783ded948f)(\_name, \_cb, true)

[ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE](#gace4ac9da0e1bab7ba72797783ded948f)

#define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE(\_name, \_cb, \_enable)

Define and initialize a listener.

**Definition** zbus.h:453

Define and initialize a listener.

This macro defines an observer of listener type. This macro establishes the callback where the listener will be notified synchronously and initialize the struct [zbus\_observer](structzbus__observer.md "Type used to represent an observer.") defining the listener. The listeners are defined in the enabled state with this macro.

Parameters
:   | [in] | \_name | The listener's name. |
    | --- | --- | --- |
    | [in] | \_cb | The callback function. |

## [◆ ](#gace4ac9da0e1bab7ba72797783ded948f)ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE

| #define ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_cb*, |
|  |  |  | *\_enable* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

static struct [zbus\_observer\_data](structzbus__observer__data.md) \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

.enabled = \_enable, \

IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

.priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

)) \

}; \

\_ZBUS\_CPP\_EXTERN const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([zbus\_observer](structzbus__observer.md), \_name) = { \

ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

.type = [ZBUS\_OBSERVER\_LISTENER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c), \

.data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

.callback = (\_cb) \

}

[ZBUS\_OBSERVER\_LISTENER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c)

@ ZBUS\_OBSERVER\_LISTENER\_TYPE

**Definition** zbus.h:114

[zbus\_observer\_data](structzbus__observer__data.md)

**Definition** zbus.h:119

[zbus\_observer](structzbus__observer.md)

Type used to represent an observer.

**Definition** zbus.h:144

Define and initialize a listener.

This macro defines an observer of listener type. This macro establishes the callback where the listener will be notified synchronously, and initialize the struct [zbus\_observer](structzbus__observer.md "Type used to represent an observer.") defining the listener.

Parameters
:   | [in] | \_name | The listener's name. |
    | --- | --- | --- |
    | [in] | \_cb | The callback function. |
    | [in] | \_enable | The listener initial enable state. |

## [◆ ](#ga4bf8c445814c1fcee9b9819a36bc9bd6)ZBUS\_MSG\_INIT

| #define ZBUS\_MSG\_INIT | ( |  | *\_val*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

{ \

\_val, ##\_\_VA\_ARGS\_\_ \

}

Initialize a message.

This macro initializes a message by passing the values to initialize the message struct or union.

Parameters
:   | [in] | \_val | Variadic with the initial values. ZBUS\_INIT(0) means {0}, as ZBUS\_INIT(.a=10, .b=30) means {.a=10, .b=30}. |
    | --- | --- | --- |

## [◆ ](#ga07a0c2c428c9e4891e86a63a420b2268)ZBUS\_MSG\_SUBSCRIBER\_DEFINE

| #define ZBUS\_MSG\_SUBSCRIBER\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](#ga6089c1ae0dad91306f79d48a63b31785)(\_name, true)

[ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](#ga6089c1ae0dad91306f79d48a63b31785)

#define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_enable)

Define and initialize a message subscriber.

**Definition** zbus.h:492

Define and initialize an enabled message subscriber.

This macro defines an observer of message subscriber type. It defines a FIFO where the subscriber will receive the message asynchronously and initialize the [zbus\_observer](structzbus__observer.md "zbus_observer") defining the subscriber. The message subscribers are defined in the enabled state with this macro.

Parameters
:   | [in] | \_name | The subscriber's name. |
    | --- | --- | --- |

## [◆ ](#ga6089c1ae0dad91306f79d48a63b31785)ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE

| #define ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_enable* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

static [K\_FIFO\_DEFINE](group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274)(\_zbus\_observer\_fifo\_##\_name); \

static struct [zbus\_observer\_data](structzbus__observer__data.md) \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

.enabled = \_enable, \

IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

.priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

)) \

}; \

\_ZBUS\_CPP\_EXTERN const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([zbus\_observer](structzbus__observer.md), \_name) = { \

ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

.type = [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c), \

.data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

.message\_fifo = &\_zbus\_observer\_fifo\_##\_name, \

}

[K\_FIFO\_DEFINE](group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274)

#define K\_FIFO\_DEFINE(name)

Statically define and initialize a FIFO queue.

**Definition** kernel.h:2701

[ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c)

@ ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE

**Definition** zbus.h:116

Define and initialize a message subscriber.

This macro defines an observer of [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) type. It defines a FIFO where the subscriber will receive the message asynchronously and initialize the [zbus\_observer](structzbus__observer.md "zbus_observer") defining the subscriber.

Parameters
:   | [in] | \_name | The subscriber's name. |
    | --- | --- | --- |
    | [in] | \_enable | The subscriber's initial state. |

## [◆ ](#ga49f169c6d50a3bad57e1b319362d2924)ZBUS\_OBS\_DECLARE

| #define ZBUS\_OBS\_DECLARE | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[FOR\_EACH\_NONEMPTY\_TERM](group__sys-util.md#ga24b3862161d725f5503b1bb08f4e339f)(\_ZBUS\_OBS\_EXTERN, (;), \_\_VA\_ARGS\_\_)

[FOR\_EACH\_NONEMPTY\_TERM](group__sys-util.md#ga24b3862161d725f5503b1bb08f4e339f)

#define FOR\_EACH\_NONEMPTY\_TERM(F, term,...)

Like FOR\_EACH(), but with a terminator instead of a separator, and drops empty elements from the argu...

**Definition** util\_macro.h:536

This macro list the observers to be used in a file.

Internally, it declares the observers with the extern statement. Note it is only necessary when the observers are declared outside the file.

## [◆ ](#gafed25f045c3b8d438daf4ebd5e517692)ZBUS\_OBSERVERS

| #define ZBUS\_OBSERVERS | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

\_\_VA\_ARGS\_\_

This macro indicates the channel has listed observers.

Note the sequence of observer notification will follow the same as listed.

## [◆ ](#ga763dad07a1ae9bb38f9c240e1920caef)ZBUS\_OBSERVERS\_EMPTY

| #define ZBUS\_OBSERVERS\_EMPTY |
| --- |

`#include <[zbus.h](zbus_8h.md)>`

This macro indicates the channel has no observers.

## [◆ ](#gac17a735cccecfc90f26127e48cf6279a)ZBUS\_SUBSCRIBER\_DEFINE

| #define ZBUS\_SUBSCRIBER\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_queue\_size* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](#gaf56f71babe2bb27258f025332b80c58f)(\_name, \_queue\_size, true)

[ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](#gaf56f71babe2bb27258f025332b80c58f)

#define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE(\_name, \_queue\_size, \_enable)

Define and initialize a subscriber.

**Definition** zbus.h:407

Define and initialize a subscriber.

This macro defines an observer of subscriber type. It defines a message queue where the subscriber will receive the notification asynchronously, and initialize the struct
[zbus\_observer](structzbus__observer.md "Type used to represent an observer.") defining the subscriber. The subscribers are defined in the enabled state with this macro.

Parameters
:   | [in] | \_name | The subscriber's name. |
    | --- | --- | --- |
    | [in] | \_queue\_size | The notification queue's size. |

## [◆ ](#gaf56f71babe2bb27258f025332b80c58f)ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE

| #define ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_queue\_size*, |
|  |  |  | *\_enable* ) |

`#include <[zbus.h](zbus_8h.md)>`

**Value:**

[K\_MSGQ\_DEFINE](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)(\_zbus\_observer\_queue\_##\_name, \

sizeof(struct [zbus\_channel](structzbus__channel.md) \*), \

\_queue\_size, sizeof(struct [zbus\_channel](structzbus__channel.md) \*) \

); \

static struct [zbus\_observer\_data](structzbus__observer__data.md) \_CONCAT(\_zbus\_obs\_data\_, \_name) = { \

.enabled = \_enable, \

IF\_ENABLED(CONFIG\_ZBUS\_PRIORITY\_BOOST, ( \

.priority = ZBUS\_MIN\_THREAD\_PRIORITY, \

)) \

}; \

\_ZBUS\_CPP\_EXTERN const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([zbus\_observer](structzbus__observer.md), \_name) = { \

ZBUS\_OBSERVER\_NAME\_INIT(\_name) /\* Name field \*/ \

.type = [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3), \

.data = &\_CONCAT(\_zbus\_obs\_data\_, \_name), \

.queue = &\_zbus\_observer\_queue\_##\_name, \

}

[K\_MSGQ\_DEFINE](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)

#define K\_MSGQ\_DEFINE(q\_name, q\_msg\_size, q\_max\_msgs, q\_align)

Statically define and initialize a message queue.

**Definition** kernel.h:4590

[ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3)

@ ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE

**Definition** zbus.h:115

Define and initialize a subscriber.

This macro defines an observer of subscriber type. It defines a message queue where the subscriber will receive the notification asynchronously, and initialize the struct
[zbus\_observer](structzbus__observer.md "Type used to represent an observer.") defining the subscriber.

Parameters
:   | [in] | \_name | The subscriber's name. |
    | --- | --- | --- |
    | [in] | \_queue\_size | The notification queue's size. |
    | [in] | \_enable | The subscriber initial enable state. |

## Enumeration Type Documentation

## [◆ ](#ga88941281d7bdd24f3cfbb53e57711d8f)zbus\_observer\_type

| enum [zbus\_observer\_type](#ga88941281d7bdd24f3cfbb53e57711d8f) |
| --- |

`#include <[zbus.h](zbus_8h.md)>`

Type used to represent an observer type.

A observer can be a listener or a subscriber.

| Enumerator | |
| --- | --- |
| ZBUS\_OBSERVER\_LISTENER\_TYPE |  |
| ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE |  |
| ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE |  |

## Function Documentation

## [◆ ](#gaddd8ce480bc29ead4442e529915cfbf6)zbus\_chan\_add\_obs()

| int zbus\_chan\_add\_obs | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | const struct [zbus\_observer](structzbus__observer.md) \* | *obs*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Add an observer to a channel.

This routine adds an observer to the channel.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |
    | obs | The observer's reference to be added. |
    | timeout | Waiting period to add an observer, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Observer added to the channel. |
    | --- | --- |
    | -EALREADY | The observer is already present in the channel's runtime observers list. |
    | -ENOMEM | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |
    | -EINVAL | Some parameter is invalid. |

## [◆ ](#ga00bfb7db54594029f4d288bcf5b56b3a)zbus\_chan\_claim()

| int zbus\_chan\_claim | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Claim a channel.

This routine claims a channel. During the claiming period the channel is blocked for publishing, reading, notifying or claiming again. Finishing is the only available action.

Warning
:   After calling this routine, the channel cannot be used by other thread until the zbus\_chan\_finish routine is performed.
:   This routine should only be called once before a zbus\_chan\_finish.

Parameters
:   | [in] | chan | The channel's reference. |
    | --- | --- | --- |
    | [in] | timeout | Waiting period to claim the channel, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Channel claimed. |
    | --- | --- |
    | -EBUSY | The channel is busy. |
    | -EAGAIN | Waiting period timed out. |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#gafee07c355df9ac86b85e601196b56a10)zbus\_chan\_const\_msg()

| | const void \* zbus\_chan\_const\_msg | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get a constant reference for a channel message directly.

This routine returns a constant reference of a channel message. This should be used inside listeners to access the message directly. In this way zbus prevents the listener of changing the notifying channel's message during the notification process.

Warning
:   This function must only be used directly for already locked channels. This can be done inside a listener for the receiving channel or after claim a channel.

Parameters
:   | chan | The channel's constant reference. |
    | --- | --- |

Returns
:   A constant channel's message reference.

## [◆ ](#ga74747affb345e68ce1d564c349409e59)zbus\_chan\_finish()

| int zbus\_chan\_finish | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Finish a channel claim.

This routine finishes a channel claim. After calling this routine with success, the channel will be able to be used by other thread.

Warning
:   This routine must only be used after a zbus\_chan\_claim.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Return values
:   | 0 | Channel finished. |
    | --- | --- |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#gaaf8b34113b7b993438bd42db64812572)zbus\_chan\_msg()

| | void \* zbus\_chan\_msg | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the reference for a channel message directly.

This routine returns the reference of a channel message.

Warning
:   This function must only be used directly for already locked channels. This can be done inside a listener for the receiving channel or after claim a channel.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   Channel's message reference.

## [◆ ](#ga8895a18b282ca2fe7528b4e5cf48e025)zbus\_chan\_msg\_size()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) zbus\_chan\_msg\_size | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the channel's message size.

This routine returns the channel's message size.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   Channel's message size.

## [◆ ](#ga05a220636fc6bb58b97805e558b76d73)zbus\_chan\_name()

| | const char \* zbus\_chan\_name | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the channel's name.

This routine returns the channel's name reference.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   Channel's name reference.

## [◆ ](#ga6ec2f463801499e23a011fa4e68aa3e7)zbus\_chan\_notify()

| int zbus\_chan\_notify | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Force a channel notification.

This routine forces the event dispatcher to notify the channel's observers even if the message has no changes. Note this function could be useful after claiming/finishing actions.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |
    | timeout | Waiting period to notify the channel, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Channel notified. |
    | --- | --- |
    | -EBUSY | The channel's semaphore returned without waiting. |
    | -EAGAIN | Timeout to take the channel's semaphore. |
    | -ENOMEM | There is not more buffer on the messgage buffers pool. |
    | -EFAULT | A parameter is incorrect, the notification could not be sent to one or more observer, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#gadfcaba65b397c1d8c31836ef3cf61244)zbus\_chan\_pub()

| int zbus\_chan\_pub | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | const void \* | *msg*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Publish to a channel.

This routine publishes a message to a channel.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |
    | msg | Reference to the message where the publish function copies the channel's message data from. |
    | timeout | Waiting period to publish the channel, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Channel published. |
    | --- | --- |
    | -ENOMSG | The message is invalid based on the validator function or some of the observers could not receive the notification. |
    | -EBUSY | The channel is busy. |
    | -EAGAIN | Waiting period timed out. |
    | -EFAULT | A parameter is incorrect, the notification could not be sent to one or more observer, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#ga09503e2b9c01f79136f9eb600ddb3f31)zbus\_chan\_pub\_stats\_avg\_period()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zbus\_chan\_pub\_stats\_avg\_period | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the average period between publishes to a channel.

Note
:   Will return 0 if channel has not yet been published to.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   Average duration in milliseconds between publishes.

## [◆ ](#ga5648bf527de4aff89648a34bf8a7539a)zbus\_chan\_pub\_stats\_count()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zbus\_chan\_pub\_stats\_count | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the number of times a channel has been published to.

Note
:   Will return 0 if channel has not yet been published to.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   The number of times a channel has been published to.

## [◆ ](#gac5dff9990d709d736b30f36d68c0297b)zbus\_chan\_pub\_stats\_last\_time()

| | [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) zbus\_chan\_pub\_stats\_last\_time | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the time a channel was last published to.

Note
:   Will return 0 if channel has not yet been published to.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   The kernel timestamp of the last publishing action.

## [◆ ](#gaef067fb1e8b834993662af84b916483a)zbus\_chan\_pub\_stats\_update()

| | void zbus\_chan\_pub\_stats\_update | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Update the publishing statistics for a channel.

This function updates the publishing statistics for the [zbus\_chan\_claim](#ga00bfb7db54594029f4d288bcf5b56b3a) -> [zbus\_chan\_finish](#ga74747affb345e68ce1d564c349409e59) workflow, which cannot automatically determine whether new data has been published or not.

Warning
:   This function must only be used directly for already locked channels.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

## [◆ ](#ga8209721e0a295c84d112ba1a7171100e)zbus\_chan\_read()

| int zbus\_chan\_read | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | void \* | *msg*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Read a channel.

This routine reads a message from a channel.

Parameters
:   | [in] | chan | The channel's reference. |
    | --- | --- | --- |
    | [out] | msg | Reference to the message where the read function copies the channel's message data to. |
    | [in] | timeout | Waiting period to read the channel, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Channel read. |
    | --- | --- |
    | -EBUSY | The channel is busy. |
    | -EAGAIN | Waiting period timed out. |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#gaee11d7472a3f87156b8ef1dcfbe897c4)zbus\_chan\_rm\_obs()

| int zbus\_chan\_rm\_obs | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | const struct [zbus\_observer](structzbus__observer.md) \* | *obs*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Remove an observer from a channel.

This routine removes an observer to the channel.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |
    | obs | The observer's reference to be removed. |
    | timeout | Waiting period to remove an observer, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Observer removed to the channel. |
    | --- | --- |
    | -EINVAL | Invalid data supplied. |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |
    | -ENODATA | no observer found in channel's runtime observer list. |
    | -ENOMEM | Returned without waiting. |

## [◆ ](#ga3f90d50f20e7779ef257676ac10da357)zbus\_chan\_set\_msg\_sub\_pool()

| | void zbus\_chan\_set\_msg\_sub\_pool | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, | | --- | --- | --- | --- | |  |  | struct [net\_buf\_pool](structnet__buf__pool.md) \* | *pool* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Set the channel's msg subscriber [net\_buf](structnet__buf.md "Network buffer representation.") pool.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |
    | pool | The reference to the [net\_buf](structnet__buf.md "Network buffer representation.") memory pool. |

## [◆ ](#gac0b0ed0356fca5a8b65a3332931a369a)zbus\_chan\_user\_data()

| | void \* zbus\_chan\_user\_data | ( | const struct [zbus\_channel](structzbus__channel.md) \* | *chan* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the channel's user data.

This routine returns the channel's user data.

Parameters
:   | chan | The channel's reference. |
    | --- | --- |

Returns
:   Channel's user data.

## [◆ ](#ga6dffd25f4eb368e773c2bd55f34a0e10)zbus\_iterate\_over\_channels()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) zbus\_iterate\_over\_channels | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *iterator\_func*)(const struct [zbus\_channel](structzbus__channel.md) \*chan) | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Iterate over channels.

Enables the developer to iterate over the channels giving to this function an iterator\_func which is called for each channel. If the iterator\_func returns false all the iteration stops.

Parameters
:   | [in] | iterator\_func | The function that will be execute on each iteration. |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Iterator executed for all channels. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Iterator could not be executed. Some iterate returned false. |

## [◆ ](#gab8df108b0238757ff631ec1e120fa2c3)zbus\_iterate\_over\_channels\_with\_user\_data()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) zbus\_iterate\_over\_channels\_with\_user\_data | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *iterator\_func*)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[zbus.h](zbus_8h.md)>`

Iterate over channels with user data.

Enables the developer to iterate over the channels giving to this function an iterator\_func which is called for each channel. If the iterator\_func returns false all the iteration stops.

Parameters
:   | [in] | iterator\_func | The function that will be execute on each iteration. |
    | --- | --- | --- |
    | [in] | user\_data | The user data that can be passed in the function. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Iterator executed for all channels. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Iterator could not be executed. Some iterate returned false. |

## [◆ ](#ga2fa50316993afc5807e9d707d664be14)zbus\_iterate\_over\_observers()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) zbus\_iterate\_over\_observers | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *iterator\_func*)(const struct [zbus\_observer](structzbus__observer.md) \*obs) | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Iterate over observers.

Enables the developer to iterate over the observers giving to this function an iterator\_func which is called for each observer. If the iterator\_func returns false all the iteration stops.

Parameters
:   | [in] | iterator\_func | The function that will be execute on each iteration. |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Iterator executed for all channels. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Iterator could not be executed. Some iterate returned false. |

## [◆ ](#ga2f4e39c500fed0a6bcfedb5dec3f797a)zbus\_iterate\_over\_observers\_with\_user\_data()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) zbus\_iterate\_over\_observers\_with\_user\_data | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | *iterator\_func*)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[zbus.h](zbus_8h.md)>`

Iterate over observers with user data.

Enables the developer to iterate over the observers giving to this function an iterator\_func which is called for each observer. If the iterator\_func returns false all the iteration stops.

Parameters
:   | [in] | iterator\_func | The function that will be execute on each iteration. |
    | --- | --- | --- |
    | [in] | user\_data | The user data that can be passed in the function. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Iterator executed for all channels. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Iterator could not be executed. Some iterate returned false. |

## [◆ ](#gabecf160e4d468d0275ad79e22fd0fb5b)zbus\_obs\_attach\_to\_thread()

| int zbus\_obs\_attach\_to\_thread | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Set the observer thread priority by attaching it to a thread.

Parameters
:   | [in] | obs | The observer's reference. |
    | --- | --- | --- |

Return values
:   | 0 | Observer detached from the thread. |
    | --- | --- |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#ga493c125c31e44d5a222f0e9c6d01249e)zbus\_obs\_detach\_from\_thread()

| int zbus\_obs\_detach\_from\_thread | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Clear the observer thread priority by detaching it from a thread.

Parameters
:   | [in] | obs | The observer's reference. |
    | --- | --- | --- |

Return values
:   | 0 | Observer detached from the thread. |
    | --- | --- |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#ga41ae9799a52c2a7954500b0a3c78d19f)zbus\_obs\_is\_chan\_notification\_masked()

| int zbus\_obs\_is\_chan\_notification\_masked | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs*, |
| --- | --- | --- | --- |
|  |  | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *masked* ) |

`#include <[zbus.h](zbus_8h.md)>`

Get the notifications masking state from a channel to an observer.

Parameters
:   |  | obs | The observer's reference to be added. |
    | --- | --- | --- |
    |  | chan | The channel's reference. |
    | [out] | masked | The mask state. When the mask is true, the observer will not receive notifications from the channel. |

Return values
:   | 0 | Retrieved the masked state. |
    | --- | --- |
    | -ESRCH | No observation found for the related pair chan/obs. |
    | -EINVAL | Some parameter is invalid. |

## [◆ ](#ga315fd4e0b6a3c01a23307dd890e69894)zbus\_obs\_is\_enabled()

| | int zbus\_obs\_is\_enabled | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the observer state.

This routine retrieves the observer state.

Parameters
:   | [in] | obs | The observer's reference. |
    | --- | --- | --- |
    | [out] | enable | The boolean output's reference. |

Returns
:   Observer state.

## [◆ ](#ga5bb33ec5b914e6cbc87fa70bf763ad15)zbus\_obs\_name()

| | const char \* zbus\_obs\_name | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zbus.h](zbus_8h.md)>`

Get the observer's name.

This routine returns the observer's name reference.

Parameters
:   | obs | The observer's reference. |
    | --- | --- |

Returns
:   The observer's name reference.

## [◆ ](#ga9513264f912f54b60c4341642f578e5a)zbus\_obs\_set\_chan\_notification\_mask()

| int zbus\_obs\_set\_chan\_notification\_mask | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs*, |
| --- | --- | --- | --- |
|  |  | const struct [zbus\_channel](structzbus__channel.md) \* | *chan*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *masked* ) |

`#include <[zbus.h](zbus_8h.md)>`

Mask notifications from a channel to an observer.

The observer can mask notifications from a specific observing channel by calling this function.

Parameters
:   | obs | The observer's reference to be added. |
    | --- | --- |
    | chan | The channel's reference. |
    | masked | The mask state. When the mask is true, the observer will not receive notifications from the channel. |

Return values
:   | 0 | Channel notifications masked to the observer. |
    | --- | --- |
    | -ESRCH | No observation found for the related pair chan/obs. |
    | -EINVAL | Some parameter is invalid. |

## [◆ ](#ga96767314e040e42609867a36684a6349)zbus\_obs\_set\_enable()

| int zbus\_obs\_set\_enable | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *obs*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enabled* ) |

`#include <[zbus.h](zbus_8h.md)>`

Change the observer state.

This routine changes the observer state. A channel when disabled will not receive notifications from the event dispatcher.

Parameters
:   | [in] | obs | The observer's reference. |
    | --- | --- | --- |
    | [in] | enabled | State to be. When false the observer stops to receive notifications. |

Return values
:   | 0 | Observer set enable. |
    | --- | --- |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#ga84a65e276a01ef97eeb5c81b880da72b)zbus\_sub\_wait()

| int zbus\_sub\_wait | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *sub*, |
| --- | --- | --- | --- |
|  |  | const struct [zbus\_channel](structzbus__channel.md) \*\* | *chan*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Wait for a channel notification.

This routine makes the subscriber to wait a notification. The notification comes as a channel reference.

Parameters
:   | [in] | sub | The subscriber's reference. |
    | --- | --- | --- |
    | [out] | chan | The notification channel's reference. |
    | [in] | timeout | Waiting period for a notification arrival, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Notification received. |
    | --- | --- |
    | -ENOMSG | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |
    | -EINVAL | The observer is not a subscriber. |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

## [◆ ](#gaeffce45446509e488192a4e6442453fb)zbus\_sub\_wait\_msg()

| int zbus\_sub\_wait\_msg | ( | const struct [zbus\_observer](structzbus__observer.md) \* | *sub*, |
| --- | --- | --- | --- |
|  |  | const struct [zbus\_channel](structzbus__channel.md) \*\* | *chan*, |
|  |  | void \* | *msg*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[zbus.h](zbus_8h.md)>`

Wait for a channel message.

This routine makes the subscriber wait for the new message in case of channel publication.

Parameters
:   | [in] | sub | The subscriber's reference. |
    | --- | --- | --- |
    | [out] | chan | The notification channel's reference. |
    | [out] | msg | A reference to a copy of the published message. |
    | [in] | timeout | Waiting period for a notification arrival, or one of the special values, K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | Message received. |
    | --- | --- |
    | -EINVAL | The observer is not a subscriber. |
    | -ENOMSG | Could not retrieve the [net\_buf](structnet__buf.md "Network buffer representation.") from the subscriber FIFO. |
    | -EILSEQ | Received an invalid channel reference. |
    | -EFAULT | A parameter is incorrect, or the function context is invalid (inside an ISR). The function only returns this value when the  ``` CONFIG_ZBUS_ASSERT_MOCK ```  is enabled. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
