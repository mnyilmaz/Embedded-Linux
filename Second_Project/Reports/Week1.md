# Week 1

On the first week my responsibilities were understanding the basics of:
-   MicroPython
-   Raspberry Pi Pico
-   Pico LTE Module

and all these are studied well. Report related to these titles can be found below.


# MicroPython
MicroPython is an optimized Python programming language that provide run on microcontrollers. This version includes less python libraries and more efficient ram and storage usage than Python. Allows full Python compiler and runtime. Basically as a user friendly Python programming language based aids help to control hardware systems on small embedded systems. Includes all the syntax of Python 3.4 and some of earlier features of Python 3.5. 156 kB space and 16 kB RAM capacity is enough for MicroPython to operate.

> Select ports have support for `_thread` module (multithreading), `socket` and `ssl` for networking, and `asyncio`
>
> MicroPython can execute scripts in textual source form (.py files) or from precompiled bytecode (.mpy files), in both cases either from an on-device filesystem or "frozen" into the MicroPython executable.
> 
> MicroPython also provides a set of MicroPython-specific modules to access hardware-specific functionality and peripherals such as GPIO, Timers, ADC, DAC, PWM, SPI, I2C, CAN, Bluetooth, and USB.

At this point, three main features emerge:

 - **Interactive REPL**: Read, evaluate, print and loop; allows executing the code without compiling and uploading.
 - **Extensive software library**
 - **Extensibility**: Can be mixed with low level languages such as C/C++ to have a better performance.

**Sources:**
 - [MicroPython](https://micropython.org/)
 - [MicroPython Basics](https://www.digikey.com/en/maker/projects/micropython-basics-what-is-micropython/1f60afd88e6b44c0beb0784063f664fc)
 - [MicroPython GitHub](https://github.com/micropython/micropython)


# Raspberry Pi Pico
Despite other Raspberry Pi models, Pico is known as a rival to Arduino as a microcontroller. That microcontroller consists:

 - 32 bit ARM Cortex M0+ based RP2040 
 - 264 kB VRAM
 - 2 MB built-in Flash memory capacity
 - 26 GPIO PIN
 - Temperature sensor

Also supports UART, I2C, SPI, PWM protocols; C and C++ programming languages.

![RaspberryPi-Pico-Pinout-1536x922](https://github.com/mnyilmaz/Embedded-Linux/assets/68549106/d08d4e1a-7197-4370-bda5-b8af237ea154)

**Sources:**
 - [Tutorial](https://randomnerdtutorials.com/raspberry-pi-pico-vs-code-micropython/#:~:text=If%20you%20like%20to%20program,simpler%20IDEs%2C%20like%20Thonny%20IDE.)
 - [Beginner's Guide](https://maker.robotistan.com/raspberry-pi-pico/)
 - [Beginner's Guide #2](https://omerfarukyildiz.com/raspberry-pi-pico-nedir/)

# Pico LTE Module


