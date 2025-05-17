import re
from xml.dom import minidom
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import json
import datetime

##### Created by Arindam Banerjee
##### email: arindam.banerjee.in@gmail.com
##### version 1.0


######### function dowork() which runs the program from tkinter gui modlue

def dowork():
    f = open(ldmval.get(), encoding="utf8")
    n = open(ndmval.get(), encoding="utf8")
    file = minidom.parse(f)
    nsm = minidom.parse(n)
    f.close()
    n.close()
    
######### Get the tags for domains, entities and attributes
    domains = file.getElementsByTagName('LogicalDataModel:AtomicDomain')
    entities = file.getElementsByTagName('LogicalDataModel:Entity')
    attrib = file.getElementsByTagName('attributes')
    
######### Initialize dictionaries to store informations

    domval = {} # Domain value storage
    lengt = {} # Length of attributes greater than 30 char
    ents = {} # List of Entitities and their definition
    attribs = {} # List of attributes and their data types
    desc = {}  # List of attributes with no descriptions
    newdesc =[] # Capture the list of attributes for which there is no description
    mydom = {}  # Capture the list of attributes where no domain value is used
    newdom =[]  # Display the list of attributes where no domain is used
    
######### Get Domain Information
    for domain in domains:
        #print(domain.attributes['name'].value, domain.attributes['baseType'].value)
        domval.update({domain.attributes['name'].value : domain.attributes['baseType'].value})
######### Get Entity Information
    for entity in entities:
        #print(entity.attributes['name'].value , entity.attributes['description'].value)
        ents.update({entity.attributes['name'].value : entity.attributes['description'].value})
    
######### Get attribute information  
    for attribute in attrib:
        #print(attribute.attributes['name'].value , attribute.attributes['dataType'].value)  
        attribs.update({attribute.attributes['name'].value : attribute.attributes['dataType'].value})

######### Get the attributes for which the length is greater than 30 characters
        def gt30():
            for attribute in attrib:
                if  len(attribute.attributes['name'].value) > 30:
            #print(attribute.attributes['name'].value, len(attribute.attributes['name'].value) )   
                    lengt.update({attribute.attributes['name'].value : len(attribute.attributes['name'].value)})
            return lengt    
                
######### Get the attributes for which no description is present     
        def nodesc():
            for attribute in attrib:
                desc.update({attribute.attributes['name'].value : attribute.hasAttribute('description')})
            
     # The Above code produces a dictionary of all attribites, with a tag of True or False, based on Tags
     # We need to take only those for which the tag value is False
        
            for key, value in desc.items():
                if value == False:
                    newdesc.append(key)
            return newdesc        
                
######### Get the attributes where no domains are used   
        def nodomain():
            for attribute in attrib:
            #print(attribute.attributes['name'].value , attribute.attributes['dataType'].value)  
                mydom.update({attribute.attributes['name'].value : attribute.attributes['dataType'].value})
           
     # Configure a list to hold only those attributes where there is no domain used
    
            for k, v in mydom.items():
                if len(v) <16:
                    newdom.append(k)  
            return newdom        
                
######### Adding an NDM file and comparing the attribute and glossary names for missing abbreviations


    nametag = nsm.getElementsByTagName('words')    

    # Create a dictionary to store the name and abbreviation pairs

    nsmdict = {}
    def noabbr():
        for nt in nametag:
            try:
                nsmdict.update({nt.attributes['name'].value:nt.attributes['abbreviation'].value})
                    
            except Exception as e:
                #print(f'error with {str(e)}')
                pass


    # Initialize an empty list to hold the name of attributes
        attrname = []

    # store the entity names in a list
        for attribute in attrib:
            attrname.append(attribute.attributes['name'].value)

## Split the names by camelcase

