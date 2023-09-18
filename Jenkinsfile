pipeline {
    agent {
        label 'Docker'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'git clone https://github.com/GitManAmine/my-service-restful.git '
		sh 'cd /home/homelander/workspace/countryRest/my-service-restful/ && docker build -t my-app:dev . '
            }
        }

        stage('Run App'){
            steps {
                sh 'docker run --name my-service -d -p 5000:5000 my-app:dev'
            }
        }
    }
}
