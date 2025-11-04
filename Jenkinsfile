pipeline {
    agent any

    environment {
        API_BASE_URL = 'http://5.101.50.27:8000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    echo "=== Checking Python Installation ==="
                    which python3 || which python
                    python3 --version || python --version
                    pip3 --version || pip --version
                    echo "=== Current directory ==="
                    pwd
                    ls -la
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "=== Installing Python Dependencies ==="
                    pip3 install -r requirements.txt || pip install -r requirements.txt
                    echo "=== Installed packages ==="
                    pip3 list || pip list
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                sh '''
                    echo "=== Running API Tests ==="
                    python3 run_tests.py || python run_tests.py
                    echo "=== Test execution completed ==="
                '''
            }
            post {
                always {
                    script {
                        // Публикуем HTML отчет если он есть
                        if (fileExists('test-report.html')) {
                            publishHTML([
                                allowMissing: false,
                                alwaysLinkToLastBuild: true,
                                keepAll: true,
                                reportDir: '.',
                                reportFiles: 'test-report.html',
                                reportName: 'Python Test Report'
                            ])
                        }

                        // Публикуем JUnit отчет если он есть
                        if (fileExists('test-results.xml')) {
                            junit 'test-results.xml'
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo "=== Pipeline execution completed ==="
            script {
                // Очистка workspace (опционально)
                cleanWs()
            }
        }
        success {
            echo "✅ All tests passed successfully!"
        }
        failure {
            echo "❌ Some tests failed!"
        }
    }
}