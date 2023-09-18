pipeline {
    agent {
        label 'Docker'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Construire l'image Docker
                    docker.build("countryrest:dev", "-f Dockerfile .")
                }
            }
        }

        stage('Run App'){
            steps {
                sh 'docker run --name my-service -d -p 5000:5000 countryREST:dev'
            }
        }
    }
}
