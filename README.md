# Concurrency in Python with Asyncio

Source code to the Manning book *Concurrency in Python with Asyncio*.

## Running
This code ran successfully with Python version 3.9.5. Using a different version may give you different results or may not work. 

**Steps to Run Code Listing**

1. Install Python 3.9.5, installers available at the bottom of the page at: https://www.python.org/downloads/release/python-395/

2. Create a virtual environment and activate it. Instructions available [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

3. Install the dependencies for the project by running `pip install -r requirements.txt` within your virtual environment.

3. Several functions are in the `util` module - for this to import properly you need to include this module in your `PYTHONPATH`. You can do this by running `export PYTHONPATH=${PYTHONPATH}:concurrency-in-python-with-asyncio/util` within your terminal, changing `concurrency-in-python-with-asyncio` to whichever path you have cloned this repository on your local machine. 

5. You should now be able to run any code listing successfully with `python3 scriptname.py`, for example, `python3 chapter_01/listing_1_1.py` will run the first code listing from the first chapter.