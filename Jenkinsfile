pipeline {
    agent {
        label 'Docker'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'git clone https://github.com/GitManAmine/my-service-restful.git '
                sh 'cd my-service-restful ; ls ; docker build -t my-app:dev .'
            }
        }

        stage('Run App'){
            steps {
                sh 'docker run --name my-service -d -p 5000:5000 my-app:dev'
            }
        }
        
        stage ('Clean'){
            steps{
                sh 'docker stop my-service && docker rm my-service'
                sh 'docker image rm my-app:dev'
            }
        }
    }
}
