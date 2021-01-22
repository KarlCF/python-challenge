# Git

You can periodically update and keep a backup of your projects after updating or release new builds for your project. So a project could be anything, right from a web application (which may contain HTML, CSS, JS, or JSON files) to an IoT's python sets of code for Arduino. Anything can be stored, reused, shared for collaboration, and this can be done both in public and private mode. Git keeps a history of every project, i.e., Git keeps track of every change made by any collaboration team member. Moreover, it allows developers to work simultaneously on the same project, which does not collide or clash with each other's changes on that particular project. 

git config:
* git config --system
  * to every user of the system and it's repositories
  * /etc/gitconfig
  * C:/Program Files/Git/etc/gitconfig
* git config --global
  * only for your user
  * ~/.gitconfig or ~/.config/git/config
  * On windows at $HOME directory: C:\User\$USER
* git config
  * for the project directory
  * .git/config

Git file states:
* Untracked
* Unmodified
* Modified
* Staged

## Notes

* Extra reading:
  * [W3 - What is Git](https://www.w3schools.in/git/intro/)
  * [W3 - Version Control](https://www.w3schools.in/git/version-control/)
  * [git - Documentation](https://git-scm.com/doc)
    * [git config](https://git-scm.com/docs/git-config)
  * [git - Videos](https://git-scm.com/videos)
  * [git - cheatsheet(cheat.sh)](http://cheat.sh/git)
* Extra resources:
  * [learn git branching - !!! IMPORTANT !!!](https://learngitbranching.js.org/)

## Important Commands

* git init
  * initialize repository
* git status
  * check repository status
* git diff
  * check the changes
* git add
  * add the changes to the stage
* git commit
  * commits the staged changes
* git log
  * shows the repository log (history)
* git show $COMMIT_HASH
  * shows the diff on that commit
* git shortlog
  * summarize 'git log' output
  * git shortlog -sn
    * shows only numbers
* git checkout
  * switch branches or restore working tree files
  * git checkout $FILE_NAME
    * restores file to previous staged change
* git reset
  * reset current HEAD to the specified state
  * git reset HEAD
* 