pipeline {
    agent any
    
    environment {
        // Replace with your actual Docker Hub username
        DOCKER_IMAGE = "affan810/mt2025016_spe"
        // This ensures Jenkins can find Homebrew tools like Python and Docker on your Mac
        PATH = "/opt/homebrew/bin:/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        sstage('Build and Push Docker Image') {
            steps {
                // This wrapper ensures Jenkins logs in BEFORE doing anything else
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    
                    // 1. Log in to Docker Hub using your token
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    
                    // 2. Build the image (It will now successfully pull the Python base image)
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                    
                    // 3. Push the newly built image to your repository
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }
}