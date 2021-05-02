import wget
import os
import pandas as pd

# Set working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

url = "ftp://ftp.ssec.wisc.edu/pub/wisconsinview/lidar/Kenosha/Kenosha_2017_SEWRPC_QL1_Reprocessed/Classified_LAS/LAS/"

def list_files(url):
    # Call wget from the system
    os.system(
    f"""
    wget --no-remove-listing "{url}"
    """)

    # Clean up html file
    os.remove("index.html")

    # Read listing file
    tbl = pd.read_csv(".listing", header=None)

    # split to get file names
    tbl = tbl[0].str.rsplit(n=1, expand = True)

    return tbl

# Call above function
tbl = list_files(url)

def list_convert(nrows, tbl):
    # Convert to list
    ls = tbl.loc[nrows:,1].tolist()

    # concat the url with the file name
    ls = [url + s for s in ls]
    return ls

# Convert table into list of file locations with url
# the table may contain non-files which should be skipped
# This will vary by county so the table should be inspected each time
files = list_convert(nrows = 3, tbl=tbl)

# TODO download all files as for loop or other method
# wget.download(files[5])

