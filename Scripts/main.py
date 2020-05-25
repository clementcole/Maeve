#! python3
import tkinter as tk
from tkinter import Tk, Label, Canvas, Button, SEPARATOR, filedialog as fd
from tkinter import ttk
from tkinter.ttk import *
#! python3
import time
import csv
import re
import pandas as pd
import numpy as np
from past.builtins import xrange
from functools import reduce


dictKeys_1 = {
                "processed" : "processed",
                "message_id":"message_id",
                "event":"event",
                "api_key_id":"api_key_id",
                "recv_message_id":"recv_message_id",
                "credential_id":"credential_id",
                "subject":"subject",
                "from":"from",
                "email":"email",
                "asm_group_id":"asm_group_id",
                "template_id":"template_id",
                "originating_ip":"originating_ip",
                "reason":"reason",
                "outbound_ip":"outbound_ip",
                "outbound_ip_type":"outbound_ip_type",
                "mx":"mx",
                "attempt":"attempt",
                "url":"url",
                "user_agent":"user_agent",
                "type":"type",
                "is_unique":"is_unique",
                "username":"username",
                "categories":"categories",
                "marketing_campaign_id":"marketing_campaign_id",
                "marketing_campaign_name":"marketing_campaign_name",
                "marketing_campaign_split_id":"marketing_campaign_split_id",
                "marketing_campaign_version":"marketing_campaign_version",
                "unique_args":"unique_args"
        }

dictKey_2 = {
                "email":"email",
                "expiry":"expiry",
                "email_disabled":"email_disabled",
                "stripe_connected_customer_id":"stripe_connected_customer_id",
                "type":"type"
            }

