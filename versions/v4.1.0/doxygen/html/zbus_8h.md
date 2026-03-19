---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zbus_8h.html
original_path: doxygen/html/zbus_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zbus.h File Reference

`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](zbus_8h_source.md)

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
| #define | [ZBUS\_CHAN\_ADD\_OBS\_WITH\_MASK](group__zbus__apis.md#ga7f763caca474e6c910793d2c714f80b4)(\_chan, \_obs, \_masked, \_prio) |
|  | Add a static channel observation. |
| #define | [ZBUS\_CHAN\_ADD\_OBS](group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df)(\_chan, \_obs, \_prio) |
|  | Add a static channel observation. |
| #define | [ZBUS\_OBS\_DECLARE](group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924)(...) |
|  | This macro list the observers to be used in a file. |
| #define | [ZBUS\_CHAN\_DECLARE](group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f)(...) |
|  | This macro list the channels to be used in a file. |
| #define | [ZBUS\_OBSERVERS\_EMPTY](group__zbus__apis.md#ga763dad07a1ae9bb38f9c240e1920caef) |
|  | This macro indicates the channel has no observers. |
| #define | [ZBUS\_OBSERVERS](group__zbus__apis.md#gafed25f045c3b8d438daf4ebd5e517692)(...) |
|  | This macro indicates the channel has listed observers. |
| #define | [ZBUS\_CHAN\_ID\_INVALID](group__zbus__apis.md#ga1f1e0798856c54dd641c1a322789400b)   [UINT32\_MAX](stdint_8h.md#ab5eb23180f7cc12b7d6c04a8ec067fdd) |
|  | This macro indicates the channel does not have a unique ID. |
| #define | [ZBUS\_CHAN\_DEFINE](group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687)(\_name, \_type, \_validator, \_user\_data, \_observers, \_init\_val) |
|  | Zbus channel definition. |
| #define | [ZBUS\_CHAN\_DEFINE\_WITH\_ID](group__zbus__apis.md#ga7c49cba434b90d417859b37722843e5f)(\_name, \_id, \_type, \_validator, \_user\_data, \_observers, \_init\_val) |
|  | Zbus channel definition with numeric identifier. |
| #define | [ZBUS\_MSG\_INIT](group__zbus__apis.md#ga4bf8c445814c1fcee9b9819a36bc9bd6)(\_val, ...) |
|  | Initialize a message. |
| #define | [ZBUS\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](group__zbus__apis.md#gaf56f71babe2bb27258f025332b80c58f)(\_name, \_queue\_size, \_enable) |
|  | Define and initialize a subscriber. |
| #define | [ZBUS\_SUBSCRIBER\_DEFINE](group__zbus__apis.md#gac17a735cccecfc90f26127e48cf6279a)(\_name, \_queue\_size) |
|  | Define and initialize a subscriber. |
| #define | [ZBUS\_LISTENER\_DEFINE\_WITH\_ENABLE](group__zbus__apis.md#gace4ac9da0e1bab7ba72797783ded948f)(\_name, \_cb, \_enable) |
|  | Define and initialize a listener. |
| #define | [ZBUS\_LISTENER\_DEFINE](group__zbus__apis.md#gabfc7be8298e76fe2f7ae628be30b8390)(\_name, \_cb) |
|  | Define and initialize a listener. |
| #define | [ZBUS\_MSG\_SUBSCRIBER\_DEFINE\_WITH\_ENABLE](group__zbus__apis.md#ga6089c1ae0dad91306f79d48a63b31785)(\_name, \_enable) |
|  | Define and initialize a message subscriber. |
| #define | [ZBUS\_MSG\_SUBSCRIBER\_DEFINE](group__zbus__apis.md#ga07a0c2c428c9e4891e86a63a420b2268)(\_name) |
|  | Define and initialize an enabled message subscriber. |

| Enumerations | |
| --- | --- |
| enum | [zbus\_observer\_type](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) { [ZBUS\_OBSERVER\_LISTENER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa127f19c2121c9c512da9dbcbb301320c) , [ZBUS\_OBSERVER\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa22c784a85353545e8dca2ce7a0ec81b3) , [ZBUS\_OBSERVER\_MSG\_SUBSCRIBER\_TYPE](group__zbus__apis.md#gga88941281d7bdd24f3cfbb53e57711d8fa8151f9e58a5bd96449bd2f9f8695538c) } |
|  | Type used to represent an observer type. [More...](group__zbus__apis.md#ga88941281d7bdd24f3cfbb53e57711d8f) |

| Functions | |
| --- | --- |
| int | [zbus\_chan\_pub](group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244) (const struct [zbus\_channel](structzbus__channel.md) \*chan, const void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Publish to a channel. |
| int | [zbus\_chan\_read](group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e) (const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read a channel. |
| int | [zbus\_chan\_claim](group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a) (const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Claim a channel. |
| int | [zbus\_chan\_finish](group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Finish a channel claim. |
| int | [zbus\_chan\_notify](group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7) (const struct [zbus\_channel](structzbus__channel.md) \*chan, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Force a channel notification. |
| static const char \* | [zbus\_chan\_name](group__zbus__apis.md#ga05a220636fc6bb58b97805e558b76d73) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the channel's name. |
| const struct [zbus\_channel](structzbus__channel.md) \* | [zbus\_chan\_from\_id](group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_id) |
|  | Retrieve a zbus channel from its numeric identifier. |
| static void \* | [zbus\_chan\_msg](group__zbus__apis.md#gaaf8b34113b7b993438bd42db64812572) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the reference for a channel message directly. |
| static const void \* | [zbus\_chan\_const\_msg](group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get a constant reference for a channel message directly. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [zbus\_chan\_msg\_size](group__zbus__apis.md#ga8895a18b282ca2fe7528b4e5cf48e025) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the channel's message size. |
| static void \* | [zbus\_chan\_user\_data](group__zbus__apis.md#gac0b0ed0356fca5a8b65a3332931a369a) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the channel's user data. |
| static void | [zbus\_chan\_set\_msg\_sub\_pool](group__zbus__apis.md#ga3f90d50f20e7779ef257676ac10da357) (const struct [zbus\_channel](structzbus__channel.md) \*chan, struct [net\_buf\_pool](structnet__buf__pool.md) \*pool) |
|  | Set the channel's msg subscriber [net\_buf](structnet__buf.md "Network buffer representation.") pool. |
| static void | [zbus\_chan\_pub\_stats\_update](group__zbus__apis.md#gaef067fb1e8b834993662af84b916483a) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Update the publishing statistics for a channel. |
| static [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [zbus\_chan\_pub\_stats\_last\_time](group__zbus__apis.md#gac5dff9990d709d736b30f36d68c0297b) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the time a channel was last published to. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [zbus\_chan\_pub\_stats\_count](group__zbus__apis.md#ga5648bf527de4aff89648a34bf8a7539a) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the number of times a channel has been published to. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [zbus\_chan\_pub\_stats\_avg\_period](group__zbus__apis.md#ga09503e2b9c01f79136f9eb600ddb3f31) (const struct [zbus\_channel](structzbus__channel.md) \*chan) |
|  | Get the average period between publishes to a channel. |
| int | [zbus\_chan\_add\_obs](group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6) (const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Add an observer to a channel. |
| int | [zbus\_chan\_rm\_obs](group__zbus__apis.md#gaee11d7472a3f87156b8ef1dcfbe897c4) (const struct [zbus\_channel](structzbus__channel.md) \*chan, const struct [zbus\_observer](structzbus__observer.md) \*obs, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Remove an observer from a channel. |
| int | [zbus\_obs\_set\_enable](group__zbus__apis.md#ga96767314e040e42609867a36684a6349) (const struct [zbus\_observer](structzbus__observer.md) \*obs, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Change the observer state. |
| static int | [zbus\_obs\_is\_enabled](group__zbus__apis.md#ga315fd4e0b6a3c01a23307dd890e69894) (const struct [zbus\_observer](structzbus__observer.md) \*obs, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*enable) |
|  | Get the observer state. |
| int | [zbus\_obs\_set\_chan\_notification\_mask](group__zbus__apis.md#ga9513264f912f54b60c4341642f578e5a) (const struct [zbus\_observer](structzbus__observer.md) \*obs, const struct [zbus\_channel](structzbus__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) masked) |
|  | Mask notifications from a channel to an observer. |
| int | [zbus\_obs\_is\_chan\_notification\_masked](group__zbus__apis.md#ga41ae9799a52c2a7954500b0a3c78d19f) (const struct [zbus\_observer](structzbus__observer.md) \*obs, const struct [zbus\_channel](structzbus__channel.md) \*chan, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*masked) |
|  | Get the notifications masking state from a channel to an observer. |
| static const char \* | [zbus\_obs\_name](group__zbus__apis.md#ga5bb33ec5b914e6cbc87fa70bf763ad15) (const struct [zbus\_observer](structzbus__observer.md) \*obs) |
|  | Get the observer's name. |
| int | [zbus\_obs\_attach\_to\_thread](group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b) (const struct [zbus\_observer](structzbus__observer.md) \*obs) |
|  | Set the observer thread priority by attaching it to a thread. |
| int | [zbus\_obs\_detach\_from\_thread](group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e) (const struct [zbus\_observer](structzbus__observer.md) \*obs) |
|  | Clear the observer thread priority by detaching it from a thread. |
| int | [zbus\_sub\_wait](group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b) (const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for a channel notification. |
| int | [zbus\_sub\_wait\_msg](group__zbus__apis.md#gaeffce45446509e488192a4e6442453fb) (const struct [zbus\_observer](structzbus__observer.md) \*sub, const struct [zbus\_channel](structzbus__channel.md) \*\*chan, void \*msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for a channel message. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_channels](group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan)) |
|  | Iterate over channels. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_channels\_with\_user\_data](group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_channel](structzbus__channel.md) \*chan, void \*user\_data), void \*user\_data) |
|  | Iterate over channels with user data. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_observers](group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs)) |
|  | Iterate over observers. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [zbus\_iterate\_over\_observers\_with\_user\_data](group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\*iterator\_func)(const struct [zbus\_observer](structzbus__observer.md) \*obs, void \*user\_data), void \*user\_data) |
|  | Iterate over observers with user data. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [zbus](dir_4ac3b76b03f02d08133e5af61546c3d3.md)
- [zbus.h](zbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
