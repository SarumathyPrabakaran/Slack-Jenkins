pipeline {
    agent any

    environment {
        REPO_NAME = 'Slack-Jenkins'
        JOB_NAME = 'github-integration'
    }

    stages {
        stage('Hello') {
            steps {
                echo 'hii'
            }
        }

        stage('GitStage') {
            steps {
                script {
                    // Clone the repository --> My Private Repo.
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'main']],
                        userRemoteConfigs: [[url: 'https://github.com/SarumathyPrabakaran/Slack-Jenkins/']]
                    ])

                    // Get the latest commit message
                    def commitMessage = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()

                    // Include the commit message, repo name, and job name in the environment
                    currentBuild.description = "Commit Message: $commitMessage, Repo Name: $REPO_NAME, Job Name: $JOB_NAME"
                }
            }
        }

        stage('Notify') {
            steps {
                script {
                    // Send Slack notification with commit details
                    slackSend channel: 'devops-learning', color: 'good', message: currentBuild.description, tokenCredentialId: 'jenkinsSecretTokenBySlack'
                }
            }
        }
    }
}
