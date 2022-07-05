from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import traceback
from functions import delete_main, SamplingProcess,firstPassageTd,PrepareInput,secondPassageTd,samplingInputData

#Get Input file function
def getInputDataPath():
    inputSourceFilePath = filedialog.askopenfilename(initialdir = "/home", title = "Select a Input Data File", filetypes = [('Excel Files', ('*.xlsx'))])
    if inputSourceFilePath and  inputSourceFilePath.endswith(".xlsx") :
        inputSourceFile.set(inputSourceFilePath)
    else:
        messagebox.showerror("Error","Select a valid input data file")

#Get Output file function
def getOutputFilePath():
    outputSourceFilePath = filedialog.askopenfilename(initialdir = "/home", title = "Select a Output File", filetypes = [('Excel Files', ('*.xlsx'))])
    if outputSourceFilePath and  outputSourceFilePath.endswith(".xlsx") :
        outputSourceFile.set(outputSourceFilePath)
    else:
        messagebox.showerror("Error","Select a valid Output file")

def startProcess():
    passageArray01 = inputPassage(passage_1_1.get(),passage_1_2.get(),passage_1_3.get(),passage_1_4.get(),passage_1_5.get())
    passageArray02 = inputPassage(passage_2_1.get(),passage_2_2.get(),passage_2_3.get(),passage_2_4.get(),passage_2_5.get())
    inputSeqArray = inputSeq(input_seq_1.get(),input_seq_2.get(),input_seq_3.get(),input_seq_4.get(),input_seq_5.get(),input_seq_6.get())
    inputSeqArray02 = inputSeq(input_seq_1.get(),input_seq_2.get(),input_seq_3.get(),input_seq_4.get(),input_seq_5.get(),input_seq_6.get())

    percentage = percent_input_box.get()
    clusters = cluster_input_box.get()
    dataLen = 15

    input_source_file_path = inputSourceFile.get()
    output_file_path = outputSourceFile.get()
    if not input_source_file_path:
        messagebox.showerror("Error", "Select a valid excel file")
    elif not output_file_path:
        messagebox.showerror("Error", "Select a valid excel file")
    else:        
        try:
            if((percentage != "" and clusters != "") and (len(inputSeqArray) == 0 and (len(passageArray01) == 0 or len(passageArray02) == 0))):
                percentage = int(percent_input_box.get())
                clusters = int(cluster_input_box.get())
                SamplingProcess(input_source_file_path,output_file_path,percentage,clusters)
                messagebox.showinfo("Success", "The output file generated")
            elif((percentage == "" and clusters == "") and (len(inputSeqArray) > 0 and (len(passageArray01) > 0 or len(passageArray02) > 0))):
                print("Sampling step skipped....")
                print("Trim dowm step processed...")
                if(len(passageArray01) == 0 and len(passageArray02) > 0):
                    print("1st passage skipped....")
                    print("2nd passage proccessed....")
                    data = PrepareInput(input_source_file_path)
                    secondPassageTd(data,passageArray02,dataLen,inputSeqArray02,output_file_path)
                    messagebox.showinfo("Success", "The output file generated")
                elif(len(passageArray02) == 0 and len(passageArray01) > 0):
                    print("2nd passage skipped....")
                    print("1st passage proccessed....")
                    data = PrepareInput(input_source_file_path)
                    firstPassageTd(data,passageArray01,passageArray02,dataLen,inputSeqArray,inputSeqArray02,output_file_path)
                    messagebox.showinfo("Success", "The output file generated")
                else:
                    print("1st passage proccessed....")
                    print("2nd passage proccessed....")
                    data = PrepareInput(input_source_file_path)
                    firstPassageTd(data,passageArray01,passageArray02,dataLen,inputSeqArray,inputSeqArray02,output_file_path)
                    messagebox.showinfo("Success", "The output file generated")
            elif((percentage != "" and clusters != "") and (len(inputSeqArray) > 0 and (len(passageArray01) > 0 or len(passageArray02) > 0))):
                print("Sampling step proccessed....")
                print("Trim dowm step proccessed...")
                output = samplingInputData(input_source_file_path,percentage,clusters)
                output = pd.DataFrame(output)
                if(len(passageArray01) == 0 and len(passageArray02) > 0):
                    print("1st passage skipped....")
                    print("2nd passage proccessed....")
                    secondPassageTd(output,passageArray02,dataLen,inputSeqArray02,output_file_path)
                    messagebox.showinfo("Success", "The output file generated")
                elif(len(passageArray02) == 0 and len(passageArray01) > 0):
                    print("2nd passage skipped....")
                    print("1st passage proccessed....")
                    firstPassageTd(output,passageArray01,passageArray02,dataLen,inputSeqArray,inputSeqArray02,output_file_path)
                    messagebox.showinfo("Success", "The output file generated")
                else:
                    print("1st passage proccessed....")
                    print("2nd passage proccessed....")
                    firstPassageTd(output,passageArray01,passageArray02,dataLen,inputSeqArray,inputSeqArray02,output_file_path)
                    messagebox.showinfo("Success", "The output file generated")
            else:
                print("Sampling step skipped....")
                print("Trim dowm step skipped...")
                print("No output file generated..")

        except:
            print("Error generated, please check error.txt for more information...")
            with open('error.txt', 'w') as fh:
                traceback.print_exc(file=fh)
            messagebox.showerror("Error", "Something went wrong. Please try again")

