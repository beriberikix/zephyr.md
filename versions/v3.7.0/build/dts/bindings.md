---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/bindings.html
original_path: build/dts/bindings.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Devicetree bindings

A devicetree on its own is only half the story for describing hardware, as it
is a relatively unstructured format. *Devicetree bindings* provide the other
half.

A devicetree binding declares requirements on the contents of nodes, and
provides semantic information about the contents of valid nodes. Zephyr
devicetree bindings are YAML files in a custom format (Zephyr does not use the
dt-schema tools used by the Linux kernel).

These pages introduce bindings, describe what they do, note where they are
found, and explain their data format.

Note

See the [Bindings index](api/bindings.md#devicetree-binding-index) for reference information on
bindings built in to Zephyr.
