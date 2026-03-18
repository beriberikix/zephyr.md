---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/data_structures/mpsc_lockfree.html
original_path: kernel/data_structures/mpsc_lockfree.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Multi Producer Single Consumer Lock Free Queue

A *Multi Producer Single Consumer Lock Free Queue (MPSC)* is an lockfree
intrusive queue based on atomic pointer swaps as described by Dmitry Vyukov
at [1024cores](https://www.1024cores.net/home/lock-free-algorithms/queues/intrusive-mpsc-node-based-queue).

## API Reference

*group* MPSC Lockfree Queue API
:   Multiple Producer Single Consumer (MPSC) Lockfree Queue API.

    Defines

    mpsc\_ptr\_get(ptr)

    mpsc\_ptr\_set(ptr, val)

    mpsc\_ptr\_set\_get(ptr, val)

    MPSC\_INIT(symbol)
    :   Static initializer for a mpsc queue.

        Since the queue is

        Parameters:
        :   - **symbol** – name of the queue

    Typedefs

    typedef atomic\_ptr\_t mpsc\_ptr\_t

    Functions

    static inline void mpsc\_init(struct [mpsc](#c.mpsc) \*q)
    :   Initialize queue.

        Parameters:
        :   - **q** – Queue to initialize or reset

    ALWAYS\_INLINE static void mpsc\_push(struct [mpsc](#c.mpsc) \*q, struct [mpsc\_node](#c.mpsc_node) \*n)
    :   Push a node.

        Parameters:
        :   - **q** – Queue to push the node to
            - **n** – Node to push into the queue

    static inline struct [mpsc\_node](#c.mpsc_node) \*mpsc\_pop(struct [mpsc](#c.mpsc) \*q)
    :   Pop a node off of the list.

        Return values:
        :   - **NULL** – When no node is available
            - **node** – When node is available

    struct mpsc\_node
    :   *#include <mpsc\_lockfree.h>*

        Queue member.

    struct mpsc
    :   *#include <mpsc\_lockfree.h>*

        MPSC Queue.
