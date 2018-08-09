# Python-Examples


### Toga Issue:
In order to get Toga to work with Python 3.7 in windows, pythonnet needs to be
installed manually through a different repo. Enter these commands to install
both pythonnet and Toga:

    pip install wheel
    pip install git+https://github.com/pythonnet/pythonnet.git@py37
    pip install --pre toga
