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
                sh('echo /etc/ansible/key')
            }
        }
        stage('Execute ansible') {
            steps{
                ansiblePlaybook(
                    inventory: 'hosts',
                    playbook: 'playbook.yml',
                    credentialsId: '/etc/ansible/key',
                    hostKeyChecking: false
                )
            }
        }
    }
}