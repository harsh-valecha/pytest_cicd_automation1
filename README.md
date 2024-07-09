Pytest Demo Project with Allure reporting  - 

![image](https://github.com/harsh-valecha/pytest_cicd_automation1/assets/119730682/b356ca33-c2f0-44df-863f-c2f98a7fd767)



Jenkins Stages for pipeline -

pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/harsh-valecha/pytest_cicd_automation1.git']])
            }
            
        }
        
        stage('test'){
            steps{
                bat 'python -m pytest -v test_ops.py --html=report.html'
            }
        }
        
    }
}
