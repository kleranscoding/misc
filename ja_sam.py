# -*- coding: utf-8 -*-
import sys
import encodings.utf_8

sys.stdout = encodings.utf_8.StreamWriter(sys.stdout)

## jezik
srpski= u'\u0421\u0440\u043F\u0441\u043A\u0438'
hrvatski= u'\u0425\u0440\u0432\u0430\u0442\u0441\u043a\u0438'
bosanski= u'\u0411\u043e\u0441\u0430\u043d\u0441\u043a\u0438'
crnagorski= u'\u0426\u0440\u043d\u0430\u0433\u043e\u0440\u0441\u043a\u0438'
makedonski= u'\u041c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438'
slovenachki= u'\u0421\u043b\u043e\u0432\u0435\u043d\u0430\u0447\u043a\u0438'
engleski= u'\u0415\u043D\u0433\u043B\u0435\u0441\u043a\u0438'

## python
python_str= "python 2.7"

## cirilica
''' azbuka '''
cirilica= u'\u040b\u0438\u0440\u0438\u043b\u0438\u0446\u0430'
latinica= 'latinica'
''' ja sam '''
srpski_cirilica= u'\u0408\u0430 \u0441\u0430\u043C'
crnagorski_cirilica= u'\u0408\u0430 \u0441\u0430\u043C'
makedonski_cirilica= u'\u0408\u0430\u0441 \u0441\u0443\u043C'

## list
'''
print srpski + ": " + srpski_cirilica + " " + python_str + "!"
print hrvatski + ": " + "Ja sam" + " " + python_str + "!"
print bosanski + ": " + "Ja sam" + " " + python_str + "!"
print crnagorski + ": " + crnagorski_cirilica + " " + python_str + "!"
print makedonski + ": " + makedonski_cirilica + " " + python_str + "!"
print slovenachki + ": " + "Jaz sam" + " " + python_str + "!"
print engleski + ": " + "I am" + " " + python_str + "!"
#'''

## table
#'''
print "\n " + cirilica + "      " + latinica + " "
print "+----------------------------------------------+"
print "| " + srpski + "     | " + "srpski" + "     | " + " " + srpski_cirilica + " " + python_str + " |"
#print "------------------------------------------------"
print "| " + hrvatski + "   | " + "hrvatski" + "   | " + " Ja sam" + " " + python_str + " |"
#print "------------------------------------------------"
print "| " + bosanski + "   | " + "bosanski" + "   | " + " Ja sam" + " " + python_str + " |"
#print "------------------------------------------------"
print "| " + crnagorski + " | " + "crnagorski" + " | " + " " + crnagorski_cirilica + " " + python_str + " |"
#print "------------------------------------------------"
print "| " + makedonski + " | " + "makedonski" + " | " + makedonski_cirilica + " " + python_str + " |"
#print "------------------------------------------------"
print "| " + slovenachki + " | " + "slovenski" + "  | " + "Jaz sam" + " " + python_str + " |"
#print "-----------------------------------"
print "| " + engleski + "   | " + "engleski" + "   | " + "  I  am" + " " + python_str + " |"
print "+----------------------------------------------+\n"
#'''


