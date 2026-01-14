# Steps to rebuild / publish any Python Package

Follow the below youtube video link:
Link: https://youtu.be/Kz6IlDCyOUY?si=lFkpBFNhz6LJjAQ_

## Building packages
'''
python setup.py sdist bdist wheel
'''

## Local Testing
'''
pip install dist/tonique-0.2-py3-none-any.whl
'''
The above command install tonique version 0.2 in the python environment. To reinstall the package use --force-reinstall flag with the. above command.

To check if the library has been sucessfully installed run the below command and check for the library name.
'''
pip list
'''

## Push to pypi.org
1. Go to pypi.org to create an account.
2. Create a token and save it somewhere.
3. Run the below command to publish the build file to pypi.
    '''
    twine upload dist/*
    '''