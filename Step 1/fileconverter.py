#!/usr/bin/python

###############
# CSV to ARFF #
###############
import csv
import sys
from time import sleep

#main function
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
			firstSplit = line.split( "," );
			
			if firstSplit[1].count( " " ) != 2303:
				print( "Error, file has more data in one init" )
				return
				
			o.write( dict[firstSplit[0]] + "," + firstSplit[1].replace( " ", "," ) )
			
	o.close()
	

if __name__ == "__main__":
   main(sys.argv[1:])

