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
                sh('echo ${CREDS_PSW}')
            }
        }
        stage('Execute ansible') {
            steps{
                ansiblePlaybook(
                    inventory: 'hosts',
                    installation: 'ansible',
                    playbook: 'playbook.yml',
                    credentialsId: '-----BEGIN OPENSSH PRIVATE KEY-----b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcnNhAAAAAwEAAQAAAQEAmJyiVLC7ElocYEfanLMaMSgwKeUZpL1yXMi/l3QcBUC4wENxMSMuUPYR8cPbfUY9JWJTFKLUv5DfCO0aF+S8vM+9jYtgfI9/618nEJh1y4rYeQhvgqOgrN2xHZgol/ugRmwPsGwvSoNi5+vZFBemlIbBQ8PUplzFzvNAwdSyFtS4QUjkrpJ03BNfgn3G1dYndauQO2fobA3h8vg2ADerUeQQFYHnHaUtUGVXw3NkCzXV/PVtlFnYyhOgEkzW7E6c7+pLZOwZbdCwCokUGccvwOuEsyvWMEuhjm7X8zuigrpV2XWwYJqclSoasgrz3aO/5nQSFUtXvfRebjFBXx7YSQAAA8Dcy5eI3MuXiAAAAAdzc2gtcnNhAAABAQCYnKJUsLsSWhxgR9qcsxoxKDAp5RmkvXJcyL+XdBwFQLjAQ3ExIy5Q9hHxw9t9Rj0lYlMUotS/kN8I7RoX5Ly8z72Ni2B8j3/rXycQmHXLith5CG+Co6Cs3bEdmCiX+6BGbA+wbC9Kg2Ln69kUF6aUhsFDw9SmXMXO80DB1LIW1LhBSOSuknTcE1+CfcbV1id1q5A7Z+hsDeHy+DYAN6tR5BAVgecdpS1QZVfDc2QLNdX89W2UWdjKE6ASTNbsTpzv6ktk7Blt0LAKiRQZxy/A64SzK9YwS6GObtfzO6KCulXZdbBgmpyVKhqyCvPdo7/mdBIVS1e99F5uMUFfHthJAAAAAwEAAQAAAQEAl6JCVL3JEmIAgdXDLCF069TPjkD5astlfzVj0Htof/uf1kDsjfMzyPPGPp7pTh7lEGkSvZVQqAqs4TSc0ZLPyRbsc2BB/WGjq10+9mlV2Wjaz9+G1Jn6Quh/XDVcWC6HQJGMQTItBu9m7aNUbHdXZ4pBKzC/8JCLZqYh+LV6Qd2Pbf7f43yuOmomNoKCrCrXBORiOfCGvXEMa3PVVJpR/WDO1Qvi3TjTkYW/kRGO5YJMnnodBSSJCpN0BxLCZ56WPPxzw2xUbmvPxTH9XWdpsJHN+xDDbpYnf3I+dLinhfdKcMhfG/ez0Q1glmtv+RtuFbWvm//IgjHrWT0Xoq3dgQAAAIBdaBYnkxyU8/fyQtxxjhmuGWRX6NxYlJfijU4e7TzE2+aK2Tgay4EUqLnHCgt9RCYZrFBDAzi0xUcxPB84cbJG3oUDlOG/VKp0C9YYM/D8m/98kx/kcrQews7OaAHKXgOZbtNuhBU/MuSvYdYYp/rJ6pczBdBTy9nKapy0EKZnpgAAAIEAxwM6pLPQX85uTxC0WP43Ssflc8uRohR5AAg7mM1LYsZEV/ojD85w7C7fdLa9bDiDEBdiAt/aEOWDKrHF8XUQYZMAkzyndrnwEsXMgCS+8/I26jaQDYgB8177uN7q2nLvaq5qPSAWEikwYS6IygRmIr3yZlsqe93/TNKrGE88HhEAAACBAMRP9kDRxW3Q1CXhNhN8DXqKatbuwUBApY5Yc+92IKCgFmoq85/qbqDh5GyxLQa5BIubZUWupaWvdw4yHygyFQsXVSU767VMkEaV2pWCLXipUu0Q5b83fHg6iYbZMOajN2VO4UpbPnj0ojOfkhF80vNjgHVskIQeWME4zCG2FT65AAAACkpVTVBTRVJWRVI=-----END OPENSSH PRIVATE KEY-----',
                    hostKeyChecking: false
                )
            }
        }
    }
}