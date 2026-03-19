---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/debugging/cs_trace_defmt.html
original_path: services/debugging/cs_trace_defmt.html
---

# ARM Coresight Trace Deformatter

Formatter is a method of wrapping multiple trace streams (specified by 7 bit ID) into a
single output stream. Formatter is using 16 byte frames which wraps up to 15 bytes of
data. It is used, for example, by ETR (Embedded Trace Router) which is a circular RAM
buffer where data from various trace streams can be saved. Typically tracing data is
decoded offline by the host but deformatter can be used on-chip to decode the data during
application runtime.

## Usage

Deformatter is initialized with a user callback. Data is decoded using
[`cs_trace_defmt_process()`](../../doxygen/html/group__cs__trace__defmt.md#ga109bab752da74692779aa3eb96b771ba) in 16 bytes chunks. Callback is called whenever stream changes or
end of chunk is reached. Callback contains stream ID and the data.

## API documentation

[Coresight Trace Deformatter](../../doxygen/html/group__cs__trace__defmt.md)
