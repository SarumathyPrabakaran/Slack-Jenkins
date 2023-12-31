pipeline{
    agent any

    stages{
        stage('Hello'){
            sh "echo 'hii'"
        }

        stage('GitStage'){
            git branch: 'main', url: 'https://github.com/SarumathyPrabakaran/Slack-Jenkins/'
        }
    }
}