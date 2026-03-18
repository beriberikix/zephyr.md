---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/net_pkt.html
original_path: connectivity/networking/api/net_pkt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Packet Management

## [Overview](#id1)

Network packets are the main data the networking stack manipulates.
Such data is represented through the net\_pkt structure which provides
a means to hold the packet, write and read it, as well as necessary
metadata for the core to hold important information. Such an object is
called net\_pkt in this document.

The data structure and the whole API around it are defined in
[include/zephyr/net/net\_pkt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/net_pkt.h).

### [Architectural notes](#id2)

There are two network packets flows within the stack, **TX** for the
transmission path, and **RX** for the reception one. In both paths,
each net\_pkt is written and read from the beginning to the end, or
more specifically from the headers to the payload.

## [Memory management](#id3)

### [Allocation](#id4)

All net\_pkt objects come from a pre-defined pool of struct net\_pkt.
Such pool is defined via

```c
NET_PKT_SLAB_DEFINE(name, count)
```

Note, however, one will rarely have to use it, as the core provides
already two pools, one for the TX path and one for the RX path.

Allocating a raw net\_pkt can be done through:

```c
pkt = net_pkt_alloc(timeout);
```

However, by its nature, a raw net\_pkt is useless without a buffer and
needs various metadata information to become relevant as well. It
requires at least to get the network interface it is meant to be sent
through or through which it was received. As this is a very common
operation, a helper exist:

```c
pkt = net_pkt_alloc_on_iface(iface, timeout);
```

A more complete allocator exists, where both the net\_pkt and its buffer
can be allocated at once:

```c
pkt = net_pkt_alloc_with_buffer(iface, size, family, proto, timeout);
```

See below how the buffer is allocated.

### [Buffer allocation](#id5)

