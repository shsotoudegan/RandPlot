This progect, creates a csv file that has numbers and repeates to create a dataset with your given middle. Then plot that use matplotlib.

First do:
python3 -m pip -r requirements.txt

usage: randplot.py [-h] -s SIZE -min MIN -max MAX -m MIDDLE -step PLOT_STEP [-rfp RANDOMS_FILE_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Size of randoms.
  -min MIN, --min MIN   Minimum number of rabdoms
  -max MAX, --max MAX   Maximum number of rabdoms
  -m MIDDLE, --middle MIDDLE    Middle of randoms   
  -step PLOT_STEP, --plot-step PLOT_STEP Steps of plot
  -rfp RANDOMS_FILE_PATH, --randoms-file-path RANDOMS_FILE_PATH   Randoms csv file path. path from current directory