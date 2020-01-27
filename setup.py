from distutils.core import setup
setup(
  name = 'topsis_code',         
  packages = ['topsis_code'],   
  version = '0.3',      
  license='MIT',        
  description = 'code on topsis',  
  author = 'Harshita Agarwal',               
  author_email = 'harshitaagrawal1998@gmail.com',      
  url = 'https://github.com/harshita-agr/topsis_code',   
  download_url = 'https://github.com/harshita-agr/topsis_code/archive/v_03.tar.gz',    
  keywords = ['TOPSIS'],
  install_requires=[                     
          'pandas', 
           'numpy', 
           'sys' ,
           'argparse'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',       
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
