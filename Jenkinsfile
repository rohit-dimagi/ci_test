pipeline {
    agent { docker { image 'python:2.7' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'git clone https://github.com/rohit-dimagi/ci_test.git'
                    sh 'pip install  --user -r ci_test/requirements.txt'
                }
            }
        }
        stage('test') {
            steps {
                sh 'nose2'
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}


