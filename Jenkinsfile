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
    }
}