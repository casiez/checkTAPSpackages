import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='checkTAPSpackages',  
     version='0.3',
     scripts=['checkTAPSpackages'] ,
     author="Géry Casiez",
     author_email="gery.casiez@univ-lille.fr",
     description="Checks if a document complies with the list of LaTeX packages allowed by TAPS.",
     long_description=long_description,

     long_description_content_type="text/markdown",
     url="https://github.com/casiez/checkTAPSpackages",
     packages=setuptools.find_packages(),
     install_requires=[ 'argparse'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

 )