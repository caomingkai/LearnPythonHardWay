from sys import argv
from os.path import exists
# unpack the parameter argv with three variables
script, from_file, to_file = argv
# print out the name of the source file and the destination file.
print "Copying from %s to %s " %(from_file, to_file)
# open the source file, and set the file object to in_file
in_file = open(from_file)
# read the data from the source file to the indata variable
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CRTL - C to abort."
# The code below is not written is just alright.
raw_input()
# open the destination file with option 'w'
out_file = open(to_file, 'w')
# copy the source data 'indata' from the source file to destination file .
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
