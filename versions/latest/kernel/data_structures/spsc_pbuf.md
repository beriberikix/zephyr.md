---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/data_structures/spsc_pbuf.html
original_path: kernel/data_structures/spsc_pbuf.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Single Producer Single Consumer Packet Buffer

A *Single Producer Single Consumer Packet Buffer (SPSC\_PBUF)* is a circular
buffer, whose contents are stored in first-in-first-out order. Variable size
packets are stored in the buffer. Packet buffer works under assumption that there
is a single context that produces packets and a single context that consumes the
data.

Implementation is focused on performance and memory footprint.

Packets are added to the buffer using `spsc_pbuf_write()` which copies a
data into the buffer. If the buffer is full error is returned.

Packets are copied out of the buffer using `spsc_pbuf_read()`.
