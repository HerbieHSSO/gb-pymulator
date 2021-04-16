#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Documentation source:
# - https://gbdev.gg8.se/wiki/articles/Sound_Controller

import simpleaudio as sa
import threading
import numpy as np
import array
class SoundDriver():

    TICKS_PER_SEC = 4000000
    BUFFER_SIZE = int(22050 * 0.4)
    
    #BUFFER_SIZE = 220

    def __init__(self):
        self.sample_rate = 22050
        self.buffer = np.array([0]*SoundDriver.BUFFER_SIZE)
        self.ticks = 0
        self.div = SoundDriver.TICKS_PER_SEC // (self.sample_rate )
        self.i = 0
        self.play_obj = None
        self.has_sound = False
        
    
    def play(self, left, right, ticks):
        
        self.ticks += ticks
        #if self.ticks <= self.div:
            #return
            
        self.ticks = 0

        if left:
            self.has_sound = True
        self.i += 2
        self.buffer[self.i] = left
        self.i += 2
        self.buffer[self.i+1] = right
        
        
        #if self.i >= SoundDriver.BUFFER_SIZE:
            #if self.has_sound:
        threading.Thread(target=self.play_sound, args=(self.buffer,)).start()
            #self.i = 0
        self.has_sound = False

    def stop(self):
        self.buffer = np.array([0]*4096, dtype=np.float32)
        if self.play_obj is not None:
            try:
                self.play_obj.stop()
            except:
                pass

    def play_sound(self,wave):
        try:
            wave_obj = sa.WaveObject(wave,2,1,self.sample_rate)
            #while self.play_obj and self.play_obj.is_playing():
                #pass
            self.play_obj = wave_obj.play()
        except:
            pass
