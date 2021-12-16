### 아마존-리눅스 시스템 업데이트.
```
sudo yum update -y && upgrade -y
sudo yum install java-11-amazon-corretto -y
```

### 젠킨스 설치.
```
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
sudo yum install jenkins -y | sudo amazon-linux-extras install epel -y 
usermod -aG docker jenkins
```
### nginx 설치.
```
sudo yum install nginx -y
```
### 깃 설치
```
sudo yum install git -y
```
### 도커 설치
```
sudo yum install docker -y
sudo yum install docker-compose -y
```
### 도커 컴포저 설치
```
sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```