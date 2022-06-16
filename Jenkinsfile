pipeline {
    agent any
    stages {
        stage('Cleaning ssh hosts') {
            steps{
                sh('touch ~/.ssh/known_hosts')
                sh('rm ~/.ssh/known_hosts')
            }
        }
        stage('Execute ansible') {
            steps{
                ansiblePlaybook(
                    inventory: 'hosts',
                    installation: 'ansible',
                    playbook: 'playbook.yml',
                    credentialsId: '$jumpserver'
                )
            }
        }
    }
}