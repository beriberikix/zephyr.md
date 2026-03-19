---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/services/data_passing/queues.html
original_path: kernel/services/data_passing/queues.html
---

# Queues

A Queue in Zephyr is a kernel object that implements a traditional queue, allowing
threads and ISRs to add and remove data items of any size. The queue is similar
to a FIFO and serves as the underlying implementation for both [k\_fifo](fifos.md#fifos-v2) and [k\_lifo](lifos.md#lifos-v2). For more information on usage see
[k\_fifo](fifos.md#fifos-v2).

## Configuration Options

Related configuration options:

- None

## API Reference

[Queue APIs](../../../doxygen/html/group__queue__apis.md)
