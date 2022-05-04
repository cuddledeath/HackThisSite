# Encryption

import mechanize, os, cookielib, urllib, sys, re, lxml, md5
from lxml import html
from bs4 import BeautifulSoup
from PIL import Image

#function evalCrossTotal($strMD5)
#{
    #$intTotal = 0;
   # $arrMD5Chars = str_split($strMD5, 1); //put characters into array
   # foreach ($arrMD5Chars as $value)
   # {
   #     $intTotal += '0x0'.$value; //turn char to hexadecimal value and add it to $intTotal
   # }
   # return $intTotal;

#function encryptString($strString, $strPassword)
#{
    #// $strString is the content of the entire file with serials
    #$strPasswordMD5 = md5($strPassword); #md5 hash of Password
   # $intMD5Total = evalCrossTotal($strPasswordMD5); //$intMD5Total is the hexadecimal sum of the MD5 Encrypted password
    #$arrEncryptedValues = array();
    #$intStrlen = strlen($strString);
   # for ($i=0; $i<$intStrlen; $i++)
   # {
     #   $arrEncryptedValues[] =  ord(substr($strString, $i, 1))
      #                          +  ('0x0' . substr($strPasswordMD5, $i%32, 1))
       #                         -  $intMD5Total;
       # $intMD5Total = evalCrossTotal(substr(md5(substr($strString,0,$i+1)), 0, 16)
      #                          .  substr(md5($intMD5Total), 0, 16)); #returns substring of hash value of string from 0 to 16 characters. 
    #}
    #return implode(' ' , $arrEncryptedValues); //returns string from array with seperator

#This is the encrypted text:

#-161 -179 -156 -183 -207 -161 -180 -174 -149 -165 -158 -183 -109 -173 -190 -174 -134 -175 -154 -284 -192 -132 -232 -189 -151 -180 -119 -163 -114 -201 -107 -201 -155 -108 -204 -192 -144 -262 -152 -223 -131 -218 -180 -176 -174 -156 -201 -158 -104 -179 -172 -222 -148 -189 -151 -196 -199 -207 -216 -174 -218 -165 -133 -187 -181 -156 -169 -209 -142 -174 -122 -200 -197 -167 -174-187 -160 -160 -182 -265 -118 -178 -121 -187 -169 -122 -149 -179 -151 -123 -145 -192 -140 -174 -176 -218 -180 -152 -190 -192

serials = open("serials.txt", "r")
seriallist = serials.readlines()
serials.close

password = 'password'

password = 
