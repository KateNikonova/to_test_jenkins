pipeline {
    agent any

    tools {
        python 'Python3'  // Название установленного Python в Jenkins
    }

    environment {
        API_BASE_URL = 'http://5.101.50.27:8000'
        // Токен можно добавить через Jenkins Credentials
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                script {
                    echo "Python version:"
                    sh 'python --version'
                    sh 'pip --version'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install -r requirements.txt
                    python -c "import requests; print(f'Requests version: {requests.__version__}')"
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    python run_tests.py
                '''
            }
            post {
                always {
                    // Сохраняем отчеты
                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '.',
                        reportFiles: 'test-report.html',
                        reportName: 'Python Test Report'
                    ])
                    junit 'test-results.xml'
                }
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                    echo "Running basic security checks..."
                    pip list
                    # Можно добавить safety check или bandit
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed"
            cleanWs()  // Очистка workspace
        }
        success {
            echo "✅ All tests passed successfully!"
            // Можно добавить уведомления
        }
        failure {
            echo "❌ Some tests failed!"
            // Можно добавить уведомления об ошибках
        }
    }
}