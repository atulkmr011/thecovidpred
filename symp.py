from flask import Flask, render_template , request
app = Flask(__name__)
import pickle


file = open('C:\\Users\\Atul\\Desktop\\progs\\covidpredict\\model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods = ["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        age = int(myDict['age'])
        fever = int(myDict['fever'])
        cough = int(myDict['cough'])
        shortnessofbreath = int(myDict['shortnessofbreath'])
        sorethroat = int(myDict['sorethroat'])
        musclepain = int(myDict['musclepain'])
        nausea = int(myDict['nausea'])
        diarrhoea = int(myDict['diarrhoea'])
        fatigue = int(myDict['fatigue'])
        vomiting = int(myDict['vomiting'])
        headache = int(myDict['headache'])      
        inputFeatures = [age, fever,cough,shortnessofbreath,sorethroat,musclepain,nausea,diarrhoea,fatigue,vomiting,headache]
        infProb =clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html', inf=round(infProb*100))
    return render_template('index.html')
    # return 'Hello, World!' + str(infProb)


if __name__ =="__main__":
    app.run(debug=True)       