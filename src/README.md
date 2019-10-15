To run the program, you have to run Main.py.
This will execute Forward A*, Backwards A*, and Adaptive A* for all 50 maps.
The solution for only the last executed A* algorithm will be saved, if using the primary method as it is.

To execute the A* algorithm individually,
you will have to create an AlgorithmPicker object.
After this, you can run each algorithm individually, by passing in the file path of the map you want to run.

For example, if you want to run the Forward A* algorithm on map0, then you will want to have this:
`algo_picker.executeForwardAstar("resources/map0")`

If the path is found, then a file called `solution` will appear and have the map, and its path saved.