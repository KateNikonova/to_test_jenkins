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
                    // Сохраняем JUnit отчет
                    junit 'test-results.xml'

                    // Сохраняем HTML отчет как артефакт
                    archiveArtifacts artifacts: 'test-report.html', fingerprint: true
                }
            }
        }

        stage('Save Test Results') {
            steps {
                sh '''
                    echo "=== Saving Test Results ==="
                    echo "Tests completed at: $(date)" > test-summary.txt
                    echo "API Base URL: ${API_BASE_URL}" >> test-summary.txt
                    echo "Python Version: $(python3 --version 2>/dev/null || python --version 2>/dev/null)" >> test-summary.txt
                '''
                archiveArtifacts artifacts: 'test-summary.txt', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "=== Pipeline execution completed ==="

            // Показываем ссылки на артефакты
            script {
                if (currentBuild.result == 'SUCCESS') {
                    echo "✅ All tests passed successfully!"
                    echo "📊 Test report: ${env.BUILD_URL}artifact/test-report.html"
                } else {
                    echo "❌ Some tests failed!"
                    echo "📊 Test report: ${env.BUILD_URL}artifact/test-report.html"
                }
            }
        }

        success {
            // Можно добавить уведомления о успешном выполнении
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "All tests passed! Check report at: ${env.BUILD_URL}",
                to: "user@example.com"
            )
        }

        failure {
            // Уведомления о неудаче
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "Some tests failed! Check console output at: ${env.BUILD_URL}console",
                to: "user@example.com"
            )
        }
    }
}