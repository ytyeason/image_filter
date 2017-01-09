#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
import ctypes
import os, sys


libc = ctypes.cdll.LoadLibrary("libfast_filter.so")

size = len(sys.argv)

if(sys.argv[1] == "undo") and size ==2:
    result = open("result.pickle",'rb')
    #input
    list2 = []
    while True:
        try:
            list = list2
            list2 = pickle.load(result)
        except EOFError:
            break
    position2 = list[len(list)-1]#track the position

    if position2 != 1:
        position = position2 -1

        del list[len(list)-1]
        list.append(position)
        result = open("result.pickle",'ab')
        pickle.dump(list, result)

        input_image_data = list[position-1]
        output_image_data = ' ' * len(input_image_data)
        output_image_path = open("result.bmp",'wb')
        output_image_path.write(input_image_data)
    else:
        print "unable to undo"
elif(sys.argv[1] == "redo") and size == 2:
    result = open("result.pickle",'rb')
    #input
    list2 = []
    while True:
        try:
            list = list2
            list2 = pickle.load(result)
        except EOFError:
            break
    position2 = list[len(list)-1]#track the position

    if position2 != len(list)-1:
        position = position2 +1
        
        del list[len(list)-1]
        list.append(position)
        result = open("result.pickle",'ab')
        pickle.dump(list, result)
        
        input_image_data = list[position-1]
        output_image_data = ' ' * len(input_image_data)
        output_image_path = open("result.bmp",'wb')
        output_image_path.write(input_image_data)
    else:
        print "unable to redo"

elif(sys.argv[1] == "load") and size == 3:
    
    result = open("result.pickle",'wb')
    input_image_path = open(sys.argv[2],'rb')
    input_image_data = input_image_path.read()

    output_image_data = ' ' * len(input_image_data)
    output_image_path = open("result.bmp",'wb')
    output_image_path.write(input_image_data)
    #add file
    pickle_list = [input_image_data,1]
    pickle.dump(pickle_list, result)
        
    output_image_path.close()
    input_image_path.close()


elif(sys.argv[1] == "filter") and size > 3:
    if(sys.argv[1] == "filter"):
        result = open("result.pickle",'rb')
        #input
        list2 = []
        while True:
            try:
                list = list2
                list2 = pickle.load(result)
            except EOFError:
                break
    
        position = list[len(list)-1]#track the position
        if position!= len(list)-1 :
            del list[position:len(list)]
            input_image_data = list[len(list)-1]
        else:
            del list[len(list)-1]
            input_image_data = list[len(list)-1]
        
        #width
        width = int(sys.argv[2])
        #weights
        weights = []
        for arg in sys.argv[3:]:
            weights.append(float(arg))
        c = ctypes.c_float * len(weights)
        d = c( *weights )
        #output
        output_image_data = ' ' * len(input_image_data)
        output_image_path = open("result.bmp",'wb')

        libc.doFiltering(ctypes.c_char_p(input_image_data), d, ctypes.c_int(width), ctypes.c_char_p(output_image_data))
            
        output_image_path.write(output_image_data)
        output_image_path.close()

        result = open("result.pickle",'ab')
        list.append(output_image_data)
        list.append(position+1)
        pickle.dump(list, result)
else:
    print "please enter right argument"

