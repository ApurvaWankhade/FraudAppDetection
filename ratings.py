word1="score"
count=0;
isfound=False
ratings=""
with open('urldata.txt','r',errors="ignore") as file:
    # reading each line    
    for line in file:
        # reading each word        
        for word in line.split():
            if word1 in word:
                #print(word)
                isfound=True
            ratings=word
            if(isfound):
                count=count+1;
            if(count==2):
                break;
print("ratings is ",ratings)               
   
        
            
