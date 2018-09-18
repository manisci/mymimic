import os
import numpy as np
def xtracttopfeat():
    ## this functions reads the text files , strcture and organize them , and returns 
    ## a feature matrix for further processing, it imputes unrecoreded values with the mean of that feature
    ## you further need to take care of general descriptors by treating them in a special way and also take out data
    ## specific for an ICU type
    # This one is for the 8 predefined features only. 
    ## reading the text file to construct feature matrix 


    gendiscname = "/Users/manisci/Documents/research/Fall2018/mimic/generaldesc.csv"
    gd=open(gendiscname, 'r')
    prevpat = 0.1
    line = gd.readline()
    icutkypedict = {}
    agedict = {}
    losdict = {}
    genderdict = {}
    epid = 1
    line = gd.readline()
    while(line):
        if len(line) == 0:
            continue
        info = line.split(",")
        if len(info[2]) == 0:
            continue
        patid = int(info[0])
        icutype = info[1]
        if icutype == "MICU":
            icutype = 3
        elif icutype == "CCU":
            icutype = 1
        elif icutype == "TSICU":
            icutype = 14
        elif icutype == "CSRU":
            icutype = 2
        elif icutype == "SICU":
            icutype = 4
        if patid == prevpat:
            epid +=1
        else:
            epid = 1
        lengthofstay = float(info[2])
        gender = info[3]
        age = float(info[4])
        icutkypedict[(patid,epid)] = icutype
        agedict[(patid,epid)] = age
        losdict[(patid,epid)] = lengthofstay
        genderdict[(patid,epid)] = gender
        # print "hi"
        prevpat = patid
        line = gd.readline()
    gd.close()

    # just a simple test 
    featset = ["GCS","Temp","HR","WBC","Glucose","Urine","NIDiasABP"]
    # featset = ["HR"]
    numbfeats = len(featset)
    featmtrx = np.empty((5,21139,5 * numbfeats))  # should be moved?
    featmtrx1st24 = np.empty((5,21139,5 * numbfeats))  # should be moved?
    featmtrx2nd24 = np.empty((5,21139,5 * numbfeats))  # should be moved?
    icutype = 0
    ages = []
    genders = []
    ## extracting features dictionary
    # 
    icutypes = [1,2,3,4,14,15]
    paticutype = dict.fromkeys(icutypes) 
    for type in icutypes:
        paticutype[type] = []



    # for ind in range(132539,142673):
    #     filename = str(ind) + ".txt"
    #     # print(filename)
    #     ## checking to see if the file exists in the directory 
    #     try:
    #         f = open(filename,'r')
    #     except IOError as e:
    #         pass
    #     ## readaway the first lien
    #     f.readline()
    #     for line in f:
    #         curline = line.split(",")
    #         feat = curline[1]
    #         featset.append(feat)
    #         featset = list(set(featset))
    # featset = list(set(featset)) ## taking out the icutype 
    # # setting up the feature matrix in this order , first, min , mean, max. last
    meanfeat = [0] * (len(featset) )
    meanfeat1st24 = [0] * (len(featset))
    meanfeat2nd24 = [0] * (len(featset))
    combkeys = [(1,1),(2,1), (3,1),(4,1),(14,1),(15,1), (1,2),(2,2),(3,2), (4,2),(14,2),(15,2)]
    dumbak = [0] * 7
    meanfeaticu = dict.fromkeys(combkeys,dumbak)
    meanfeaticualltime = dict.fromkeys(icutypes,dumbak)
    index = -1
    # the keys are icu type, time, value 
    heartratedict = dict.fromkeys(range(21139)) 
    WBCdict = dict.fromkeys(range(21139)) 
    tempdict = dict.fromkeys(range(21139)) 
    GCSdict = dict.fromkeys(range(21139)) 
    urinedict = dict.fromkeys(range(21139)) 
    glucosedict = dict.fromkeys(range(21139)) 
    NIDSdict = dict.fromkeys(range(21139)) 
    changesdictmedians = dict.fromkeys(featset)
    changesdictmeans = dict.fromkeys(featset)

    for featak in featset:
        changesdictmedians[featak] = []
        changesdictmeans[featak] = []
        

    for d in range(21139):
        heartratedict[d] = []
        WBCdict[d] = []
        tempdict[d] = []
        GCSdict[d] = []
        urinedict[d] = []
        glucosedict[d] = []
        NIDSdict[d] = []
    featlength = {}
    for feat in featset:
        featlength [feat] = 0
    ages = []
    genders = []
    directory = "/Users/manisci/Documents/research/Fall2018/mimic/smallds"
    for root,dirs,files in os.walk(directory):
        for file in files:
            info = file.split("_")
            patientno = int(info[0])
            epno = int(info[1][-1])
            if file.endswith(".csv"):
                file = directory + "/" + file
                f=open(file, 'r')
                #  perform calculation
                featdict = dict.fromkeys(featset,[])
                featdict1st24 = dict.fromkeys(featset,[])
                featdict2nd24 = dict.fromkeys(featset,[])
                ## taking the maximum patients in an Icu type

                for key in featdict.keys():
                    featdict[key] = []
                    featdict1st24[key] = []
                    featdict2nd24[key] = []
                line = f.readline()
                while(True):
                    line = f.readline()
                    if not line:
                        break
                    curline = line.split(",")
                    print curline
                    print "hi!"




                
                f.close()
xtracttopfeat()


    