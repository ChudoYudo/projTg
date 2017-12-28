import requests
import misc
import json
import random
import time
import sys

token=misc.token
print (token)

#https://api.telegram.org/bot477404019:AAGJgsUxaMbeLRnZnJTrN1ZtiuAwzY832w0/sendmessage?chat_id=204077935&text=hello
URL = 'https://api.telegram.org/bot'+token+'/'
global lastid
lastid = 0

def get_updates():
	url=URL+'getupdates?timeout=2'
	r=requests.get(url)
	return r.json()

def add_person(sender):
	send_message(sender['chat_id'],'Pleaze,enter name of group')
	while True:
		ans=get_message()
		if ans!=None:
			break
	namef=ans['text']+'.txt'
	try :
		ff=open(namef)
	except IOError as e:
		send_message(ans['chat_id'],'There are no this group, you can create it with help /creategroup comand')
		return 	
	print(namef)

	


	pasF=ans['text']+'_pas'+'.txt'
	print(pasF)
	

	filepas=open (str(pasF), 'r') 
	pasread=filepas.read()
	i=0
	#print (pasread)
	#print(type(pasread))
	send_message(ans['chat_id'],'Password:')
	while i<3:
		print('enter pas')
		while True:
			anspas=get_message()
			if anspas!=None:
				break
		password=anspas['text']		
		#print(password)
		password=str(password)
		#print(password)
		#print ('pas:'+pasread)
		#print(type(pasread))
		#print(type(password))
		

		password='"'+password+'"'
		print(pasread)
		print(password)

		if password == pasread:
			print ('yes')
		#send_message(ans['chat_id'],'Incorrect Pass,try again')
				
			
			with open (str(namef), 'r') as file2:
				k=json.loads(file2.read())	
			
			kk=list(k)	
			print(kk)

			
			ans2=ans['name']+' '+ans['sec_name']	
			
				

			if kk.count(ans2)>0:
				send_message(ans['chat_id'],'you are member of this group')	
				return			

			kk.append(ans2)
			send_message(ans['chat_id'],'welcome to '+ans['text']+' group!')
			print(kk)
			
			with open (str(namef), 'w') as file:
				json.dump(kk,file, indent=2) 
			break
				
		else:
			send_message(ans['chat_id'],'incorrect password for this group')
			i=i+1
		if i==3:
			break
				


def get_message():
	dataid = get_updates()
	
	last_obj=dataid['result'][-1]['update_id']
	global lastid
	if lastid != last_obj:
		lastid=last_obj
		Name= dataid['result'][-1]['message']['chat']['first_name']
		Sec_Name= dataid['result'][-1]['message']['chat']['last_name']
		chat_id= dataid['result'][-1]['message']['chat']['id']
		text= dataid['result'][-1]['message']['text']
		mes={'chat_id':chat_id,
			 'name':Name,
			'text':text,
			'sec_name':Sec_Name
			}
		return mes	
	
	return None	




def send_message(chat_id,text):
	url=URL +'sendmessage?chat_id={}&text={}'.format(chat_id,text)
	requests.get(url)

#AgADAgADyKgxGxfqAAFK9C8hSJ5YMZOmAAEzDgAEpDDUzyccmqv_BgIAAQI

def send_file (chat_id):
	url=URL +'sendPhoto?chat_id={}&photo=AgADAgADyKgxGxfqAAFK0c6OIUD1aA-mAAEzDgAFtYgeebnTmwABBwIAAQI'.format(chat_id)
	requests.get(url)




def create_group(sender):
	send_message(sender['chat_id'],'Pleaze,enter a name of your group')
	flag=False 
	while True:
		ans=get_message()
		if ans!=None:
			break
	namef=ans['text']+'.txt'
	print(namef)
	try :
		ff=open(namef)
	except IOError as e:
		flag=True
	if flag==False:
		send_message(ans['chat_id'],'Group with name :'+'"'+ans['text']+'"'+' is alredy exist')
		return 	
	k=[]
	#file2=open (str(namef), 'w')
	with open (str(namef), 'w') as file:
		json.dump(k,file, indent=2)
	pasF=ans['text']+'_pas'+'.txt'
	print('pas:')
	send_message(ans['chat_id'],'Create a password for your group:')
	while True:
		anspas=get_message()
		if anspas!=None:
			break
	password=anspas['text']	
	
	with open (str(pasF), 'w') as file:
		json.dump(password,file, indent=2)	

	send_message(ans['chat_id'],'Group '+ans['text']+' is sucsesfuly created!')	
	

def get_People(ans):

	send_message(ans['chat_id'],'Pleaze,enter name of group')
	while True:
		ans=get_message()
		if ans!=None:
			break
	namef=ans['text']+'.txt'
	try :
		ff=open(namef)
	except IOError as e:
		send_message(ans['chat_id'],'There are no this group, you can create it with help /creategroup comand')
		return 	
	print(namef)

	


	pasF=ans['text']+'_pas'+'.txt'
	print(pasF)
	

	filepas=open (str(pasF), 'r') 
	pasread=filepas.read()
	i=0
	#print (pasread)
	#print(type(pasread))
	send_message(ans['chat_id'],'Password:')


	while i<3:
		print('enter pas')
		while True:
			anspas=get_message()
			if anspas!=None:
				break
		password=anspas['text']		
		#print(password)
		password=str(password)
		#print(password)
		#print ('pas:'+pasread)
		#print(type(pasread))
		#print(type(password))
		print(pasread)
		print(password)

		password='"'+password+'"'

		if password == pasread:
			with open (namef, 'r') as file:
				k=json.loads(file.read())	

					
			x=len(k)
			ran=random.randint(0,x-1)
			mm=ans['name']+' '+ans['sec_name']
			while True:
				print(k[ran])
				print(mm)
				if mm!=k[ran]:
					break

			#print(ran)
			your_people=k.pop(ran)

			with open (namef, 'w') as file2:
				json.dump(k,file2, indent=2) 

			return your_people	
			
				
		else:
			send_message(ans['chat_id'],'incorrect password for this group')
			i=i+1
		if i==3:
			break





	with open ('names.txt', 'r') as file:
		k=json.loads(file.read())

		


	
	



def main():
	#n=['Andrey','Polina','Sabina','Roma','Vlad','Dima','Alexandr','Lena','Kolya']
	
	#d = get_updates()
	#n=get_name()
	#i=get_chatid()
	#u=0
	#send_message(get_chatid(),"Its your name?")


	
	
	while True:
		ans=get_message()
		#time.sleep(30)
		if ans!=None:
			if ans['text']=='/start':
				send_message(ans['chat_id'],'Hello,this bot created by Raman Yudo.It is intended for Secret santa game.Send a /get to choise')
				
			
			if ans['text']=='/get':
				sub=get_People(ans)
				if sub==None:
					continue
				answer=ans['name']+',you must give a gift for '+sub
				send_message(ans['chat_id'],answer)
				send_file(ans['chat_id'])


			if ans['text']=='/creategroup':
				create_group(ans)
			
			if ans['text']=='/add':
				add_person(ans)


			if ans['text']=='stopit':
				send_message(ans['chat_id'],'program is stop')
				sys.exit(0)
				
			



		#j_d=open('names.txt').read()
		#k=json.loads(j_d)


	#with open ('names2.txt', 'w') as f:
		#json.dump(n,f, indent=2) 



	#print (n)
	#print (i)
	#send_message(i,'kek')



if __name__ == '__main__':
	main()