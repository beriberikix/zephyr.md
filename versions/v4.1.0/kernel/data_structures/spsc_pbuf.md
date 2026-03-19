---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/data_structures/spsc_pbuf.html
original_path: kernel/data_structures/spsc_pbuf.html
---

# Single Producer Single Consumer Packet Buffer

A *Single Producer Single Consumer Packet Buffer (SPSC\_PBUF)* is a circular
buffer, whose contents are stored in first-in-first-out order. Variable size
packets are stored in the buffer. Packet buffer works under assumption that there
is a single context that produces packets and a single context that consumes the
data.

Implementation is focused on performance and memory footprint.

Packets are added to the buffer using [`spsc_pbuf_write()`](../../doxygen/html/group__spsc__buf.md#ga492c895f1723567445ce23c73ed3d0ef) which copies a
data into the buffer. If the buffer is full error is returned.

Packets are copied out of the buffer using [`spsc_pbuf_read()`](../../doxygen/html/group__spsc__buf.md#ga24d4cc2a41fd2c42c6085e106bf71c0c).
