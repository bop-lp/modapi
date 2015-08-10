import config

import os

# Generates requirements.txt file from modules
found = ['server_requirements.txt']

for f in os.listdir(config.MODULES_DIR):
    path = os.path.join(config.MODULES_DIR, f)
    if os.path.isdir(path):
      path = os.path.join(path, 'requirements.txt')
      if os.path.isfile(path):
        found.append(path)

with open('requirements.txt', 'w') as file:
  for f in found:
    file.write('-r %s\n' % f)

with open('requirements.sh', 'w') as file:
  for f in found:
    file.write('pip install -r %s\n' % f)
