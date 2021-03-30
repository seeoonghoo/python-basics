git init

git add -A
파일 이름 있으면 디렉토리/파일 이렇게 해도 됨

git commit -m "first commit"

git remote add origin https://github.com/seeoonghoo/python-basics.git

git push origin master


push에서 오류 생기면
git pull origin master 이걸로 땡겨서 
add부터 다시 해보기

========================================

1. 계정 설정
git config --global user.email "내 계정 이메일"
git config --global user.name "내 계정 이름"

git config --global user.email "seeoonghoo@gmail.com"
git config --global user.name "seeoonghoo"

2. 프로젝트 깃서비 인증 삭제 하기
git credential-manager uninstall

------------------------

3. 로컬 레파지토리 설정 // 프로젝트 폴더에서 
git init

3-1. 확인은 
dir /a
로 가능

4. github에서 레포지토리를 생성

5. staging 작업(변경을 감시)// 프로젝트 폴더에서
git add -A

6. commit 작업(파일 옆에 커밋 다는거)// 프로젝트 폴더에서
git commit -m "멘트적을거"
   
7. 처음 git server에 push 할 때 원격 레포지토리 연결 작업 (master branch 설정)
git remote add origin https://github.com/seeoonghoo/tmp.git
   에서 저기 뒤에 주소는 다름 레포지토리마다 
   
8. 푸쉬함
git push origin master