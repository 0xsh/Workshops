Step 2
------

Remove the gui components in the transmit graph
------------------------------------------------
Disable:
* QT GUI Range "tx_freq"
* QT GUI Time Sink 

Create:
* Create a variable called "tx_freq" and set to 2000

Modify:
* Modify the "top_block" to "No GUI" and "Run to Completion"

Remove the gui components in the receive graph
------------------------------------------------
Disable:
* QT GUI Range "vol"
* QT GUI Range "tune_freq"
* QT GUI Waterfall Sink x 2
* Decimating FIR Filter & QT GUI Constellation Sink
* QT GUI Time Sink

Create:
* Create a variable called "tune_freq" and set to 2003

Modify:
* Modify the "top_block" to "No GUI" and "Run to Completion"


Generate python code
---------------------
* In the transmit block, run Generate (F5)
* save the "top_blocks.py" as "psk31_tx.py"
* In the receive block, run Generate (F5)
* save the "top_blocks.py" as "psk31_rx.py"

Test
----
Run the transmit and receive graphs in gnuradio-companion and confirm the message is still received and no graphical components are displayed
