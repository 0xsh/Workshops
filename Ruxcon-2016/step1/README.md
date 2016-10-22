Step 1
======

Download the transmit and receive graphs
----------------------------------------
Download "psk31_tx.grc" & "psk31_rx.grc" from this GitHub (step1 directory).
These are based on tkuester's great PSK31 examples from: https://github.com/tkuester/gr-psk31. 
They are modified slightly to use an audio card instead of a recorded wav file.
These graphs require installation of gr-ham for the varicode block: https://github.com/argilo/gr-ham

Install gr-psk31
----------------
Download https://github.com/tkuester/gr-psk31/ (also included here for ease of access)

$ mkdir build

$ cd build

$ cmake ../  (may need to apt-get install cmake & python-pkgconfig)

$ make

$ sudo make install


Run the transmit and receive graphs
------------------------------------
Open both graphs in gnuradio-companion.

Note, you may need to replace the missing block in "psk31_tx.grc" with a new "Varicode Encoder" block after installing gr-ham. Just use the search icon and type "Varicode Encoder" to find it and drag onto the screen.

Next, execute the transmit and receive graphs and check if you are receiving the text in the gnuradio-companion console. 
If not, you may need to tune using the "Tune Freq" on the right hand side of the receive graph.

