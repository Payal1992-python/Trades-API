pipeline {
    agent any

    environment {
        PY = 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Check Python') {
            steps { bat '"%PY%" --version' }
        }
        stage('Install') {
            steps {
                bat '"%PY%" -m venv venv'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps { bat 'venv\\Scripts\\python manage.py test' }
        }
    }
}