# Initialize an empty list to hold the split values

        splitattr = []

        for attr in attrname:
            splitattr.append((re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', attr)))

# Initialize an empty list to hold merged elements of the nested list
    
        mergelist = []

# Merge the nested lists in one list

        for nestedlist in splitattr:
            for items in nestedlist:
                mergelist.append(items)   

# For each item in the mergelist, check whether an abbreviation is present. 
# Show the attributes which requires addition of abbreviation in NSM file
        translist = []    
        finallist = []

        for item in mergelist:
            if item not in nsmdict.keys():
                translist.append(item) 
# Remove duplicate from the list of abbreviations                
        for i in translist:
            if i not in finallist:
                finallist.append(i)
                
        return finallist    
           
######### Dump the captured information in a report file with date and time added to the name of the file
    try:

   # Capturing the current datetime      
        filename = datetime.datetime.now()
        with open("IDA LDM Sanity Report_"+filename.strftime("%d %B %Y-%H %M %S")+".txt", "w") as outfile:
            outfile.write("Domain Values Used In The Model:\r\n")
            outfile.write("========\r\n")
            json.dump(domval, outfile, indent = 4)
            outfile.write("\r\n")
            outfile.write("Columns Which Are More Than 30 Characters Long:\r\n")
            outfile.write("========\r\n")
            json.dump(gt30(), outfile, indent = 4)
            outfile.write("\r\n")
            outfile.write("Names For Which Abbreviations To Be Added in NDM File:\r\n")
            outfile.write("========\r\n")
            json.dump(noabbr(), outfile, indent = 4)
            outfile.write("\r\n")
            outfile.write("List Of Attribuites Where No Description is Present:\r\n") 
            outfile.write("========\r\n")
            json.dump(nodesc(), outfile, indent = 4)
            outfile.write("\r\n")
            outfile.write("List Of Attribuites Where No Domain is Used:\r\n") 
            outfile.write("========\r\n")
            json.dump(nodomain(), outfile, indent = 4)
    except Exception as e:
        return(f'error with {str(e)}')   

    return messagebox.showinfo('IDA Sanity Check Complete','File Generated')
    # Return Control to program
    parent.destroy()
####=======Python GUI Screen Section. This takes the LDM and NSM file paths and call the main ===============================================####    

parent = Tk()  
parent.geometry('700x300')
parent.title('IBM IDA LDM Sanity Chaecking Tool - by Arindam Banerjee')

# Heading of the tool
Label(parent, text = 'IBM IDA LDM Sanity Checkling Tool', font = 'ar 15 bold', fg = 'blue').grid(row=0, column=1)

# Creating and packing Fields
ldmlabel = Label(parent,text = "Enter Full Path of IDA LDM").grid(row=3, column=0)
ndmlabel = Label(parent,text = "Enter Full Path of IDA NDM").grid(row=4, column=0)
desclabel = Label(parent,text = "This tool takes an IBM IDA generated Logical Data Model LDM File").place(x=10, y=120)
desclabel2 = Label(parent,text = "and a Naming Standard NDM File for abbreviations as inputs.").place(x=360, y=120)
desclabel3 = Label(parent,text = "It generates a file to provide useful information such as -").place(x=10, y=140)
desclabel4 = Label(parent,text = "-List of Domain Values and their data type used.").place(x=60, y=160)
desclabel5 = Label(parent,text = "-List of Columns which are more than 30 Char in length.").place(x=60, y=180)
desclabel6 = Label(parent,text = "-List of abbreviations which are absent from the NDM.").place(x=60, y=200)
desclabel7 = Label(parent,text = "-List of attributes where no description is present.").place(x=60, y=220)
desclabel8 = Label(parent,text = "-List of attributes where no domain is used.").place(x=60, y=240)
desclabel9 = Label(parent,text = "Conceptualized and Created by - Arindam Banerjee", font = 'ar 10 bold', fg = 'red').place(x=360, y=260)

# Variable for storing the path
ldmval = StringVar()
ndmval = StringVar()

# Creating and packing entry fields
ldmpath = Entry(parent, textvariable = ldmval).grid(row=3, column=1)
ndmpath = Entry(parent, textvariable = ndmval).grid(row=4, column=1)

#browseldm = Button(parent, text = "Browse", command = filedialog.askopenfile(parent=parent,mode='rb',title='Choose a file')).grid(row=3,column=2)

# Submit and Quit button

submit = Button(parent, text = "Submit", command = dowork)
submit.place(x=450,y=75)
quit = Button(parent, text = "Quit", command = parent.destroy)
quit.place(x=520,y=75)

parent.mainloop() 

##### End of Python GUI Screen Section. 

