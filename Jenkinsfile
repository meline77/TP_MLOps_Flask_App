pipeline {
  agent any
  stages{ 
    stage('Create Staging branch'){
      steps{
        echo 'Create Staging branch'
        sh 'git checkout dev'
        sh 'git pull'
        sh 'git checkout -b staging'
        //sh 'git pull'
        sh 'git merge dev'
        sh 'git push --set-upstream origin staging'
      }
    }
    stage('build'){
      steps{
        echo 'build'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test'){
      steps{
        echo 'test'
        sh 'python test_main.py'
      }
    } 
    stage('deploy'){
      steps{
        echo 'deploy'
        sh 'docker build -t jenkins-private .'
      }
    }
    stage('merge'){
      steps{
        echo 'merge'
        sh 'git checkout main'
        sh 'git merge staging'
        sh 'git push'

      }
    }
  }
}
