pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/deepakjogi433/aws-devops-project.git'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r app/requirements.txt
                    pip install pytest
                    python -m pytest
                '''
            }
        }

        stage('Deploy to App EC2') {
            steps {
                sshagent(['app-ec2-ssh']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no \
                            ec2-user@13.127.76.124 \
                            "cd ~/aws-devops-project && git pull && docker build -t aws-devops-app:${BUILD_NUMBER} . && docker rm -f aws-devops-container || true && docker run -d -p 5000:5000 --name aws-devops-container aws-devops-app:${BUILD_NUMBER}"
                    '''
                }
            }
        }

    }
}


