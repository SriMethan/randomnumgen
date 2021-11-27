from distutils.core import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'randomnumgen',         
  packages = ['randomnumgen'],   
  version = '0.1',      
  license='MIT',        
  description = 'A Python3 library that generates random numbers.',   
  author = 'SriMethan',                   
  url = 'https://github.com/SriMethan/randomnumgen',  
  download_url = 'https://github.com/SriMethan/randomnumgen/archive/refs/heads/main.zip',    
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.7',
  ],
)
