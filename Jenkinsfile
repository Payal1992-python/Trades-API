pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub source code checked out'
            }
        }

        stage('Check Environment') {
            steps {
                bat '''
                    echo Checking available tools
                    whoami
                    cd
                    git --version || echo git NOT found
                    java -version || echo java NOT found
                    python --version || echo python NOT found
                    where python || echo python NOT on PATH
                    where docker || echo docker NOT installed
                    dir
                '''
            }
        }
    }
}
