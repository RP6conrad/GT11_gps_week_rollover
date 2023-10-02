import struct
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#file=open("M10.sbp","rb")
if __name__ == "__main__":
    YES = ("Y", "y", "YES,", "yes", "True")
    NO = ("N", "n", "NO,", "no", "False")
    filetypes = (
        ('sbp files', '*.sbp'),('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a ubx file',
        initialdir='/',
        filetypes=filetypes)

    new_file_name=filename.replace(".sbp","_new.sbp")
    file=open(filename,"rb")
    SBP_header=file.read(64)
    SBP_frame=file.read(32)
    bin_file=open(new_file_name, 'wb')
    bin_file.write(SBP_header)
    
    while SBP_frame:
        SBP_frame=file.read(32)
        #check for end of file !!!
        if len(SBP_frame)<32 :break
        #print(struct.unpack('bBhiiiiihhhbb',SBP_frame))
        SBP=struct.unpack('bBhiiiiihhhbb',SBP_frame)
        second=SBP[3]&63
        min=(SBP[3]>>6)&63
        hour=(SBP[3]>>12)&31
        day=(SBP[3]>>17)&31
        month=(SBP[3]>>22)%12
        year=int((SBP[3]>>22)/12+2000)
        dt = datetime(year, month,day, 0, 0)
        #print('Seconds since epoch:', dt.timestamp())
        # convert the timestamp to a datetime object in the local timezone
        # 1024 weeks = 619315200 seconds, but +1h ???
        new_date = datetime.fromtimestamp(dt.timestamp()+619311600)
        #print('New Date :',new_date)
        #print(new_date.day)
        #print(new_date.month)
        #print(new_date.year)
        SBP_list=list(SBP)
        #print(SBP_list)
        SBP_list[3]=(((new_date.year-2000)*12+new_date.month)<<22)+(new_date.day<<17)+(hour<<12)+(min<<6)+second
        SBP_new_frame=struct.pack('bBhiiiiihhhbb',SBP_list[0],SBP_list[1],SBP_list[2],SBP_list[3],SBP_list[4],SBP_list[5],SBP_list[6],SBP_list[7],SBP_list[8],SBP_list[9],SBP_list[10],SBP_list[11],SBP_list[12])
        bin_file.write(SBP_new_frame)

    bin_file.close()
    showinfo(
        title='Converted file : date + 1024 weeks !',
        message=new_file_name
    )