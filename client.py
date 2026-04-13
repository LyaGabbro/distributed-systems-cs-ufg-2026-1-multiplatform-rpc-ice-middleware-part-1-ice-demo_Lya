import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

#inserir ip da máquina na qual o código vai rodar no lugar de 98.90.53.6 na linha abaixo
base = communicator.stringToProxy("SimplePrinter:tcp -h 98.90.53.6 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello! This is a string from the printer.")