The net\_pkt object does not define its own buffer, but instead uses an
existing object for this: [`net_buf`](net_buf.md#c.net_buf "net_buf"). (See
[Network Buffer](net_buf.md#net-buf-interface) for more information). However, it mostly
hides the usage of such a buffer because net\_pkt brings network
awareness to buffer allocation and, as we will see later, its
operation too.

To allocate a buffer, a net\_pkt needs to have at least its network
interface set. This works if the family of the packet is unknown at
the time of buffer allocation. Then one could do:

```c
net_pkt_alloc_buffer(pkt, size, proto, timeout);
```

Where proto could be 0 if unknown (there is no IPPROTO\_UNSPEC).

As seen previously, the net\_pkt and its buffer can be allocated at
once via [`net_pkt_alloc_with_buffer()`](#c.net_pkt_alloc_with_buffer). It is actually the most
widely used allocator.

The network interface, the family, and the protocol of the packet are
used by the buffer allocation to determine if the requested size can
be allocated. Indeed, the allocator will use the network interface to
know the MTU and then the family and protocol for the headers space
(if only these 2 are specified). If the whole fits within the MTU,
the allocated space will be of the requested size plus, eventually,
the headers space. If there is insufficient MTU space, the requested
size will be shrunk so the possible headers space and new size will
fit within the MTU.

For instance, on an Ethernet network interface, with an MTU of 1500
bytes:

```c
pkt = net_pkt_alloc_with_buffer(iface, 800, AF_INET4, IPPROTO_UDP, K_FOREVER);
```

will successfully allocate 800 + 20 + 8 bytes of buffer for the new
net\_pkt where:

```c
pkt = net_pkt_alloc_with_buffer(iface, 1600, AF_INET4, IPPROTO_UDP, K_FOREVER);
```

will successfully allocate 1500 bytes, and where 20 + 8 bytes (IPv4 +
UDP headers) will not be used for the payload.

On the receiving side, when the family and protocol are not known:

```c
pkt = net_pkt_rx_alloc_with_buffer(iface, 800, AF_UNSPEC, 0, K_FOREVER);
```

will allocate 800 bytes and no extra header space.
But a:

```c
pkt = net_pkt_rx_alloc_with_buffer(iface, 1600, AF_UNSPEC, 0, K_FOREVER);
```

will allocate 1514 bytes, the MTU + Ethernet header space.

One can increase the amount of buffer space allocated by calling
[`net_pkt_alloc_buffer()`](#c.net_pkt_alloc_buffer), as it will take into account the
existing buffer. It will also account for the header space if
net\_pkt’s family is a valid one, as well as the proto parameter. In
that case, the newly allocated buffer space will be appended to the
existing one, and not inserted in the front. Note however such a use
case is rather limited. Usually, one should know from the start how
much size should be requested.

### [Deallocation](#id6)

Each net\_pkt is reference counted. At allocation, the reference is set
to 1. The reference count can be incremented with
[`net_pkt_ref()`](#c.net_pkt_ref) or decremented with
[`net_pkt_unref()`](#c.net_pkt_unref). When the count drops to zero the buffer is
also un-referenced and net\_pkt is automatically placed back into the
free net\_pkt\_slabs

If net\_pkt’s buffer is needed even after net\_pkt deallocation, one
will need to reference once more all the chain of net\_buf before
calling last net\_pkt\_unref. See [Network Buffer](net_buf.md#net-buf-interface) for more
information.

## [Operations](#id7)

There are two ways to access the net\_pkt buffer, explained in the
following sections: basic read/write access and data access, the
latter being the preferred way.

### [Read and Write access](#id8)

As said earlier, though net\_pkt uses net\_buf for its buffer, it
provides its own API to access it. Indeed, a network packet might be
scattered over a chain of net\_buf objects, the functions provided by
net\_buf are then limited for such case. Instead, net\_pkt provides
functions which hide all the complexity of potential non-contiguous
access.

Data movement into the buffer is made through a cursor maintained
within each net\_pkt. All read/write operations affect this
cursor. Note as well that read or write functions are strict on their
length parameters: if it cannot r/w the given length it will
fail. Length is not interpreted as an upper limit, it is instead the
exact amount of data that must be read or written.

As there are two paths, TX and RX, there are two access modes: write
and overwrite. This might sound a bit unusual, but is in fact simple
and provides flexibility.

In write mode, whatever is written in the buffer affects the length of
actual data present in the buffer. Buffer length should not be
confused with the buffer size which is a limit any mode cannot pass.
In overwrite mode then, whatever is written must happen on valid data,
and will not affect the buffer length. By default, a newly allocated
net\_pkt is on write mode, and its cursor points to the beginning of
its buffer.

Let’s see now, step by step, the functions and how they behave
depending on the mode.

When freshly allocated with a buffer of 500 bytes, a net\_pkt has 0
length, which means no valid data is in its buffer. One could verify
this by:

```c
len = net_pkt_get_len(pkt);
```

Now, let’s write 8 bytes:

```c
net_pkt_write(pkt, data, 8);
```

The buffer length is now 8 bytes.
There are various helpers to write a byte, or big endian uint16\_t, uint32\_t.

```c
net_pkt_write_u8(pkt, &foo);
net_pkt_write_be16(pkt, &ba);
net_pkt_write_be32(pkt, &bar);
```

Logically, net\_pkt’s length is now 15. But if we try to read at this
point, it will fail because there is nothing to read at the cursor
where we are at in the net\_pkt. It is possible, while in write mode,
to read what has been already written by resetting the cursor of the
net\_pkt. For instance:

```c
net_pkt_cursor_init(pkt);
net_pkt_read(pkt, data, 15);
```

This will reset the cursor of the pkt to the beginning of the buffer
and then let you read the actual 15 bytes present. The cursor is then
again pointing at the end of the buffer.

To set a large area with the same byte, a memset function is provided:

```c
net_pkt_memset(pkt, 0, 5);
```

Our net\_pkt has now a length of 20 bytes.

Switching between modes can be achieved via
`net_pkt_set_overwrite()` function. It is possible to switch
mode back and forth at any time. The net\_pkt will be set to overwrite
and its cursor reset:

```c
net_pkt_set_overwrite(pkt, true);
net_pkt_cursor_init(pkt);
```

Now the same operators can be used, but it will be limited to the
existing data in the buffer, i.e. 20 bytes.

If it is necessary to know how much space is available in the net\_pkt
call:

```c
net_pkt_available_buffer(pkt);
```

Or, if headers space needs to be accounted for, call:

```c
net_pkt_available_payload_buffer(pkt, proto);
```

If you want to place the cursor at a known position use the function
[`net_pkt_skip()`](#c.net_pkt_skip). For example, to go after the IP header, use:

```c
net_pkt_cursor_init(pkt);
net_pkt_skip(pkt, net_pkt_ip_header_len(pkt));
```

### [Data access](#id9)

Though the API shown previously is rather simple, it involves always
copying things to and from the net\_pkt buffer. In many occasions, it
is more relevant to access the information stored in the buffer
contiguously, especially with network packets which embed headers.

These headers are, most of the time, a known fixed set of bytes. It is
then more natural to have a structure representing a certain type of
header. In addition to this, if it is known the header size appears
in a contiguous area of the buffer, it will be way more efficient to
cast the actual position in the buffer to the type of header. Either
for reading or writing the fields of such header, accessing it
directly will save memory.

Net pkt comes with a dedicated API for this, built on top of the
previously described API. It is able to handle both contiguous and
non-contiguous access transparently.

There are two macros used to define a data access descriptor:
[`NET_PKT_DATA_ACCESS_DEFINE`](#c.NET_PKT_DATA_ACCESS_DEFINE) when it is not possible to
tell if the data will be in a contiguous area, and
[`NET_PKT_DATA_ACCESS_CONTIGUOUS_DEFINE`](#c.NET_PKT_DATA_ACCESS_CONTIGUOUS_DEFINE) when
it is guaranteed the data is in a contiguous area.

Let’s take the example of IP and UDP. Both IPv4 and IPv6 headers are
always found at the beginning of the packet and are small enough to
fit in a net\_buf of 128 bytes (for instance, though 64 bytes could be
chosen).

```c
NET_PKT_DATA_ACCESS_CONTIGUOUS_DEFINE(ipv4_access, struct net_ipv4_hdr);
struct net_ipv4_hdr *ipv4_hdr;

ipv4_hdr = (struct net_ipv4_hdr *)net_pkt_get_data(pkt, &ipv4_access);
```

It would be the same for struct net\_ipv4\_hdr. For a UDP header it
is likely not to be in a contiguous area in IPv6
for instance so:

```c
NET_PKT_DATA_ACCESS_DEFINE(udp_access, struct net_udp_hdr);
struct net_udp_hdr *udp_hdr;

udp_hdr = (struct net_udp_hdr *)net_pkt_get_data(pkt, &udp_access);
```

At this point, the cursor of the net\_pkt points at the beginning of
the requested data. On the RX path, these headers will be read but not
modified so to proceed further the cursor needs to advance past the
data. There is a function dedicated for this:

```c
net_pkt_acknowledge_data(pkt, &ipv4_access);
```

On the TX path, however, the header fields have been modified. In such
a case:

```c
net_pkt_set_data(pkt, &ipv4_access);
```

If the data are in a contiguous area, it will advance the cursor
relevantly. If not, it will write the data and the cursor will be
updated. Note that [`net_pkt_set_data()`](#c.net_pkt_set_data) could be used in the RX
path as well, but it is slightly faster to use
[`net_pkt_acknowledge_data()`](#c.net_pkt_acknowledge_data) as this one does not care about
contiguity at all, it just advances the cursor via
[`net_pkt_skip()`](#c.net_pkt_skip) directly.

## [API Reference](#id10)

Related code samples

[Dumb HTTP server](../../../samples/net/sockets/dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.")
:   Implement a simple, portable, HTTP server using BSD sockets.

[Dumb HTTP server (multi-threaded)](../../../samples/net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")
:   Implement a simple HTTP server supporting simultaneous connections using BSD sockets.

*group* net\_pkt
:   Network packet management library.

    Defines

    NET\_PKT\_SLAB\_DEFINE(name, count)
    :   Create a [net\_pkt](#structnet__pkt) slab.

        A [net\_pkt](#structnet__pkt) slab is used to store meta-information about network packets. It must be coupled with a data fragment pool ([NET\_PKT\_DATA\_POOL\_DEFINE](#group__net__pkt_1ga94ab6300b59d739c4e3c5604d3fbe8a5)) used to store the actual packet data. The macro can be used by an application to define additional custom per-context TX packet slabs (see net\_context\_setup\_pools()).

        Parameters:
        :   - **name** – Name of the slab.
            - **count** – Number of [net\_pkt](#structnet__pkt) in this slab.

    NET\_PKT\_TX\_SLAB\_DEFINE(name, count)

    NET\_PKT\_DATA\_POOL\_DEFINE(name, count)
    :   Create a data fragment [net\_buf](net_buf.md#structnet__buf) pool.

        A [net\_buf](net_buf.md#structnet__buf) pool is used to store actual data for network packets. It must be coupled with a [net\_pkt](#structnet__pkt) slab ([NET\_PKT\_SLAB\_DEFINE](#group__net__pkt_1gafc7e98d5b64d816faabcbaa2ec22a2bb)) used to store the packet meta-information. The macro can be used by an application to define additional custom per-context TX packet pools (see net\_context\_setup\_pools()).

        Parameters:
        :   - **name** – Name of the pool.
            - **count** – Number of [net\_buf](net_buf.md#structnet__buf) in this pool.

    net\_pkt\_print\_frags(pkt)
    :   Print fragment list and the fragment sizes.

        Only available if debugging is activated.

        Parameters:
        :   - **pkt** – Network pkt.

    NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type)

    NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type)

    Functions

    struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*net\_pkt\_get\_reserve\_rx\_data(size\_t min\_len, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Get RX DATA buffer from pool.

        Normally you should use [net\_pkt\_get\_frag()](#group__net__pkt_1gafa7d666bddb182149d5f540880c46b4e) instead.

        Normally this version is not useful for applications but is mainly used by network fragmentation code.

        Parameters:
        :   - **min\_len** – Minimum length of the requested fragment.
            - **timeout** – Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait up to the specified time.

        Returns:
        :   Network buffer if successful, NULL otherwise.

    struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*net\_pkt\_get\_reserve\_tx\_data(size\_t min\_len, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Get TX DATA buffer from pool.

        Normally you should use [net\_pkt\_get\_frag()](#group__net__pkt_1gafa7d666bddb182149d5f540880c46b4e) instead.

        Normally this version is not useful for applications but is mainly used by network fragmentation code.

        Parameters:
        :   - **min\_len** – Minimum length of the requested fragment.
            - **timeout** – Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait up to the specified time.

        Returns:
        :   Network buffer if successful, NULL otherwise.

    struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*net\_pkt\_get\_frag(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t min\_len, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Get a data fragment that might be from user specific buffer pool or from global DATA pool.

        Parameters:
        :   - **pkt** – Network packet.
            - **min\_len** – Minimum length of the requested fragment.
            - **timeout** – Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait up to the specified time.

        Returns:
        :   Network buffer if successful, NULL otherwise.

    void net\_pkt\_unref(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Place packet back into the available packets slab.

        Releases the packet to other use. This needs to be called by application after it has finished with the packet.

        Parameters:
        :   - **pkt** – Network packet to release.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_ref(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Increase the packet ref count.

        Mark the packet to be used still.

        Parameters:
        :   - **pkt** – Network packet to ref.

        Returns:
        :   Network packet if successful, NULL otherwise.

    struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*net\_pkt\_frag\_ref(struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*frag)
    :   Increase the packet fragment ref count.

        Mark the fragment to be used still.

        Parameters:
        :   - **frag** – Network fragment to ref.

        Returns:
        :   a pointer on the referenced Network fragment.

    void net\_pkt\_frag\_unref(struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*frag)
    :   Decrease the packet fragment ref count.

        Parameters:
        :   - **frag** – Network fragment to unref.

    struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*net\_pkt\_frag\_del(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*parent, struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*frag)
    :   Delete existing fragment from a packet.

        Parameters:
        :   - **pkt** – Network packet from which frag belongs to.
            - **parent** – parent fragment of frag, or NULL if none.
            - **frag** – Fragment to delete.

        Returns:
        :   Pointer to the following fragment, or NULL if it had no further fragments.

    void net\_pkt\_frag\_add(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*frag)
    :   Add a fragment to a packet at the end of its fragment list.

        Parameters:
        :   - **pkt** – pkt Network packet where to add the fragment
            - **frag** – Fragment to add

    void net\_pkt\_frag\_insert(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*frag)
    :   Insert a fragment to a packet at the beginning of its fragment list.

        Parameters:
        :   - **pkt** – pkt Network packet where to insert the fragment
            - **frag** – Fragment to insert

    void net\_pkt\_compact(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Compact the fragment list of a packet.

        After this there is no more any free space in individual fragments.

        Parameters:
        :   - **pkt** – Network packet.

    void net\_pkt\_get\_info(struct k\_mem\_slab \*\*rx, struct k\_mem\_slab \*\*tx, struct [net\_buf\_pool](net_buf.md#c.net_buf_pool "net_buf_pool") \*\*rx\_data, struct [net\_buf\_pool](net_buf.md#c.net_buf_pool "net_buf_pool") \*\*tx\_data)
    :   Get information about predefined RX, TX and DATA pools.

        Parameters:
        :   - **rx** – Pointer to RX pool is returned.
            - **tx** – Pointer to TX pool is returned.
            - **rx\_data** – Pointer to RX DATA pool is returned.
            - **tx\_data** – Pointer to TX DATA pool is returned.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_alloc([k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate an initialized [net\_pkt](#structnet__pkt).

        for the time being, 2 pools are used. One for TX and one for RX. This allocator has to be used for TX.

        Parameters:
        :   - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   a pointer to a newly allocated [net\_pkt](#structnet__pkt) on success, NULL otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_alloc\_from\_slab(struct k\_mem\_slab \*slab, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate an initialized [net\_pkt](#structnet__pkt) from a specific slab.

        unlike [net\_pkt\_alloc()](#group__net__pkt_1ga90d97ba913a875b3ee438e0ea8a970fd) which uses core slabs, this one will use an external slab (see [NET\_PKT\_SLAB\_DEFINE()](#group__net__pkt_1gafc7e98d5b64d816faabcbaa2ec22a2bb)). Do *not* use it unless you know what you are doing. Basically, only net\_context should be using this, in order to allocate packet and then buffer on its local slab/pool (if any).

        Parameters:
        :   - **slab** – The slab to use for allocating the packet
            - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   a pointer to a newly allocated [net\_pkt](#structnet__pkt) on success, NULL otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_rx\_alloc([k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate an initialized [net\_pkt](#structnet__pkt) for RX.

        for the time being, 2 pools are used. One for TX and one for RX. This allocator has to be used for RX.

        Parameters:
        :   - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   a pointer to a newly allocated [net\_pkt](#structnet__pkt) on success, NULL otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_alloc\_on\_iface(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a network packet for a specific network interface.

        Parameters:
        :   - **iface** – The network interface the packet is supposed to go through.
            - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   a pointer to a newly allocated [net\_pkt](#structnet__pkt) on success, NULL otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_rx\_alloc\_on\_iface(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)

    int net\_pkt\_alloc\_buffer(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t size, enum [net\_ip\_protocol](ip_4_6.md#c.net_ip_protocol "net_ip_protocol") proto, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate buffer for a [net\_pkt](#structnet__pkt).

        : such allocator will take into account space necessary for headers, MTU, and existing buffer (if any). Beware that, due to all these criteria, the allocated size might be smaller/bigger than requested one.

        Parameters:
        :   - **pkt** – The network packet requiring buffer to be allocated.
            - **size** – The size of buffer being requested.
            - **proto** – The IP protocol type (can be 0 for none).
            - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   0 on success, negative errno code otherwise.

    int net\_pkt\_alloc\_buffer\_raw(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t size, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate buffer for a [net\_pkt](#structnet__pkt), of specified size, w/o any additional preconditions.

        : The actual buffer size may be larger than requested one if fixed size buffers are in use.

        Parameters:
        :   - **pkt** – The network packet requiring buffer to be allocated.
            - **size** – The size of buffer being requested.
            - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   0 on success, negative errno code otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_alloc\_with\_buffer(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, size\_t size, [sa\_family\_t](ip_4_6.md#c.sa_family_t "sa_family_t") family, enum [net\_ip\_protocol](ip_4_6.md#c.net_ip_protocol "net_ip_protocol") proto, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a network packet and buffer at once.

        Parameters:
        :   - **iface** – The network interface the packet is supposed to go through.
            - **size** – The size of buffer.
            - **family** – The family to which the packet belongs.
            - **proto** – The IP protocol type (can be 0 for none).
            - **timeout** – Maximum time to wait for an allocation.

        Returns:
        :   a pointer to a newly allocated [net\_pkt](#structnet__pkt) on success, NULL otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_rx\_alloc\_with\_buffer(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, size\_t size, [sa\_family\_t](ip_4_6.md#c.sa_family_t "sa_family_t") family, enum [net\_ip\_protocol](ip_4_6.md#c.net_ip_protocol "net_ip_protocol") proto, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)

    void net\_pkt\_append\_buffer(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*buffer)
    :   Append a buffer in packet.

        Parameters:
        :   - **pkt** – Network packet where to append the buffer
            - **buffer** – Buffer to append

    size\_t net\_pkt\_available\_buffer(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Get available buffer space from a pkt.

        Note

        Reserved bytes (headroom) in any of the fragments are not considered to be available.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) which buffer availability should be evaluated

        Returns:
        :   the amount of buffer available

    size\_t net\_pkt\_available\_payload\_buffer(struct [net\_pkt](#c.net_pkt) \*pkt, enum [net\_ip\_protocol](ip_4_6.md#c.net_ip_protocol "net_ip_protocol") proto)
    :   Get available buffer space for payload from a pkt.

        Unlike [net\_pkt\_available\_buffer()](#group__net__pkt_1gaeed119d192e3a14ea3eea6e623334519), this will take into account the headers space.

        Note

        Reserved bytes (headroom) in any of the fragments are not considered to be available.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) which payload buffer availability should be evaluated
            - **proto** – The IP protocol type (can be 0 for none).

        Returns:
        :   the amount of buffer available for payload

    void net\_pkt\_trim\_buffer(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Trim [net\_pkt](#structnet__pkt) buffer.

        This will basically check for unused buffers and deallocate them relevantly

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) which buffer will be trimmed

    int net\_pkt\_remove\_tail(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t length)
    :   Remove *length* bytes from tail of packet.

        This function does not take packet cursor into account. It is a helper to remove unneeded bytes from tail of packet (like appended CRC). It takes care of buffer deallocation if removed bytes span whole buffer(s).

        Parameters:
        :   - **pkt** – Network packet
            - **length** – Number of bytes to be removed

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If packet length is shorter than *length*.

    void net\_pkt\_cursor\_init(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Initialize [net\_pkt](#structnet__pkt) cursor.

        This will initialize the [net\_pkt](#structnet__pkt) cursor from its buffer.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) whose cursor is going to be initialized

    static inline void net\_pkt\_cursor\_backup(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_pkt\_cursor](#c.net_pkt_cursor) \*backup)
    :   Backup [net\_pkt](#structnet__pkt) cursor.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) whose cursor is going to be backed up
            - **backup** – The cursor where to backup [net\_pkt](#structnet__pkt) cursor

    static inline void net\_pkt\_cursor\_restore(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_pkt\_cursor](#c.net_pkt_cursor) \*backup)
    :   Restore [net\_pkt](#structnet__pkt) cursor from a backup.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) whose cursor is going to be restored
            - **backup** – The cursor from where to restore [net\_pkt](#structnet__pkt) cursor

    static inline void \*net\_pkt\_cursor\_get\_pos(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Returns current position of the cursor.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) whose cursor position is going to be returned

        Returns:
        :   cursor’s position

    int net\_pkt\_skip(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t length)
    :   Skip some data from a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized Cursor position will be updated after the operation. Depending on the value of pkt->overwrite bit, this function will affect the buffer length or not. If it’s true, it will advance the cursor to the requested length. If it’s false, it will do the same but if the cursor was already also at the end of existing data, it will increment the buffer length. So in this case, its behavior is just like net\_pkt\_write or net\_pkt\_memset, difference being that it will not affect the buffer content itself (which may be just garbage then).

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) whose cursor will be updated to skip given amount of data from the buffer.
            - **length** – Amount of data to skip in the buffer

        Returns:
        :   0 in success, negative errno code otherwise.

    int net\_pkt\_memset(struct [net\_pkt](#c.net_pkt) \*pkt, int byte, size\_t length)
    :   Memset some data in a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The [net\_pkt](#structnet__pkt) whose buffer to fill starting at the current cursor position.
            - **byte** – The byte to write in memory
            - **length** – Amount of data to memset with given byte

        Returns:
        :   0 in success, negative errno code otherwise.

    int net\_pkt\_copy(struct [net\_pkt](#c.net_pkt) \*pkt\_dst, struct [net\_pkt](#c.net_pkt) \*pkt\_src, size\_t length)
    :   Copy data from a packet into another one.

        Both [net\_pkt](#structnet__pkt) cursors should be properly initialized and, if needed, positioned using net\_pkt\_skip. The cursors will be updated after the operation.

        Parameters:
        :   - **pkt\_dst** – Destination network packet.
            - **pkt\_src** – Source network packet.
            - **length** – Length of data to be copied.

        Returns:
        :   0 on success, negative errno code otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_clone(struct [net\_pkt](#c.net_pkt) \*pkt, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Clone pkt and its buffer.

        The cloned packet will be allocated on the same pool as the original one.

        Parameters:
        :   - **pkt** – Original pkt to be cloned
            - **timeout** – Timeout to wait for free buffer

        Returns:
        :   NULL if error, cloned packet otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_rx\_clone(struct [net\_pkt](#c.net_pkt) \*pkt, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Clone pkt and its buffer.

        The cloned packet will be allocated on the RX packet poll.

        Parameters:
        :   - **pkt** – Original pkt to be cloned
            - **timeout** – Timeout to wait for free buffer

        Returns:
        :   NULL if error, cloned packet otherwise.

    struct [net\_pkt](#c.net_pkt) \*net\_pkt\_shallow\_clone(struct [net\_pkt](#c.net_pkt) \*pkt, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Clone pkt and increase the refcount of its buffer.

        Parameters:
        :   - **pkt** – Original pkt to be shallow cloned
            - **timeout** – Timeout to wait for free packet

        Returns:
        :   NULL if error, cloned packet otherwise.

    int net\_pkt\_read(struct [net\_pkt](#c.net_pkt) \*pkt, void \*data, size\_t length)
    :   Read some data from a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet from where to read some data
            - **data** – The destination buffer where to copy the data
            - **length** – The amount of data to copy

        Returns:
        :   0 on success, negative errno code otherwise.

    static inline int net\_pkt\_read\_u8(struct [net\_pkt](#c.net_pkt) \*pkt, uint8\_t \*data)

    int net\_pkt\_read\_be16(struct [net\_pkt](#c.net_pkt) \*pkt, uint16\_t \*data)
    :   Read uint16\_t big endian data from a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet from where to read
            - **data** – The destination uint16\_t where to copy the data

        Returns:
        :   0 on success, negative errno code otherwise.

    int net\_pkt\_read\_le16(struct [net\_pkt](#c.net_pkt) \*pkt, uint16\_t \*data)
    :   Read uint16\_t little endian data from a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet from where to read
            - **data** – The destination uint16\_t where to copy the data

        Returns:
        :   0 on success, negative errno code otherwise.

    int net\_pkt\_read\_be32(struct [net\_pkt](#c.net_pkt) \*pkt, uint32\_t \*data)
    :   Read uint32\_t big endian data from a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet from where to read
            - **data** – The destination uint32\_t where to copy the data

        Returns:
        :   0 on success, negative errno code otherwise.

    int net\_pkt\_write(struct [net\_pkt](#c.net_pkt) \*pkt, const void \*data, size\_t length)
    :   Write data into a [net\_pkt](#structnet__pkt).

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet where to write
            - **data** – Data to be written
            - **length** – Length of the data to be written

        Returns:
        :   0 on success, negative errno code otherwise.

    static inline int net\_pkt\_write\_u8(struct [net\_pkt](#c.net_pkt) \*pkt, uint8\_t data)

    static inline int net\_pkt\_write\_be16(struct [net\_pkt](#c.net_pkt) \*pkt, uint16\_t data)

    static inline int net\_pkt\_write\_be32(struct [net\_pkt](#c.net_pkt) \*pkt, uint32\_t data)

    static inline int net\_pkt\_write\_le32(struct [net\_pkt](#c.net_pkt) \*pkt, uint32\_t data)

    static inline int net\_pkt\_write\_le16(struct [net\_pkt](#c.net_pkt) \*pkt, uint16\_t data)

    size\_t net\_pkt\_remaining\_data(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Get the amount of data which can be read from current cursor position.

        Parameters:
        :   - **pkt** – Network packet

        Returns:
        :   Amount of data which can be read from current pkt cursor

    int net\_pkt\_update\_length(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t length)
    :   Update the overall length of a packet.

        Unlike [net\_pkt\_pull()](#group__net__pkt_1ga434c347a32600ee113c0e1cc13f70cd4) below, this does not take packet cursor into account. It’s mainly a helper dedicated for ipv4 and ipv6 input functions. It shrinks the overall length by given parameter.

        Parameters:
        :   - **pkt** – Network packet
            - **length** – The new length of the packet

        Returns:
        :   0 on success, negative errno code otherwise.

    int net\_pkt\_pull(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t length)
    :   Remove data from the packet at current location.

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, eventually, properly positioned using net\_pkt\_skip/read/write. Note that [net\_pkt](#structnet__pkt)’s cursor is reset by this function.

        Parameters:
        :   - **pkt** – Network packet
            - **length** – Number of bytes to be removed

        Returns:
        :   0 on success, negative errno code otherwise.

    uint16\_t net\_pkt\_get\_current\_offset(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Get the actual offset in the packet from its cursor.

        Parameters:
        :   - **pkt** – Network packet.

        Returns:
        :   a valid offset on success, 0 otherwise as there is nothing that can be done to evaluate the offset.

    bool net\_pkt\_is\_contiguous(struct [net\_pkt](#c.net_pkt) \*pkt, size\_t size)
    :   Check if a data size could fit contiguously.

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip.

        Parameters:
        :   - **pkt** – Network packet.
            - **size** – The size to check for contiguity

        Returns:
        :   true if that is the case, false otherwise.

    size\_t net\_pkt\_get\_contiguous\_len(struct [net\_pkt](#c.net_pkt) \*pkt)
    :   Get the contiguous buffer space.

        Parameters:
        :   - **pkt** – Network packet

        Returns:
        :   The available contiguous buffer space in bytes starting from the current cursor position. 0 in case of an error.

    void \*net\_pkt\_get\_data(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_pkt\_data\_access](#c.net_pkt_data_access) \*access)
    :   Get data from a network packet in a contiguous way.

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Unlike other functions, cursor position will not be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet from where to get the data.
            - **access** – A pointer to a valid [net\_pkt\_data\_access](#structnet__pkt__data__access) describing the data to get in a contiguous way.

        Returns:
        :   a pointer to the requested contiguous data, NULL otherwise.

    int net\_pkt\_set\_data(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_pkt\_data\_access](#c.net_pkt_data_access) \*access)
    :   Set contiguous data into a network packet.

        [net\_pkt](#structnet__pkt)’s cursor should be properly initialized and, if needed, positioned using net\_pkt\_skip. Cursor position will be updated after the operation.

        Parameters:
        :   - **pkt** – The network packet to where the data should be set.
            - **access** – A pointer to a valid [net\_pkt\_data\_access](#structnet__pkt__data__access) describing the data to set.

        Returns:
        :   0 on success, a negative errno otherwise.

    static inline int net\_pkt\_acknowledge\_data(struct [net\_pkt](#c.net_pkt) \*pkt, struct [net\_pkt\_data\_access](#c.net_pkt_data_access) \*access)
    :   Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrite mode.

    struct net\_pkt\_cursor
    :   *#include <net\_pkt.h>*

        Public Members

        struct [net\_buf](net_buf.md#c.net_buf "net_buf") \*buf
        :   Current [net\_buf](net_buf.md#structnet__buf) pointer by the cursor.

        uint8\_t \*pos
        :   Current position in the data buffer of the [net\_buf](net_buf.md#structnet__buf).

    struct net\_pkt
    :   *#include <net\_pkt.h>*

        Network packet.

        Note that if you add new fields into [net\_pkt](#structnet__pkt), remember to update [net\_pkt\_clone()](#group__net__pkt_1gaefefe50d0c68fb4997abc7b309740959) function.

        Public Members

        intptr\_t fifo
        :   The fifo is used by RX/TX threads and by socket layer.

            The [net\_pkt](#structnet__pkt) is queued via fifo to the processing thread.

        struct k\_mem\_slab \*slab
        :   Slab pointer from where it belongs to.

        union [net\_pkt](#c.net_pkt).[anonymous] [anonymous]
        :   buffer holding the packet

        struct [net\_pkt\_cursor](#c.net_pkt_cursor) cursor
        :   Internal buffer iterator used for reading/writing.

        struct net\_context \*context
        :   Network connection context.

        struct [net\_if](net_if.md#c.net_if "net_if") \*iface
        :   Network interface.

    struct net\_pkt\_data\_access
    :   *#include <net\_pkt.h>*