def deleteProcess():
    outputFilePath = outputSourceFile.get()
    if not outputFilePath:
        messagebox.showerror("Error","Select a valid Output file")
    else:        
        try:
            delete_main(outputFilePath)
            messagebox.showinfo("Success","The file is clean.")            
        except:
            #messagebox.showerror("Error","Please check error.txt for more information...")
            with open('error.txt', 'w') as fh:
                    traceback.print_exc(file=fh)
            messagebox.showerror("Error","Something went wrong. Please try again")
  
def inputPassage(val1,val2,val3,val4,val5):
    passageArray =[]
    if val1:
        passageArray.append(val1)   
    if val2: 
        passageArray.append(val2)    
    if val3:
        passageArray.append(val3)    
    if val4:
        passageArray.append(val4)    
    if val5:
        passageArray.append(val5)

    return passageArray

def inputSeq(val1,val2,val3,val4,val5,val6):
    inputSeqArray =[]
    if val1:
        inputSeqArray.append(val1)   
    if val2: 
        inputSeqArray.append(val2)    
    if val3:
        inputSeqArray.append(val3)    
    if val4:
        inputSeqArray.append(val4)    
    if val5:
        inputSeqArray.append(val5)
    if val6:
        inputSeqArray.append(val6)

    return inputSeqArray

#Create GUI Object
window = Tk()
window.geometry('590x360')
window.resizable(False,False)
window.title('Data Processor')

#Define Variable
inputSourceFile = StringVar()
outputSourceFile = StringVar()


MAIN_IMAGE = PhotoImage(file="image/data_analysis.png")
INPUT_SOURCE_ICON_BTN = PhotoImage(file="image/inbox.png")
INPUT_SOURCE_BTN = PhotoImage(file="image/input.png")
OUTPUT_SOURCE_ICON_BTN = PhotoImage(file="image/outbox.png")
OUTPUT_SOURCE_BTN = PhotoImage(file="image/output.png")
DELETE_BTN = PhotoImage(file="image/delete.png")
RUN_BTN = PhotoImage(file="image/run.png")
main_label = Label(window,image=MAIN_IMAGE)
main_label.place(x=170,y=10)

# Input Output File Section
input_source_label = Label(window, text="Input Data:", font=('bold',12))
input_source_label.place(x=10, y=75)

input_source_icon_btn = Button(window, image=INPUT_SOURCE_ICON_BTN,command=getInputDataPath)
input_source_icon_btn.place(x=95,y=70)

inputData = Entry(window, textvariable=inputSourceFile,font=('',15),width=28)
inputData.place(x=140,y=75)
input_source_btn = Button(window, image=INPUT_SOURCE_BTN,command=getInputDataPath)
input_source_btn.place(x=470,y=75)

