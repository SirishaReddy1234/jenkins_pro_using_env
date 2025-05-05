pipeline {
    agent any
    environment{
        ECR_REGISTRY="448049823362.dkr.ecr.ap-south-1.amazonaws.com/myimage"
        dockerImageTag = "${env.BUILD_NUMBER}"
        CONTAINER_PORT = "8085"
        HOST_PORT = "8089" 


    }


    stages {
        stage('checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SirishaReddy1234/jenkins_pro_using_env.git'
            }
        }
        
        stage('build') {
            steps {
                sh 'docker build --tag ${ECR_REGISTRY}:${dockerImageTag} .'
            }
        }
        stage('pushECR') {
            steps {
              sh 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 448049823362.dkr.ecr.ap-south-1.amazonaws.com'
             
              sh 'docker push ${ECR_REGISTRY}:${dockerImageTag}'
            }
        }
        stage('contianer') {
            steps {
              
              sh 'docker pull ${ECR_REGISTRY}:${dockerImageTag}'
              sh 'docker run -itd -p ${HOST_PATH}:${CONTAINER_PORT} ${ECR_REGISTRY}:${dockerImageTag}'
            }
        }
    
}
}