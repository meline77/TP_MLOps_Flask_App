pipeline {
  agent any
  stages{ 
    stage('Create Staging branch'){
      steps{
        echo 'Create Staging branch'
        
        bat 'git branch -d staging'
        // bat 'git push origin --delete staging'
         
        bat 'git branch'
        // bat 'git checkout main'
        bat 'git checkout dev'
        bat 'git pull'
        bat 'git checkout -b staging'
        //bat 'git pull'
        bat 'git merge dev'
        bat 'git push --set-upstream origin staging'
      }
    }
    stage('build'){
      steps{
        echo 'build'
        bat 'pip install -r requirements.txt'
      }
    }
    stage('test'){
      steps{
        echo 'test'
        bat 'python test_main.py'
      }
    } 
    stage('deploy'){
      steps{
        echo 'deploy'
        bat 'docker build -t jenkins-private .'
      }
    }
    stage('merge'){
      steps{
        echo 'merge'
        bat 'git checkout main'
        bat 'git merge staging'
        bat 'git push'
      }
    }
    
    stage('delete staging'){
      steps{
        echo 'delete'
        bat 'git branch -d staging'
        bat 'git push origin --delete staging'
      }
    }
  }
}
