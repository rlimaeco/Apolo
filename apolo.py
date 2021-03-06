#!/usr/bin/env python
# coding: utf-8

import os, sys
from subprocess import call
import yad

class Apolo():
    """
    Rafael da Silva Lima - rafael.liverpool@gmail.com
    Este programa irá controlar suas músicas de acordo com suas necessidades,
    ainda há muito a fazer como reconhecimento de players existentes, sincronia 
    com API do Grooveshark e utilização de player cli , como moc por exemplo 
    Uso: basta executar o arquivo apolo.py

    YAD Presets:
    Interface ; 
        Qual Ouvir = 512
        Reproduzir = 0
        Parar = 256

    """
  
    interface = """
    yad --width 300 --on-top --center --entry --title "Apolo" \
              --image=stock_media-play           \
              --button="_Qual ouvir:2"                     \
              --button="gtk-media-play:0" --button="gtk-media-stop:1"    \
    """

    ask_interface = """
    yad --form --title='Pergunto-lhe..' --columns=3 --center \
            --text='Deseja parar outros tocadores?' --button='Não':1 --button='Sim':0
    """

    # def menu_apolo(resp):
    #     if resp == 0:
    #         print "Ligar música"
    #         call("clementine")
    #     if resp == 256:
    #         print "Desligar música"
    #         os.system("killall clementine")
    #     if resp == 512:
    #         print "Procurar música"
    #         os.system("java -jar GrooveDown.jar")


        
    #resp = os.system(interface)
    #print resp
    #menu_apolo(resp)

    # Parâmetros YAD
    # form(self,fields=None,align="left",columns=1,separator=None,iseparator=None,scroll=False)
    
    if yad.checkpython() and yad.checkyad(): 
        yad = yad.yad()
        yad.code()