from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c or extract e? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):

                
                
                self.name = "Author: Jurijus pacalovas"

                print(self.name)
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                        
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    long=len(name)

                    

                    
                    
                   
                    
                    Deep_long=120
                    Deep_long_All=Deep_long*15
                    block_size_long=15
                    Times_compression=1
                    	
                    nameas=name+".bin"
                
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        import brotlicffi
                        data=brotlicffi.compress(data)
                        data1=data
                        size_after2=len(data)
                        #print(size_after2)
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                     
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)

                                
                                    
                                
                                size_data3=size_data2
                                long_file=len(size_data3)
                                size_data10=""
                                size_data9=""
                                size_data5=""
                                fda5=""
                                size_data4=""
                                size_data6=""
                                size_data7=""
                                size_data12=""
                                size_data19=""
                                size_data10=size_data3
                           
                                
                                long_block=16
                               
                               
                                
                                
                                times_of_times=0
                           
                                str_find=""
                          
                                

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                  
                                    long2=len(size_data3)
                                    Deep=long2//28
                                    times2=Deep
                                    long_block=block_size_long
                               
                                    before_block=0
                                    check_size_block=0
                                    before_block_After_check=0


                                    size_data_not_compress=size_data3
                                    #print(size_data_not_compress)
                                    
                                
                                    Times6=0
                                    
                                   
                                    
                                  
                                    
                                    Find_guess=0
                                    while Find_guess!=1:
                                        
                                        while  times_of_times!=Times_compression:


                                                    
                                                   
                                                    long_block=block_size_long
                                                    long2=len(size_data3)
                                                    
                                                    
                                                       
                                                     
                                  
                                                 
                                                
                                                    blocks=long_block
                                                    size_compress=63
                                                 
                                                    
                                                     
                                                    block=0

                                                    #b=format(predict,'04b')
                                                    #predict=predict+1
                                                    #if predict==16:
                                                        #predict=0
                                                    
                                                    
                                                        
                                                        
                                                    
                                                    
                                                   

                                                    

                                                   
  
                                                    
                                                    long=len(size_data3)
                                                    #print(long)
                                                    
                                                    while block<long:

                                                                                Times6=Times6+1
                                                                                Zeroes=size_data3[block:block+blocks]
                                                                                size_of_block=len(Zeroes)
                                                                                #print(size_of_block)

                                                                                Zeroes_number=int(Zeroes,2)

                                                                                

                                                                                size_data24=bin(Zeroes_number)[2:]
                                                                                
                                                                                lenf=len(size_data24)
                                                                                if lenf>long_block:
                                                                                    print("File too big")
                                                                                    raise SystemExit
                                                                                                                                        
                                                                                                                                        
                                                                                                                                    
                                                                                add_bits118=""
                                                                                count_bits=long_block-lenf%long_block
                                                                                z=0
                                                                                
                                                                                if count_bits!=long_block:
                                                                                        while z<count_bits:
                                                                                            add_bits118="0"+add_bits118
                                                                                            z=z+1
                                                                                                                                                                
                                                                                MAX_zeroes=bin(long_block)[2:]
                                                                                Size_max_zeroes=len(MAX_zeroes)
                                                                                
                                                                                lenf=len(add_bits118)
                                                                                size_data26=bin(lenf)[2:]
                                                                                lenf=len(size_data26)
                                                                                if lenf>Size_max_zeroes:
                                                                                    print("File too big")
                                                                                    raise SystemExit
                                                                                                                                        
                                                                                                                                        
                                                                                                                                    
                                                                                add_bits118=""
                                                                                count_bits=Size_max_zeroes-lenf%Size_max_zeroes
                                                                                z=0
                                                                               
                                                                                if count_bits!=Size_max_zeroes:
                                                                                        while z<count_bits:
                                                                                            add_bits118="0"+add_bits118
                                                                                            z=z+1
                                                                                                                                                                
                                                                                                                                                                            
                                                                                size_data7=add_bits118+size_data26+size_data24

                                                                                size_after_block=len(size_data7)
                                                                                #print(size_after_block)


                                                                                if Times6>=Deep_long or size_of_block!=long_block or  len(data)<=Deep_long_All:
                                                                                    size_data4=Zeroes

                                                                                elif size_of_block<=size_after_block+1 and Times6<Deep_long and size_of_block==long_block:
                                                                                    size_data4="0"+Zeroes
                                                                                    
                                                                                elif size_of_block>size_after_block+1 and Times6<=Deep_long and size_of_block==long_block:
                                                                                    size_data4="1"+size_data7
                                                                                    
                                                                                
                                                                                size_data6=size_data6+size_data4       
                                                                                block=block+blocks
                                                                                #print(block)
                                                         
                                                    times_compression=times_compression+1
                                                    
                                                    #print(times_compression)
                                                    
                                                    
                                                    size_data3=size_data6
                                                    
                                                    Where4=0
                                                    
                                                    
                                                    #print(len(size_data6))
                                                    size_data6=""
                                                    times_of_times=times_of_times+1
                                                    
                                        long_after=len(size_data3)
                                        long2=len(size_data3)

                                        
                                        size_data9=size_data3
                                        
                                           

                                        
                                        long_file=len(size_data10)
                                        long_after=len(size_data9)
                                        #print(long_after) 
                                       
                                        if long_file>long_after or long_block<=long_after:
                                           
                                            size_data11=size_data9
                                            Find_guess=1

                                    
                                            
                                    
                                        
                                        
       
                                    
                                    size_data11="1"+size_data11
                                    
                                    
                           
                                    lenf=len(size_data11)
                                        
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                    
                                    if count_bits!=8:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                    size_data11=add_bits118+size_data11
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    n = int(size_data11, 2)
                                
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    
                                    
                                    data2=jl

                                    if len(data2)<len(data1):
                                        jl=b'\x00'+data2
                                       


                                    elif len(data1)<len(data2):
                                        jl=b'\xff'+data1
                                        
                                
                                    size_after=len(jl)
                                    #print(size_after)
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:

                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                  
                    
                    long=len(nameas)

                    
                    
                    
                    
                    Deep_long=120
                    Deep_long_All=Deep_long*15
                    block_size_long=15
                    Times_compression=1
                    	
                    
                    
                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data3 = binary_file.read()

                        data=data3[1:]

                        
                        
                        if data3[0:1]==b'\xff':
                        	import brotlicffi
                        	data= brotlicffi.decompress(data)
                        data1=data

                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    size_data3=size_data2
                                    if size_data3[0:9]=="000000001":
                                        size_data3=size_data3[9:]
                                    elif size_data3[0:8]=="00000001":
                                        size_data3=size_data3[8:]
                                    elif size_data3[0:7]=="0000001":
                                        size_data3=size_data3[7:]
                                    elif size_data3[0:6]=="000001":
                                        size_data3=size_data3[6:]
                                    elif size_data3[0:5]=="00001":
                                        size_data3=size_data3[5:]
                                    elif size_data3[0:4]=="0001":
                                        size_data3=size_data3[4:]
                                    elif size_data3[0:3]=="001":
                                        size_data3=size_data3[3:]
                                    elif size_data3[0:2]=="01":
                                        size_data3=size_data3[2:]
                                    elif size_data3[0:1]=="1":
                                        size_data3=size_data3[1:]


                                    times_compression=0  
                                 
                                    long2=len(size_data3)
                                    Deep=long2//28
                                    times2=Deep
                                    long_block=1023
                                  
                                    before_block=0
                                    check_size_block=0
                                    before_block_After_check=0


                                    size_data_not_compress=size_data3
                                    times_of_times=0
                                    #print(size_data_not_compress)
                                    
                                
                                    
                                    
                                    block_compression2=0
                                    size_data6=""
                                    Times6=0
                                    
                                    start=-1
                                    Left_Right=0
                                    Find_guess=0
                                    times_of_times1=0
                                        
                                    while  times_of_times1!=Times_compression:

                                                    

                                                    
                                                   
                                                    long_block=block_size_long
                                                    #print(long_block)
                                                    start=0
                                                   
                                                    blocks=long_block
                                                    long2=len(size_data3)
                                                   
                                                    size_compress=63
                                                    end=blocks
                                                    
                                                     
                                                    block=0

                                                    #b=format(predict,'04b')
                                                    #predict=predict+1
                                                    #if predict==16:
                                                        #predict=0
                                                    
                                                    
                                                        
                                                        
                                                    
                                                    
                                                    Find=1

                                                    Left_Right=Left_Right+1

                                                    if Left_Right==2:
                                                        Left_Right=1
                                                    
                                                    long=len(size_data3)
                                                    #print(long)
                                                    block2=0
                                                    
                                                    
                                                    while block!=long:


                                                                                Times6=Times6+1
                                                                                block2=block
                                                                                

                                                                                Zeroes=size_data3[block:block+1]
                                                                                Zeroes2=size_data3[block+1:block+blocks+1]
                                                                                Zeroes5=size_data3[block:block+blocks]
                                                                                size_after2=len(Zeroes5)

                                                                                if Times6>=Deep_long or size_after2!=long_block or  len(data)<=Deep_long_All:
                                                                                    Zeroes4=size_data3[block:block+blocks]
                                                                                    size_after4=len(Zeroes4)
                                                                                    size_data4=Zeroes4

                                                                                    block=block+size_after4
                                                                                    
                                                                                elif Zeroes=="0" and size_after2==long_block and Times6<=Deep_long:
                                                                                    block=block+1
                                                                                    Zeroes3=size_data3[block:block+blocks]
                                                                                    size_after3=len(Zeroes3)
                                                                                    size_data4=Zeroes3
                                                                                    
                                                                                    block=block+size_after3
                                                                                    #print(len(size_data4))
                                                                                    
                                                                                    
                                                                                

                                                                                elif Zeroes=="1" and size_after2==long_block and Times6<=Deep_long:
                                                                                    block=block+1
                                                                                
                                                                                    size_of_block=len(Zeroes)
                                                                                    #print(size_of_block)

                                                                                    
                                                                                                                                                                    
                                                                                    MAX_zeroes=bin(long_block)[2:]
                                                                                    Size_max_zeroes=len(MAX_zeroes)

                                                                                    Times_extract_of_time_zeroes=""
                                                                                    
                                                                                    Times_extract_of_time_zeroes=size_data3[block:block+Size_max_zeroes]
                                                                                    #print(Times_extract_of_time_zeroes)
                                                                                    
                                                                                    times_of_times=int(Times_extract_of_time_zeroes,2)
                                                                                    

                                                                                    Forty_bits=long_block
                                                                                    Times_bits=Forty_bits-times_of_times
                                                                                    
                                                                                    block=block+Size_max_zeroes
                                                                                    
                                                                                    size_data8=size_data3[block:block+Times_bits]

                                                                                    size_data24=size_data8
                                                                                
                                                                                    lenf=len(size_data24)
                                                                                    if lenf>long_block:
                                                                                        #print(lenf)
                                                                                        print("File too big")
                                                                                        raise SystemExit
                                                                                                                                            
                                                                                                                                            
                                                                                                                                        
                                                                                    add_bits118=""
                                                                                    count_bits=long_block-lenf%long_block
                                                                                    z=0
                                                                                   
                                                                                    if count_bits!=long_block:
                                                                                            while z<count_bits:
                                                                                                add_bits118="0"+add_bits118
                                                                                                z=z+1

                                                                                                
                                    
                                                                                    
                                                                                    
                                                                                    size_data4=add_bits118+size_data8
                                                                                    
                                                                                    #print(len(size_data4))
                                                                                    #print(Times_bits3)
                                                                                    #print("T")
                                                                                    block=block+Times_bits
                                                                                size_data6=size_data6+size_data4
                                                                            
                                                                                
                                                                                if block2==block:
                                                                                    block=long
                                                                                #print(block)
                                                         
                                                    times_compression=times_compression+1
                                                    
                                                    #print(times_compression)
                                                    
                                                    
                                                    size_data3=size_data6
                                                    
                                                    Where4=0
                                                    
                                                    
                                                    #print(len(size_data6))
                                                    size_data6=""
                                                    times_of_times1=times_of_times1+1
                                                    
                                        
                                           
                                            
                                        
                                    long_after=len(size_data3)
                                    long2=len(size_data3)
                                        
                                    size_data9=size_data3

                                    size_data3=size_data9
                                    

                                       
                                    
                                        
                                     
                                    lenf=len(size_data3)
                                        
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                   
                                   
                                    if count_bits!=8:
                                               while z<count_bits:
                                                   add_bits118="0"+add_bits118
                                                   z=z+1
                                                                    
                                                                    
                                    size_data3=add_bits118+size_data3
                                      
                                    n = int(size_data3, 2)
                                    
                                    
                                    qqwslenf=len(size_data3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    if data3[0:1]==b'\x00':
                                    	import brotlicffi
                                    	jl= brotlicffi.decompress(jl)
                                   
                                    
                                    data2=jl

                                    if data3[0:1]==b'\xff':
                                        jl=data1


                                    elif data3[0:1]==b'\x00':
                                        jl=data2
                               
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

 
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
