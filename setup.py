import setuptools
import subprocess
import os

cf_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in cf_remote_version

assert os.path.isfile("cf_remote/version.py")
with open("cf_remote/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{cf_remote_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'randomnumgen',         
  packages = ['randomnumgen'],   
  version = '1.0',      
  license='MIT',        
  description = 'A Python3 library that generates random numbers.',   
  author = 'SriMethan',                   
  url = 'https://github.com/SriMethan/randomnumgen',  
  download_url = 'https://github.com/SriMethan/randomnumgen/archive/refs/heads/main.zip',    
  keywords = ['RANDOMNUMGEN', 'MEANINGFULL', 'KEYWORDS'],   
  classifiers=[
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.7',
  ],
)
