import pandas as pd
import numpy as np
import sys
import argparse

def topsis_fnc(X,weights,impacts):
    
    if(type(X)!=np.ndarray):
        print("Parameter passed should be matrix")
        sys.exit(0)

    for i in weights:
        if type(i)!=int:
            print(type(i))
            print('weights should be in float')
            sys.exit(0)

    a=0
    
    for i in weights:
        a=a+i

    for i,j in enumerate(weights):
        weights[i]=j/a



    for i in impacts:
        if type(i)!=str:
            print('Impact should be a string')
            sys.exit(0)

    if(len(impacts)!=np.shape(X)[1] or len(weights)!=np.shape(X)[1]):
        print("Parameters length didn't match")
        sys.exit(0)
        
    col=np.sqrt(np.sum(np.square(X), axis=0))

    for i,j in enumerate(col):
        X[:,i]=np.divide(X[:,i],j)

    for i,j in enumerate(weights):
        X[:,i]=X[:,i]*j

    A=np.zeros((2,np.shape(X)[1]))
    
    for i,j in enumerate(impacts):
        
        if j=='+':
            A[0][i]=np.max(X[:,i])
            A[1][i]=np.min(X[:,i])
       
        else:
            A[0][i]=np.min(X[:,i])
            A[1][i]=np.max(X[:,i])


    B=np.zeros((np.shape(X)[0],5))
    B[:,0]= np.sqrt(np.sum(np.square(X-A[0]),axis=1))
    B[:,1]= np.sqrt(np.sum(np.square(X-A[1]),axis=1))
    B[:,2]=B[:,0]+B[:,1]
    B[:,3]=np.divide(B[:,1],B[:,2])



    l=sorted(B[:,3],reverse=True)

    dic={}
    j=1
    for i in l:
        dic[i]=j
        j+=1
    ans=np.zeros((np.shape(X)[0],2))

    for i,j in enumerate(B[:,3]):
        ans[i][1]=dic[j]
        ans[i][0]=i+1


    print('{0:^20}'.format("topsis_fncsis Selection"))
    print('{0:10} | {1:10}'.format("Models","Rank"))
    print('{0:20}'.format("-----------------------"))
    
    for i in range(np.shape(ans)[0]):
        print('{0:<10} | {1:<10}'.format(int(ans[i][0]),int(ans[i][1])))

def main():
    parser=argparse.ArgumentParser(description='Find out the ranking table')
    parser.add_argument("filename",help='Name of the file to be extracted',type=str)
    parser.add_argument('-w',"--weights",help='Enter the weights of attributes'  ,nargs="+", type=int,default=[1,1,1,1])
    parser.add_argument('-i',"--impacts",help='Enter the impacts of attributes',nargs='+',type=str,default=['+','+','+','+'])
    args=parser.parse_args()

    file=args.filename
    data=pd.read_csv(file)


    X=data.iloc[:,1:].values


    impacts=args.impacts
    weights=args.weights
    if(len(impacts)!=np.shape(X)[1] or len(weights)!=np.shape(X)[1]):
        print("Values didnt match:")
        sys.exit(0)



    if(topsis_fnc(X,weights,impacts)==None):
        print("Executed successfully")

if __name__=='__main__':
   main()
