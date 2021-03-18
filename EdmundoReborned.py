
from private import token
from private import whitelist




userlist=[ "Thegroucher" ]
#print("https://api.telegram.org/bot"+token+"/METHOD_NAME")
lastID=0

username=" "

import urllib.request
import json
import webbrowser
import time


offset=1000
while True:                 #Infinite loop
    time.sleep(5)           #Every 5 seconds

    try:
        content = urllib.request.urlopen("https://api.telegram.org/bot"+token+"/getUpdates?offset="+str(offset)+"&limit=1").read() #Asks for one message with the apropied offset.

    except ConnectionResetError:
        print (time.asctime(time.localtime()))
        print("hubo un error 1")
        time.sleep(5)
        content = urllib.request.urlopen("https://api.telegram.org/bot"+token+"/getUpdates?offset="+str(offset)+"&limit=1").read() #Asks for one message with the apropied offset.
        
    except urllib.error.URLError:
        print (time.asctime(time.localtime()))
        print("hubo un error 2")
        time.sleep(5)
        continue

        
   
    #print (content)
    

    jsonObj = json.loads(content)                   #Transforms the json object in to python redeable lits and dictionaries.
    
    #print (json.dumps(jsonObj,ensure_ascii=False,indent=2)) #print the message



    if (len(jsonObj['result']) >0 ):#If not and empty message
        
        #Saving different pieces in variables for easy acces.
        
        result=jsonObj["result"][0]                     
        update_id = jsonObj['result'][0]['update_id']
        offset= update_id + 1                            #update offset
        if "message" not in result:
            message=result['edited_message']
            
            
        message=result['message']   
            
        chat_id=message["chat"]["id"]
        
        if "username" in message["chat"]:
            username=message["chat"]["username"]
        if message["text"]==("/start"):
                send_text= urllib.parse.quote("Greetings!")
                callback=json.loads(urllib.request.urlopen("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+str(chat_id)+"&text="+send_text).read())
                print(json.dumps(callback["result"]))
                send_text= urllib.parse.quote("Human!")
                urllib.request.urlopen("https://api.telegram.org/bot"+token+"/editMessageText?chat_id="+str(chat_id)+"&message_id="+str(callback["result"]["message_id"])+"&text="+send_text).read()
                
       
            
            
        if "new_chat_members"  in message:
            print (message["new_chat_members"][0]["username"]) #print the message if it has no text

        elif "left_chat_member" in message:
            print( message["left_chat_member"]["username"] +"LEFT") #Print who leaves the chat
            
        else:                                                               #print if the message  has  text
            print (time.asctime(time.localtime()))
            print (json.dumps(message["chat"],ensure_ascii=False,indent=2)) 
            print (json.dumps(message["text"],ensure_ascii=False,indent=2)) 
            
        if ("text" in message) : # The message has text 

             
            text = jsonObj['result'][0]['message']['text'] #Save text in variable

            if jsonObj["result"][0]["message"]["message_id"]!=lastID: #checks that the message is not the same. This should not be necesary if the offset is working properly.
                
                lastID=jsonObj["result"][0]["message"]["message_id"] #Updates the last ID
                if ((chat_id in whitelist)or username in userlist)&(len(text)==40): #checking if users are alowed and also if the message is a hash
                    #Say thanks
                    send_text= urllib.parse.quote("Thanks !")
                    urllib.request.urlopen("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+str(chat_id)+"&text="+send_text).read()
                    
                    #Donwload the torrent
                    strURL = "magnet:?xt=urn:btih:"+text
                    webbrowser.open(strURL, new=2)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------USEFUL THINGS-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#SEND MESSAGE
    
        
        
