pipeline{
    agent any

    stages{
        stage('Hello'){
            steps{
            sh "echo 'hii'"
            }
        }

        stage('GitStage'){
            steps{
            git branch: 'main', url: 'https://github.com/SarumathyPrabakaran/Slack-Jenkins/'
            }
        }

        stage('Notify'){
            steps{
                slackSend channel: 'devops-learning', color: 'warning', message: 'Heyy!! Commit Has been made', tokenCredentialId: 'jenkinsSecretTokenBySlack'
            }
        }
    }
}