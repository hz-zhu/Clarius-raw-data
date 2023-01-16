# Clarius-raw-data
Processing and visualizing raw data collected from Clarius probes

The raw data downloaded by using Clarius probes with Clarius Cast API comes individual zip files with binary image data (doubly compressed) and machine parameters. For the convenient reading and processing directly from the collected tar files, I created python codes to extract and transform the data into usable format, i.e., numpy array and python dict. This code is adopted from Clarius official repositories. This code works for Windows OS only.

To run the code, the following packages are needed with Python 3:
Numpy
Scipy
Matplotlib

File “Visual.ipynb” shows an example of directing reading from a tar file. CData is the class that handles tar file processing. It takes three arguments to initialize, which are folder_path (the path to the intended tar file), filename (the name for the tar file), and lzop_path (the path to the unzip_data.exe file that extracts compressed data.

By calling CData.plot_rf(), we can get all raw image data in the file. Examples of how to use the returned object from CData.plot_rf() can be found in function CData.plot_rf(...).

By calling CData.plot_rf(start=0, stop=float('inf'), step), we can visualize the multi-frame data, starting from index start, ending with index stop with increment step step.

Note: The unzip_data.exe file may be misidentified as a virus. Please white list the file if misidentified. 
