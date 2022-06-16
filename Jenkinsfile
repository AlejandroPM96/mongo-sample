pipeline {
    agent any
    environment {
        CREDS = credentials('jumpserver')
        ANSIBLE_CONFIG='etc/ansible/ansible.cfg'
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
                    credentialsId: '${CREDS}',
                    disableHostKeyChecking: true
                )
            }
        }
    }
}