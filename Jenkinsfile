pipeline {
    agent any

    triggers { pollSCM('H/2 * * * *') }

    environment {
        PY = 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Install') {
            steps {
                bat '"%PY%" -m venv venv'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }
        stage('Django Check') {
            steps { bat 'venv\\Scripts\\python manage.py check' }
        }
        stage('Test') {
            steps { bat 'venv\\Scripts\\python manage.py test' }
        }
        stage('Deploy') {
            steps { echo 'Pretend deploy: copy app to server / restart service' }
        }
    }
}
