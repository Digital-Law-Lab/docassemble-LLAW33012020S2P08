import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S2P08',
      version='1.0',
      description=('DSP Compass'),
      long_description='### Disability Support Pension Compass \r\n\r\n*What is the application?* \r\n\r\nThis application is designed to assist the clients of **Community Bridging Services Inc.** who receive the **Disability Support Pension**.  \r\n\r\nThere is a limitation on how much income an individual can earn from paid work whilst remaining eligible to receive their full Disability Support Pension each fortnight.  \r\n\r\nThe application was created to assist Disability Support Pension recipients in understanding how their finances will be affected by undertaking additional paid work. The application will enable the users to be able to make an informed decision before increasing their paid workload. \r\n\r\n*How does it work?* \r\n\r\nThis application calculates based upon the user’s entered characteristics and income how their Disability Support Pension might be affected if they were to earn more income than what they are currently earning. \r\n\r\nThe application will act as a first reference for the individual by providing an estimate of any deductions to their Disability Support Pension that may occur based upon their total working income. \r\n\r\nThe application will also produce an estimate of the user’s total income (including DSP, current income, additional income from increasing workload and any deductions) so that the user can see if they would be in a better financial position by working more hours. \r\n\r\nThe estimate produced by the application can be checked by contacting Centrelink for further advice. Any information provided is expressly stated as an estimate and should not be considered legal advice. \r\n\r\n*Is it safe to use?* \r\n\r\nThe application is anonymous and does not store information. The user can elect to save a copy of the information produced by sending an email to themselves. The email functionality is also useful for users to be able to send the information to a CBS Inc. staff member for reference if necessary. The created information will cease to exist once the user exits the application, except where it is emailed. \r\n\r\n## Authors\r\n\r\n- Caleb Rothe\r\n- Delaini Gates\r\n- Joshua Duncliffe\r\n- Lukas Hannett\r\n- Rui Seah\r\n',
      long_description_content_type='text/markdown',
      author='Caleb Rothe, Delaini Gates, Joshua Duncliffe, Lukas Hannett, Rui Seah',
      author_email='ferr0182@flinders.edu.au',
      license='Copyright (c) 2020 Flinders University All Rights Reserved',
      url='https://flinders.edu.au',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S2P08/', package='docassemble.LLAW33012020S2P08'),
     )

