 Each call to the program implements one image operation, which is specified by the command-line arguments:
 
• load input image path: loads the specified file, discards any existing history and makes this image the active image.

• filter filter width filter weights (same argument format from Q1): ap- plies the specified filter to the previously active image. The filtered result becomes the new active image and is placed at the next step in the history. Any previous history from this point forwards must be truncated.

• undo: moves the active image backwards by one step in history, if this is possible.
2
           
           
• redo: moves the active image forwards by one step in history, if this is possible.
The active image must always be written to result.bmp in the present working directory. Whenever an operation cannot be completed properly, print a sensible message to standard output.
