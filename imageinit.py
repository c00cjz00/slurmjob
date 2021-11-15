#!/usr/bin/env python
import os
import sys
import sysconfig

def myimage(myENV,resetPackage=None):
    # 1. 新增個人安裝目錄 (可選)
    #myENV='mycolab'
    #SINGULARITY_NAME=os.environ["SINGULARITY_NAME"]
    #myENV = os.path.basename(SINGULARITY_NAME).split('.')[0]   
    uaername = get_ipython().getoutput('whoami')
    myPackageHome='/work/'+uaername[0]+'/myenv'

    ## 導入環境變數 export PATH=...
    os.environ['PATH']=myPackageHome+"/.package_"+myENV+"_nchc_conda/envs/"+myENV+"/bin:"+os.environ['PATH'] 

    ## 設定單一環境變數
    %env CONDA_PKGS_DIRS={myPackageHome}/.package_{myENV}_nchc_conda/pkgs
    %env CONDA_ENVS_DIRS={myPackageHome}/.package_{myENV}_nchc_conda/envs
    %env PYTHONUSERBASE={myPackageHome}/.package_{myENV}_nchc_conda/envs/{myENV}

    ## 新增讀取sitepackage目錄
    tmp=(sysconfig.get_paths()["purelib"])
    dirname=os.path.dirname(tmp)
    basename01=os.path.basename(tmp)
    basename02=os.path.basename(dirname)
    sys_path_add=myPackageHome+"/.package_"+myENV+"_nchc_conda/envs/"+myENV+"/lib/"+basename02+"/"+basename01 
    mypipDir=sys_path_add
    sys.path.insert(0, sys_path_add)

    ## 更新pip安裝目錄
    get_ipython().run_line_magic('env', 'PYTHONUSERBASE={myPackageHome}/.package_{myENV}_nchc_conda/envs/{myENV}')
    get_ipython().run_line_magic('env', 'PIP_TARGET={sys_path_add}')
    
    
    if resetPackage:
        # 2. 是否要刪除安裝目錄
        print('rm -rf '+myPackageHome+"/.package_"+myENV+"_nchc_conda")
        get_ipython().system('rm -rf "$myPackageHome"/.package_"$myENV"_nchc_conda')
    

def myimage_singularity(resetPackage=None):
    # 1. 新增個人安裝目錄 (可選)
    #myENV='mycolab'
    SINGULARITY_NAME=os.environ["SINGULARITY_NAME"]
    myENV = os.path.basename(SINGULARITY_NAME).split('.')[0]   
    uaername = get_ipython().getoutput('whoami')
    myPackageHome='/work/'+uaername[0]+'/myenv'

    ## 導入環境變數 export PATH=...
    os.environ['PATH']=myPackageHome+"/.package_"+myENV+"_nchc_conda/envs/"+myENV+"/bin:"+os.environ['PATH'] 

    ## 設定單一環境變數
    %env CONDA_PKGS_DIRS={myPackageHome}/.package_{myENV}_nchc_conda/pkgs
    %env CONDA_ENVS_DIRS={myPackageHome}/.package_{myENV}_nchc_conda/envs
    %env PYTHONUSERBASE={myPackageHome}/.package_{myENV}_nchc_conda/envs/{myENV}

    ## 新增讀取sitepackage目錄
    tmp=(sysconfig.get_paths()["purelib"])
    dirname=os.path.dirname(tmp)
    basename01=os.path.basename(tmp)
    basename02=os.path.basename(dirname)
    sys_path_add=myPackageHome+"/.package_"+myENV+"_nchc_conda/envs/"+myENV+"/lib/"+basename02+"/"+basename01 
    sys.path.insert(0, sys_path_add)

    ## 更新pip安裝目錄
    get_ipython().run_line_magic('env', 'PYTHONUSERBASE={myPackageHome}/.package_{myENV}_nchc_conda/envs/{myENV}')
    get_ipython().run_line_magic('env', 'PIP_TARGET={sys_path_add}')


    if resetPackage:
        # 2. 是否要刪除安裝目錄
        print('rm -rf '+myPackageHome+"/.package_"+myENV+"_nchc_conda")
        get_ipython().system('rm -rf "$myPackageHome"/.package_"$myENV"_nchc_conda')
    