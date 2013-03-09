# Command to build:
from distutils.core import setup
import glob

package_prefix = "Lib/site-packages/aiml"

setup(name="PyAIML",
    version="0.8.6",
    author="Cort Stratton",
    author_email="cort@users.sourceforge.net",
    maintainer="Cort Stratton",
    maintainer_email="cort@users.sourceforge.net",
    
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description="""PyAIML implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.""",
    url="http://pyaiml.sourceforge.net/",
    platforms=["any"],
    classifiers=["Development Status :: 3 - Alpha",
                 "Environment :: Console",
                 "Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Operating System :: OS Independent",
                 "Topic :: Communications :: Chat",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence"
                 ],
      
    packages=["aiml"],
    data_files=[
        (package_prefix, glob.glob("aiml/self-test.aiml")),
        (package_prefix, glob.glob("*.txt")),
    ],
)
