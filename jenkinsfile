pipeline {
    agent any

    environment {
        FLASK_ENV = 'production'
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from your version control system (e.g., Git)
                checkout scm
            }
        }

        stage('Lint') {
            steps {
                // Lint the code using flake8
                script {
                    docker.image('python:3.8-slim').inside {
                        sh 'pip install flake8'
                        sh 'flake8 Jenkins-docker-k8'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                // Use a Python Docker image to build the application
                script {
                    docker.image('python:3.8-slim').inside('-u root') {
                        sh 'pip install --upgrade pip'
                        sh 'pip install -r Jenkins-docker-k8/requirements.txt'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                // Run your tests here
                script {
                    docker.image('python:3.8-slim').inside {
                        sh 'python Jenkins-docker-k8/test_app.py'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your Flask application to Kubernetes
                script {
                    sh 'kubectl apply -f Jenkins-docker-k8/kubernetes/deployment.yaml'
                    sh 'kubectl apply -f Jenkins-docker-k8/kubernetes/service.yaml'
                }
            }
        }
    }

    post {
        success {
            // Additional steps to perform on success
        }
        failure {
            // Additional steps to perform on failure
        }
    }
}
