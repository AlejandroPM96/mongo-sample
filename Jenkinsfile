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
            }
        }
        stage('Setting jump server ip'){
            steps{
                withCredentials([file(credentialsId: 'GCLOUD_CREDS', variable: 'GC_KEY')]) {
                    script{
                        sh("gcloud auth activate-service-account --key-file=${GC_KEY}")
                        HOST_IP = sh '''gcloud compute instances describe jump-server --format='get(networkInterfaces[0].accessConfigs[0].natIP)' --zone=us-central1-a
                                        echo ${HOST_IP}
                                        echo -en ${HOST_IP} > hosts
                        '''
                    }
                }
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