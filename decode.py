import subprocess
fname ="/home/seppo/githubcheck.txt"
f = open (fname, "r") 
line = f.readline()
line = line.replace("\n", "")
command_line = "unzip -o -P " +line+ " test.zip"
p = subprocess.Popen(command_line, shell=True, stderr=subprocess.PIPE)


