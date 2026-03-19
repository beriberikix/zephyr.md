---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/api/mesh/health_cli.html
original_path: connectivity/bluetooth/api/mesh/health_cli.html
---

# Health Client

The Health Client model interacts with a Health Server model to read out
diagnostics and control the node’s attention state.

All message passing functions in the Health Client API have `cli` as
their first parameter. This is a pointer to the client model instance to be
used in this function call. The second parameter is the `ctx` or message
context. Message context contains netkey index, appkey index and unicast
address that the target node uses.

The Health Client model is optional, and may be instantiated on any element.
However, if a Health Client model is instantiated on an element other than the
primary, an instance must also be present on the primary element.

See [Health faults](health_srv.md#bluetooth-mesh-health-faults) for a list of specification defined
fault values.

## API reference

[Health Client Model](../../../../doxygen/html/group__bt__mesh__health__cli.md)
