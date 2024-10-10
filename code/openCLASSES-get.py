import openai
dict={}
# Set up the OpenAI API client
openai.api_key = ""
# Set up the model and prompt
model_engine = "text-davinci-003"
#model_engine = "text-curie-001"
catg=set()
vali=1
totalpres=0
curpres=0
file1 = open("out"+str(vali)+".txt", 'r')
Lines = file1.readlines()
f = open("TESToutAI"+str(vali)+".txt", "w")
#f.write("Now the file has more content!")

count = 0
cura=185
cc=0
# Strips the newline character
for line in Lines:
    
    if cc>=cura:
        x =line.split('\t')
        x[1] = x[1].strip()
    
        #print(str(count)+ " "+x[1])
        prompt = "one word that defines under which broad category is  "+x[1]+" if it is geographical item return georgaphy if is art related return art if it is science related return science if it is politics related return politics if it is economics or business related return economics if it is history related return history if it is human related return human if it is health related return health if it is technology related return technology "
        
        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        
        response = completion.choices[0].text
        
        response = response.strip()
        response=response.replace("\n","")
        response=response.replace("\r","")
        response=response.replace(".","")
       
        try:
           
        #respose=response.replace(".","")
        
            #print("    --->["+response+']')
            print(x[1]+"\t"+response)
           # f.write(x[1]+"\t"+response+"\n")
            catg.add(response)
            count=count+1
            curpres=int(x[2])
            if response not in dict:
                dict[response]=0
            dict[response]=dict[response]+curpres;
            totalpres=totalpres+int(x[2])
          
    
        except:
            print("EXEC")# if count==4:
        #     break
        # if count==10:
        #     break;
        if count%40==0:
            import time
           # print("sleeping")
    
            time.sleep(120)
    cc=cc+1
        # if count>10:
        #     break

# print("size "+str(len(catg)))
# for l in catg:
#     print(l)
f.close();
tota=0
import operator
sdict={k: v for k, v in sorted(dict.items(), key=lambda item: item[1],reverse=True)}
for  keys, value in sdict.items():
    # print(str(value))

    #print(keys+" "+str(value*100/totalpres))
   
    tota=tota+value
#print(str(tota)+" "+str(totalpres))
