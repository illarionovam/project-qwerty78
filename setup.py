from setuptools import setup, find_namespace_packages

setup(name='project_qwerty78',
      version='0.0.0',
      description='Personal assistant bot is a console application that helps you to maintain your contacts and '
                  'notes. You can add phones, birthday, email and address to the contacts. You can add tags to the '
                  'notes. It saves your data locally on your machine.',
      url='https://github.com/illarionovam/project-qwerty78',
      author='group-13',
      author_email='illarionovam@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['collections', 'difflib', 'rich', 'datetime'],
      entry_points={'console_scripts': ['run_bot = project_qwerty78.bot:main']}
      )
