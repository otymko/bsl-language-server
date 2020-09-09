import sys
import os
import platform
import re
import ntpath
import shutil

def is_windows():
  thisPlatform = platform.system()
  return thisPlatform == 'Windows'  

jdk14Path = sys.argv[1] # ${{ matrix.jdk14Path }}
prefix = sys.argv[2] # ${{ matrix.prefix }}
app_image = sys.argv[3] # ${{ matrix.app-image }}

dirName = os.path.join(os.getcwd(), 'build', 'libs')

pattern = r"bsl.+\.jar"
isWindows = is_windows()          

if isWindows:
  jpackage = os.path.join(os.getcwd(), jdk14Path, 'bin', 'jpackage.exe')
else:
  jpackage = os.path.join(os.getcwd(), jdk14Path, 'bin', 'jpackage')       

def start():
  fullname = get_bslls_jar(dirName)
  if (fullname == None):
    return

  tmp_dir = os.path.join(dirName, 'tmp')
  os.mkdir(tmp_dir)
  shutil.copyfile(os.path.join(dirName, fullname), os.path.join(tmp_dir, fullname))

  cmd_args = [jpackage]
  cmd_args.append('--name')
  cmd_args.append('bsl-language-server')
  cmd_args.append('--input')
  cmd_args.append(tmp_dir)
  cmd_args.append('--main-jar')
  cmd_args.append(fullname)
  if isWindows:
    cmd_args.append('--win-console')
  cmd_args.append('--type')
  cmd_args.append('app-image')
  cmd_args.append('--java-options')
  cmd_args.append('-Xmx2g')

  cmd = ' '.join(cmd_args) 
  print(cmd)
  os.system(cmd)
                          
  shutil.rmtree(tmp_dir)
  shutil.make_archive("bsl-language-server_" + prefix, 'zip', './', app_image)

def get_bslls_jar(dir):
  names = os.listdir(dir)
  for name in names:
    fullname = os.path.join(dir, name)
    if os.path.isfile(fullname) and re.search(pattern, fullname) and fullname.find('exec.jar') != -1:
      return ntpath.basename(fullname)
  return None

start()