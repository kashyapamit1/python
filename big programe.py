age=int(input("enter your age"))
symptoms=str(input("enter your symptoms"))
temprature=int(input("enter your temprature"))
heartrate=int(input("enter your heartrate"))
bloodpressure=int(input("enter your bloodpressure"))
if(age<=12):
    if(symptoms=="fever"):
        if(temprature>=39):
           print("urgent care needed")
        elif(temprature<=39):
            print("monitor and give antipyertics")
        else:
            print("")
    elif(symptoms=="cough+withshortness of breadth"):
            print("see a pediatrician immedately")
    elif("cough+withoutshortnes of breadth"):
            print("monitor at home")
elif(age>=13 and age<=17):
    if(symptoms=="fever"):
        if(temprature>=39):
            print("urgent care needed")
        elif(temprature<=39):
            print("monitor and give antipyertic")
    elif(symptoms=="cough+ withahortness of breadth"):
            print("see a doctor immeditely")
    elif("withoutshortness of breadth"):
            print("monitor at home")
    else:
        print("")
elif(age>=18 and age<=64):
    if(symptoms=="fever"):
        if(temprature>=39):
            print("urgent care needed")
        elif(temprature<=39):
            print("monitor at give antipyretics")
    elif(symptoms=="chest pain"):
        if(heartrate>=100 or bloodpresssure<=140/90):
            print("immidate emergency room")
        elif(heartrate<=100 and blood pressure<=140/90):
             print("monitor and schedule checkup")
elif(age>=65):
    if(symptoms=="fever"):
        if(temprature>=38):
            print("urgent care needed")
        elif(temprature<=38):
            print("monitor and give antipyretics")
    elif(symptoms=="chestpain"):
        if(heartrate>=100 or bloodpreesure<140):
            print("immidate emergency room")
        elif(heartrate<=100 and bloodpressure<=140):
            print("monitor and schedule checkup")
else:
    print("")

            
    
            
    