#Output Section
output_source_label = Label(window, text="Output File:",font=('bold',12))
output_source_label.place(x=10, y=115)

output_source_icon_btn = Button(window, image=OUTPUT_SOURCE_ICON_BTN,command=getOutputFilePath)
output_source_icon_btn.place(x=95,y=110)

outputData = Entry(window, textvariable=outputSourceFile,font=('',15), width=28)
outputData.place(x=140,y=110)

output_source_btn = Button(window, image=OUTPUT_SOURCE_BTN,command=getOutputFilePath)
output_source_btn.place(x=470,y=110)

#Step 1
step_one_label = Label(window,text="Step 1: Sampling",font=('bold',12))
step_one_label.place(x=10,y=150)
delete_btn = Button(window, image=DELETE_BTN, command=deleteProcess)
delete_btn.place(x=470,y=145)

#######
percent_label = Label(window,text="Percentage:",font=('bold',12))
percent_label.place(x=10,y=180)

percent_input_box = Entry(window, width=4,font=('',15))
percent_input_box.place(x=105,y=180)

cluster_label = Label(window,text="Cluster:",font=('bold',12))
cluster_label.place(x=160,y=180)

cluster_input_box = Entry(window, width=4,font=('',15))
cluster_input_box.place(x=220,y=180)

all_empty_label = Label(window,text="Skip if all empty",font=('bold',12))
all_empty_label.place(x=280,y=180)

run_btn = Button(window, image=RUN_BTN,command=startProcess)
run_btn.place(x=470,y=180)



#Step 2
step_two_label = Label(window,text="Step 2: Trim down",font=('bold',12))
step_two_label.place(x=10,y=220)
delete_set_seq_label = Label(window,text="Delete set if all present",font=('',12))
delete_set_seq_label.place(x=280,y=220)

input_seq_label = Label(window,text="Input Sequence",font=('',12))
input_seq_label.place(x=10,y=240)

input_seq_label = Label(window,text="(3~5)-skip if all empty",font=('',12))
input_seq_label.place(x=280,y=240)

input_seq_1 = Entry(window, width=3,font=('',15))
input_seq_2 = Entry(window, width=3,font=('',15))
input_seq_3 = Entry(window, width=3,font=('',15))
input_seq_4 = Entry(window, width=3,font=('',15))
input_seq_5 = Entry(window, width=3,font=('',15))
input_seq_6 = Entry(window, width=3,font=('',15))
input_seq_1.place(x=10,y=270)
input_seq_2.place(x=50,y=270)
input_seq_3.place(x=90,y=270)
input_seq_4.place(x=130,y=270)
input_seq_5.place(x=170,y=270)
input_seq_6.place(x=210,y=270)

passage_1_1 = Entry(window, width=3,font=('',15))
passage_1_2 = Entry(window, width=3,font=('',15))
passage_1_3 = Entry(window, width=3,font=('',15))
passage_1_4 = Entry(window, width=3,font=('',15))
passage_1_5 = Entry(window, width=3,font=('',15))

passage_1_1.place(x=280,y=270)
passage_1_2.place(x=320,y=270)
passage_1_3.place(x=360,y=270)
passage_1_4.place(x=400,y=270)
passage_1_5.place(x=440,y=270)

passage_1_Label = Label(window,text="1st passage",font=('',12))
passage_1_Label.place(x=480,y=270)

passage_2_1 = Entry(window, width=3,font=('',15))
passage_2_2 = Entry(window, width=3,font=('',15))
passage_2_3 = Entry(window, width=3,font=('',15))
passage_2_4 = Entry(window, width=3,font=('',15))
passage_2_5 = Entry(window, width=3,font=('',15))

passage_2_1.place(x=280,y=300)
passage_2_2.place(x=320,y=300)
passage_2_3.place(x=360,y=300)
passage_2_4.place(x=400,y=300)
passage_2_5.place(x=440,y=300)

passage_2_Label = Label(window,text="2nd passage",font=('',12))
passage_2_Label.place(x=480,y=300)

#Start Program
window.mainloop()