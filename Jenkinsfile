pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sshPublisher(publishers: [sshPublisherDesc(configName: 'otp-server', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/var/www/html/snap/', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '**/*.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            }
        }
        stage('Permission Change'){
            steps {
                sh 'sudo chown -R www-data:www-data /var/www/html/snap'
            }
        }
    }
}
