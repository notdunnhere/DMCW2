#!/usr/bin/python

###############
# CSV to ARFF #
###############
import csv
import sys
from time import sleep

def main(argv):
	
	filename = sys.argv[1]
	newfilename = filename.split(".")
	
	o = open( newfilename[0] + ".arff",'w')
	nmax = 0;
	
	o.write( "@relation " + newfilename[0] + "\n" )
	o.write( "@ATTRIBUTE 'emotion' {'Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Suprise', 'Neutral'}\n" )
	
	dict = {'0' : "'Angry'", '1' : "'Disgust'", '2' : "'Fear'", '3' : "'Happy'", '4' : "'Sad'", '5' : "'Suprise'", '6' : "'Neutral'"}
	
	
	for x in range(0, 2303):
		o.write( "@attribute pixel%d NUMERIC\n" % (x) )
		
	
	with open(filename) as f:
		f.readline()
		o.write( "@data\n" )
		for line in f:
			#print( line )
			
			n = line.count(" ", 3)
			
			if( n > nmax):
				nmax = n
			
			
			
			print(  )

			o.write( dict[line[0]] + "," + line[3:].replace( " ", "," ) )
			
	o.close()
	

if __name__ == "__main__":
   main(sys.argv[1:])
