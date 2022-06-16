pipeline {
    agent any
    environment {
        CREDS = credentials('jumpserver')
    }
    stages {
        stage('Cleaning ssh hosts') {
            steps{
                sh('touch ~/.ssh/known_hosts')
                sh('rm ~/.ssh/known_hosts')
                sh('echo $jumpserver')
            }
        }
        stage('Execute ansible') {
            steps{
                ansiblePlaybook(
                    inventory: 'hosts',
                    installation: 'ansible',
                    playbook: 'playbook.yml',
                    credentialsId: '${CREDS}',
                    hostKeyChecking: false
                )
            }
        }
    }
}