import os
import io
import setuptools

def read_description():
  description = io.open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8').read()
  return description

setup(
  name = 'randomnumgen',         
  packages = ['randomnumgen'],   
  version = '1.0',      
  license='MIT',        
  description = 'A Python3 library that generates random numbers.',   
  author = 'SriMethan',                   
  url = 'https://github.com/SriMethan/randomnumgen',  
  download_url = 'https://github.com/SriMethan/randomnumgen/archive/refs/heads/main.zip',    
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   
  classifiers=[
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.7',
  ],
)
