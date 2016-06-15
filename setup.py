from setuptools import setup

setup(name='whois-oracle',
      version='1.0.3',
      description='Module for retrieving and parsing the WHOIS data for a domain. Supports most domains. No dependencies.',
      author='Sander ten Hoor, original by Sven Slootweg',
      url='https://github.com/MasterFenrir/whois-oracle',
      packages=['pythonwhois', 'pythonwhois.caching', 'pythonwhois.ratelimit', 'pythonwhois.response'],
      package_data={"pythonwhois": ["*.dat"]},
      install_requires=['argparse'],
      provides=['pythonwhois'],
      scripts=["whois-oracle"],
      license="WTFPL"
      )
