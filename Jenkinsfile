pipeline {
    agent any

    stages {
        stage('Установка зависимостей') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Smoke тесты') {
            steps {
                sh 'pytest tests/ -m smoke '
            }
        }

        stage('Regress тесты') {
            steps {
                sh 'pytest tests/ -m regress'
            }
        }
    }
    
    post {
        always {
            allure includeProperties: false,
                results: [[path: 'reports']]
        }
    }
}
