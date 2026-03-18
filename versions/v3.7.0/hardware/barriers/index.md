---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/barriers/index.html
original_path: hardware/barriers/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Barriers API

*group* Barrier Services APIs
:   **Since**
    :   3.4

    **Version**
    :   0.1.0

    Functions

    ALWAYS\_INLINE static void barrier\_dmem\_fence\_full(void)
    :   Full/sequentially-consistent data memory barrier.

        This routine acts as a synchronization fence between threads and prevents re-ordering of data accesses instructions across the barrier instruction.

    ALWAYS\_INLINE static void barrier\_dsync\_fence\_full(void)
    :   Full/sequentially-consistent data synchronization barrier.

        This routine acts as a synchronization fence between threads and prevents re-ordering of data accesses instructions across the barrier instruction like [barrier\_dmem\_fence\_full()](#group__barrier__apis_1gab0dd6769236babde7cf48c32007edf31), but has the additional effect of blocking execution of any further instructions, not just loads or stores, or both, until synchronization is complete.

        Note

        When not supported by hardware or architecture, this instruction falls back to a full/sequentially-consistent data memory barrier.

    ALWAYS\_INLINE static void barrier\_isync\_fence\_full(void)
    :   Full/sequentially-consistent instruction synchronization barrier.

        This routine is used to guarantee that any subsequent instructions are fetched and to ensure any previously executed context-changing operations, such as writes to system control registers, have completed by the time the routine completes. In hardware terms, this might mean that the instruction pipeline is flushed, for example.

        Note

        When not supported by hardware or architecture, this instruction falls back to a compiler barrier.
