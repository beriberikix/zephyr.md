---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/modbus/index.html
original_path: services/modbus/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Modbus

Modbus is an industrial messaging protocol. The protocol is specified
for different types of networks or buses. Zephyr OS implementation
supports communication over serial line and may be used
with different physical interfaces, like RS485 or RS232.
TCP support is not implemented directly, but there are helper functions
to realize TCP support according to the application’s needs.

Modbus communication is based on client/server model.
Only one client may be present on the bus. Client can communicate with several
server devices. Server devices themselves are passive and must not send
requests or unsolicited responses.
Services requested by the client are specified by function codes (FCxx),
and can be found in the specification or documentation of the API below.

Zephyr RTOS implementation supports both client and server roles.

More information about Modbus and Modbus RTU can be found on the website
[MODBUS Protocol Specifications](https://www.modbus.org/specs.php).

## Samples

- [Modbus RTU server](../../samples/subsys/modbus/rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.") and [Modbus RTU client](../../samples/subsys/modbus/rtu_client/README.md#modbus-rtu-client "Communicate with a Modbus RTU server.") samples give
  the possibility to try out RTU server and RTU client implementation with an evaluation board.
- [Modbus TCP server](../../samples/subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.") sample is a simple Modbus TCP server.
- [Modbus TCP-to-serial gateway](../../samples/subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.") sample shows how to build a TCP to serial line
  gateway with Zephyr OS.

## API Reference

Related code samples

[Modbus RTU client](../../samples/subsys/modbus/rtu_client/README.md#modbus-rtu-client "Communicate with a Modbus RTU server.")
:   Communicate with a Modbus RTU server.

[Modbus RTU server](../../samples/subsys/modbus/rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.")
:   Implement a Modbus RTU server exposing Modbus commands to control LEDs.

[Modbus TCP server](../../samples/subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.")
:   Implement a Modbus TCP server exposing Modbus commands to control LEDs.

[Modbus TCP-to-serial gateway](../../samples/subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.")
:   Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.

*group* MODBUS
:   MODBUS transport protocol API.

    Modbus exception codes

    MODBUS\_EXC\_NONE
    :   No exception.

    MODBUS\_EXC\_ILLEGAL\_FC
    :   Illegal function code.

    MODBUS\_EXC\_ILLEGAL\_DATA\_ADDR
    :   Illegal data address.

    MODBUS\_EXC\_ILLEGAL\_DATA\_VAL
    :   Illegal data value.

    MODBUS\_EXC\_SERVER\_DEVICE\_FAILURE
    :   Server device failure.

    MODBUS\_EXC\_ACK
    :   Acknowledge.

    MODBUS\_EXC\_SERVER\_DEVICE\_BUSY
    :   Server device busy.

    MODBUS\_EXC\_MEM\_PARITY\_ERROR
    :   Memory parity error.

    MODBUS\_EXC\_GW\_PATH\_UNAVAILABLE
    :   Gateway path unavailable.

    MODBUS\_EXC\_GW\_TARGET\_FAILED\_TO\_RESP
    :   Gateway target device failed to respond.

    Defines

    MODBUS\_MBAP\_LENGTH
    :   Length of MBAP Header.

    MODBUS\_MBAP\_AND\_FC\_LENGTH
    :   Length of MBAP Header plus function code.

    MODBUS\_CUSTOM\_FC\_DEFINE(name, user\_cb, user\_fc, userdata)
    :   INTERNAL\_HIDDEN.

        Helper macro for initializing custom function code structs

    Typedefs

    typedef int (\*modbus\_raw\_cb\_t)(const int iface, const struct [modbus\_adu](#c.modbus_adu) \*adu, void \*user\_data)
    :   ADU raw callback function signature.

        Param iface:
        :   Modbus RTU interface index

        Param adu:
        :   Pointer to the RAW ADU struct to send

        Param user\_data:
        :   Pointer to the user data

        Retval 0:
        :   If transfer was successful

    typedef bool (\*modbus\_custom\_cb\_t)(const int iface, const struct [modbus\_adu](#c.modbus_adu) \*const rx\_adu, struct [modbus\_adu](#c.modbus_adu) \*const tx\_adu, uint8\_t \*const excep\_code, void \*const user\_data)
    :   Custom function code handler function signature.

        Modbus allows user defined function codes which can be used to extend the base protocol. These callbacks can also be used to implement function codes currently not supported by Zephyr’s Modbus subsystem.

        If an error occurs during the handling of the request, the handler should signal this by setting excep\_code to a modbus exception code.

        User data pointer can be used to pass state between subsequent calls to the handler.

        Param iface:
        :   Modbus interface index

        Param rx\_adu:
        :   Pointer to the received ADU struct

        Param tx\_adu:
        :   Pointer to the outgoing ADU struct

        Param excep\_code:
        :   Pointer to possible exception code

        Param user\_data:
        :   Pointer to user data

        Retval true:
        :   If response should be sent, false otherwise

    Enums

    enum modbus\_mode
    :   Modbus interface mode.

        *Values:*

        enumerator MODBUS\_MODE\_RTU
        :   Modbus over serial line RTU mode.

        enumerator MODBUS\_MODE\_ASCII
        :   Modbus over serial line ASCII mode.

        enumerator MODBUS\_MODE\_RAW
        :   Modbus raw ADU mode.

    Functions

    int modbus\_read\_coils(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint8\_t \*const coil\_tbl, const uint16\_t num\_coils)
    :   Coil read (FC01).

        Sends a Modbus message to read the status of coils from a server.

        Note that the array that will be receiving the coil values must be greater than or equal to: (num\_coils - 1) / 8 + 1

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Coil starting address
            - **coil\_tbl** – Pointer to an array of bytes containing the value of the coils read. The format is:

              ```text
                              MSB                               LSB
                              B7   B6   B5   B4   B3   B2   B1   B0
                              -------------------------------------
              coil_tbl[0]     #8   #7                            #1
              coil_tbl[1]     #16  #15                           #9
                   :
                   :
              ```
            - **num\_coils** – Quantity of coils to read

        Return values:
        :   **0** – If the function was successful

    int modbus\_read\_dinputs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint8\_t \*const di\_tbl, const uint16\_t num\_di)
    :   Read discrete inputs (FC02).

        Sends a Modbus message to read the status of discrete inputs from a server.

        Note that the array that will be receiving the discrete input values must be greater than or equal to: (num\_di - 1) / 8 + 1

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Discrete input starting address
            - **di\_tbl** – Pointer to an array that will receive the state of the discrete inputs. The format of the array is as follows:

              ```text
                            MSB                               LSB
                            B7   B6   B5   B4   B3   B2   B1   B0
                            -------------------------------------
              di_tbl[0]     #8   #7                            #1
              di_tbl[1]     #16  #15                           #9
                   :
                   :
              ```
            - **num\_di** – Quantity of discrete inputs to read

        Return values:
        :   **0** – If the function was successful

    int modbus\_read\_holding\_regs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint16\_t \*const reg\_buf, const uint16\_t num\_regs)
    :   Read holding registers (FC03).

        Sends a Modbus message to read the value of holding registers from a server.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Register starting address
            - **reg\_buf** – Is a pointer to an array that will receive the current values of the holding registers from the server. The array pointed to by ‘reg\_buf’ needs to be able to hold at least ‘num\_regs’ entries.
            - **num\_regs** – Quantity of registers to read

        Return values:
        :   **0** – If the function was successful

    int modbus\_read\_input\_regs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint16\_t \*const reg\_buf, const uint16\_t num\_regs)
    :   Read input registers (FC04).

        Sends a Modbus message to read the value of input registers from a server.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Register starting address
            - **reg\_buf** – Is a pointer to an array that will receive the current value of the holding registers from the server. The array pointed to by ‘reg\_buf’ needs to be able to hold at least ‘num\_regs’ entries.
            - **num\_regs** – Quantity of registers to read

        Return values:
        :   **0** – If the function was successful

    int modbus\_write\_coil(const int iface, const uint8\_t unit\_id, const uint16\_t coil\_addr, const bool coil\_state)
    :   Write single coil (FC05).

        Sends a Modbus message to write the value of single coil to a server.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **coil\_addr** – Coils starting address
            - **coil\_state** – Is the desired state of the coil

        Return values:
        :   **0** – If the function was successful

    int modbus\_write\_holding\_reg(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, const uint16\_t reg\_val)
    :   Write single holding register (FC06).

        Sends a Modbus message to write the value of single holding register to a server unit.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Coils starting address
            - **reg\_val** – Desired value of the holding register

        Return values:
        :   **0** – If the function was successful

    int modbus\_request\_diagnostic(const int iface, const uint8\_t unit\_id, const uint16\_t sfunc, const uint16\_t data, uint16\_t \*const data\_out)
    :   Read diagnostic (FC08).

        Sends a Modbus message to perform a diagnostic function of a server unit.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **sfunc** – Diagnostic sub-function code
            - **data** – Sub-function data
            - **data\_out** – Pointer to the data value

        Return values:
        :   **0** – If the function was successful

    int modbus\_write\_coils(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint8\_t \*const coil\_tbl, const uint16\_t num\_coils)
    :   Write coils (FC15).

        Sends a Modbus message to write to coils on a server unit.

        Note that the array that will be receiving the coil values must be greater than or equal to: (num\_coils - 1) / 8 + 1

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Coils starting address
            - **coil\_tbl** – Pointer to an array of bytes containing the value of the coils to write. The format is:

              ```text
                              MSB                               LSB
                              B7   B6   B5   B4   B3   B2   B1   B0
                              -------------------------------------
              coil_tbl[0]     #8   #7                            #1
              coil_tbl[1]     #16  #15                           #9
                   :
                   :
              ```
            - **num\_coils** – Quantity of coils to write

        Return values:
        :   **0** – If the function was successful

    int modbus\_write\_holding\_regs(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, uint16\_t \*const reg\_buf, const uint16\_t num\_regs)
    :   Write holding registers (FC16).

        Sends a Modbus message to write to integer holding registers to a server unit.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Register starting address
            - **reg\_buf** – Is a pointer to an array containing the value of the holding registers to write. Note that the array containing the register values must be greater than or equal to ‘num\_regs’
            - **num\_regs** – Quantity of registers to write

        Return values:
        :   **0** – If the function was successful

    int modbus\_read\_holding\_regs\_fp(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, float \*const reg\_buf, const uint16\_t num\_regs)
    :   Read floating-point holding registers (FC03).

        Sends a Modbus message to read the value of floating-point holding registers from a server unit.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Register starting address
            - **reg\_buf** – Is a pointer to an array that will receive the current values of the holding registers from the server. The array pointed to by ‘reg\_buf’ needs to be able to hold at least ‘num\_regs’ entries.
            - **num\_regs** – Quantity of registers to read

        Return values:
        :   **0** – If the function was successful

    int modbus\_write\_holding\_regs\_fp(const int iface, const uint8\_t unit\_id, const uint16\_t start\_addr, float \*const reg\_buf, const uint16\_t num\_regs)
    :   Write floating-point holding registers (FC16).

        Sends a Modbus message to write to floating-point holding registers to a server unit.

        Parameters:
        :   - **iface** – Modbus interface index
            - **unit\_id** – Modbus unit ID of the server
            - **start\_addr** – Register starting address
            - **reg\_buf** – Is a pointer to an array containing the value of the holding registers to write. Note that the array containing the register values must be greater than or equal to ‘num\_regs’
            - **num\_regs** – Quantity of registers to write

        Return values:
        :   **0** – If the function was successful

    int modbus\_iface\_get\_by\_name(const char \*iface\_name)
    :   Get Modbus interface index according to interface name.

        If there is more than one interface, it can be used to clearly identify interfaces in the application.

        Parameters:
        :   - **iface\_name** – Modbus interface name

        Return values:
        :   **Modbus** – interface index or negative error value.

    int modbus\_init\_server(const int iface, struct [modbus\_iface\_param](#c.modbus_iface_param) param)
    :   Configure Modbus Interface as raw ADU server.

        Parameters:
        :   - **iface** – Modbus RTU interface index
            - **param** – Configuration parameter of the server interface

        Return values:
        :   **0** – If the function was successful

    int modbus\_init\_client(const int iface, struct [modbus\_iface\_param](#c.modbus_iface_param) param)
    :   Configure Modbus Interface as raw ADU client.

        Parameters:
        :   - **iface** – Modbus RTU interface index
            - **param** – Configuration parameter of the client interface

        Return values:
        :   **0** – If the function was successful

    int modbus\_disable(const uint8\_t iface)
    :   Disable Modbus Interface.

        This function is called to disable Modbus interface.

        Parameters:
        :   - **iface** – Modbus interface index

        Return values:
        :   **0** – If the function was successful

    int modbus\_raw\_submit\_rx(const int iface, const struct [modbus\_adu](#c.modbus_adu) \*adu)
    :   Submit raw ADU.

        Parameters:
        :   - **iface** – Modbus RTU interface index
            - **adu** – Pointer to the RAW ADU struct that is received

        Return values:
        :   **0** – If transfer was successful

    void modbus\_raw\_put\_header(const struct [modbus\_adu](#c.modbus_adu) \*adu, uint8\_t \*header)
    :   Put MBAP header into a buffer.

        Parameters:
        :   - **adu** – Pointer to the RAW ADU struct
            - **header** – Pointer to the buffer in which MBAP header will be placed.

    void modbus\_raw\_get\_header(struct [modbus\_adu](#c.modbus_adu) \*adu, const uint8\_t \*header)
    :   Get MBAP header from a buffer.

        Parameters:
        :   - **adu** – Pointer to the RAW ADU struct
            - **header** – Pointer to the buffer containing MBAP header

    void modbus\_raw\_set\_server\_failure(struct [modbus\_adu](#c.modbus_adu) \*adu)
    :   Set Server Device Failure exception.

        This function modifies ADU passed by the pointer.

        Parameters:
        :   - **adu** – Pointer to the RAW ADU struct

    int modbus\_raw\_backend\_txn(const int iface, struct [modbus\_adu](#c.modbus_adu) \*adu)
    :   Use interface as backend to send and receive ADU.

        This function overwrites ADU passed by the pointer and generates exception responses if backend interface is misconfigured or target device is unreachable.

        Parameters:
        :   - **iface** – Modbus client interface index
            - **adu** – Pointer to the RAW ADU struct

        Return values:
        :   **0** – If transfer was successful

    int modbus\_register\_user\_fc(const int iface, struct modbus\_custom\_fc \*custom\_fc)
    :   Register a user-defined function code handler.

        The Modbus specification allows users to define standard function codes missing from Zephyr’s Modbus implementation as well as add non-standard function codes in the ranges 65 to 72 and 100 to 110 (decimal), as per specification.

        This function registers a new handler at runtime for the given function code.

        Parameters:
        :   - **iface** – Modbus client interface index
            - **custom\_fc** – User defined function code and callback pair

        Return values:
        :   **0** – on success

    struct modbus\_adu
    :   *#include <modbus.h>*

        Frame struct used internally and for raw ADU support.

        Public Members

        uint16\_t trans\_id
        :   Transaction Identifier.

        uint16\_t proto\_id
        :   Protocol Identifier.

        uint16\_t length
        :   Length of the data only (not the length of unit ID + PDU).

        uint8\_t unit\_id
        :   Unit Identifier.

        uint8\_t fc
        :   Function Code.

        uint8\_t data[CONFIG\_MODBUS\_BUFFER\_SIZE - 4]
        :   Transaction Data.

        uint16\_t crc
        :   RTU CRC.

    struct modbus\_user\_callbacks
    :   *#include <modbus.h>*

        Modbus Server User Callback structure.

        Public Members

        int (\*coil\_rd)(uint16\_t addr, bool \*state)
        :   Coil read callback.

        int (\*coil\_wr)(uint16\_t addr, bool state)
        :   Coil write callback.

        int (\*discrete\_input\_rd)(uint16\_t addr, bool \*state)
        :   Discrete Input read callback.

        int (\*input\_reg\_rd)(uint16\_t addr, uint16\_t \*reg)
        :   Input Register read callback.

        int (\*input\_reg\_rd\_fp)(uint16\_t addr, float \*reg)
        :   Floating Point Input Register read callback.

        int (\*holding\_reg\_rd)(uint16\_t addr, uint16\_t \*reg)
        :   Holding Register read callback.

        int (\*holding\_reg\_wr)(uint16\_t addr, uint16\_t reg)
        :   Holding Register write callback.

        int (\*holding\_reg\_rd\_fp)(uint16\_t addr, float \*reg)
        :   Floating Point Holding Register read callback.

        int (\*holding\_reg\_wr\_fp)(uint16\_t addr, float reg)
        :   Floating Point Holding Register write callback.

    struct modbus\_serial\_param
    :   *#include <modbus.h>*

        Modbus serial line parameter.

        Public Members

        uint32\_t baud
        :   Baudrate of the serial line.

        enum [uart\_config\_parity](../../hardware/peripherals/uart.md#c.uart_config_parity "uart_config_parity") parity
        :   parity UART’s parity setting: UART\_CFG\_PARITY\_NONE, UART\_CFG\_PARITY\_EVEN, UART\_CFG\_PARITY\_ODD

        enum [uart\_config\_stop\_bits](../../hardware/peripherals/uart.md#c.uart_config_stop_bits "uart_config_stop_bits") stop\_bits\_client
        :   stop\_bits\_client UART’s stop bits setting if in client mode: UART\_CFG\_STOP\_BITS\_0\_5, UART\_CFG\_STOP\_BITS\_1, UART\_CFG\_STOP\_BITS\_1\_5, UART\_CFG\_STOP\_BITS\_2,

    struct modbus\_server\_param
    :   *#include <modbus.h>*

        Modbus server parameter.

        Public Members

        struct [modbus\_user\_callbacks](#c.modbus_user_callbacks) \*user\_cb
        :   Pointer to the User Callback structure.

        uint8\_t unit\_id
        :   Modbus unit ID of the server.

    struct modbus\_raw\_cb
    :   *#include <modbus.h>*

    struct modbus\_iface\_param
    :   *#include <modbus.h>*

        User parameter structure to configure Modbus interface as client or server.

        Public Members

        enum [modbus\_mode](#c.modbus_mode) mode
        :   Mode of the interface.

        uint32\_t rx\_timeout
        :   Amount of time client will wait for a response from the server.

        struct [modbus\_serial\_param](#c.modbus_serial_param) serial
        :   Serial support parameter of the interface.

        struct [modbus\_raw\_cb](#c.modbus_raw_cb) rawcb
        :   Pointer to raw ADU callback function.
