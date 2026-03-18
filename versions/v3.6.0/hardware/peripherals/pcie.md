---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/pcie.html
original_path: hardware/peripherals/pcie.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Peripheral Component Interconnect express Bus (PCIe)

## Overview

## API Reference

*group* pcie\_host\_interface
:   PCIe Host Interface.

    Defines

    PCIE\_ID\_IS\_VALID(id)

    PCIE\_DT\_ID(node\_id)
    :   Get the PCIe Vendor and Device ID for a node.

        Parameters:
        :   - **node\_id** – DTS node identifier

        Returns:
        :   The VID/DID combination as [pcie\_id\_t](#group__pcie__host__interface_1ga30840d0e312e35f00790660193fd4c04)

    PCIE\_DT\_INST\_ID(inst)
    :   Get the PCIe Vendor and Device ID for a node.

        This is equivalent to `[PCIE_DT_ID(DT_DRV_INST(inst))](#group__pcie__host__interface_1ga304228150cd8ec56aa24be468e9d79bf)`

        Parameters:
        :   - **inst** – Devicetree instance number

        Returns:
        :   The VID/DID combination as [pcie\_id\_t](#group__pcie__host__interface_1ga30840d0e312e35f00790660193fd4c04)

    DEVICE\_PCIE\_DECLARE(node\_id)
    :   Declare a PCIe context variable for a DTS node.

        Declares a PCIe context for a DTS node. This must be done before using the [DEVICE\_PCIE\_INIT()](#group__pcie__host__interface_1gab6c472838e13293980cd53c65aaa3c47) macro for the same node.

        Parameters:
        :   - **node\_id** – DTS node identifier

    DEVICE\_PCIE\_INST\_DECLARE(inst)
    :   Declare a PCIe context variable for a DTS node.

        This is equivalent to `[DEVICE_PCIE_DECLARE(DT_DRV_INST(inst))](#group__pcie__host__interface_1gad0b870d891458c4ebd7ab2ac1c372eec)`

        Parameters:
        :   - **inst** – Devicetree instance number

    DEVICE\_PCIE\_INIT(node\_id, name)
    :   Initialize a named struct member to point at a PCIe context.

        Initialize PCIe-related information within a specific instance of a device config struct, using information from DTS. Using the macro requires having first created PCIe context struct using the [DEVICE\_PCIE\_DECLARE()](#group__pcie__host__interface_1gad0b870d891458c4ebd7ab2ac1c372eec) macro.

        Example for an instance of a driver belonging to the “foo” subsystem

        struct foo\_config { struct [pcie\_dev](#structpcie__dev) \*pcie; … };

        DEVICE\_PCIE\_ID\_DECLARE(DT\_DRV\_INST(…)); struct foo\_config my\_config = { [DEVICE\_PCIE\_INIT(pcie, DT\_DRV\_INST(…))](#group__pcie__host__interface_1gab6c472838e13293980cd53c65aaa3c47), … };

        Parameters:
        :   - **node\_id** – DTS node identifier
            - **name** – Member name within config for the MMIO region

    DEVICE\_PCIE\_INST\_INIT(inst, name)
    :   Initialize a named struct member to point at a PCIe context.

        This is equivalent to `[DEVICE_PCIE_INIT(DT_DRV_INST(inst), name)](#group__pcie__host__interface_1gab6c472838e13293980cd53c65aaa3c47)`

        Parameters:
        :   - **inst** – Devicetree instance number
            - **name** – Name of the struct member (of type struct [pcie\_dev](#structpcie__dev) \*)

    PCIE\_HOST\_CONTROLLER(n)
    :   Get the BDF for a given PCI host controller.

        This macro is useful when the PCI host controller behind PCIE\_BDF(0, 0, 0) indicates a multifunction device. In such a case each function of this endpoint is a potential host controller itself.

        Parameters:
        :   - **n** – Bus number

        Returns:
        :   BDF value of the given host controller

    PCIE\_CONF\_CAPPTR

    PCIE\_CONF\_CAPPTR\_FIRST(w)

    PCIE\_CONF\_CAP\_ID(w)

    PCIE\_CONF\_CAP\_NEXT(w)

    PCIE\_CONF\_EXT\_CAPPTR

    PCIE\_CONF\_EXT\_CAP\_ID(w)

    PCIE\_CONF\_EXT\_CAP\_VER(w)

    PCIE\_CONF\_EXT\_CAP\_NEXT(w)

    PCIE\_CONF\_ID

    PCIE\_CONF\_CMDSTAT

    PCIE\_CONF\_CMDSTAT\_IO

    PCIE\_CONF\_CMDSTAT\_MEM

    PCIE\_CONF\_CMDSTAT\_MASTER

    PCIE\_CONF\_CMDSTAT\_INTERRUPT

    PCIE\_CONF\_CMDSTAT\_CAPS

    PCIE\_CONF\_CLASSREV

    PCIE\_CONF\_CLASSREV\_CLASS(w)

    PCIE\_CONF\_CLASSREV\_SUBCLASS(w)

    PCIE\_CONF\_CLASSREV\_PROGIF(w)

    PCIE\_CONF\_CLASSREV\_REV(w)

    PCIE\_CONF\_TYPE

    PCIE\_CONF\_MULTIFUNCTION(w)

    PCIE\_CONF\_TYPE\_BRIDGE(w)

    PCIE\_CONF\_TYPE\_GET(w)

    PCIE\_CONF\_TYPE\_STANDARD

    PCIE\_CONF\_TYPE\_PCI\_BRIDGE

    PCIE\_CONF\_TYPE\_CARDBUS\_BRIDGE

    PCIE\_CONF\_BAR0

    PCIE\_CONF\_BAR1

    PCIE\_CONF\_BAR2

    PCIE\_CONF\_BAR3

    PCIE\_CONF\_BAR4

    PCIE\_CONF\_BAR5

    PCIE\_CONF\_BAR\_IO(w)

    PCIE\_CONF\_BAR\_MEM(w)

    PCIE\_CONF\_BAR\_64(w)

    PCIE\_CONF\_BAR\_ADDR(w)

    PCIE\_CONF\_BAR\_IO\_ADDR(w)

    PCIE\_CONF\_BAR\_FLAGS(w)

    PCIE\_CONF\_BAR\_NONE

    PCIE\_CONF\_BAR\_INVAL

    PCIE\_CONF\_BAR\_INVAL64

    PCIE\_CONF\_BAR\_INVAL\_FLAGS(w)

    PCIE\_BUS\_NUMBER

    PCIE\_BUS\_PRIMARY\_NUMBER(w)

    PCIE\_BUS\_SECONDARY\_NUMBER(w)

    PCIE\_BUS\_SUBORDINATE\_NUMBER(w)

    PCIE\_SECONDARY\_LATENCY\_TIMER(w)

    PCIE\_BUS\_NUMBER\_VAL(prim, sec, sub, lat)

    PCIE\_IO\_SEC\_STATUS

    PCIE\_IO\_BASE(w)

    PCIE\_IO\_LIMIT(w)

    PCIE\_SEC\_STATUS(w)

    PCIE\_IO\_SEC\_STATUS\_VAL(iob, iol, sec\_status)

    PCIE\_MEM\_BASE\_LIMIT

    PCIE\_MEM\_BASE(w)

    PCIE\_MEM\_LIMIT(w)

    PCIE\_MEM\_BASE\_LIMIT\_VAL(memb, meml)

    PCIE\_PREFETCH\_BASE\_LIMIT

    PCIE\_PREFETCH\_BASE(w)

    PCIE\_PREFETCH\_LIMIT(w)

    PCIE\_PREFETCH\_BASE\_LIMIT\_VAL(pmemb, pmeml)

    PCIE\_PREFETCH\_BASE\_UPPER

    PCIE\_PREFETCH\_LIMIT\_UPPER

    PCIE\_IO\_BASE\_LIMIT\_UPPER

    PCIE\_IO\_BASE\_UPPER(w)

    PCIE\_IO\_LIMIT\_UPPER(w)

    PCIE\_IO\_BASE\_LIMIT\_UPPER\_VAL(iobu, iolu)

    PCIE\_CONF\_INTR

    PCIE\_CONF\_INTR\_IRQ(w)

    PCIE\_CONF\_INTR\_IRQ\_NONE

    PCIE\_MAX\_BUS

    PCIE\_MAX\_DEV

    PCIE\_MAX\_FUNC

    PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p)
    :   Initialize an interrupt handler for a PCIe endpoint IRQ.

        This routine is only meant to be used by drivers using PCIe bus and having fixed or MSI based IRQ (so no runtime detection of the IRQ). In case of runtime detection see [pcie\_connect\_dynamic\_irq()](#group__pcie__host__interface_1ga14970194de1024a1a4669b69f932a4f5)

        Parameters:
        :   - **bdf\_p** – PCIe endpoint BDF
            - **irq\_p** – IRQ line number.
            - **priority\_p** – Interrupt priority.
            - **isr\_p** – Address of interrupt service routine.
            - **isr\_param\_p** – Parameter passed to interrupt service routine.
            - **flags\_p** – Architecture-specific IRQ configuration flags..

    Typedefs

    typedef uint32\_t pcie\_bdf\_t
    :   A unique PCI(e) endpoint (bus, device, function).

        A PCI(e) endpoint is uniquely identified topologically using a (bus, device, function) tuple. The internal structure is documented in include/dt-bindings/pcie/pcie.h: see PCIE\_BDF() and friends, since these tuples are referenced from devicetree.

    typedef uint32\_t pcie\_id\_t
    :   A unique PCI(e) identifier (vendor ID, device ID).

        The PCIE\_CONF\_ID register for each endpoint is a (vendor ID, device ID) pair, which is meant to tell the system what the PCI(e) endpoint is. Again, look to PCIE\_ID\_\* macros in include/dt-bindings/pcie/pcie.h for more.

    typedef bool (\*pcie\_scan\_cb\_t)([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, [pcie\_id\_t](#c.pcie_id_t) id, void \*cb\_data)
    :   Callback type used for scanning for PCI endpoints.

        Param bdf:
        :   BDF value for a found endpoint.

        Param id:
        :   Vendor & Device ID for the found endpoint.

        Param cb\_data:
        :   Custom, use case specific data.

        Return:
        :   true to continue scanning, false to stop scanning.

    Enums

    enum [anonymous]
    :   *Values:*

        enumerator PCIE\_SCAN\_RECURSIVE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Scan all available PCI host controllers and sub-busses.

        enumerator PCIE\_SCAN\_CB\_ALL = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Do the callback for all endpoint types, including bridges.

    Functions

    [pcie\_bdf\_t](#c.pcie_bdf_t) pcie\_bdf\_lookup([pcie\_id\_t](#c.pcie_id_t) id)
    :   Look up the BDF based on PCI(e) vendor & device ID.

        This function is used to look up the BDF for a device given its vendor and device ID.

        *Deprecated:*

        See also

        [DEVICE\_PCIE\_DECLARE](#group__pcie__host__interface_1gad0b870d891458c4ebd7ab2ac1c372eec)

        Parameters:
        :   - **id** – PCI(e) vendor & device ID encoded using PCIE\_ID()

        Returns:
        :   The BDF for the device, or PCIE\_BDF\_NONE if it was not found

    uint32\_t pcie\_conf\_read([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int reg)
    :   Read a 32-bit word from an endpoint’s configuration space.

        This function is exported by the arch/SoC/board code.

        Parameters:
        :   - **bdf** – PCI(e) endpoint
            - **reg** – the configuration word index (not address)

        Returns:
        :   the word read (0xFFFFFFFFU if nonexistent endpoint or word)

    void pcie\_conf\_write([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int reg, uint32\_t data)
    :   Write a 32-bit word to an endpoint’s configuration space.

        This function is exported by the arch/SoC/board code.

        Parameters:
        :   - **bdf** – PCI(e) endpoint
            - **reg** – the configuration word index (not address)
            - **data** – the value to write

    int pcie\_scan(const struct [pcie\_scan\_opt](#c.pcie_scan_opt) \*opt)
    :   Scan for PCIe devices.

        Scan the PCI bus (or busses) for available endpoints.

        Parameters:
        :   - **opt** – Options determining how to perform the scan.

        Returns:
        :   0 on success, negative POSIX error number on failure.

    bool pcie\_probe([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, [pcie\_id\_t](#c.pcie_id_t) id)
    :   Probe for the presence of a PCI(e) endpoint.

        *Deprecated:*

        See also

        [DEVICE\_PCIE\_DECLARE](#group__pcie__host__interface_1gad0b870d891458c4ebd7ab2ac1c372eec)

        Parameters:
        :   - **bdf** – the endpoint to probe
            - **id** – the endpoint ID to expect, or PCIE\_ID\_NONE for “any device”

        Returns:
        :   true if the device is present, false otherwise

    bool pcie\_get\_mbar([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int bar\_index, struct [pcie\_bar](#c.pcie_bar) \*mbar)
    :   Get the MBAR at a specific BAR index.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint
            - **bar\_index** – 0-based BAR index
            - **mbar** – Pointer to struct [pcie\_bar](#structpcie__bar)

        Returns:
        :   true if the mbar was found and is valid, false otherwise

    bool pcie\_probe\_mbar([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int index, struct [pcie\_bar](#c.pcie_bar) \*mbar)
    :   Probe the nth MMIO address assigned to an endpoint.

        A PCI(e) endpoint has 0 or more memory-mapped regions. This function allows the caller to enumerate them by calling with index=0..n. Value of n has to be below 6, as there is a maximum of 6 BARs. The indices are order-preserving with respect to the endpoint BARs: e.g., index 0 will return the lowest-numbered memory BAR on the endpoint.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint
            - **index** – (0-based) index
            - **mbar** – Pointer to struct [pcie\_bar](#structpcie__bar)

        Returns:
        :   true if the mbar was found and is valid, false otherwise

    bool pcie\_get\_iobar([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int bar\_index, struct [pcie\_bar](#c.pcie_bar) \*iobar)
    :   Get the I/O BAR at a specific BAR index.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint
            - **bar\_index** – 0-based BAR index
            - **iobar** – Pointer to struct [pcie\_bar](#structpcie__bar)

        Returns:
        :   true if the I/O BAR was found and is valid, false otherwise

    bool pcie\_probe\_iobar([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int index, struct [pcie\_bar](#c.pcie_bar) \*iobar)
    :   Probe the nth I/O BAR address assigned to an endpoint.

        A PCI(e) endpoint has 0 or more I/O regions. This function allows the caller to enumerate them by calling with index=0..n. Value of n has to be below 6, as there is a maximum of 6 BARs. The indices are order-preserving with respect to the endpoint BARs: e.g., index 0 will return the lowest-numbered I/O BAR on the endpoint.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint
            - **index** – (0-based) index
            - **iobar** – Pointer to struct [pcie\_bar](#structpcie__bar)

        Returns:
        :   true if the I/O BAR was found and is valid, false otherwise

    void pcie\_set\_cmd([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, uint32\_t bits, bool on)
    :   Set or reset bits in the endpoint command/status register.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint
            - **bits** – the powerset of bits of interest
            - **on** – use true to set bits, false to reset them

    unsigned int pcie\_alloc\_irq([pcie\_bdf\_t](#c.pcie_bdf_t) bdf)
    :   Allocate an IRQ for an endpoint.

        This function first checks the IRQ register and if it contains a valid value this is returned. If the register does not contain a valid value allocation of a new one is attempted. Such function is only exposed if CONFIG\_PCIE\_CONTROLLER is unset. It is thus available where architecture tied dynamic IRQ allocation for PCIe device makes sense.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint

        Returns:
        :   the IRQ number, or PCIE\_CONF\_INTR\_IRQ\_NONE if allocation failed.

    unsigned int pcie\_get\_irq([pcie\_bdf\_t](#c.pcie_bdf_t) bdf)
    :   Return the IRQ assigned by the firmware/board to an endpoint.

        Parameters:
        :   - **bdf** – the PCI(e) endpoint

        Returns:
        :   the IRQ number, or PCIE\_CONF\_INTR\_IRQ\_NONE if unknown.

    void pcie\_irq\_enable([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int irq)
    :   Enable the PCI(e) endpoint to generate the specified IRQ.

        If MSI is enabled and the endpoint supports it, the endpoint will be configured to generate the specified IRQ via MSI. Otherwise, it is assumed that the IRQ has been routed by the boot firmware to the specified IRQ, and the IRQ is enabled (at the I/O APIC, or wherever appropriate).

        Parameters:
        :   - **bdf** – the PCI(e) endpoint
            - **irq** – the IRQ to generate

    uint32\_t pcie\_get\_cap([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, uint32\_t cap\_id)
    :   Find a PCI(e) capability in an endpoint’s configuration space.

        Parameters:
        :   - **bdf** – the PCI endpoint to examine
            - **cap\_id** – the capability ID of interest

        Returns:
        :   the index of the configuration word, or 0 if no capability.

    uint32\_t pcie\_get\_ext\_cap([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, uint32\_t cap\_id)
    :   Find an Extended PCI(e) capability in an endpoint’s configuration space.

        Parameters:
        :   - **bdf** – the PCI endpoint to examine
            - **cap\_id** – the capability ID of interest

        Returns:
        :   the index of the configuration word, or 0 if no capability.

    bool pcie\_connect\_dynamic\_irq([pcie\_bdf\_t](#c.pcie_bdf_t) bdf, unsigned int irq, unsigned int priority, void (\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)
    :   Dynamically connect a PCIe endpoint IRQ to an ISR handler.

        Parameters:
        :   - **bdf** – the PCI endpoint to examine
            - **irq** – the IRQ to connect (see [pcie\_alloc\_irq()](#group__pcie__host__interface_1gad69ae431e5f91992f071dee9d7fa9110))
            - **priority** – priority of the IRQ
            - **routine** – the ISR handler to connect to the IRQ
            - **parameter** – the parameter to provide to the handler
            - **flags** – IRQ connection flags

        Returns:
        :   true if connected, false otherwise

    struct pcie\_dev
    :   *#include <pcie.h>*

    struct pcie\_bar
    :   *#include <pcie.h>*

    struct pcie\_scan\_opt
    :   *#include <pcie.h>*

        Options for performing a scan for PCI devices.

        Public Members

        uint8\_t bus
        :   Initial bus number to scan.

        [pcie\_scan\_cb\_t](#c.pcie_scan_cb_t) cb
        :   Function to call for each found endpoint.

        void \*cb\_data
        :   Custom data to pass to the scan callback.

        uint32\_t flags
        :   Scan flags.
