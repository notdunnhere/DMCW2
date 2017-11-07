#!/usr/bin/python

#Data Mining and Machine Learning Coursework 2
#Due Tuesday 7/11
#Step 1
#This file converts csv files to arff files

#imports
import csv
import sys
from time import sleep

#main function
def main(argv):
	
	#store the filename temporarily
	#this is so that fer2017.csv will not lose it's name
	#it will become fer2017.arff
	filename = sys.argv[1]
	newfilename = filename.split(".")
	
	#writes new filename
	o = open( newfilename[0] + ".arff",'w')
	
	#starts writing the file
	#write relation line
	o.write( "@relation " + newfilename[0] + "\n" )
	#writes attribute line
	o.write( "@ATTRIBUTE 'emotion' {'Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral'}\n" )
	
	#creates a dictionary to convert the numbers to the words that we want 
	#for our class attribute
	dict = {'0' : "'Angry'", '1' : "'Disgust'", '2' : "'Fear'", '3' : "'Happy'", '4' : "'Sad'", '5' : "'Surprise'", '6' : "'Neutral'"}
	
	#writes the instances in the file
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
				
				#uses dictionary to replace numbers with words
			o.write( dict[firstSplit[0]] + "," + firstSplit[1].replace( " ", "," ) )
			
	o.close()
	

if __name__ == "__main__":
   main(sys.argv[1:])

