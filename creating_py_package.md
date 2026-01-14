# Steps to rebuild / publish any Python Package

Follow the below youtube video link:
Link: https://youtu.be/Kz6IlDCyOUY?si=lFkpBFNhz6LJjAQ_

## Building packages
The below command builds the distributable source archives and built packages (wheels) for a Python project.

`bash
python setup.py sdist bdist wheel
`

## Local Testing
The below command can be utilised to download the package internally within a local environment and test the package working.

`bash
pip install dist/tonique-0.2-py3-none-any.whl
`

The above command install tonique version 0.2 in the python environment. To reinstall the package use --force-reinstall flag with the. above command.

To check if the library has been sucessfully installed run the below command and check for the library name.
`bash
pip list
`

## Push to pypi.org
1. Go to pypi.org to create an account.
2. Create a token and save it somewhere.
3. Run the below command to publish the build file to pypi.

    `bash
    twine upload dist/*
    `