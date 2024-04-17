# python_huffman
Repo for the huffman compression algorithm activity for the analysis of algorithms class at Universidad de Guadalajara, CUCEI.
Code has a front-end made in Tkinter, using the tkinter and numpy libraries.
The front end lets any user connect it to a personal back-end, as long as they link the back-end functions to the interface's buttons.
Front-end is fully implemented in a single file, containing a class named Interface and all its methods fairly commented and explained as well as some attributes.
The interface provides a simple window with a text frame and 3 buttons, one for opening files (only supports txt and binary extensions)
and 2 other buttons for either compressing or decompressing depending on the extension of the selected file
If the selected file is a txt file, the interface counts the characters, builds and sorts a dictionary stored as an attribute called char_count.
If the selected file the interface just stores the content of the file in the file_content variable.
The idea is that the back-end functions have parameters for receiving a dictionary (for the compression of txt files) or just a string (the compressed binary file)
After receiving those arguments, they can operate and make the compression or decompression internally, and possibly return a file or just a string for interface to show.
