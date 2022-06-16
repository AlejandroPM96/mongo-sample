pipeline {
    agent any
    stages {
        stage('Execute ansible') {
            steps{
                ansiblePlaybook(
                    inventory: 'hosts',
                    installation: 'ansible',
                    playbook: 'playbook.yml'
                )
            }
        }
    }
}