from flask import Flask, request
import os

app=Flask(__name__)

def run(tutorialNumber,numberOfQuestions, outputDirectory):

    newDirectoryName=f'Turorial {tutorialNumber}'
    os.chdir(outputDirectory)
    os.mkdir(newDirectoryName)
    os.chdir(newDirectoryName)

    parentDirectory=os.getcwd()

    for i in range(1,numberOfQuestions+1):
        with open(f'Question {i}.cpp','w') as f:
            os.chdir(f'Question {i}')

        with open(f'Question {i}.cpp','w') as f:
            pass

        os.chdir(parentDirectory)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tutorialNumber = request.form['tutorial']
        numberOfQuestions = int(request.form['questions'])
        outputDirectory = request.form['path']
        run(tutorialNumber, numberOfQuestions, outputDirectory)
        return 'Task completed successfully!'  # Return some response to indicate success
    return 'Hello, please submit the form.'

if __name__ == '__main__':
    app.run(debug=True)