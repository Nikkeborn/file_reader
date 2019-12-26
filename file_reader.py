def str_insert(orig_str, insert):
    str_len=len(orig_str)
    new_str=orig_str[:str_len-4]+insert+orig_str[str_len-4:] 
    return new_str  
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
    parser.set_defaults(v=False)
#################################################################    
    subparsers=parser.add_subparsers(help='Script command for add results to file')
#################################################################    
    parser_f=subparsers.add_parser('f')
    parser_f.set_defaults(v=True)
    parser_f.add_argument('-d','--dir',action='store', dest='rfdir', type=str, nargs='?', default='', help='Input directory for result file')
#################################################################    
    args = parser.parse_args()
##############################################################    
    filedict=file_word_calc(args.file_path)
    print(filedict)
###########debug##########    
    print(args)
    print(args._get_kwargs())
    print(args.v)
###########debug##########
##########################    
    if args.v==True:        
        print ('\n\n\n')        
        if not args.rfdir:
            res_file_name=str_insert(args.file_path, '_calc')
            print(res_file_name)
            with open(res_file_name, 'w', encoding='utf-8') as tf:
                print(tf.name)
                print(tf)    
        else:
            import os
            base=os.path.basename(args.file_path)
            print(f'################{base}#######################')
            res_base_name=str_insert(base, '_calc')
            print(f'################{res_base_name}#######################')
            if os.path.isdir(args.rfdir):
                with open(f'{args.rfdir}\\{res_base_name}', 'w', encoding='utf-8') as tf:                
                    print(tf.name)
                    print(tf)    
                print(args.rfdir)
                print(f'###########{args.rfdir}\\{res_base_name}#######################')
            else:
                print(f'{args.rfdir} directory not found')
##########################            
############debug#########        
        print(args)
        print(args.v)
        print(args.rfdir)
###########debug##########