class MainGUI(object):
    pathToCSVOneFile = "Path to CSV File 1"
    pathToCSVTwoFile = "Path to CSV File 2"
    pathToCSVFileOutput = "Path To CSV File output"
    colorCodes = {
                    "isa_info" : "#45cea2", #Shamrock
                    "isa_success" : "#80ff00", #Emerald
                    "isa_warning" : "#FEEFB3",
                    "isa_error" : "#D8000C"
                  }
    fonts = {
                    "isa_info" : ('Calibri',11,'italic'),
                    "isa_success" : ('Calibri',11,'bold italic'),
                    "isa_warning" : ('Calibri',11,'bold italic'),
                    "isa_error" : ('Calibri',11,'bold italic')
            }
    ArbSelectMap = {}
    TruthFilterDictMap = {}
    currentOffset = 0
    prompter = " >_ : "
    def __init__(self, master):
        self.master = master
        self.master.title("Historicly Process CSV Files")
        self.master.configure(background='#1f1f1f')
        # self.pack(fill=BOTH, expand=1)
        s = ttk.Style()
        #self.HorizontalPanelLine = ttk.Separator(root).place(x=0, y=250, relwidth=1)
        self.HorizontalPanelLine = ttk.Separator(self.master).place(x=0, y=250, relwidth=1)
        self.canvasWidth, self.canvasHeight = 50, 0
        self.canvasTextWidth, self.canvasTextHeight = 500, 500
        #self.OutputTextTerminal = Canvas(root, bg="#000000", width=500, height=1000)
        self.OutputTextTerminal = Canvas(self.master, bg="#000000", width=500, height=1000)
        self.OutputTextTerminal.place(x=0, y=255, relwidth=1)
        global bt_GetCSVFile1, bt_GetCSVFile2, bt_Filter, bt_GetTruthFile, bt_GetOutputFile, bt_FilterNames, current_Action, rd_TruthProcessingMode
        #Define modes for running TruthProcessing

        # Create a style object
        styleFilter = Style()
        styleGetFilePath = Style()

        # This will be adding style, and
        # naming that style variable as
        # W.Tbutton (TButton is used for ttk.Button).
        styleFilter.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), background = 'red', foreground='black')
        styleGetFilePath.configure('G.TButton', font=('calibri', 10, 'bold', 'underline'), background = 'green', foreground='red')

        current_Action = tk.Label(self.master, text="⬅", borderwidth=0.1, relief="groove", fg="#00ff00", bg="#4c4c4c")

        bt_GetCSVFile1 = Button(self.master, text="Get Members CSV File 1", width=40, command=self.GetCSVFileOne) #1  # .grid(row=0, column=1,  pady=5)
        bt_GetCSVFile2 = Button(self.master, text="Get Members CSV File 2", width=40, state="disabled", command=self.GetCSVFileTwo) #2
        bt_Filter = Button(self.master, text="Filter",  style = 'W.TButton', state="disabled",  command=self.Fitler) #3

        #bt_GetTruthFile = Button(self.master, text="Get Truth File", width=40, state="disabled", command=self.SetTruthFilePath) #3
        #bt_GetOutputFile = Button(self.master, text="Set Output File Path Location", width=40, state="disabled", command=self.SetOutputFilePath) #4
        #bt_FilterNames = Button(self.master, text="Run Truth",  style = 'W.TButton', state="disabled", command=self.FilterNames) #5

        bt_GetCSVFile1.grid(row=0, column=0, padx=5, pady=5)
        bt_GetCSVFile2.grid(row=1, column=0, padx=5,  pady=5)
        bt_Filter.grid(row=2, column=0, padx=5, pady=5)

    def GetCSVFileOne(self):
        self.pathToCSVOneFile = fd.askopenfilename()
        self.OutputTextTerminal.create_text(0,
                                            self.currentOffset,
                                            fill=self.colorCodes["isa_info"],
                                            font=self.fonts["isa_info"],
                                            text=self.prompter +" Path to CSV File 1 : " + self.pathToCSVOneFile,
                                            anchor='nw',
                                            state="normal")
        self.ResetLineOffset(20)
        self.OutputTextTerminal.create_text(0,
                                            self.currentOffset,
                                            fill=self.colorCodes["isa_success"],
                                            font=self.fonts["isa_success"],
                                            text=self.prompter + "CLICK  ➡  [Select Directory of CSV File 2]",
                                            anchor='nw',
                                            state="normal")
        self.ResetLineOffset(20)
        bt_GetCSVFile2["state"] = "normal"
        bt_GetCSVFile1["state"] = "disabled"
        current_Action.grid(row=1, column=1, padx=5, pady=5)


    def GetCSVFileTwo(self):
        self.pathToCSVTwoFile = fd.askopenfilename()
        #self.TruthFilterDictMap = self.GetCSVFile2(self.pathToTruthFilePath)
        self.OutputTextTerminal.create_text(0,
                                            self.currentOffset,
                                            fill=self.colorCodes["isa_info"],
                                            font=self.fonts["isa_info"],
                                            text=self.prompter + " Path to Second CSV File : " + self.pathToCSVTwoFile,
                                            anchor='nw',
                                            state="normal")
        self.ResetLineOffset(20)
        bt_GetCSVFile2["state"] = "disabled"
        bt_Filter["state"]= "normal"
        current_Action.grid(row=2, column=2, padx=5, pady=5)


    def Fitler(self):
        self.filter(self.pathToCSVOneFile, self.pathToCSVTwoFile)
        self.OutputTextTerminal.create_text( 0,
                                            self.currentOffset,
                                            fill=self.colorCodes["isa_info"],
                                            font=self.fonts["isa_info"],
                                            text= self.prompter +  "SUCCESS!!! Creation of ArbSelect File complete" + ('\U0001f44d') +  ('\U0001f44d') + ('\U0001f44d') ,
                                            anchor='nw',
                                             state="normal")
        self.ResetLineOffset(20)
        self.OutputTextTerminal.create_text(0,
                                            self.currentOffset,
                                            fill=self.colorCodes["isa_success"],
                                            font=self.fonts["isa_success"],
                                            text= self.prompter + "CLICK  ➡  [Get Truth File Location]",
                                            anchor='nw',
                                            state="normal")
        self.ResetLineOffset(20)
        bt_Filter["state"] = "disabled"
        bt_GetCSVFile1["state"] = "normal"
        current_Action.grid(row=3, column=2, padx=5, pady=5)

    def filter(self, csvone, csvtwo):
        allsubs = pd.read_csv(csvone)
        subswithInvites = pd.read_csv(csvtwo)
        subswithInvites[dictKeys_1["email"]] = subswithInvites[dictKeys_1["email"]].str.lower()
        allsubs[dictKeys_1["email"]] = allsubs[dictKeys_1["email"]].str.lower()
        subswithInvitesMod = subswithInvites.apply(lambda x: x.astype(str).str.lower()).drop_duplicates(subset=[dictKeys_1["email"]], keep='first')
        allsubsMod = allsubs.apply(lambda x: x.astype(str).str.lower()).drop_duplicates(subset=[dictKeys_1["email"]], keep='first')
        subswithInvitesMod.replace('nan', '', inplace=True)
        allsubsMod.replace('nan', '', inplace=True)
        #subswithInvitesMod.to_csv("C:\\Code\\ProcessedCSVs\\output\\allsubs.csv",mode='w', index=False)
        #allsubsMod.to_csv("C:\\Code\\ProcessedCSVs\\output\\subswithinvite.csv", mode='w', index=False)
        emaillistSubsWithInvites = subswithInvitesMod[dictKeys_1["email"]].values.tolist() #Get list of emails from subswith invites to discord
        emaillistSubsWithInvites = list(set(emaillistSubsWithInvites))
        emaillistAllSubs = allsubsMod[dictKeys_1["email"]].values.tolist() #Get list of emails from subswith invites to discord
        emaillistAllSubs = list(set(emaillistAllSubs))
        #subscribersDF = allsubs[allsubs[dictKeys_1["email"]].isin(list_of_emails)] #Contains
        #nonSubscribersDF = allsubs[~allsubs[dictKeys_1["email"]].isin(list_of_emails)] #Difference
        #for item in list_of_emails:
        #    item.lower()
        #subs_in_invite_but_not_in_subscribers = allsubsMod[~allsubsMod[dictKeys_1["email"]].isin(list_of_emails)] #Difference
        #subs_in_invite_but__in_subscribers = allsubsMod[allsubsMod[dictKeys_1["email"]].isin(list_of_emails)]

        #print(list_of_emails)
        #print(len(list_of_emails))
        #subscribersDF.to_csv("C:\\Code\\ProcessedCSVs\\subscriberstest1.csv",mode='w', index=True)
        #subs_in_invite_but_not_in_subscribers.replace('nan', '', inplace=True)
        #subs_in_invite_but__in_subscribers.replace('nan', '', inplace=True)
        #subs_in_invite_but_not_in_subscribers.to_csv("C:\\Code\\ProcessedCSVs\\output\\nonSubscribers1.csv",mode='w', index=False)
        difference = self.list_diff(emaillistAllSubs,emaillistSubsWithInvites)
        with open('C:\\Code\\ProcessedCSVs\\emaillistSubsWithInvites.txt', 'w') as filehandle:
            for listitem in emaillistSubsWithInvites:
                filehandle.write('%s\n' % listitem)
        with open('C:\\Code\\ProcessedCSVs\\emaillistAllSubs.txt', 'w') as filehandle:
            for listitem in emaillistAllSubs:
                filehandle.write('%s\n' % listitem)
        with open('C:\\Code\\ProcessedCSVs\\emailList.txt', 'w') as filehandle:
            for listitem in difference:
                filehandle.write('%s\n' % listitem)

        #return dictFrameCSV

    def list_diff(self, list1, list2):
        return (list(set(list1) - set(list2)))

    def ResetLineOffset(self, number):
        self.currentOffset = self.currentOffset + number

    #def ReadCSV(self):
def main():
    root = Tk()
    root.geometry("700x500")
    mainEntry = MainGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()