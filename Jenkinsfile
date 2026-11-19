pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub source code checked out'
            }
        }

        
stage('Check Environment') {
    steps {
        sh '''
            echo "Checking available tools"
            whoami
            pwd
            git --version
            java -version
            docker --version
            which python
            which python3
            which docker
        '''
    }
}

    }
}
