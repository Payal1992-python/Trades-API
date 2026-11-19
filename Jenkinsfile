pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub source code checked out'
            }
        }

        stage('Python Version') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}
