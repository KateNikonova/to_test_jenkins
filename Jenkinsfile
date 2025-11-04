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

                    echo "=== Checking Allure Results ==="
                    ls -la allure-results/ || echo "Allure results directory not found"
                '''
            }
            post {
                always {
                    // Сохраняем JUnit отчет
                    junit 'test-results.xml'

                    // Сохраняем HTML отчет как артефакт
                    archiveArtifacts artifacts: 'test-report.html', fingerprint: true

                    // Сохраняем Allure результаты
                    archiveArtifacts artifacts: 'allure-results/**/*', fingerprint: true
                }
            }
        }

        stage('Install Allure Commandline') {
            steps {
                sh '''
                    echo "=== Installing Allure Commandline ==="

                    # Проверяем, не установлен ли уже Allure
                    if ! command -v allure &> /dev/null; then
                        echo "Allure not found, installing..."

                        # Скачиваем Allure
                        wget -q -O allure-2.27.0.tgz https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz

                        # Распаковываем
                        tar -xvzf allure-2.27.0.tgz

                        # Делаем исполняемым
                        chmod +x allure-2.27.0/bin/allure

                        # Добавляем в PATH для текущей сессии
                        export PATH="$PWD/allure-2.27.0/bin:$PATH"

                        echo "Allure version:"
                        ./allure-2.27.0/bin/allure --version
                    else
                        echo "Allure already installed"
                        allure --version
                    fi
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    echo "=== Generating Allure Report ==="

                    # Используем локально установленный Allure
                    ./allure-2.27.0/bin/allure generate allure-results -o allure-report --clean

                    echo "=== Allure Report Generated ==="
                    ls -la allure-report/
                '''

                // Публикуем HTML отчет Allure
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Report'
                ])
            }
        }

        stage('Save Test Results') {
            steps {
                sh '''
                    echo "=== Saving Test Results ==="
                    echo "Tests completed at: $(date)" > test-summary.txt
                    echo "API Base URL: ${API_BASE_URL}" >> test-summary.txt
                    echo "Python Version: $(python3 --version 2>/dev/null || python --version 2>/dev/null)" >> test-summary.txt
                    echo "Allure Report: ${BUILD_URL}Allure_20Report/" >> test-summary.txt
                '''
                archiveArtifacts artifacts: 'test-summary.txt', fingerprint: true
                archiveArtifacts artifacts: 'allure-report/**/*', fingerprint: true
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
                    echo "📊 HTML Test report: ${env.BUILD_URL}artifact/test-report.html"
                    echo "📈 Allure Report: ${env.BUILD_URL}Allure_20Report/"
                } else {
                    echo "❌ Some tests failed!"
                    echo "📊 HTML Test report: ${env.BUILD_URL}artifact/test-report.html"
                    echo "📈 Allure Report: ${env.BUILD_URL}Allure_20Report/"
                }
            }
        }

        success {
            // Можно добавить уведомления о успешном выполнении
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """
                All tests passed!

                Reports:
                - Allure Report: ${env.BUILD_URL}Allure_20Report/
                - HTML Report: ${env.BUILD_URL}artifact/test-report.html
                - Console Output: ${env.BUILD_URL}console
                """,
                to: "e.nikonova.0407@gmail.com"
            )
        }

        failure {
            // Уведомления о неудаче
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """
                Some tests failed!

                Reports:
                - Allure Report: ${env.BUILD_URL}Allure_20Report/
                - HTML Report: ${env.BUILD_URL}artifact/test-report.html
                - Console Output: ${env.BUILD_URL}console
                """,
                to: "e.nikonova.0407@gmail.com"
            )
        }

        cleanup {
            // Очищаем временные файлы
            sh '''
                echo "=== Cleaning up ==="
                rm -rf allure-2.27.0.tgz || true
            '''
        }
    }
}