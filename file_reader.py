def uni_el_calc(li):
    dict={}
    for di in li:
        if dict.get(di, False):
            dict[di]+=1
        else:
            dict[di]=1
    return dict
def file_word_calc(file):
    with open(file, 'r', encoding='utf-8') as tf:
        ftemp=tf.read()#read everything
    ############same
    #sili=[]
    #for si in ftemp:
    #    sili.append(si)
    #print(sili)
    #print(len(sili))
    #print(type(sili))
    ##############################
    sisili=list(ftemp)#####same
    lettli=[]
    for le in sisili:
        if le==',' or le=='.' or le=='?' or le=='!' or le==':' or le==';' or le=='\n':
            continue
        else:
            lettli.append(le)
    lettstr=''.join(lettli)
    wordli=lettstr.split(' ')
    wordict=uni_el_calc(wordli)
#    ##########debug######################
#    #print(ftemp)
#    print(len(ftemp))
#    print(type(ftemp))
#    print('\n\n')
#    ###############################
#    #print(sisili)
#    print(len(sisili))
#    print(type(sisili))
#    print('\n\n')
#    ################################
#    print(lettli)
#    print(len(lettli))
#    print('\n\n')
#    ################################
#    print('\n\n')
#    print(lettstr)
#    print(type(lettstr))
#    print(len(lettstr))
#    ################################
#    print('\n\n')
#    print(wordli)
#    print(type(wordli))
#    print(len(wordli))
#    ###################################
#    print('\n\n')
#    print(wordict)
#    print(type(wordict))
#    print(len(wordict))
#    ##############debug##################
    return wordict
#filedict=file_word_calc('')
#print(filedict)
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='file_word_calc')
    parser.add_argument('file_path', type=str, help='Input file path')
    parser.add_argument('-f', '--file', action="store_true", dest="rf", required=False, help='Input \'-f\' or \'--file\' to have a result file in the current directory')
    parser.add_argument('rfdir',action="store", type=str, nargs='?', help='Input directory for result file')
    args = parser.parse_args()    
    filedict=file_word_calc(args.file_path)
    print(filedict)
#################debug#############    
    print(args)
    print(args.rf)
    print(args.rfdir)
###############debug###############
###################################    
    if args.rf:
        print ('\n\n\n')
        with open(args.file_path, 'r', encoding='utf-8') as tf:
            print (tf.name)
####################################            
##############debug#################            
        print(args.rfdir)
##############debug#################                









